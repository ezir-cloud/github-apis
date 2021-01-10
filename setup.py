from distutils.core import setup
import setuptools
from setuptools import setup


setup(
    name = 'githubapis',
    version = '0.0.1',
    packages =setuptools.find_packages(),
    url = "https://github.com/ezir-cloud/github-apis",
    license = '' ,
    author = 'ezir',
    author_email = 'dev@ezir.cloud',
    long_description = open('README.txt').read(),
    include_package_data=True,
    zip_safe=False,
    install_requires = ["requests==2.23.0"],
    classifiers=[
        'Programming Language :: Python :: 3.8'
    ]
)