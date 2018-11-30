import setuptools

with open("readME.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sortdict",
    version="0.0.1",
    author="Anshul Gupta",
    author_email="anshulgupta217@gmail.com",
    description="This library is to sort dictionary list given to corresponding keys",
    long_description="This packages sorts dictionary in efficient and fastest way",
    long_description_content_type="text/markdown",
    url="https://github.com/ANSHUL217",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
