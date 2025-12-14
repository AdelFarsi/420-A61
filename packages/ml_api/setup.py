from setuptools import find_packages, setup

setup(
    name="ml_api",
    version="0.1.0",
    packages=find_packages(include=["ml_api", "ml_api.*"]),
    install_requires=[
        "flask==2.2.5",
        "pydantic==1.10.2",
        "regression_model==0.1.0",
    ],
)