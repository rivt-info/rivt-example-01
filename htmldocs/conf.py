import sys
import os
from pathlib import Path
sys.path.append(str(Path(".").resolve()))
pypathS = os.path.dirname(sys.executable)
rvstyleP = os.path.join(
    pypathS,
    "Lib",
    "site-packages",
    "rivtlib",
    "styles",
)
project = 'rivt.info'
copyright = '2023 StructureLabs LLC'
author = 'rholland'
release = '0.3.0'

extensions = ['sphinx.ext.githubpages','sphinx_togglebutton',
              "sphinxcontrib.jquery", 'sphinx_copybutton',
              'sphinx_favicon', 'sphinx.ext.duration',
              'sphinx.ext.doctest', 'sphinx.ext.autodoc',
              'sphinx_design','sphinx_new_tab_link',
              'rst2pdf.pdfbuilder']
master_doc = 'index'
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
source_suffix = ['.rst', '.md']
templates_path = ['_templates']
locale_dirs = ['_locale'] 
html_title = "rivt"
html_theme = 'pydata_sphinx_theme'
html_show_sourcelink = False
html_context = {"default_mode": "dark"}
html_sidebars = {"**": ["sidebar-nav-bs.html"]}
html_static_path = ['_static', '_static/img']
html_css_files = ['css/custom.css',]
html_theme_options = {
    "pygments_light_style": "tango",  
    "pygments_dark_style": "github-dark",   
    "navbar_start": ["navbar-logo"],
    "collapse_navigation": True ,
    "header_links_before_dropdown": 6,
    "navbar_align": "left",
    "show_toc_level": 1,
    "navigation_depth": 1,
    "footer_start": ["copyright"],
    "footer_end": [],
    "logo": {
        "text": "rivt",
        "image_dark": "rivhome11c.png",
        "image_light": "rivhome11c.png",
    }
}
favicons = [
    {
        "rel": "icon",
        "sizes": "16x16",
        "href": "favicon-16x16.png",
    },
    {
        "rel": "icon",
        "sizes": "32x32",
        "href": "favicon-32x32.png",
    },

]

# -- Options for PDF output -------------------------------------------------
# List of tuples  (source start file, target name, title, author, options).
# The options element is a dictionary that lets you override
# this config per-document. For example:
# ('index', 'MyProject', 'My Project', 'Author Name', {'pdf_compressed': True})
# More than one author, separate them with \\.
# r'Guido van Rossum\\Fred L. Drake, Jr., editor'
#
pdf_documents = [
    ('index', 'rivt_manual', 'rivt', 'r holland'),
]
# Label to use as a prefix for the subtitle on the cover page
subtitle_prefix = 'User Manual'
# A list of folders to search for stylesheets. Example:
pdf_style_path = ['./pdfdocs/stylepdf']
# A colon-separated list of folders to search for fonts. Example:
pdf_font_path = ['./pdfdocs/fontpdf']
# A comma-separated list of custom stylesheets. Example:
pdf_stylesheets = ['stylepdf1.yaml']
# Example: compressed=True
pdf_compressed = False
# Language to be used for hyphenation support
pdf_language = "en_US"
# literal blocks wider than the frame overflow, shrink or truncate
pdf_fit_mode = "shrink"
# 1 means top-level sections start in a new page 0 disabled
pdf_break_level = 0
# When a section starts in a new page, force it to be 'even', 'odd',
# or just use 'any'
pdf_breakside = 'any'
# If false, no coverpage is generated.
pdf_use_coverpage = True
# Name of the cover page template to use
pdf_cover_template = 'pdfcover.rst'
# Page template name for "regular" pages
# pdf_page_template = 'cutePage'
# Documents to append as an appendix to all manuals.
# pdf_appendices = []
# Enable experimental feature to split table cells. Use it
# if you get "DelayedTable too big" errors
# pdf_splittables = False
# Set the default DPI for images
# pdf_default_dpi = 72
# Enable rst2pdf extension modules
# pdf_extensions = []
# Show Table Of Contents at the beginning?
pdf_use_toc = True
# How many levels deep should the table of contents be?
pdf_toc_depth = 9999
# Insert footnotes where they are defined instead of
# at the end.
pdf_inline_footnotes = True
# verbosity level. 0 1 or 2
# pdf_verbosity = 0
# If false, no index is generated.
pdf_use_index = True
# If false, no modindex is generated.
pdf_use_modindex = False
# Add section number to section references
pdf_use_numbered_links = False
# Background images fitting mode
pdf_fit_background_mode = 'scale'
# Repeat table header on tables that cross a page boundary?
pdf_repeat_table_rows = True
# Enable smart quotes (1, 2 or 3) or disable by setting to 0
pdf_smartquotes = 0