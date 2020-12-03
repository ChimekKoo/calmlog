# $ python3 setup.py sdist bdist_wheel
# $ twine upload dist/*

import setuptools

with open("README.md", "r") as file:
    long_description = file.read()

setuptools.setup(
    name="simplog",
    version="0.1",
    author="ChimekKoo",
    author_email="chimeksushi@gmail.com",
    description="Simple and easy logging.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ChimekKoo/simplog",
    packages=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)