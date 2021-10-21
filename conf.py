# Configuration file for the Sphinx documentation builder.
# This file only contains a selection of the most common options.
# For a full list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------
# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
import os
import sys
import re
# sys.path.insert(0, os.path.abspath('.'))
import sphinx_rtd_theme
from sphinx.locale import _

# -- Project information -----------------------------------------------------
project = u'jamovi'
slug = re.sub(r'\W+', '-', project.lower())
author = u'The section authors, The jamovi project, and Sebastian Jentschke (curating this documentation)'
copyright = u'2020, ' + author + '. This work is licensed under a Creative Commons Attribution-Non Commercial 4.0 International License.'
# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'en'
locale_dirs = ['_locale']
gettext_compact = False

# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
#   'sphinx.ext.imgmath',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'sphinx_copybutton',
    'sphinx_multiversion',
]

# Add any paths that contain templates here, relative to this directory.
# templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', '_tmp', '_env', 'Thumbs.db', '.DS_Store', 'README.*']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
source_suffix = ['.rst', '.md']

# The master toctree document.
master_doc = 'index'

# Automatically number figures, tables and code-blocks if they have a caption
numfig = True

# Whether codeauthor and sectionauthor directives produce any output in the built files
show_authors = True

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'default'


# -- Options for HTML output -------------------------------------------------
# Customize the "best image" order for the StandaloneHTMLBuilder class.
from sphinx.builders.html import StandaloneHTMLBuilder
StandaloneHTMLBuilder.supported_image_types = [
    'image/svg+xml',
    'image/gif',
    'image/png',
    'image/jpeg'
]

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = "sphinx_rtd_theme"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the documentation.
# https://sphinx-rtd-theme.readthedocs.io/en/latest/configuring.html
html_theme_options = {
    # Google Analytics
#   'analytics_id': 'G-XXXXXXXXXX',
    'analytics_anonymize_ip': False,
    # show version number is shown at the top of the sidebar (default: True)
    'display_version': False,
    # only display the logo image, do not display the project name at the top of the sidebar (default: False)
    'logo_only': True,
    # location of the prev / next buttons (default: 'bottom') and allow navigating using the keyboard’s left and right arrows (default: False)
    'prev_next_buttons_location': 'bottom',
    'navigation_with_keys': True,
    # add an icon next to external links (default: False)
    'style_external_links': False,
    # display style for code-versioning-systems (github, etc.)     
    'vcs_pageview_mode': '',
    # changes the background of the search area in the navigation bar
    'style_nav_header_background': '#FFFFFF',
    # width of the sidebar (defaults to 230 pixels)
    'sidebarwidth': '20%',
    # minimal and maximal width of the document body (use 'none' if you don’t want a width limit; defaults depend on the theme: often 450px [min] and 800px [max])
    'body_min_width': 0,
    'body_max_width': 0,
    # ToC options
    # navigation entries are not expandable – the [+] icons next to each entry are removed (default: True)
    'collapse_navigation': True,
    # scroll the navigation with the main page content as you scroll the page
    'sticky_navigation': True,
    # maximum depth of the table of contents tree (default: 4; allow unlimited depth: -1)
    'navigation_depth': 3,
    # whether the navigation includes hidden table(s) of contents (i.e., toctree directives marked with the :hidden: option; default: True)
    'includehidden': True,
    # page subheadings are not included in the navigation (default: False)
    'titles_only': True
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = [u'_static']

# The “title” for HTML documentation generated with Sphinx’s own templates.
# This is appended to the <title> tag of individual pages, and used in the
# navigation bar as the “topmost” element. It defaults to '<project> v<revision> documentation'.
html_title = 'jamovi Documentation'

# Name of an image file (path relative to the configuration directory) that is the logo of the docs.
# It is placed at the top of the sidebar; its width should therefore not exceed 200 pixels. Default: None.
html_logo = '_images/header-logo.svg'

# Name of an image file (path relative to the configuration directory) that is the favicon of the docs.
# Modern browsers use this as the icon for tabs, windows and bookmarks. It should be a Windows-style icon file (.ico), which is 16x16 or 32x32 pixels large. Default: None.
html_favicon = '_images/jamovi-v.svg'

# A list of CSS files. The entry must be a filename string or a tuple containing the filename string and the attributes dictionary.
# The filename must be relative to the html_static_path, or a full URI with scheme like http://example.org/style.css.
# The attributes is used for attributes of <link> tag. It defaults to an empty list.
# Example:
# html_css_files = ['custom.css',
#                   'https://example.com/css/custom.css',
#                   ('print.css', {'media': 'print'})]
html_css_files = ['jamovi.css', # jamovi style (adapted)
                 ]

# Custom sidebar templates, must be a dictionary that maps document names to template names.
# The list specifies the complete list of sidebar templates to include.
# If all or some of the default sidebars are to be included, they must be put into this list as well.
# The default sidebars (for documents that don’t match any pattern) are defined by theme itself.
# Builtin themes are using these templates by default: ['localtoc.html', 'relations.html', 'sourcelink.html', 'searchbox.html'].
# Builtin sidebar templates that can be rendered are:
# localtoc.html – a fine-grained table of contents of the current document
# globaltoc.html – a coarse-grained table of contents for the whole documentation set, collapsed
# relations.html – two links to the previous and next documents
# sourcelink.html – a link to the source of the current document, if enabled in html_show_sourcelink
# searchbox.html – the “quick search” box
# Example:
# html_sidebars = {'**':            ['globaltoc.html', 'sourcelink.html', 'searchbox.html'],
#                  'using/windows': ['windowssidebar.html', 'searchbox.html'], }
# This will render the custom template windowssidebar.html and the quick search box within the sidebar of the given document, 
# and render the default sidebars for all other pages (except that the local TOC is replaced by the global TOC).
# Note that this value only has no effect if the chosen theme does not possess a sidebar, like the builtin scrolls and haiku themes.
html_sidebars = {'**': ['localtoc.html',
                        'globaltoc.html',
                        'relations.html',
                        'searchbox.html',
                        'versioning.html'], }

# If true, the reST sources are included in the HTML build as _sources/name. The default is True.
html_copy_source = False

# If true (and html_copy_source is true as well), links to the reST sources will be added to the sidebar. The default is True.
html_show_sourcelink = False

# If true, “Created using Sphinx” is shown in the HTML footer. Default is True.
html_show_sphinx = False

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
html_show_copyright = True


# -- Options for HTMLHelp output ------------------------------------------
# Output file base name for HTML help builder.
htmlhelp_basename = 'jamoviDocs'

# -- Options for shinx-multiversion ---------------------------------------
smv_tag_whitelist = ""  				# Whitelist pattern for tags (set to None to ignore all tags)
smv_branch_whitelist = ""    			# Whitelist pattern for branches (set to None to ignore all branches)
smv_remote_whitelist = None				# Whitelist pattern for remotes (set to None to use local branches only)
smv_released_pattern = r'^tags/.*$'		# Pattern for released versions
smv_outputdir_format = '{ref.name}'		# Format for versioned output directories inside the build directory
smv_prefer_remote_refs = False			# Determines whether remote or local git branches/tags are preferred if their output dirs conflict


# -- Options for ePub output ----------------------------------------------
# Options for epub output
# These options influence the epub output. As this builder derives from the HTML builder, the HTML options also apply where appropriate.
# The actual values for some of the options is not really important, they just have to be entered into the Dublin Core metadata.

# The basename for the epub file. It defaults to the project name.
epub_basename = 'jamoviDocs'

# The title and the description of the document. It defaults to the html_title option but can be set independently for epub creation. It defaults to the project option.
epub_title = 'Documentation for jamovi'
epub_description = 'Documentation for jamovi, a free and open statistical software to bridge the gap between researcher and statistician.'
epub_publisher = 'www.jamovi.org'
# An identifier and the publication scheme for the document. This is put in the Dublin Core metadata.
# For published documents this is the ISBN number and the scheme is 'ISBN'.
# You can also use an alternative scheme, e.g. the project homepage, then the scheme is 'URL'. 
# NB: Might be wise to set this to a DOI later.
epub_identifier = 'www.jamovi.org'
epub_scheme = 'URL'
# The cover page information. This is a tuple containing the filenames of the cover image and the html template.
# The rendered html cover page is inserted as the first item in the spine in content.opf. If the template filename is empty,
# no html cover page is created. No cover at all is created if the tuple is empty. Examples:
# epub_cover = ('_static/cover.png', 'epub-cover.html')
# epub_cover = ('_static/cover.png', '')
epub_cover = ()

# Meta data for the guide element of content.opf. This is a sequence of tuples containing the type, the uri and the title of the optional guide information.
# See the OPF documentation at http://idpf.org/epub for details. If possible, default entries for the cover and toc types are automatically inserted.
# However, the types can be explicitly overwritten if the default entries are not appropriate. Example:
# epub_guide = (('cover', 'cover.html', u'Cover Page'),)
epub_guide = ()

# Additional files that should be inserted before or after the text generated by Sphinx. It is a list of tuples containing the file name and the title.
# If the title is empty, no entry is added to toc.ncx. Example:
# epub_pre_files = [('index.html', 'Welcome'), ]
epub_pre_files = []
epub_post_files = []
# A list of files that are generated/copied in the build directory but should not be included in the epub file.
epub_exclude_files = []

# The depth of the table of contents in the file toc.ncx. It should be an integer greater than zero. The default value is 3. Note: A deeply nested table of contents may be difficult to navigate.
epub_tocdepth = 2
# This flag determines if a toc entry is inserted again at the beginning of its nested toc listing.
# This allows easier navigation to the top of a chapter, but can be confusing because it mixes entries of different depth in one list. The default value is True.
epub_tocdup = False
# This setting control the scope of the epub table of contents. The setting can have the following values:
# 'default' – include all toc entries that are not hidden (default)
# 'includehidden' – include all toc entries
epub_tocscope = 'default'

# Determines if sphinx should try to fix image formats that are not supported by some epub readers.
# At the moment palette images with a small color table are upgraded. You need Pillow, the Python Image Library, installed to use this option.
# The default value is False because the automatic conversion may lose information.
epub_fix_images = False
# This option specifies the maximum width of images. If it is set to a value greater than zero,
# images with a width larger than the given value are scaled accordingly. If it is zero, no scaling is performed.
# The default value is 0. You need the Python Image Library (Pillow) installed to use this option.
epub_max_image_width = 1

# Control whether to display URL addresses. This is very useful for readers that have no other means to display the linked URL. The settings can have the following values:
# 'inline' – display URLs inline in parentheses (default)
# 'footnote' – display URLs in footnotes
# 'no' – do not display URLs
epub_show_urls = 'inline'

# If true, add an index to the epub document. It defaults to the html_use_index option but can be set independently for epub creation.
epub_use_index = True

# It specifies writing direction. It can accept 'horizontal' (default) and 'vertical'
# https://developer.mozilla.org/en-US/docs/Web/CSS/writing-mode
epub_writing_mode = 'horizontal'


# -- Options for LaTeX output ---------------------------------------------
# The LaTeX engine to build the docs. The setting can have the following values:
# 'pdflatex' (default), 'xelatex' (default for 'ch', 'gr'), 'lualatex', 'platex' (default for 'ja'), 'uplatex' (experimental)
# 'pdflatex'’s support for Unicode characters is limited.
# 'pdflatex' support in Latin language document adds support of occasional Cyrillic or Greek letters or words. This is not automatic, see the discussion of the latex_elements 'fontenc' key.
# If your project uses Unicode characters, setting the engine to 'xelatex' or 'lualatex' and making sure to use an OpenType font with wide-enough glyph coverage is often easier
# than trying to make 'pdflatex' work with the extra Unicode characters. Since Sphinx 2.0 the default is the GNU FreeFont which covers well Latin, Cyrillic and Greek.
# Contrarily to MathJaX math rendering in HTML output, LaTeX requires some extra configuration to support Unicode literals in math:
# the only comprehensive solution (as far as we know) is to use 'xelatex' or 'lualatex' and to add r'\usepackage{unicode-math}' (e.g. via the latex_elements 'preamble' key).
# You may prefer r'\usepackage[math-style=literal]{unicode-math}' to keep a Unicode literal such as α (U+03B1) for example as is in output, rather than being rendered as α.
latex_engine = 'xelatex'

# Grouping the document tree into LaTeX files. List of tuples
#   (source start file, target name,      title,                       author,                theme,    toctree_only).
latex_documents = [
    (master_doc,        'jamoviDocs.tex', u'Documentation for jamovi', u'The jamovi project', 'manual', True),
]

# If given, this must be the name of an image file (relative to the configuration directory) that
# is the logo of the docs. It is placed at the top of the title page. Default: None.
#latex_logo = None

# If true, the topmost sectioning unit is parts, else it is chapters. Default: False.
latex_use_parts = False

# A dictionary that contains LaTeX snippets that override those Sphinx usually puts into the generated .tex files.
# Keep in mind that backslashes must be doubled in Python string literals to avoid interpretation as escape sequences.
# Keys that are set by other options and therefore should not be overridden are:
# 'docclass', 'classoptions', 'title', 'date', 'release', 'author', 'logo', 'releasename', 'makeindex', 'shorthandoff'
latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    'papersize': 'a4paper',

    # The font size ('10pt', '11pt' or '12pt').
    'pointsize': '10pt',

    # “babel” package inclusion, default '\\usepackage{babel}'.
    'babel': '\\usepackage{babel}',
    
    # Font package inclusion, default '\\usepackage{times}' (which uses Times and Helvetica).
    # You can set this to '' to use the Computer Modern fonts.
    # Defaults to '' when the language uses the Cyrillic script.
    'fontpkg': '\\usepackage{times}',

    # Inclusion of the “fncychap” package (which makes fancy chapter titles)
    # default '\\usepackage[Bjarne]{fncychap}' for English documentation, 
    #         '\\usepackage[Sonny]{fncychap}' for internationalized docs (because the “Bjarne” style uses numbers spelled out in English).
    # Other “fncychap” styles you can try include “Lenny”, “Glenn”, “Conny” and “Rejne”. You can also set this to '' to disable fncychap.
    'fncychap': '\\usepackage[Bjarne]{fncychap}', 
   
    # “inputenc” package inclusion, default '\\usepackage[utf8]{inputenc}'.
    'inputenc' :  '\\usepackage[utf8x]{inputenc}',
#    'utf8extra': ('\\ifdefined\\DeclareUnicodeCharacter\n'
#                  ' \\ifdefined\\DeclareUnicodeCharacterAsOptional\\else\n'
#                  '  \\DeclareUnicodeCharacter{2261}{\\equiv}\n'
#                  '  \\DeclareUnicodeCharacter{2630}{\\equiv}\n'
#                  '\\fi\\fi'),

    # “fontenc” package inclusion, default '\\usepackage[T1]{fontenc}'.
    'fontenc': '\\usepackage[T1]{fontenc}',

    # Latex figure (float) alignment
    'figure_align': 'htbp',
}

# If true, add page references after internal references. This is very useful for printed copies of the manual. Default is False.
latex_show_pagerefs = True

# Control whether to display URL addresses. This is very useful for printed copies of the manual. The setting can have the following values:
# 'no' – do not display URLs (default)
# 'footnote' – display URLs in footnotes
# 'inline' – display URLs inline in parentheses
latex_show_urls = 'inline'

# If true, add page references after internal references. This is very useful for printed copies of the manual. Default is False.
latex_show_pagerefs = True


# -- Options for manual page output ---------------------------------------
# One entry per manual page. List of tuples
#   (source start file, name,             description,                 authors,  manual section).
man_pages = [
    (master_doc,        'jamoviDocs',     u'Documentation for jamovi', [author], 1),
]

# -- Options for Texinfo output -------------------------------------------
# Grouping the document tree into Texinfo files. List of tuples
#   (source start file, target name,      title,                       author,   dir menu entry, description,                                                                                category)
texinfo_documents = [
    (master_doc,        'jamoviDocs',     u'Documentation for jamovi', [author], 'jamoviDocs',   'free and open statistical software to bridge the gap between researcher and statistician', 'Mathematics'),
]

# -- Options for Sphinx extensions ----------------------------------------
imgmath_image_format = 'svg'
