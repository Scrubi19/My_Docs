import os
import sys
import sphinx_rtd_theme

project = 'My_Docs'
copyright = '2020, Bulatov Alexandr'
author = 'Bulatov Alexandr'

version = ''

release = '0.0.1'

# needs_sphinx = '1.0'

templates_path = ['_templates']

html_static_path = ['_static']

source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

language = 'ru'

exclude_patterns = ['cryptography.rst', 'ruby.rst', 'sql.rst']

pygments_style = None

numpydoc_show_class_members = False

html_static_path = ['_static']

htmlhelp_basename = 'My_Docsdoc'


latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'flushleft'
}

epub_title = project

epub_exclude_files = ['search.html']

html_theme_path = ['themes']  # папка внутри source, где лежат папки тем

# sphinx_rtd_theme
html_theme = "sphinx_rtd_theme"

html_logo = "_static/logo2.svg"

html_theme_options = {
    'canonical_url': '',
    'logo_only': True,
    'display_version': False,
    'prev_next_buttons_location': '',
    'style_external_links': True,
    'style_nav_header_background': '#343131',
    # Toc options
    'collapse_navigation': False,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False
}

extensions = [
    "sphinx.ext.intersphinx",
    "sphinx.ext.autodoc",
    "sphinx.ext.mathjax",
    "sphinx.ext.viewcode",
    'sphinx_rtd_theme'
]

#My CSS
def setup(app):
    app.add_stylesheet("main.css") # also can be a full URL
    # app.add_stylesheet("ANOTHER.css")
    # app.add_stylesheet("AND_ANOTHER.css")