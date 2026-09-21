#!/usr/bin/env python3
"""Bouwt de openbare website van de Belegger Kees Methode uit de Markdown in deze repository.

Gebruik:  python site/build.py            (schrijft naar _site/)
          SITE_URL=https://voorbeeld.nl python site/build.py

Uitgangspunten
- Alleen bestanden die in Git staan komen op de site. Wat Git negeert, komt er nooit op.
- De Markdown blijft onaangeroerd; titels, omschrijvingen en metadata worden afgeleid.
- Geen JavaScript en geen extern verzoek: lettertypen zijn lokaal, opmaak staat in site/style.css.
"""
import html, json, os, re, shutil, subprocess, sys, unicodedata
from datetime import date
from urllib.parse import urlparse
import markdown

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SITE_DIR = os.path.join(ROOT, "site")
OUT = os.path.join(ROOT, "_site")
CFG = json.load(open(os.path.join(SITE_DIR, "config.json"), encoding="utf-8"))
SITE_URL = os.environ.get("SITE_URL", CFG["site_url"]).rstrip("/")
BASE = urlparse(SITE_URL).path.rstrip("/")          # "/belegger-kees-methode" of ""
EXCLUDE_MD = {"CLAUDE.md", "AGENTS.md"}             # blijven alleen op GitHub
TODAY = date.today().isoformat()

DISCLAIMER = ("De content op Belegger Kees is uitsluitend bedoeld voor educatieve doeleinden en vormt geen persoonlijk beleggingsadvies. "
              "Beleggen brengt risico's met zich mee. De waarde van beleggingen kan fluctueren en je kunt je inleg verliezen. "
              "Resultaten uit het verleden bieden geen garantie voor de toekomst. Raadpleeg een erkende financieel adviseur voor advies op maat. "
              "Belegger Kees is geen geregistreerde beleggingsonderneming bij de AFM.")
MONTHS = {"januari": 1, "februari": 2, "maart": 3, "april": 4, "mei": 5, "juni": 6, "juli": 7, "augustus": 8,
          "september": 9, "oktober": 10, "november": 11, "december": 12}
SECTION_LABELS = {"docs": "Docs", "manifesto": "Manifesto", "analyseproces": "Analyseproces", "onderzoek": "Onderzoek",
                  "resources": "Resources", "community": "Community", "nlp-coaching-voor-beleggers": "NLP-coaching",
                  "over-belegger-kees": "Over Belegger Kees"}


# Ecosysteemblok in de voet: identiek in de vier sites van het merk Kees van Wanrooij
# (hub keesvanwanrooij.nl, deze methode, cursus-elektrotechniek en cursus-cv-ketels).
HUB = "https://keesvanwanrooij.nl"
ECO = [
    ("Beleggen", [
        ("belegger-kees", "https://beleggerkees.nl", "Belegger Kees"),
        ("methode", HUB + "/belegger-kees-methode/", "Belegger Kees Methode"),
        ("beleggen", HUB + "/beleggen/", "Beleggen met GARP en NLP"),
    ]),
    ("Gratis cursussen", [
        ("elektro", HUB + "/cursus-elektrotechniek/", "Cursus Elektrotechniek"),
        ("cv", HUB + "/cursus-cv-ketels/", "Cursus CV-ketels"),
    ]),
    ("Kees van Wanrooij", [
        ("home", HUB + "/", "Home"),
        ("over-mij", HUB + "/over-mij/", "Over mij"),
        ("linkedin", "https://www.linkedin.com/in/keesvanwanrooij/", "LinkedIn"),
        ("instagram", "https://www.instagram.com/beleggerkees/", "Instagram"),
        ("github", "https://github.com/keesvanwanrooij", "GitHub"),
    ]),
]
ECO_HERE = "methode"


def eco_html():
    cols = []
    for kop, links in ECO:
        lis = "".join(
            f'<li><a href="{esc(h)}"{" aria-current=" + chr(34) + "true" + chr(34) if k == ECO_HERE else ""}>{esc(t)}</a></li>'
            for k, h, t in links)
        cols.append(f'<nav aria-label="{esc(kop)}"><p class="foot-h">{esc(kop)}</p><ul>{lis}</ul></nav>')
    return ('<div class="foot-eco"><div><p class="foot-brand">Kees van Wanrooij<span class="dot">.</span></p>'
            '<p class="foot-tag">Belegger en NLP-practitioner. Oprichter van Belegger Kees. Educatie, geen beleggingsadvies.</p></div>'
            + "".join(cols) + '</div>')


