#!/usr/bin/env python
"""scrapli_community"""
from pathlib import Path

import setuptools

__version__ = "2021.07.30"
__author__ = "Carl Montanari"

with open("README.md", "r", encoding="utf-8") as f:
    README = f.read()

with open("requirements.txt", "r") as f:
    INSTALL_REQUIRES = f.read().splitlines()

EXTRAS_REQUIRE = {}

for extra in EXTRAS_REQUIRE:
    with open(f"requirements-{extra}.txt", "r") as f:
        EXTRAS_REQUIRE[extra] = f.read().splitlines()

full_requirements = [requirement for extra in EXTRAS_REQUIRE.values() for requirement in extra]
EXTRAS_REQUIRE["full"] = full_requirements


def get_packages(package):
    """Return root package and all sub-packages"""
    return [str(path.parent) for path in Path(package).glob("**/__init__.py")]


setuptools.setup(
    name="scrapli_community",
    version=__version__,
    author=__author__,
    author_email="carl.r.montanari@gmail.com",
    description="Easily add support for 'non-core' platforms to scrapli",
    long_description=README,
    long_description_content_type="text/markdown",
    keywords="ssh telnet netconf automation network cisco iosxr iosxe nxos arista eos juniper "
    "junos",
    url="https://github.com/scrapli/scrapli_community",
    project_urls={
        "Changelog": "https://scrapli.github.io/scrapli_community/changelog/",
        "Docs": "https://scrapli.github.io/scrapli_community/",
    },
    license="MIT",
    package_data={"scrapli_community": ["py.typed"]},
    packages=get_packages("scrapli_community"),
    install_requires=INSTALL_REQUIRES,
    dependency_links=[],
    extras_require=EXTRAS_REQUIRE,
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.6",
)
