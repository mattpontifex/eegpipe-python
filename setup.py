#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    #https://uoftcoders.github.io/studyGroup/lessons/python/packages/lesson/
    
    # Needed to silence warnings (and to be a worthwhile package)
    name='eegpipe',
    url='https://github.com/mattpontifex/eegpipe-python',
    author='Matthew B. Pontifex',
    author_email='pontifex@msu.edu',
    # Needed to actually package something
    packages=['eegpipe'],
    # Needed for dependencies
    install_requires=['numpy', 'scipy', 'pandas', 'matplotlib'],
    # *strongly* suggested for sharing
    version='0.1',
    # The license can be anything you like
    license='MIT',
    description='A python package for rapidly processing EEG data.',
    # We will also need a readme eventually (there will be a warning)
    # long_description=open('README.txt').read(),
    
    classifiers=['Intended Audience :: Science/Research',
       'Programming Language :: Python',
       'Topic :: Scientific/Engineering',
       'Operating System :: Microsoft :: Windows',
       'Operating System :: MacOS',
       'Programming Language :: Python :: 3',
       ],
    keywords='neuroscience neuroimaging EEG brain',
)
