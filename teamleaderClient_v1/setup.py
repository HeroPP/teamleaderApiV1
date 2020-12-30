from setuptools import find_packages, setup

setup(
    name="teamleaderClient_v1",
    version="0.2",
    packages=find_packages(),
    url="",
    license="Apache 2.0",
    author="Jaap van den Broek",
    author_email="jaap@rechtdirect.nl",
    description="Python framework on top of the teamleader v1 api",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
