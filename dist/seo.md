# SEO fields per page

## EN
- URL key: `sheikh-mohammed`
- Meta title: Books by His Highness Sheikh Mohammed bin Rashid Al Maktoum | Explorer
- Meta description: Discover and buy the books of His Highness Sheikh Mohammed bin Rashid Al Maktoum: My Story, Lessons from Life, Flashes of Verse and more, in print and digital, in many languages.

## AR
- URL key: `sheikh-mohammed-ar`
- Meta title: كتب صاحب السمو الشيخ محمد بن راشد آل مكتوم | إكسبلورر
- Meta description: اكتشف واقتنِ كتب صاحب السمو الشيخ محمد بن راشد آل مكتوم: قصتي، علّمتني الحياة، ومضات من شعر وغيرها، بنسخ مطبوعة ورقمية وبلغات عدة.

## hreflang (XML sitemap)
CMS pages cannot add `<link rel="alternate">` to the head by default, so declare the pair in the XML sitemap
(or via a small layout/head block if your developer prefers):

```xml
<url>
  <loc>https://shop.askexplorer.com/sheikh-mohammed</loc>
  <xhtml:link rel="alternate" hreflang="en" href="https://shop.askexplorer.com/sheikh-mohammed"/>
  <xhtml:link rel="alternate" hreflang="ar" href="https://shop.askexplorer.com/sheikh-mohammed-ar"/>
  <xhtml:link rel="alternate" hreflang="x-default" href="https://shop.askexplorer.com/sheikh-mohammed"/>
</url>
<url>
  <loc>https://shop.askexplorer.com/sheikh-mohammed-ar</loc>
  <xhtml:link rel="alternate" hreflang="en" href="https://shop.askexplorer.com/sheikh-mohammed"/>
  <xhtml:link rel="alternate" hreflang="ar" href="https://shop.askexplorer.com/sheikh-mohammed-ar"/>
  <xhtml:link rel="alternate" hreflang="x-default" href="https://shop.askexplorer.com/sheikh-mohammed"/>
</url>
```
(add `xmlns:xhtml="http://www.w3.org/1999/xhtml"` to the `<urlset>` tag)
