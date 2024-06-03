from setuptools import setup, find_packages

setup(
    name="ct-configcreator",
    version="0.1.1",
    packages=find_packages(),
    install_requires=[],
    author="Clevrthings",
    author_email="info@clevrthings.com",
    description="A Python script that generates a configuration file from a YAML template, dynamically creating corresponding Python classes and methods for easy configuration management.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/clevrthings/ConfigCreator",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
