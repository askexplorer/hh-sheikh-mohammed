#!/usr/bin/env python3
"""Builds the Magento CMS blocks (EN + AR) and local preview pages.

    python3 build.py

Outputs:
  dist/cms/hh-en.html, dist/cms/hh-ar.html   -> paste into a Magento CMS page (Page Builder > HTML Code)
  dist/preview/en.html, dist/preview/ar.html -> open locally to review (mock shop header/footer around the block)
  dist/seo.md                                -> meta title/description + hreflang sitemap snippet per language
"""
import json, os, re, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))
import products as P
from strings import STRINGS, PAGE_URL, SITE

ROOT = os.path.dirname(os.path.abspath(__file__))
TEMPLATE = open(os.path.join(ROOT, "src", "template.html"), encoding="utf-8").read()
CMS_IMG = "/media/wysiwyg/hh/"          # where the optimised images get uploaded in Magento
PREVIEW_IMG = "../../img/"

EXTRA = {
    "en": {"meta_short": "Page sections"},
    "ar": {"meta_short": "أقسام الصفحة"},
}


def titles_for(lang):
    S = STRINGS[lang]
    out = []
    for key, _en in P.TITLES:
        n, d = S["titles"][key]
        out.append({"k": key, "n": n, "d": d, "items": P.items(key)})
    return out


def jsonld(lang):
    S = STRINGS[lang]
    page = SITE + PAGE_URL[lang]
    person = {"@type": "Person", "@id": SITE + "/#sheikh-mohammed", "name": "His Highness Sheikh Mohammed bin Rashid Al Maktoum",
              "alternateName": "صاحب السمو الشيخ محمد بن راشد آل مكتوم"}
    publisher = {"@type": "Organization", "name": "Explorer Publishing & Distribution", "url": "https://www.askexplorer.com"}
    books = []
    pos = 0
    for key, en_name in P.TITLES:
        for it in P.items(key):
            if it["f"] == "ebook":
                continue
            pos += 1
            b = {"@type": "Book", "name": en_name, "url": it["u"], "image": it["i"], "author": {"@id": person["@id"]}, "publisher": publisher}
            if it["l"] in P.ISO_LANG:
                b["inLanguage"] = P.ISO_LANG[it["l"]]
            if it["f"] == "paperback":
                b["bookFormat"] = "https://schema.org/Paperback"
            b["offers"] = {"@type": "Offer", "price": str(it["p"]), "priceCurrency": "AED",
                           "availability": "https://schema.org/OutOfStock" if it["o"] else "https://schema.org/InStock", "url": it["u"]}
            books.append({"@type": "ListItem", "position": pos, "item": b})
    graph = [
        person,
        {"@type": "WebPage", "@id": page, "url": page, "name": S["meta_title"], "description": S["meta_desc"], "inLanguage": lang,
         "about": {"@id": person["@id"]}, "primaryImageOfPage": {"@type": "ImageObject", "url": SITE + CMS_IMG + "hh-portrait-blue-1080.webp"}},
        {"@type": "VideoObject", "name": "The Journey: HH Sheikh Mohammed Bin Rashid Al Maktoum",
         "description": "An animation highlighting the most important achievements of His Highness Sheikh Mohammed bin Rashid Al Maktoum.",
         "thumbnailUrl": "https://i.ytimg.com/vi/aRPfsFaw1mk/maxresdefault.jpg", "uploadDate": "2014-03-31",
         "embedUrl": "https://www.youtube.com/embed/aRPfsFaw1mk", "contentUrl": "https://www.youtube.com/watch?v=aRPfsFaw1mk"},
        {"@type": "ItemList", "name": S["shelf_title"], "itemListElement": books},
    ]
    return json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, separators=(",", ":"))