def git(*args):
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True, encoding="utf-8").stdout


def slug(text):
    s = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    s = re.sub(r"^\d+-", "", s.lower())
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")


def gh_slug(value, sep="-"):                      # gelijk aan de ankers die GitHub maakt
    s = re.sub(r"`", "", value.strip().lower())
    s = re.sub(r"[^\w\- ]", "", s)
    return s.replace(" ", "-")


def esc(s):
    return html.escape(s, quote=True)


# ---------------------------------------------------------------- bestanden
tracked = [f for f in git("-c", "core.quotepath=false", "ls-files").split("\n") if f]
tracked_set = set(tracked)
md_files = sorted(f for f in tracked if f.endswith(".md") and f not in EXCLUDE_MD and not f.startswith(("site/", ".github/")))
STATIC = {"LICENSE": "LICENSE.txt", "CITATION.cff": "CITATION.cff", "llms.txt": "llms.txt"}
for f in tracked:
    if f.startswith("05-Resources/Templates/") and f.lower().endswith((".xlsx", ".docx")):
        STATIC[f] = "resources/templates/" + os.path.basename(f)


def page_url(path):
    parts = path.split("/")
    dirs, name = parts[:-1], parts[-1]
    segs = [slug(d) for d in dirs]
    if name.lower() != "readme.md":
        segs.append(slug(name[:-3]))
    return "/" + "/".join(segs) + ("/" if segs else "")


URL_OF = {p: page_url(p) for p in md_files}
assert len(set(URL_OF.values())) == len(URL_OF), "dubbele URL's"


def href(url):
    return BASE + url


# ---------------------------------------------------------------- markdown lezen
def read(path):
    return open(os.path.join(ROOT, path), encoding="utf-8").read()


def strip_md(s):
    s = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", s)
    s = re.sub(r"[*_`]+", "", s)
    return re.sub(r"\s+", " ", s).strip()


def make_description(body):
    for block in re.split(r"\n\s*\n", body):
        b = block.strip()
        if not b or re.match(r"^(>|\||[-*+] |\d+\. |#|```|<|---)", b):
            continue
        txt = strip_md(b)
        if len(txt) <= 158:
            return txt
        cut = txt[:158]
        i = max(cut.rfind(". "), cut.rfind("? "), cut.rfind("! "))
        if i >= 90:
            return cut[:i + 1]
        return cut[:cut.rfind(" ", 0, 156)].rstrip(",;:") + "…"
    return CFG["default_description"]


def make_title(h1, path):
    brand = " | " + CFG["site_name"]
    if "Belegger Kees" in h1 and len(h1) <= 62:
        return h1
    short = h1
    if len(h1) + len(brand) > 66 and ":" in h1:
        short = h1.split(":", 1)[0].strip()
    elif len(h1) + len(brand) > 66 and " en " in h1 and False:
        pass
    if path.startswith("07-NLP-coaching-voor-beleggers/Technieken/") and not path.endswith("README.md"):
        short = short + " (NLP-techniek)"
    elif path.startswith("05-Resources/Sectoren/") and not path.endswith("README.md"):
        short = short + " (sector)"
    t = short + brand
    return t if len(t) <= 72 else short


def nav_label(h1, path):
    if path == "README.md":
        return "Startpagina"
    parts = path.split("/")
    if parts[-1].lower() == "readme.md" and len(parts) == 2:
        return SECTION_LABELS.get(slug(parts[0]), h1.split(":")[0])
    lab = h1.split(":")[0].strip()
    return lab if len(lab) <= 46 else lab[:44].rsplit(" ", 1)[0] + "…"


def modified_date(path, text):
    m = re.search(r"Bijgewerkt: (\d{1,2}) (\w+) (\d{4})\.", text)
    if m and m.group(2).lower() in MONTHS:
        return f"{int(m.group(3)):04d}-{MONTHS[m.group(2).lower()]:02d}-{int(m.group(1)):02d}"
    d = git("log", "-1", "--format=%cs", "--", path).strip()
    return d or TODAY


