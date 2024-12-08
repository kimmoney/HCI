from setuptools import setup, find_packages

setup(
    name="dotpad-sdk",
    version="1.0.0",
    description="Python bindings for DotPad SDK",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/yourname/dotpad-sdk",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
    ],
    install_requires=[],
    include_package_data=True,
    python_requires=">=3.7",
)
