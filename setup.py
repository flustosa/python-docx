#!/usr/bin/env python

from distutils.core import setup
from glob import glob

# Make data go into site-packages (http://tinyurl.com/site-pkg)
from distutils.command.install import INSTALL_SCHEMES
for scheme in INSTALL_SCHEMES.values():
    scheme['data'] = scheme['purelib']

setup(name='docx',
      version='0.0.1',
      requires=['lxml'],
      description='The docx module creates, reads and writes Microsoft Office Word 2007 docx files',
      author='Mike MacCana',
      author_email='python.docx@librelist.com',
      url='http://github.com/mikemaccana/python-docx',
      py_modules=['docx'],
      data_files=[
          ('template/_rels', glob('template/_rels/.*')),
          ('template/docProps', glob('template/docProps/*.*')),
          ('template/word', glob('template/word/*.xml')),
          ('template/word/media', glob('template/word/media/*.*')),
          ('template/word/theme', glob('template/word/theme/*.*')),
          ],
      )
