from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .' #Install the current project in editable mode.
# pip install -e .

def get_requirements(file_path:str)->List[str]: # file type and return type
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") 
        for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

        return requirements


setup( # libraries does project require
    name='DiamondPricePrediction',
    version='0.0.1',
    author='Affan',
    author_email='affanahmed0128@gmail.com',
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages()
 #This automatically searches your project and finds Python packages.
)

#Python projects to make your project installable as a package.
#Take your Python project, identify its packages, install its dependencies, and make the project installable with pip.
