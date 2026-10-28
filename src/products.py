# Product data captured from https://shop.askexplorer.com/sheikh-mohammed-books.html (pages 1 and 2) on 2026-10-19.
# (id, title_key, lang, fmt, price, url, image_path, out_of_stock)
# fmt: print | paperback | ebook | audio | braille.  audio and braille rows link to an external page (or a shop product), with no cart button.  ebooks have no price in the listing, so they link to the product page.

SHOP = "https://shop.askexplorer.com"
IMG = SHOP + "/media/catalog/product/cache/b86d527f2b20d32aba03f0618086efa3/"

LFL = "lessons-from-life-part-%s-%s-by-his-highness-sheikh-mohammed-bin-rashid-al-maktoum%s.html"

ROWS = [
    # My Story
    (2987, "my-story", "ar", "print", 110, "my-story-arabic-arabic.html", "t/m/tmp1873_1633158494.png", 0),
    (2896, "my-story", "en", "print", 110, "uae-mst-01-p-0-en-tu2110140415.html", "t/m/tmp1854_1622716478_1_1_1.png", 0),
    (2872, "my-story", "fr", "print", 110, "uae-mst-01-p-0-fr-3g2110140412.html", "t/m/tmp1880_1622716540.png", 0),
    (2884, "my-story", "de", "print", 110, "uae-mst-01-p-0-de-cr2110140413.html", "t/m/tmp1878_1622715690.png", 0),
    (2891, "my-story", "zh", "print", 110, "uae-mst-01-p-0-ch-ms2110140415.html", "t/m/tmp1882_1622715843.png", 0),
    (2880, "my-story", "ru", "print", 110, "uae-mst-01-p-0-ru-q72110140413.html", "t/m/tmp1884_1622715551.png", 0),
    (2883, "my-story", "es", "print", 110, "uae-mst-01-p-0-sp-co2110140413.html", "t/m/tmp1886_1622715606.png", 0),
    (3061, "my-story", "ar", "paperback", 49, "my-story-paperback-arabic.html", "u/a/uae-mst-01-p-0-ar-sb-3d.png", 0),
    (3062, "my-story", "en", "paperback", 49, "my-story-paperback-english.html", "u/a/uae-mst-01-p-0-en-sb-3d.png", 0),
    (3060, "my-story", "ru", "paperback", 49, "my-story-paperback-russian.html", "u/a/uae-mst-01-p-0-ru-sb-3d.png", 0),
    (2997, "my-story", "ar", "ebook", None, "uae-mst-01-e-0-ar-ep2111041121.html", "t/m/tmp1872_1637225626_1.png", 0),
    (2998, "my-story", "en", "ebook", None, "uae-mst-01-e-0-en-gy2111041122.html", "t/m/tmp1877_1637226017_1_1_1.png", 0),
    (2992, "my-story", "fr", "ebook", None, "uae-mst-01-e-0-fr-wz2111041121.html", "t/m/tmp1881_1637226260_1.png", 0),
    (2995, "my-story", "de", "ebook", None, "uae-mst-01-e-0-de-ho2111041121.html", "t/m/tmp1879_1637225927_1.png", 0),
    (3016, "my-story", "fa", "ebook", None, "uae-mst-01-e-0-fa-vc2111190214.html", "t/m/tmp1922_1637226185_1.png", 0),
    (3014, "my-story", "hi", "ebook", None, "uae-mst-01-e-0-hi-cz2111190214.html", "t/m/tmp1927_1637226348_1.png", 0),
    (3015, "my-story", "ja", "ebook", None, "uae-mst-01-e-0-jp-y72111190214.html", "t/m/tmp1921_1637226534_1.png", 0),
    (2991, "my-story", "ko", "ebook", None, "uae-mst-01-e-0-kr-n72111041121.html", "t/m/tmp1920_1637226615_1.png", 0),
    (2993, "my-story", "zh", "ebook", None, "uae-mst-01-e-0-ch-v52111041121.html", "t/m/tmp1883_1637225832_1.png", 0),
    (2994, "my-story", "ru", "ebook", None, "uae-mst-01-e-0-ru-p52111041121.html", "t/m/tmp1885_1637227472_1.png", 0),
    (2996, "my-story", "es", "ebook", None, "uae-mst-01-e-0-sp-uu2111041121.html", "t/m/tmp1887_1637227541_1.png", 0),
    # Lessons from Life, Part I
    (3065, "lessons-1", "ar", "print", 89, LFL % ("one", "ar", ""), "u/a/uae-lfl-01-p-0-ar_3d_2.png", 0),
    (3071, "lessons-1", "en", "print", 89, LFL % ("one", "en", ""), "u/a/uae-lfl-01-p-0-en_3d_1_1.png", 0),
    (3078, "lessons-1", "fr", "print", 89, LFL % ("one", "fr", ""), "u/a/uae-lfl-01-p-0-fr_3d.png", 0),
    (3079, "lessons-1", "de", "print", 89, LFL % ("one", "de", ""), "t/m/tmp2395_1771898245_1.png", 0),
    (3076, "lessons-1", "zh", "print", 89, LFL % ("one", "zh", ""), "t/m/tmp2392_1771898195_1.png", 0),
    (3077, "lessons-1", "ru", "print", 89, LFL % ("one", "ru", ""), "t/m/tmp2391_1771898216_1.png", 0),
    (3080, "lessons-1", "es", "print", 89, LFL % ("one", "es", ""), "t/m/tmp2394_1771898156_1.png", 0),
    (3098, "lessons-1", "ar", "ebook", None, LFL % ("one", "ar", "-1"), "u/a/uae-lfl-01-e-0-ar_3d.png", 0),
    (3097, "lessons-1", "en", "ebook", None, LFL % ("one", "en", "-1"), "u/a/uae-lfl-01-e-0-en_3d.png", 0),
    # Lessons from Life, Part II
    (3092, "lessons-2", "ar", "print", 89, "lessons-from-life-part-two-the-letters-ar-by-his-highness-sheikh-mohammed-bin-rashid-al-maktoum.html", "u/a/uae-lfl-02-p-0-ar_3d_2.png", 0),
    (3093, "lessons-2", "en", "print", 89, "lessons-from-life-part-two-the-letters-en-by-his-highness-sheikh-mohammed-bin-rashid-al-maktoum.html", "u/a/uae-lfl-02-p-0-en_3d.png", 0),
    # Flashes of Verse
    (2949, "flashes", "xx", "print", 70, "flashes-of-verse.html", "u/a/uae-fvl-01-p-0-ml-ar.png", 0),
    (3009, "flashes", "xx", "ebook", None, "uae-fvr-01-e-0-ml-5o2111041122.html", "t/m/tmp1367_1637119938_1.png", 0),
    # Mission to Mars
    (2928, "mars", "ar", "print", 120, "uae-mar-01-p-1-ar-xj2110140420.html", "t/m/tmp1654_1622698782_1.png", 0),
    (2929, "mars", "en", "print", 120, "uae-mar-01-p-1-en-la2110140420.html", "t/m/tmp1653_1622701713.png", 0),
    # Reflections on Happiness & Positivity
    (2927, "reflections", "fr", "print", 79, "uae-rop-01-p-0-fr-062110140420.html", "t/m/tmp1716_1622704220.png", 0),
    (2923, "reflections", "hi", "print", 79, "uae-rop-01-p-0-hi-cj2110140419.html", "t/m/tmp1714_1622704591.png", 0),
    (3056, "reflections", "id", "print", 79, "uae-rop-01-p-0-in-gp2405220524.html", "t/m/tmp2282_1716355252_1.png", 0),
    (2919, "reflections", "kk", "print", 79, "uae-rop-01-p-0-ka-ra2110140419.html", "t/m/tmp1742_1622704695.png", 0),
    (2926, "reflections", "ru", "print", 79, "uae-rop-01-p-0-ru-nd2110140420.html", "t/m/tmp1711_1622719139.png", 0),
    (2925, "reflections", "es", "print", 79, "uae-rop-01-p-0-sp-4j2110140419.html", "t/m/tmp1715_1622704268.png", 0),
    (2922, "reflections", "ur", "print", 79, "uae-rop-01-p-0-ur-m02110140419.html", "t/m/tmp1712_1622702319.png", 0),
    (0, "reflections", "ar", "print", 79, "uae-rop-01-p-0-ar-xe2408070715.html", "t/m/tmp1460_1622713633_1_1_1.png", 1),
    (0, "reflections", "ja", "print", 79, "uae-rop-01-p-0-jp-2f2110140417.html", "t/m/tmp1839_1622712795.png", 1),
    (0, "reflections", "zh", "print", 79, "uae-rop-01-p-0-ch-ut2110140419.html", "t/m/tmp1713_1622712965_1.png", 1),
    # The Sheikh CEO / Zayed
    (2854, "ceo", "en", "print", 95, "uae-ceo-01-p-3-en-vy2110140411.html", "t/m/tmp1955_1632996333_1_1_1.png", 0),
    (2913, "zayed", "ar", "print", 95, "uae-zyr-01-p-0-ar-fe2110140418.html", "t/m/tmp1802_1622710437.png", 0),
]

# Title order on the page, with the English name used for SEO/JSON-LD.
TITLES = [
    ("my-story", "My Story"),
    ("lessons-1", "Lessons from Life: Part I"),
    ("lessons-2", "Lessons from Life: Part II – The Letters"),
    ("flashes", "Flashes of Verse"),
    ("mars", "Mission to Mars"),
    ("reflections", "Reflections on Happiness & Positivity"),
    ("ceo", "The Sheikh CEO"),
    ("zayed", "Zayed"),
]

ISO_LANG = {"ar": "ar", "en": "en", "fr": "fr", "de": "de", "zh": "zh", "ru": "ru", "es": "es", "fa": "fa",
            "hi": "hi", "ja": "ja", "ko": "ko", "id": "id", "kk": "kk", "ur": "ur"}


def items(key):
    out = []
    for (pid, k, lang, fmt, price, url, img, oos) in ROWS:
        if k != key:
            continue
        out.append({"id": pid, "l": lang, "f": fmt, "p": price, "u": SHOP + "/" + url, "i": IMG + img, "o": oos})
    return out
