"""
	wikilink
	~~~~~~~~

	wikilink is a web-scraping application to find minimum number 
	of links between two given wiki pages. 
    
    :copyright: (c) 2016 - 2019 by Tran Ly VU. All Rights Reserved.
    :license: Apache License 2.0.
"""
from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
	name='wikilink',
	version="1.2.1",
	author='Tran Ly Vu',
	author_email='vutransingapore@gmail.com',
	maintainer='Tran Ly Vu <vutransingapore@gmail.com>',
	maintainer_email='vutransingapore@gmail.com',
	description='A web-scraping application to find the minimum number of links between 2 given wiki pages',
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/tranlyvu/wiki-link",
	packages=find_packages(where="wikilink", exclude=['docs', 'tests*']),
	package_dir={'':'wikilink'},
	license='Apache License 2.0',
	classifiers=[
		'Programming Language :: Python :: 3',
		"Programming Language :: Python :: 3.6",
		"Programming Language :: Python :: 3.7",
		"License :: OSI Approved :: Apache Software License ",
		"Operating System :: POSIX",
		"Operating System :: Linux",
		"Operating System :: Unix",
		"Development Status :: 5 - Production/Stable ",
		"Natural Language :: English",
		"Environment :: Console",
		"Intended Audience :: Education",
		"Intended Audience :: End Users/Desktop",
		"Intended Audience :: Information Technology",
		'Intended Audience :: Science/Research',
		'Topic :: Scientific/Engineering :: Artificial Intelligence',
		"Topic :: Scientific/Engineering :: Information Analysis",
		"Topic :: Education"
	],
	keywords=["Web Scraping", "Artificial Intelligence", "Breadth First Search", "Graph", "Data Science", "Web Extracting", "Information Analysis"],
	project_urls={
    'Source': 'https://github.com/tranlyvu/wiki-link',
    'Tracker': 'https://github.com/tranlyvu/wiki-link/issues',
    'Chat: Gitter': 'https://gitter.im/find-link/Lobby',
    'CI: Travis': 'https://travis-ci.org/tranlyvu/wiki-link',
    'Coverage: coveralls': 'https://coveralls.io/github/tranlyvu/wiki-link',
	},
	py_modules=["six"],
	install_requires=[
		"beautifulsoup4",
		"requests",
		"SQLAlchemy-Utils",
		"SQLAlchemy"
		],
	python_requires='>=2.6, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, !=3.5.*, <4',
	tests_require = [
    	'pytest',
    	'python-coveralls'
    ]	
)