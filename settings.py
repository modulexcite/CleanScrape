#!/usr/bin/env python

"""
This file defines the configuration settings for CleanScraper.py;
change them according to your environment, or use a local_settings.py
file which is excluded from source control.

"""

from string import Template

ENCODING = 'utf-8'
UA = "CleanScrape/1.0 +http://github.com/dpapathanasiou/CleanScrape"

# Define where the converted epub and pdf files will reside
OUTPUT_FOLDER = '/tmp'

#
# EPUB conversion

# Get and install pandoc from:
# http://johnmacfarlane.net/pandoc/installing.html
# and update this path accordingly
PANDOC_PATH = '/usr/bin'

EPUB_XML = Template("""<dc:title>$title</dc:title>
<dc:language>$lang</dc:language>
<dc:date>$date</dc:date>
$identifier""")

ISBN_XML = Template('<dc:identifier id="BookId" opf:scheme="ISBN">urn:isbn:$isbn_number</dc:identifier>')

EPUB_CSS   = 'epub.css'
EPUB_COVER = 'epub_cover.jpg'
EPUB_LANG  = 'en-US'

#
# PDF conversion

# Get and install wkhtmltopdf from:
# http://wkhtmltopdf.org/
# and update this path accordingly
WKHTMLTOX_PATH  = '/usr/local/bin'

# Set the pdf output page size
PDF_PAGE_SIZE = 'Letter'

# Define the html which frames the content to be converted
# into pdf format in this string template
HTML_FRAME = Template(u"""<html><head><meta charset="utf-8"><title>$title</title></head><body>
<div style="text-align:center"><div style="margin:0 auto;width:85%;text-align:left">
$content
</div></div>
<hr>
<p style="font-size:0.8em;font-weight:lighter;font-style:italic;font-family:sans-serif;color:#808080">Source: <a href="$url">$url</a><br />
Generated by <a href="https://github.com/dpapathanasiou/CleanScrape">CleanScrape</a></p>
</body></html>""") 

# Override any of the above settings for your local environment in a
# separate local_settings.py file which is *not* checked into  source
# control

try:
    from local_settings import *
except ImportError:
    pass
