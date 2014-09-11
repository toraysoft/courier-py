#!/usr/bin/env python

from setuptools import setup, find_packages
from courier import version

url="https://github.com/toraysoft/courier-py"

long_description="Courier (A SMS Broker) Client for Python"

setup(name="courier",
      version=version,
      description=long_description,
      maintainer="jeff kit",
      maintainer_email="jeff@toraysoft.com",
      url = url,
      long_description=long_description,
      py_modules=['courier'],
     )


