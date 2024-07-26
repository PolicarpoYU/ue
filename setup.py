from setuptools import setup, find_packages

# Ler o conteúdo do README.md
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='ulianovellipse',
    version='1.1.0',
    description='Library for handling Ulianov elliptical functions',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Policarpo Yoshin Ulianov',
    author_email='poliyu77@gmail.com',
    packages=find_packages(),
    install_requires=[
        'numpy',
    ],
    setup_requires=[
        'numpy',
    ],
)
