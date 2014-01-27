from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='shiji.policy',
      version=version,
      description="ShiJi Policy Package",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.rst")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author='TsungWei Hu',
      author_email='marr.tw@gmail.com',
      url='http://shiji.com',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['shiji'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'Plone',
#         'shiji.theme',
#         'shiji.content',
      ],
      extras_require={
          'test': ['plone.app.testing',]
      },
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
# uncomment these to re-enable support for Paster local commands
#     setup_requires=["PasteScript"],
#     paster_plugins=["ZopeSkel"],
      )
