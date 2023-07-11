# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Cow Pi'
copyright = '2021-2023, Christopher Bohn'
author = 'Christopher Bohn'

release = '2023.07'
version = '2023.07.11'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

rst_prolog = """
.. |i2c| replace:: :math:`\mathrm{I}^2\mathrm{C}`
"""
numfig = True

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    # 'sphinx.ext.autosectionlabel',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinxcontrib.tikz'
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'alabaster'
# html_static_path = ['_static']

html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'logo_only': True,
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
# tikz_latex_preamble = 'x=.1in, y=.1in'
