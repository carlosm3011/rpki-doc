# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

import os
import datetime
import sphinx_rtd_theme
import requests

# -- Project information -----------------------------------------------------

project = u'RPKI'
copyright = u'2018-2024, NLnet Labs (CC-BY 3.0)'
author = u'The RPKI Team'

# The short X.Y version
version = u''
# The full version, including alpha/beta/rc tags
release = u''

try:
    response_versions = requests.get(
        f"https://readthedocs.org/api/v2/version/?project__slug=rpki&active=true",
        timeout=2,
    ).json()
    versions = [
        (version["slug"], f"/{version['project']['language']}/{version['slug']}/")
        for version in response_versions["results"]
    ]
except Exception:
    versions = []

# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.todo',
    'sphinx.ext.extlinks',
    'sphinxcontrib.plantuml',
    'sphinx_rtd_theme'
]

# If true, figures, tables and code-blocks are automatically numbered if they have a caption.
numfig = True

# Add any paths that contain templates here, relative to this directory.
# templates_path = ['../templates']

locale_dirs = ['locale/']   #path is example but recommended.
gettext_compact = False     #optional.

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = None


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    'collapse_navigation': False,
    'titles_only': False
  }

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['resources']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}

# Set canonical URL from the Read the Docs Domain
html_baseurl = os.environ.get("READTHEDOCS_CANONICAL_URL", "")
scheme = "https"

html_context = {
        'html_theme': html_theme,
        'current_version': version,
        'version_slug': version,

        'PRODUCTION_DOMAIN': "readthedocs.org",
        'versions': versions,
        # "downloads": downloads,
        # "subprojects": subprojects,

        'slug': "unbound",
        'rtd_language': language,
        'canonical_url': html_baseurl,

        'conf_py_path': "/source/",

        'github_user': "NLnetLabs",
        'github_repo': "rpki-doc",
        'github_version': os.environ.get("READTHEDOCS_GIT_IDENTIFIER", "main"),
        'display_github': True,
        'READTHEDOCS': True,
        'using_theme': False,
        'new_theme': True,
        'source_suffix': ".rst",
        'docsearch_disabled': False,
    }

# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'TheRPKIDocumentationdoc'


# -- Options for LaTeX output ------------------------------------------------

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
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'TheRPKIDocumentation.tex', u'The RPKI Documentation',
     u'Alex Band and the RPKI Community', 'manual'),
]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'therpkidocumentation', u'The RPKI Documentation',
     [author], 1)
]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'TheRPKITools', u'The RPKI Tools Documentation',
     author, 'TheRPKITools', 'One line description of project.',
     'Miscellaneous'),
]


# -- Options for Epub output -------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']


# -- Extension configuration -------------------------------------------------

# -- Options for todo extension ----------------------------------------------

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

# -- Extension interface --------------------------------------------------
from sphinx import addnodes
def parse_cmd_args_node(env, sig, signode):
    try:
        cmd, args = sig.strip().split(' ', 1)
    except ValueError:
        cmd, args = sig, None
    # distinguish cmd from its args
    signode += addnodes.desc_name(cmd, cmd)
    if args:
        args = ' ' + args
        signode += addnodes.desc_addname(args, args)
    return cmd
# define new directive/role that can be used as .. subcmd::/:subcmd:
def setup(app):
    app.add_object_type('subcmd', 'subcmd',
                        objname='module sub-command',
                        indextemplate='pair: %s; module sub-command',
                        parse_node=parse_cmd_args_node)
    app.add_css_file('css/dark.css')
    app.add_css_file('css/light.css')

# -- Options for extlinks extension

krill_api_docs_base = 'http://redocly.github.io/redoc/?url=https://raw.githubusercontent.com/NLnetLabs/krill/v0.8.0/doc/openapi.yaml'
extlinks = {
    'krill_api': (krill_api_docs_base + '#operation/%s', None),
}