def published_date(path):
    d = git("log", "--diff-filter=A", "--format=%cs", "--", path).strip().split("\n")[-1].strip()
    return d or TODAY


pages = {}
for p in md_files:
    raw = read(p)
    m = re.search(r"^# (.+)$", raw, flags=re.M)
    h1 = m.group(1).strip()
    body = raw[:m.start()] + raw[m.end():] if m else raw
    body = re.sub(r"<!-- alleen-github-begin -->.*?<!-- alleen-github-einde -->\s*", "", body, flags=re.S)
    body = body.lstrip("\n")
    pages[p] = dict(path=p, url=URL_OF[p], h1=h1, body=body, raw=raw,
                    title=make_title(h1, p), desc=make_description(body), label=nav_label(h1, p),
                    modified=modified_date(p, raw), published=published_date(p))

# ---------------------------------------------------------------- markdown -> html
def resolve_link(src_path, target):
    """Geeft de nieuwe href voor een relatieve link in een Markdown-bestand."""
    if re.match(r"^(https?:|mailto:|tel:)", target):
        return target
    if target.startswith("#"):
        return target
    path, _, anchor = target.partition("#")
    joined = os.path.normpath(os.path.join(os.path.dirname(src_path), path)).replace("\\", "/")
    if joined in (".", ""):
        joined = ""
    if target.endswith("/") or (joined and not os.path.splitext(joined)[1] and (joined + "/README.md") in URL_OF):
        joined = (joined + "/README.md").lstrip("/")
    frag = ("#" + anchor) if anchor else ""
    if joined in URL_OF:
        return href(URL_OF[joined]) + frag
    if joined in STATIC:
        return href("/" + STATIC[joined])
    if joined in tracked_set:
        return CFG["repo_url"] + "/blob/main/" + joined + frag
    print("WAARSCHUWING: link niet te herleiden:", src_path, "->", target, file=sys.stderr)
    return target


def render_md(page):
    md = markdown.Markdown(extensions=["tables", "fenced_code", "toc", "sane_lists"],
                           extension_configs={"toc": {"slugify": gh_slug, "permalink": False}})
    out = md.convert(page["body"])
    out = re.sub(r'href="([^"]+)"', lambda m: 'href="' + esc(html.unescape(resolve_link(page["path"], html.unescape(m.group(1))))) + '"', out)
    out = out.replace("<table>", '<div class="table-wrap"><table>').replace("</table>", "</table></div>")
    out = re.sub(r"<blockquote>\s*<p>In English:", '<blockquote class="in-english" lang="en"><p><span class="lbl">In English:</span>', out)
    out = re.sub(r"<p>(Bijgewerkt: [^<]*)</p>", r'<p class="updated">\1</p>', out)
    out = re.sub(r"<p>(De content op Belegger Kees is uitsluitend[^<]*)</p>", r'<aside class="disclaimer"><p>\1</p></aside>', out)
    out = re.sub(r"<p><strong>(<a href=\"[^\"]+\">[^<]+</a>)</strong></p>",
                 lambda m: '<p class="cta">' + m.group(1).replace("<a ", '<a class="btn" ', 1) + "</p>", out)
    out = re.sub(r"<hr\s*/?>", '<hr class="end">', out)
    return out


# ---------------------------------------------------------------- navigatie
def build_tree():
    tree = {"page": None, "files": [], "dirs": {}}
    for p in md_files:
        parts = p.split("/")
        node = tree
        for d in parts[:-1]:
            node = node["dirs"].setdefault(d, {"page": None, "files": [], "dirs": {}})
        if parts[-1].lower() == "readme.md":
            node["page"] = pages[p]
        else:
            node["files"].append(pages[p])
    return tree


TREE = build_tree()


def render_node(node, current, name=None, top=False):
    items = []
    for f in node["files"]:
        cur = ' aria-current="page"' if f["url"] == current else ""
        items.append(f'<li><a href="{href(f["url"])}"{cur}>{esc(f["label"])}</a></li>')
    for d in sorted(node["dirs"]):
        items.append(render_node(node["dirs"][d], current, d))
    inner = "<ul>" + "".join(items) + "</ul>"
    if name is None:
        return inner
    pg = node["page"]
    label = SECTION_LABELS.get(slug(name)) if top else None
    label = label or (pg["label"] if pg else name)
    is_open = current.startswith(pg["url"]) if pg else False
    cur = ' aria-current="page"' if pg and pg["url"] == current else ""
    summary = f'<a href="{href(pg["url"])}"{cur}>{esc(label)}</a>' if pg else esc(label)
    return f'<li class="grp"><details{" open" if is_open else ""}><summary>{summary}</summary>{inner}</details></li>'


