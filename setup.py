# -*- coding: utf-8 -*-
"""
File Name  setup.py
Created on 2020-01-10

@author: jj

"""
import codecs

from setuptools import setup

with codecs.open('README.rst', encoding='utf-8') as f:
    readme = f.read()


setup(
    author='Chinese',
    author_email='576801035@qq.com',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django :: 3.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Internet :: WWW/HTTP',
    ],
    description=('A Django Central Authentication Service server '
                 'implementing the CAS Protocol 3.0 Specification'
                 ),
    keywords=['django', 'cas', 'cas3', 'server', 'sso', 'single sign-on', 'authentication', 'auth'],
    license='BSD',
    long_description=readme,
    name='django3-cas-server',
    
    packages=[
        'cas_server', 'cas_server.migrations',
        'cas_server.management', 'cas_server.management.commands',
        'cas_server.tests', 'cas_server.templatetags'
    ],
    
    package_data={
        'cas_server': [
            'templates/cas_server/*',
            'static/cas_server/*',
            'locale/*/LC_MESSAGES/*',
        ]
    },
    # url='',
    # bugtrack_url='',  # not support this key
    # download_url ='',
    version='3.0.0',
    python_requires=">=3.5",
    install_requires=[
        'Django>=3.0',
        'requests >= 2.4',
        'requests_futures >= 0.9.5',
        'lxml >= 3.4',
        'six>=1.13.0',
    ],
    zip_safe=False,  # dot not package as egg or django will not found management commands
)
if __name__ == '__main__':
    pass