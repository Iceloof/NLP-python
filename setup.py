import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="NLP-python",
    version="1.1.0",
    author="Hurin Hu",
    author_email="hurin@live.ca",
    description="Natural Language Processing to detect sentences are positive or negative",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/HurinHu/NLP-python",
    packages=setuptools.find_packages(),
    install_requires=['scikit-learn','pandas','numpy'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
