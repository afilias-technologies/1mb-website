# 1mb-website
This is source for website that acts as reference for page weight measurement tools

The web development community was missing a page size reference. This site is that reference—the International Prototype of the Kilogram, but for web.

The transfer size of this website is precisely 1 MB or 1,000,000 bytes by definition. Transfer size means the amount of data that must be transferred over the network to the browser in order to display the page fully.

The exact resources that constitute a web page are not mandatory; clients are not obliged to fetch all of them. In this case the 1 MB transfer size is reached if the browser downloads all linked images, JavaScript, CSS and the site's favicon, as the vast majority of browsers do. The 1 MB transfer size includes the size of the response headers from the web server in its totals, since these are part of the cost of fetching a page.

If your web test tool reports anything other than exactly 1 MB as the size of this page it is either incorrect or is measuring something different.

Note that the page weight of the resulting website depends on multiple aspects of your web server configuration. In this case gzip compression is enabled for everything except JPEG images.

This site is currently hosted at http://1mb.website.
