from setuptools import setup, find_packages

setup(
    name="pkg",
    version="0.1",
    packages=find_packages(exclude=["tests*"]),
    description="A python package for doing spaced repetition for language learning",
    url="https://github.com/mathematiguy/spaced-repetition",
    author="Caleb Moses",
    author_email="calebjdmoses@gmail.com",
    include_package_data=True,
)