def render_nav(current):
    top = TREE
    start = pages["README.md"]
    cur = ' aria-current="page"' if start["url"] == current else ""
    rows = [f'<li><a href="{href(start["url"])}"{cur}>Startpagina</a></li>']
    for d in sorted(top["dirs"]):
        rows.append(render_node(top["dirs"][d], current, d, top=True))
    return '<nav class="sidenav" aria-label="Inhoud"><ul>' + "".join(rows) + "</ul></nav>"


def breadcrumbs(page):
    crumbs = [("Startpagina", href("/"), SITE_URL + "/")]
    parts = page["path"].split("/")[:-1]
    for i in range(len(parts)):
        rp = "/".join(parts[:i + 1]) + "/README.md"
        if rp in pages:
            crumbs.append((pages[rp]["label"], href(pages[rp]["url"]), SITE_URL + pages[rp]["url"]))
    if page["path"] != "README.md" and page["path"].lower().split("/")[-1] != "readme.md":
        crumbs.append((page["label"], href(page["url"]), SITE_URL + page["url"]))
    return crumbs


# ---------------------------------------------------------------- structured data
ORG_ID, WEB_ID = CFG["brand_url"] + "/#organization", SITE_URL + "/#website"
AUTHOR_URL = SITE_URL + URL_OF["08-Over-Belegger-Kees/README.md"]
PERSON_ID = AUTHOR_URL + "#kees-van-wanrooij"
SAMEAS = [CFG["brand_url"], CFG["instagram"], CFG["linkedin"]]


def faq_items(body):
    m = re.search(r"^## [^\n]*Veelgestelde vragen[^\n]*\n(.*?)(?=^## |\Z)", body, flags=re.M | re.S)
    if not m:
        return []
    items = []
    for q in re.finditer(r"^### (.+?)\n(.*?)(?=^### |\Z)", m.group(1), flags=re.M | re.S):
        ans = strip_md(re.sub(r"\n{2,}", " ", q.group(2)).strip())
        if ans:
            items.append({"@type": "Question", "name": strip_md(q.group(1)),
                          "acceptedAnswer": {"@type": "Answer", "text": ans}})
    return items


def json_ld(page, kind):
    canonical = SITE_URL + page["url"]
    graph = [
        {"@type": "Organization", "@id": ORG_ID, "name": CFG["site_name"], "url": CFG["brand_url"],
         "logo": SITE_URL + "/assets/icon-512.png", "sameAs": SAMEAS[1:],
         "contactPoint": {"@type": "ContactPoint", "email": CFG["contact_email"], "contactType": "customer service"}},
        {"@type": "WebSite", "@id": WEB_ID, "url": SITE_URL + "/", "name": CFG["site_title"], "inLanguage": "nl-NL",
         "publisher": {"@id": ORG_ID}},
        {"@type": "Person", "@id": PERSON_ID, "name": "Kees van Wanrooij", "url": AUTHOR_URL,
         "jobTitle": "Oprichter van Belegger Kees", "worksFor": {"@id": ORG_ID}, "sameAs": SAMEAS,
         "knowsAbout": ["Fundamentele aandelenanalyse", "Waardering met een DCF-model", "Beleggingspsychologie",
                        "Neurolinguïstisch programmeren"]},
    ]
    main = {"@type": {"home": "WebPage", "author": "ProfilePage"}.get(kind, "Article"), "@id": canonical + "#page",
            "url": canonical, "name": page["h1"], "headline": page["h1"][:110], "description": page["desc"],
            "inLanguage": "nl-NL", "isPartOf": {"@id": WEB_ID}, "dateModified": page["modified"],
            "datePublished": page["published"], "author": {"@id": PERSON_ID}, "publisher": {"@id": ORG_ID},
            "image": SITE_URL + "/assets/og-default.png", "license": "https://creativecommons.org/licenses/by-sa/4.0/"}
    if kind == "author":
        main["mainEntity"] = {"@id": PERSON_ID}
        for k in ("headline", "author", "publisher", "license"):
            main.pop(k, None)
    graph.append(main)
    crumbs = breadcrumbs(page)
    if len(crumbs) > 1:
        graph.append({"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": c[0], "item": c[2]} for i, c in enumerate(crumbs)]})
    faq = faq_items(page["body"])
    if faq:
        graph.append({"@type": "FAQPage", "mainEntity": faq})
    return json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, separators=(",", ":"))


