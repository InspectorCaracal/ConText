#!/usr/bin/env python3

import setuptools

with open("README.md", "r") as f:
	long_description = f.read()

setuptools.setup(
	name="Con-Text",
	version="0.0.1",
	
	author="Cal Sinclair",
	author_email="cal@clockworkcaracal.com",
	
	description="ConText, a tool for conlang dictionary creation, management and translation.",
	long_description=long_description,
	long_description_content_type="text/markdown",
	
	url="https://github.com/InspectorCaracal/ConText",
	
	packages=["Con-Text"],
	
	python_requires='>=3',
  install_requires=['genling'],
	classifiers=(
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
		"Operating System :: OS Independent"
	)
)