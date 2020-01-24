# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

with open('VALD_CLIENT_PYTHON_VERSION') as f:
    version = f.read()

setup(
    name='vald-client-python',
    version=version,
    description='a client library for Vald (https://github.com/vdaas/vald).',
    long_description=readme,
    author='Rintaro Okamura',
    author_email='rintaro.okamura@gmail.com',
    install_requires=['protobuf', 'grpcio'],
    url='https://github.com/vdaas/vald-client-python',
    license=license,
    package_dir={'': 'src'},
    packages=find_packages('src')
)
