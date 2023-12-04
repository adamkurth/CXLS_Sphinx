# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'CXLS Sphinx'
copyright = '2023, Sabine Botha, Adam Kurth, and more'
author = 'Sabine Botha, Adam Kurth, and more'
# release = 'N'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.

extensions = [
    'sphinx.ext.duration',
    'sphinxawesome_theme.highlighting'
]

templates_path = ['_templates']
exclude_patterns = []
pygments_style = 'sphinx'



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinxawesome_theme'
html_static_path = ['_static']

# themes installed with pip 
# 'sphinx_rtd_theme'
# 'insegel'
# 'sphinx_material'
# 'sphinx_book_theme'
# 'sphinx_py3doc_enhanced_theme'
# 'sphinxawesome_theme'