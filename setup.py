from setuptools import find_packages,setup
from typing import List
HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path,'r') as file_object:
        requirements=file_object.readlines()
        requirements=[i.replace('\n','') for i in requirements]
    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)
    return requirements
    
setup(
    name='GEM11_V1',
    version='0.0.1',
    author='chandan',
    author_email='chandannadve@gmail.com',
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages()
)