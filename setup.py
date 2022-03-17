import setuptools

__version__ = "VERSIONADDEDBYGITHUB"

__title__ = "objectrest"
__github_project_name__ = "objectrest"
__author__ = "Nate Harris"
__author_email__ = "n8gr8gbln@gmail.com"
__github_username__ = "nwithan8"
__copyright__ = "Copyright © YEARADDEDBYGITHUB - Nate Harris"
__license__ = "GNU General Public License v3 (GPLv3)"
__description__ = "A Python package to handle REST API requests, JSON parsing, and pydantic object generation."
__keywords__ = [
    "API",
    "REST",
    "objects",
    "pydantic",
    "JSON",
    "requests",
    "OAuth2",
    "token",
]

with open("requirements.txt", 'r') as fh:
    REQUIREMENTS = fh.read().splitlines()

DEV_REQUIREMENTS = [
    "black",
    "flake8",
    "isort",
    "pytest-cov==3.*",
    "pytest-vcr==1.*",
    "pytest==7.*",
    "pydantic"
]
DEV_REQUIREMENTS.extend(REQUIREMENTS)

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name=__title__,
    packages=setuptools.find_packages(),
    version=__version__,
    license=__license__,
    description=__description__,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author=__author__,
    author_email=__author_email__,
    url=f'https://github.com/{__github_username__}/{__github_project_name__}',
    download_url=f'https://github.com/{__github_username__}/{__github_project_name__}/archive/{__version__}.tar.gz',
    keywords=__keywords__,
    install_requires=REQUIREMENTS,
    extras_require={
        "dev": DEV_REQUIREMENTS,
    },
    test_suite="test",
    python_requires='>=3.7',
    classifiers=[
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Development Status :: 4 - Beta',
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',  # Define that your audience are developers
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: Python :: 3',  # Specify which python versions that you want to support
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Multimedia :: Video',
        'Topic :: Multimedia',
        'Topic :: Internet :: WWW/HTTP',
        'Operating System :: OS Independent'
    ]
)
