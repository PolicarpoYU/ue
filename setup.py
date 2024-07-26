from setuptools import setup, find_packages

# Ler o conteúdo do README.md
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='ulianovorbit',
    version='1.1.0',
    description='Library for handling Ulianov Orbit functions',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Policarpo Yoshin Ulianov',
    author_email='poliyu77@gmail.com',
    packages=find_packages(),
    install_requires=[
        'numpy','ulianovellipse'
    ],
    setup_requires=[
        'numpy','ulianovellipse'
    ],
)