# ---------------------------------------------------------------- pagina's
CSS_VERSION = ""


def head(title, desc, canonical, kind, ld=None, noindex=False, modified=None):
    og_image = SITE_URL + "/assets/og-default.png"
    verify = ""
    if CFG.get("google_site_verification"):
        verify += f'<meta name="google-site-verification" content="{esc(CFG["google_site_verification"])}">\n'
    if CFG.get("bing_site_verification"):
        verify += f'<meta name="msvalidate.01" content="{esc(CFG["bing_site_verification"])}">\n'
    robots = "noindex,follow" if noindex else "index,follow,max-image-preview:large"
    art = ""
    if kind in ("article", "author") and modified:
        art = f'<meta property="article:modified_time" content="{modified}">\n<meta property="article:author" content="{esc(AUTHOR_URL)}">\n'
    return f'''<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{esc(canonical)}">
<meta name="robots" content="{robots}">
<meta name="author" content="Kees van Wanrooij">
<meta name="theme-color" content="#C4303C">
{verify}<meta property="og:type" content="{"website" if kind in ("home", "misc") else "article"}">
<meta property="og:site_name" content="{esc(CFG["site_name"])}">
<meta property="og:locale" content="nl_NL">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{esc(canonical)}">
<meta property="og:image" content="{og_image}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Belegger Kees: aandelenanalyse, waardering en NLP">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(title)}">
<meta name="twitter:description" content="{esc(desc)}">
<meta name="twitter:image" content="{og_image}">
{art}<link rel="icon" href="{href("/assets/favicon.svg")}" type="image/svg+xml">
<link rel="icon" href="{href("/assets/favicon.ico")}" sizes="48x48">
<link rel="icon" href="{href("/assets/favicon-32x32.png")}" sizes="32x32" type="image/png">
<link rel="icon" href="{href("/assets/favicon-16x16.png")}" sizes="16x16" type="image/png">
<link rel="apple-touch-icon" href="{href("/assets/apple-touch-icon.png")}">
<link rel="manifest" href="{href("/assets/site.webmanifest")}">
<link rel="preload" href="{href("/assets/fonts/inter-latin-variable.woff2")}" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{href("/assets/site.css")}?v={CSS_VERSION}">
{f'<script type="application/ld+json">{ld}</script>' if ld else ""}'''


def header_html():
    return f'''<header class="topbar">
<div class="wrap topbar-in">
<a class="brand" href="{href("/")}" aria-label="Belegger Kees, startpagina">Belegger Kees<span class="dot">.</span></a>
<nav class="topnav" aria-label="Hoofdmenu">
<a href="{href("/manifesto/")}">Methode</a>
<a href="{href("/analyseproces/")}">Analyseproces</a>
<a href="{href("/resources/")}">Resources</a>
<a href="{href("/nlp-coaching-voor-beleggers/")}">NLP-coaching</a>
<a href="{href("/over-belegger-kees/")}">Over Kees</a>
</nav>
<a class="btn" href="{esc(CFG["quiz_url"])}">Doe de quiz</a>
</div>
</header>'''


