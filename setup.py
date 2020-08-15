from setuptools import setup, find_packages

setup(
    name="flask_pastedeploy",
    version="0.1",
    packages=find_packages(),
    description="use flask as a pastedeploy app",
    author="CaesarLinsa",
    author_email="CaesarLinsa@163.com",
    install_requires=['Flask', 'PasteDeploy'],
    py_modules=['flask_pastedeploy']
)
