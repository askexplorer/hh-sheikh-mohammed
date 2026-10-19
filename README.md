# Sheikh Mohammed books page (EN + AR) for the Explorer Magento shop

## What's here
- `dist/cms/hh-en.html`, `dist/cms/hh-ar.html`: the two pages, ready to paste into Magento CMS pages.
- `img/`: 30 optimised WebP photos (about 150 MB of originals reduced to a few MB).
- `dist/preview/en.html`, `ar.html`: open in a browser (needs internet). They load the real Explorer shop CSS, header and footer so you can judge the page in context. Header menus, icons and search may not work from a local file; the cart is simulated off the shop domain; the film opens on YouTube when the page is opened as a file, and plays in a pop-up once it is on the shop domain.
- `dist/seo.md`: meta title/description for each page and the hreflang sitemap snippet.
- `src/` + `build.py`: copy, product data and template. Edit `src/strings.py`, then run `python3 build.py`.

## Install in Magento (about 10 minutes)
1. Upload everything in `img/` to `pub/media/wysiwyg/hh/` (Content > Elements > Media Gallery > create folder `hh` > upload).
2. Content > Pages > Add new page (English):
   - Title: Books by His Highness Sheikh Mohammed bin Rashid Al Maktoum. URL key: `sheikh-mohammed`.
   - Content heading: leave empty. Layout: 1 column.
   - Content: Page Builder > drag an **HTML Code** element in, paste all of `hh-en.html`. (If your editor is plain WYSIWYG, switch it off with "Show / Hide Editor" first, or the script gets stripped.)
   - Search Engine Optimization tab: paste meta title and description from `dist/seo.md`.
3. Repeat for Arabic with URL key `sheikh-mohammed-ar` and `hh-ar.html`.
4. Add the hreflang pair to your XML sitemap (snippet in `dist/seo.md`).
5. System > Cache Management > flush.
If you pick different URL keys, change `PAGE_URL` in `src/strings.py` and rebuild.

## How the cart works
Each print edition posts to Magento's own `/checkout/cart/add/product/<id>` with the page's `form_key`, then refreshes the mini-cart. If the add is rejected the visitor is sent to the product page. eBooks and out-of-stock editions don't add to cart (eBooks link to their product page because their listing shows no price).
Tested against the live shop: a guest add of My Story Paperback (English) took the cart from 0 to 1 at AED 49, and the item was removed again.

## Needs your input before launch
- Replace every "Placeholder" text and the quote (English and Arabic).
- Confirm the Arabic titles for Mission to Mars, The Sheikh CEO and Zayed.
- Product prices and stock are in `src/products.py` (snapshot of 2026-10-19). Cart prices always come from Magento, but displayed prices on the page are from that snapshot. Re-run the capture when prices change.
- The film is the 2014 YouTube video; replace the ID `aRPfsFaw1mk` in the template when you have a newer one.

## Design notes
- Fonts follow the shop theme: Poppins for text and buttons, Libre Baskerville for headings and the quote; Arabic uses AR One Sans and Amiri.
- Motion (no Magento extension needed): word-by-word headline reveal, count-up stats, parallax on photos, hover tilt on covers, button shine, add-to-cart pop. All switch off for visitors who prefer reduced motion.
- On the live theme the block hides the breadcrumb and page title and removes the page padding so the hero meets the header and the footer directly. Checked on shop.askexplorer.com with the real theme CSS.

## Round 2 changes
- Film: three-stage portrait poster with a play button; the video plays inside the page (no jump to YouTube). A second tab plays the "My Story" YouTube playlist in the same player.
- Top bar: only the Arabic / English switch.
- Hero: image width is capped by the hero height so wide screens show the whole figure, not just the head.
- Quote: his portrait is the section background. The face stays centred and the words sit in the dark side (below 1000px the picture stacks above the words).
- Free-shipping line removed (it is in the shop footer).
- Language availability confirmed: Mission to Mars (Arabic + English), The Sheikh CEO (English only), Zayed (Arabic only).

## Review with the team
Text to supply is marked "Placeholder" in `src/strings.py` (English block and Arabic block). Edit it, run `python3 build.py`, and `dist/cms/` holds the updated blocks.

## Keeping it out of search engines
This repo holds draft copy. `robots.txt` and the `noindex` tag in the preview pages ask crawlers to skip it, but they are requests, not locks. A public GitHub repo can still be indexed, so keep the repo **private** while the team reviews. The live CMS blocks (`dist/cms/`) are not marked noindex, because those are the real shop pages.

## How to preview from this repo
1. Download or clone the repo (Code > Download ZIP, then unzip).
2. **Mac:** double-click `Preview.command` (right-click > Open if macOS blocks it). **Any system:** in the folder, run `python3 -m http.server 8765`, then open http://localhost:8765/dist/preview/en.html (Arabic: `ar.html`).
3. The video plays inside the page only when served this way. Opening the HTML file directly shows everything except in-page video.
The preview loads the real shop styling from the internet. Menus and search don't work and the cart is simulated.
