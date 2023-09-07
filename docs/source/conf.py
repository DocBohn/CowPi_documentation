# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import sys, subprocess, os

subprocess.call('cd CowPi; doxygen', shell=True)
subprocess.call('cd CowPi_stdio; doxygen', shell=True)
sys.path.append('ext/breathe/')

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Cow Pi'
copyright = '2021-2023, Christopher Bohn'
author = 'Christopher Bohn'

release = '2023.09'
version = '2023.09.07'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

rst_prolog = """
..  |i2c| replace:: I\ :sup:`2`\ C
..  |i2c-italics| replace:: *I*\ :sup:`2`\ *C*
"""
# .. |i2c| replace:: :math:`\mathrm{I}^2\mathrm{C}`
numfig = True

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    # 'sphinx.ext.autosectionlabel',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinxcontrib.tikz',
    'sphinx.ext.imgmath',
    'sphinx.ext.todo',
    'sphinx_copybutton',
    'breathe',
    # "sphinxcontrib.video",
    'linuxdoc.rstFlatTable'
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']
exclude_patterns = []

todo_include_todos = True

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'alabaster'
# html_static_path = ['_static']

html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'logo_only': True,
    # 'prev_next_buttons_location': None,
    'style_nav_header_background': '#FF2400'
}
html_context = {}
html_static_path = ['_static']
html_logo = '_static/CowPiLogo.png'
epub_show_urls = 'footnote'

# TIKZ
# https://sphinxcontrib-tikz.readthedocs.io/en/latest/

tikz_proc_suite = 'GhostScript'
tikz_tikzlibraries = 'shapes.geometric'

# DOXYGEN / BREATHE

breathe_projects = {
    'CowPi': 'CowPi/xml/',
    'CowPi_stdio': 'CowPi_stdio/xml/'
}

breathe_default_project = 'CowPi_stdio'

# primary_domain = 'c'
# highlight_language = 'c'
primary_domain = 'cpp'
