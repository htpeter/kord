import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cFlat",
    version="0.6",
    author="Federico Rizzo",
    author_email="foo@bar.com",
    description='a python framework for programming music applications',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/synestematic/cFlat",
    license="MIT",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3 :: Only",
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS :: MacOS X",
    ],
    install_requires=[
        'bestia',
    ],
)
