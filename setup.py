import re
from codecs import open  # To use a consistent encoding
from os import path

from setuptools import find_packages, setup

here = path.abspath(path.dirname(__file__))


# Get version without importing, which avoids dependency issues
def get_version():
    with open("idx_stream/__init__.py") as version_file:
        return re.search(
            r"""__version__\s+=\s+(['"])(?P<version>.+?)\1""", version_file.read()
        ).group("version")


install_requires = [
    "fastapi>=0.68.2",
    "pydantic>=1.9.2",
    "uvicorn>=0.16.0",
    "gunicorn>=19.9.0",
    "gevent>=1.4.0",
    "python-nomad>=1.4.1",
    "pyYAML>=5.1.2",
    "markupsafe>=2.0.1",
]


test_requires = [
    "pytest",
    "pytest-sugar",
    "pytest-asyncio",
    "pytest-cov",
]


setup(
    name="idx-stream",
    description="",
    long_description="",
    version=get_version(),
    include_package_data=True,
    install_requires=install_requires,
    setup_requires=["pytest-runner"],
    entry_points={},
    tests_require=test_requires,
    packages=find_packages(),
    zip_safe=False,
    author="Taufiqurrahman",
    author_email="taufiqurrahman@hotmail.com",
    classifiers=[
        "Programming Language :: Python :: 3.10",
    ],
)
