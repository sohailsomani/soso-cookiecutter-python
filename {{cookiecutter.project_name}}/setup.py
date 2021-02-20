# flake8: noqa
# type: ignore

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="soso-{{cookiecutter.project_name}}",
    version="0.0.1",
    author="Sohail Somani",
    author_email="me@sohailsomani.com",
    description="{{cookiecutter.short_description}}",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sohailsomani/{{cookiecutter.project_name}}",
    packages=['soso.{{cookiecutter.project_name}}','soso'],
    package_data = {
        'soso':['*.pyi','py.typed'],
        'soso.{{cookiecutter.project_name}}':['*.pyi','py.typed']
    },
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires=">=3.8",
)
