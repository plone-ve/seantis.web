from setuptools import setup, find_packages

name = 'seantis.web'
description = (
    "The seantis website."
)
version = '1.3.1'

long_description = (
    open('README.rst').read()
)

setup(name=name,
      version=version,
      description=description,
      long_description=long_description,
      classifiers=[
          "Development Status :: 4 - Beta",
          "Environment :: Web Environment",
          "Framework :: Plone",
          "Framework :: Plone :: 4.1",
          "Framework :: Plone :: 4.2",
          "Framework :: Plone :: 4.3",
          "Framework :: Plone :: Theme",
          "Framework :: Zope2",
          "Framework :: Zope3",
          "Intended Audience :: Developers",
          "Intended Audience :: End Users/Desktop",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          "Programming Language :: Python :: 2.6",
          "Programming Language :: Python :: 2.7",
          "Topic :: Internet",
          "Topic :: Software Development :: Libraries :: Python Modules",
      ],
      keywords='plone seantis website',
      author='Seantis GmbH',
      author_email='info@seantis.ch',
      url='https://github.com/seantis/seantis.web',
      license='gpl',
      packages=find_packages('.'),
      namespace_packages=['seantis', ],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'plone.app.theming',
          'plone.app.themingplugins',
          'Products.ContentWellPortlets',
          'collective.portlet.embed',
          'collective.blogging',
      ],
      extras_require={'test': ['plone.app.testing']},
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
