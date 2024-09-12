# -*- coding: utf-8 -*-

"""
Módulo de configuração básica.
"""

from setuptools import setup

def readme():

    """
    Função LEIA-ME.
    """

    with open('README.md') as file:
        return file.read()

# remove older distribuitions
# shutil.rmtree('proplib.egg-info/')
# shutil.rmtree('dist/')

setup(name='proplib',
      version='0.0.2',
      description='Library of functions related to propulsion for the'
                  'APR (Propulsion Division) team.',
      long_description=readme(),
      classifiers=[
        'Development Status :: 0 - Alpha',
        'License :: OSI Approved :: MIT License',  # TODO: update!
        'Programming Language :: Python :: 3.8',
        'Topic :: Thermodynamics :: Rocket propulsion'],
      url='https://gitlab.com/iae-apr/proplib',
      author='APR',
      author_email=' ',
      license=' ',
      packages=[
          'proplib',
          'proplib.LPRE_lib',
          'proplib.LPRE_lib.util',
          'proplib.LPRE_lib.cycle',
          'proplib.LPRE_lib.components',
          'proplib.LPRE_lib.components.thrust_chamber_assembly',
          'proplib.LPRE_lib.components.thrust_chamber_assembly',
          'proplib.util',
          'proplib.util.properties',
          'proplib.util.software_interfaces',
          'main_files',
          'main_files.LPRE_main_files'],
      python_requires='>=3.4',
      install_requires=['coolprop',
                        'matplotlib',
                        'numpy',
                        'pandas',
                        'pytest',
                        'scipy',
                        'sympy',
                        'Pillow'],
      # scripts=['main_files/LPRE_main_files/TCA_main.py'],
      entry_points={
          'console_scripts': [
              'TCA_main=main_files.LPRE_main_files.TCA_main:main',
              'pump_main=main_files.LPRE_main_files.pump_main:main',
              'compare_inputs=proplib.util.check_modules:compare_external',
              'sign_sha1=proplib.util.check_modules:sign_sha1_external']},
      # test_suite='nose.collector',
      tests_require=['nose', 'pytest'],
      include_package_data=True,
      zip_safe=False)
