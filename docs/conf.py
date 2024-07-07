import sphinx
import os
import sys
sys.path.append(os.path.abspath(r'..'))
#sys.path.append(os.path.abspath(r'../src'))


# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'PyStarter'
copyright = '2024, Rob Howard'
author = 'Rob Howard'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
  'sphinx.ext.autodoc',  # Core library for html generation from docstrings
  'sphinx.ext.autosummary',  # Create neat summary tables
  'sphinx.ext.napoleon',  # Support for NumPy and Google style docstrings
]

templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
pygments_style = 'sphinx'
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
todo_include_todos = True


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# THEMES: See https://sphinx-themes.org/
html_theme = 'alabaster'
html_theme = 'python-docs-theme'
html_theme = 'classic'
html_static_path = ['_static']
