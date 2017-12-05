from setuptools import setup, find_packages

version = '1.1.0'

setup(name='safestr',
      version=version,
      py_modules=['safestr'],
      description="Ultimate python unicode/types solution, run well with both python 2 and python3",
      long_description="""\
Ultimate python unicode/types solution, run well with both python 2 and python3""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='safe, str, py2, py3',
      author='jerrychen',
      author_email='jerrychen1990@gmail.com',
      url='http://jerrychen1990.github.io',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
