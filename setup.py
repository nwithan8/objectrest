import setuptools

from objectrest import __info__ as package_info

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
    name=package_info.__title__,
    packages=setuptools.find_packages(),
    version=package_info.__version__,
    license=package_info.__license__,
    description=package_info.__description__,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author=package_info.__author__,
    author_email=package_info.__author_email__,
    url=f'https://github.com/{package_info.__github_username__}/{package_info.__github_project_name__}',
    download_url=f'https://github.com/{package_info.__github_username__}/{package_info.__github_project_name__}/archive/{package_info.__version__}.tar.gz',
    keywords=package_info.__keywords__,
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
