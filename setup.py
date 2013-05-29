# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os

version = open(os.path.join("lx", "site", "wilker", "version.txt")).read().strip()

setup(name='lx.site.wilker',
      version=version,
      description="",
      long_description=open(os.path.join("lx", "site", "wilker", "README.txt")).read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Framework :: Zope2",
        "Framework :: Zope3",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='web zope plone theme skin lx',
      author='Lucas Aquino',
      author_email='contato@lucasaquino.com.br',
      url='http://www.lucasaquino.com.br/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['lx', 'lx.site'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )

