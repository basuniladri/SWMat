from distutils.core import setup
setup(
  name = 'SWMat',
  packages = ['SWMat'],
  version = '0.1.0',
  license='Apache License 2.0',
  description = 'A package for making stunning graphs/charts using matplotlib in just few lines of code!',
  author = 'Puneet Grover',
  author_email = 'grover.puneet1995@gmail.com',
  url = 'https://github.com/PuneetGrov3r/SWMat',
  download_url = 'https://github.com/PuneetGrov3r/SWMat/archive/v0.1.0-alpha.tar.gz',
  keywords = ['plot', 'visualization', 'data', 'big data', 'exploration', 'data exploration', 'communication', 'python', 'matplotlib', 'machine learning', 'data science'],
  install_requires=[
          'matplotlib',
          'numpy',
          'pandas'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Data Communicators, Analysts, Data Scientists',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: Apache License 2.0',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
