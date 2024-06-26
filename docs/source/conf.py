import os, pkg_resources, sys, time
sys.path.insert(0, os.path.abspath("../../"))
sys.path.insert(0, os.path.abspath("../../luna_soc"))

import sphinx_rtd_theme

extensions = [
    'sphinx_rtd_theme'
]

# -- Project information -----------------------------------------------------

project = 'luna-soc'
copyright = time.strftime('2018-%Y, Great Scott Gadgets')
author = 'Great Scott Gadget'

version = pkg_resources.get_distribution('luna_soc').version
release = ''


# -- General configuration ---------------------------------------------------

templates_path = ['_templates']
exclude_patterns = ['build']
source_suffix = '.rst'
master_doc = 'index'
language = "en"
exclude_patterns = []
pygments_style = None

extensions = [
    'recommonmark',
    'sphinx.ext.autodoc',
    'sphinx.ext.coverage',
    'sphinx.ext.doctest',
    'sphinx.ext.extlinks',
    'sphinx.ext.napoleon',
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',
    'sphinxcontrib.apidoc',
]

# configure extension: sphinxcontrib.apidoc
apidoc_module_dir = '../../luna_soc'
apidoc_output_dir = 'api_docs'
apidoc_excluded_paths = ['gateware/vendor/']
apidoc_separate_modules = True

# configure extension: extlinks
extlinks = {
    'repo':    ('https://github.com/greatscottgadgets/luna-soc/blob/main/%s',          '%s'),
    'example': ('https://github.com/greatscottgadgets/luna-soc/blob/main/examples/%s', '%s'),
}

# configure extension: napoleon
napoleon_google_docstring = True
napoleon_numpy_docstring = False
napoleon_include_init_with_doc = True
napoleon_use_ivar = True
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_param = False


# -- Options for HTML output -------------------------------------------------
# run pip install sphinx_rtd_theme if you get sphinx_rtd_theme errors
html_theme = "sphinx_rtd_theme"
html_css_files = ['status.css']