def footer_html(has_disclaimer):
    disc = "" if has_disclaimer else f'<aside class="disclaimer"><p>{esc(DISCLAIMER)}</p></aside>'
    return f'''<footer class="foot">
<div class="wrap">
{disc}
{eco_html()}
<div class="foot-grid">
<div><p class="foot-h">Community en contact</p>
<ul><li><a href="{esc(CFG["quiz_url"])}">Quiz: welke belegger ben jij?</a></li>
<li><a href="{esc(CFG["register_url"])}">Gratis registreren in de Community</a></li>
<li><a href="mailto:{esc(CFG["contact_email"])}">{esc(CFG["contact_email"])}</a></li></ul></div>
<div><p class="foot-h">Betrouwbaarheid</p>
<ul><li><a href="{href("/over-belegger-kees/")}">Over Kees van Wanrooij</a></li>
<li><a href="{href("/docs/redactionele-werkwijze/")}">Redactionele werkwijze</a></li>
<li><a href="{href("/docs/educatieve-afbakening/")}">Educatieve afbakening</a></li>
<li><a href="{href("/docs/bronnen/")}">Bronnen</a></li></ul></div>
<div><p class="foot-h">Deze site</p>
<ul><li><a href="{href("/sitemap/")}">Sitemap</a></li>
<li><a href="{href("/llms.txt")}">llms.txt</a></li>
<li><a href="{esc(CFG["repo_url"])}">Bron op GitHub</a></li>
<li><a href="{esc(CFG["repo_url"])}/issues/new/choose">Een fout melden</a></li></ul></div>
</div>
<p class="foot-note">De inhoud van deze site staat onder <a href="https://creativecommons.org/licenses/by-sa/4.0/deed.nl">CC BY-SA 4.0</a>. Auteur: Kees van Wanrooij, Belegger Kees.</p>
</div>
</footer>'''


def page_html(title, desc, canonical, kind, body_html, current, h1, crumbs=None, ld=None, noindex=False,
              modified=None, has_disclaimer=True, extra_class=""):
    crumb_html = ""
    if crumbs and len(crumbs) > 1:
        crumb_html = '<nav class="crumbs" aria-label="Broodkruimelpad"><ol>' + "".join(
            f'<li><a href="{esc(c[1])}">{esc(c[0])}</a></li>' for c in crumbs[:-1]) + \
            f'<li aria-current="page">{esc(crumbs[-1][0])}</li></ol></nav>'
    return f'''<!doctype html>
<html lang="nl">
<head>
{head(title, desc, canonical, kind, ld, noindex, modified)}
</head>
<body>
<a class="skip" href="#main">Naar de inhoud</a>
{header_html()}
<div class="wrap layout">
<details class="menu"><summary>Menu</summary>{render_nav(current)}</details>
<aside class="side">{render_nav(current)}</aside>
<main id="main" class="{extra_class}">
<article>
{crumb_html}
<h1>{esc(h1)}</h1>
{body_html}
</article>
</main>
</div>
{footer_html(has_disclaimer)}
</body>
</html>
'''


def write(rel, content, binary=False):
    p = os.path.join(OUT, rel)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    if binary:
        open(p, "wb").write(content)
    else:
        open(p, "w", encoding="utf-8", newline="\n").write(content)


