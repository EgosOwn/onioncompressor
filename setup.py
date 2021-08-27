from setuptools import setup, find_packages

setup(name='onioncompressor',
      version='0.0.0',
      description='Converts Tor v3 onions into bytes without the checksum or version',
      author='VoidNetwork LLC',
      author_email='onioncompressor@voidnet.tech',
      url='https://git.voidnet.tech/kev/onioncompressor',
      packages=find_packages(exclude=['contrib', 'docs', 'tests']),
      install_requires=[],
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
      ],
     )
