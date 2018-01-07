from pipenv.project import Project
from pipenv.utils import convert_deps_to_pip
from setuptools import setup, find_packages

pipfile = Project(chdir=False).parsed_pipfile
requirements = convert_deps_to_pip(pipfile['packages'], r=False)
dev_requirements = convert_deps_to_pip(pipfile['dev-packages'], r=False)

setup(
    name='basket',
    version='0.1.0',
    packages=find_packages(),
    install_requires=requirements,
    extras_require={
        'dev': dev_requirements
    })
