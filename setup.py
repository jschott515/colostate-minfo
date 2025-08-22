import setuptools


setuptools.setup(
    name="colostate-minfo",
    version="0.0.1",
    author="jschott",
    author_email="jschott515@gmail.com",
    description="Colorado State Machine Info Tools",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/jschott515/colostate-minfo",
    packages=setuptools.find_packages(),
    python_requires=">=3.12",
    install_requires=[
        "requests>=2.32.5",
        "beautifulsoup4>=4.13.4",
    ],
    classifiers=[
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
