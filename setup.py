from setuptools import setup
from pathlib import Path

setup(
    name="flaresolverr",
    version="3.3.16",
    description="Python library for Cloudflare bypass",
    long_description=Path(__file__).parent.joinpath("README.md").read_text(),
    long_description_content_type="text/markdown",
    url="https://github.com/alex-bouget/flaresolverr",
    author="MisterMine01",
    py_modules=["flaresolverr"],
    install_requires=Path(__file__).parent.joinpath(
        "requirements.txt").read_text().splitlines(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Plugins",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Internet :: WWW/HTTP",

    ]
)
