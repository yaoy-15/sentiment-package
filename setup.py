# setup.py
from setuptools import setup, find_packages

setup(
    name="sentiment-package",
    version="0.1.0",
    author="name",
    author_email="email",
    description="A simple example for practice",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.8",
    install_requires=[
        "numpy>=1.21.0",
        "pandas>=1.3.0",
    ],
    entry_points={
        "console_scripts": [
            "sentiment-predict=sentiment_package.cli:main",
        ],
    },
)