def render(lang, img, alt_url):
    S = STRINGS[lang]
    data = {"titles": titles_for(lang)}
    n_titles = len(P.TITLES)
    n_ed = len(P.ROWS)
    n_lang = len({r[2] for r in P.ROWS if r[2] != "xx"})
    js_str = {
        "lang": lang, "currency": S["currency"], "langs": S["langs"], "fmt": S["fmt"], "add": S["add"], "adding": S["adding"],
        "added": S["added"], "viewEbook": S["view_ebook"], "oos": S["oos"], "allLangs": S["all_langs"], "allFmts": S["all_fmts"],
        "langLabel": S["lang_label"], "fmtLabel": S["fmt_label"], "countNone": S["count_none"], "toastAdded": S["toast_added"],
        "toastViewCart": S["toast_view_cart"], "toastFail": S["toast_fail"], "filmTitle": S["film_title"], "alt2": S["alt_film2"], "play2": S["film_play2"],
    }
    noscript = "".join('<li><a href="%s">%s – %s – %s</a></li>' % (
        it["u"], S["titles"][k][0], S["langs"].get(it["l"], it["l"]), S["fmt"][it["f"]])
        for k, _ in P.TITLES for it in P.items(k))
    tokens = {}
    tokens.update({k: v for k, v in S.items() if isinstance(v, str)})
    tokens.update(EXTRA[lang])
    tokens.update({
        "IMG": img, "SHOP": SITE, "alt_url": alt_url, "alt_lang": "ar" if lang == "en" else "en",
        "STAT_TITLES": str(n_titles), "STAT_EDITIONS": str(n_ed), "STAT_LANGS": str(n_lang),
        "NOSCRIPT": noscript, "JSONLD": jsonld(lang),
        "JSON_STR": json.dumps(js_str, ensure_ascii=False, separators=(",", ":")),
        "JSON_DATA": json.dumps(data, ensure_ascii=False, separators=(",", ":")),
    })
    out = TEMPLATE
    for k, v in tokens.items():
        out = out.replace("[[%s]]" % k, v)
    left = re.findall(r"\[\[[A-Za-z_0-9]+\]\]", out)
    if left:
        raise SystemExit("Unreplaced tokens: %s" % sorted(set(left)))
    return out


SHOP_CSS = [
    "https://shop.askexplorer.com/static/version1790705636/_cache/merged/1ccff07753c32102b1e3c99f186a5c30.css",
    "https://shop.askexplorer.com/static/version1790705636/frontend/Mgs/claue/en_US/MGS_Brand/css/mgs_brand.css",
    "https://shop.askexplorer.com/media/mgs/css/1/custom_config.css",
    "https://fonts.googleapis.com/css2?family=AR+One+Sans:wght@100;200;300;400;500;600;700;800&display=swap",
]

# Real preview: the live shop stylesheets + the real shop header and footer (copied from shop.askexplorer.com on 2026-10-19)
# wrapped around the block, in the same DOM structure the theme uses for a CMS page. Needs an internet connection.
MOCK = """<!doctype html>
<html lang="en" dir="ltr" class="use-header2"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow,noarchive">
<title>%(title)s</title><meta name="description" content="%(desc)s">
%(css)s
</head>
<body class="cms-page-view page-layout-1column wide" id="html-body">
<main><div class="page-wrapper">
%(header)s
<div class="breadcrumbs"><ul class="items"><li class="item home"><a href="https://shop.askexplorer.com/">Home</a></li><li class="item cms_page"><strong>Sheikh Mohammed</strong></li></ul></div>
<section class="page-main container"><div class="columns"><div class="column main">
<div class="page-title-wrapper"><h1 class="page-title"><span class="base">Sheikh Mohammed</span></h1></div>
%(block)s
</div></div></section>
<div class="page-bottom"></div>
%(footer)s
</div></main>
</body></html>
"""

# Offline stand-in (guessed theme globals) used only for local test runs when the shop stylesheets are unreachable.
MOCK_EMU = """<!doctype html>
<html lang="en" dir="ltr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow,noarchive">
<title>%(title)s</title>
<style>body{margin:0;font:14px/1.5 Arial,sans-serif;color:#333;background:#f5f5f5}
.mock-hdr{height:84px;background:#fff;border-bottom:1px solid #ddd;display:flex;align-items:center;justify-content:space-between;padding:0 30px}
.page-main{max-width:1280px;margin:0 auto;padding:0 20px}.mock-ftr{background:#ffed00;color:#000;padding:40px 30px}
html{font-size:10px}body{font-family:Poppins,Arial,sans-serif;font-size:14px;line-height:1.75;color:#878787}
h1,h2,h3{font-weight:600;margin:20px 0 10px;color:#1a1a18;line-height:1.428;letter-spacing:.5px}h1{font-size:48px}h2{font-size:36px}h3{font-size:24px}
p{margin:0 0 10px}figure{margin:1em 40px}img{vertical-align:middle}a{color:#8e8e8e;text-decoration:none}a:hover,a:focus{color:#ffed00;text-decoration:underline}
blockquote{quotes:none;background:#f1f1f1;padding:30px 25px 30px 60px;margin-bottom:20px;position:relative;font-style:italic;font-size:14px;border-radius:4px;border-left:5px solid #eee;font-family:Georgia}
label{display:inline-block;max-width:100%;margin-bottom:9px;font-size:13px;color:#5f5f5f;font-weight:400}select{width:100%;border:1px solid #ccc;border-radius:0}
.btn{display:inline-block;padding:6px 12px;background:#ffed00;color:#333}.price{font-family:Poppins}button{text-transform:none;transition:300ms}ul{list-style:none;margin:0}*{box-sizing:border-box}</style></head>
<body><div class="mock-hdr"><b>EXPLORER SHOP</b><span>Menu</span></div>
<main class="page-main"><div class="columns"><div class="column main">
%(block)s
</div></div></main>
<div class="mock-ftr">Mock footer</div>
</body></html>
"""


