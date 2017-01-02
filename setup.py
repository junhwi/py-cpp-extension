from distutils.core import setup, Extension

module = Extension('spam', sources=['src/spam.c'])

setup(
  name = 'spam',
  version = '1.0',
  ext_modules = [module]
)