def main():
    global CSS_VERSION
    if os.path.exists(OUT):
        shutil.rmtree(OUT)
    os.makedirs(OUT)
    shutil.copytree(os.path.join(SITE_DIR, "assets"), os.path.join(OUT, "assets"))
    css = open(os.path.join(SITE_DIR, "style.css"), encoding="utf-8").read()
    write("assets/site.css", css)
    import hashlib
    CSS_VERSION = hashlib.md5(css.encode()).hexdigest()[:8]

    urls = []
    for p, pg in pages.items():
        kind = "home" if p == "README.md" else "author" if p.startswith("08-Over") and p.endswith("README.md") else "article"
        body = render_md(pg)
        has_disc = DISCLAIMER[:60] in pg["raw"]
        crumbs = breadcrumbs(pg)
        canonical = SITE_URL + pg["url"]
        html_out = page_html(pg["title"], pg["desc"], canonical, kind, body, pg["url"], pg["h1"], crumbs,
                             json_ld(pg, kind), modified=pg["modified"], has_disclaimer=has_disc,
                             extra_class="home" if kind == "home" else "")
        write(pg["url"].strip("/") + "/index.html" if pg["url"] != "/" else "index.html", html_out)
        urls.append((canonical, pg["modified"]))

    # leesbare sitemap
    groups = {}
    for p, pg in sorted(pages.items()):
        top = p.split("/")[0] if "/" in p else ""
        groups.setdefault(top, []).append(pg)
    sm = ""
    for top in sorted(groups):
        lab = "Startpagina" if top == "" else SECTION_LABELS.get(slug(top), top)
        sm += f"<h2>{esc(lab)}</h2><ul>" + "".join(
            f'<li><a href="{href(x["url"])}">{esc(x["h1"])}</a></li>' for x in groups[top]) + "</ul>"
    sm_page = dict(url="/sitemap/", h1="Sitemap", desc="Alle pagina's van de Belegger Kees Methode op één plek, per onderdeel gegroepeerd.",
                   path="sitemap", modified=TODAY, published=TODAY, body="")
    write("sitemap/index.html", page_html("Sitemap | Belegger Kees", sm_page["desc"], SITE_URL + "/sitemap/", "misc", sm,
                                          "/sitemap/", "Sitemap", None, None, has_disclaimer=False))
    urls.append((SITE_URL + "/sitemap/", TODAY))

    # 404
    nf = ('<p>Deze pagina bestaat niet of is verplaatst. Ga terug naar de <a href="' + href("/") + '">startpagina</a>, '
          'kies een onderdeel in het menu, of bekijk de <a href="' + href("/sitemap/") + '">sitemap</a>.</p>')
    write("404.html", page_html("Pagina niet gevonden | Belegger Kees", "Deze pagina bestaat niet. Kies een onderdeel in het menu of ga naar de startpagina.",
                                SITE_URL + "/404.html", "misc", nf, "/404/", "Pagina niet gevonden", None, None,
                                noindex=True, has_disclaimer=False))

    # sitemap.xml, robots.txt, llms.txt
    sx = ['<?xml version="1.0" encoding="UTF-8"?>', f'<?xml-stylesheet type="text/xsl" href="{href("/sitemap.xsl")}"?>',
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u, m in sorted(urls):
        sx.append(f"<url><loc>{esc(u)}</loc><lastmod>{m}</lastmod></url>")
    sx.append("</urlset>")
    write("sitemap.xml", "\n".join(sx) + "\n")
    write("sitemap.xsl", f'''<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:s="http://www.sitemaps.org/schemas/sitemap/0.9">
<xsl:output method="html" encoding="UTF-8" indent="yes"/>
<xsl:template match="/">
<html lang="nl"><head><meta charset="utf-8"/><meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>Sitemap | Belegger Kees</title>
<meta name="robots" content="noindex"/>
<link rel="icon" href="{href("/assets/favicon.svg")}" type="image/svg+xml"/>
<link rel="icon" href="{href("/assets/favicon.ico")}" sizes="48x48"/>
<link rel="stylesheet" href="{href("/assets/site.css")}"/>
</head><body><main class="wrap" style="padding-top:40px;padding-bottom:80px">
<h1>Sitemap</h1>
<p>Dit is het XML-bestand voor zoekmachines met <xsl:value-of select="count(s:urlset/s:url)"/> pagina's. Een leesbare lijst voor mensen staat op de <a href="{href("/sitemap/")}">sitemappagina</a>.</p>
<div class="table-wrap"><table><thead><tr><th>Pagina</th><th>Gewijzigd</th></tr></thead><tbody>
<xsl:for-each select="s:urlset/s:url"><tr><td><a href="{{s:loc}}"><xsl:value-of select="s:loc"/></a></td><td><xsl:value-of select="s:lastmod"/></td></tr></xsl:for-each>
</tbody></table></div></main></body></html>
</xsl:template>
</xsl:stylesheet>
''')
    write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {SITE_URL}/sitemap.xml\n")
    llms = read("llms.txt")
    origin = urlparse(SITE_URL).scheme + "://" + urlparse(SITE_URL).netloc

    def absolute(m):
        target = resolve_link("README.md", m.group(1))
        return "](" + (origin + target if target.startswith("/") else target) + ")"
    llms = re.sub(r"\]\(([^)]+)\)", absolute, llms)
    write("llms.txt", llms)

    # downloads
    for src, dst in STATIC.items():
        if src == "llms.txt":
            continue
        shutil.copyfile(os.path.join(ROOT, src), os.path.join(OUT, dst)) if not os.path.dirname(dst) else (
            os.makedirs(os.path.join(OUT, os.path.dirname(dst)), exist_ok=True),
            shutil.copyfile(os.path.join(ROOT, src), os.path.join(OUT, dst)))
    write(".nojekyll", "")
    cname = os.path.join(SITE_DIR, "CNAME")
    if os.path.exists(cname):
        shutil.copyfile(cname, os.path.join(OUT, "CNAME"))
    print(f"{len(pages)} pagina's, {len(urls)} URL's in de sitemap -> {OUT}")


if __name__ == "__main__":
    main()
