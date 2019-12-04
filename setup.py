import pathlib
from setuptools import setup,find_packages
HERE = pathlib.Path(__file__).parent
README_path = (HERE / "README.md")


with open(README_path, encoding='utf-8') as f:
    long_description = f.read()
setup(
    name='randaugment',
    version='1.0.2',
    packages=find_packages(),
    url='https://github.com/jizongFox/pytorch-randaugment',
    license='MIT',
    author='Jizong Peng',
    author_email='jizong.peng.1@etsmtl.net',
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=[],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
)