def fill_mock(d):
    out = MOCK
    for k, v in d.items():
        out = out.replace('%%(%s)s' % k, v)
    return out


def main():
    os.makedirs(os.path.join(ROOT, "dist", "cms"), exist_ok=True)
    os.makedirs(os.path.join(ROOT, "dist", "preview"), exist_ok=True)
    seo = ["# SEO fields per page\n"]
    for lang in ("en", "ar"):
        S = STRINGS[lang]
        cms = render(lang, CMS_IMG, PAGE_URL["ar" if lang == "en" else "en"])
        open(os.path.join(ROOT, "dist", "cms", "hh-%s.html" % lang), "w", encoding="utf-8").write(cms)
        prev = render(lang, PREVIEW_IMG, ("ar.html" if lang == "en" else "en.html"))
        css = "\n".join('<link rel="stylesheet" href="%s">' % u for u in SHOP_CSS)
        hdr = open(os.path.join(ROOT, "src", "shop", "header.html"), encoding="utf-8").read()
        ftr = open(os.path.join(ROOT, "src", "shop", "footer.html"), encoding="utf-8").read()
        open(os.path.join(ROOT, "dist", "preview", "%s.html" % lang), "w", encoding="utf-8").write(
            fill_mock({"title": S["meta_title"], "desc": S["meta_desc"], "css": css, "header": hdr, "footer": ftr, "block": prev}))
        if os.environ.get("HH_EMU"):
            os.makedirs(os.path.join(ROOT, "dist", "_emu"), exist_ok=True)
            emu = MOCK_EMU
            for k, v in {"title": S["meta_title"], "block": prev}.items():
                emu = emu.replace("%%(%s)s" % k, v)
            open(os.path.join(ROOT, "dist", "_emu", "%s.html" % lang), "w", encoding="utf-8").write(emu)
        seo.append("## %s\n- URL key: `%s`\n- Meta title: %s\n- Meta description: %s\n" % (lang.upper(), PAGE_URL[lang].lstrip("/"), S["meta_title"], S["meta_desc"]))
        print(lang, "cms", len(cms) // 1024, "KB")
    en, ar = SITE + PAGE_URL["en"], SITE + PAGE_URL["ar"]
    seo.append("""## hreflang (XML sitemap)
CMS pages cannot add `<link rel="alternate">` to the head by default, so declare the pair in the XML sitemap
(or via a small layout/head block if your developer prefers):

```xml
<url>
  <loc>%s</loc>
  <xhtml:link rel="alternate" hreflang="en" href="%s"/>
  <xhtml:link rel="alternate" hreflang="ar" href="%s"/>
  <xhtml:link rel="alternate" hreflang="x-default" href="%s"/>
</url>
<url>
  <loc>%s</loc>
  <xhtml:link rel="alternate" hreflang="en" href="%s"/>
  <xhtml:link rel="alternate" hreflang="ar" href="%s"/>
  <xhtml:link rel="alternate" hreflang="x-default" href="%s"/>
</url>
```
(add `xmlns:xhtml="http://www.w3.org/1999/xhtml"` to the `<urlset>` tag)
""" % (en, en, ar, en, ar, en, ar, en))
    open(os.path.join(ROOT, "dist", "seo.md"), "w", encoding="utf-8").write("\n".join(seo))


main()
