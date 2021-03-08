# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['utils']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'utils',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'mihai',
    'author_email': 'balint.mihai@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
