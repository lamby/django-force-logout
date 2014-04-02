import sys

from os.path import join, dirname, abspath

sys.path.insert(0, dirname(dirname(abspath(__file__))))

from django.conf import settings

settings.configure()

project = 'django-force-logout'
version = ''
release = ''
copyright = '2012, 2013, 2014 Thread, Inc.'

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.intersphinx']
html_title = "%s documentation" % project
html_static_path = ['_static']
master_doc = 'index'
exclude_trees = ['_build']
templates_path = ['_templates']
latex_documents = [
  ('index', '%s.tex' % project, html_title, u'Thread', 'manual'),
]
intersphinx_mapping = {'http://docs.python.org/': None}
