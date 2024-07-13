from setuptools import find_packages, setup
from typing import List


HYPHEN_E_DOT = '-e .'
def get_requirements(file_path:str):
    '''
    This  Function will return the list of requirements
    '''
    
    requirements = []
     
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        [req.replace("\n","") for req in requirements]
        print(requirements)
        if HYPHEN_E_DOT in requirements:
            print(f"{HYPHEN_E_DOT} Founded")
            requirements.remove(HYPHEN_E_DOT)
        
    return requirements
    
    


setup(
    
name = 'mlproject',
version = '0.0.1',
author = 'Parthiv Shah',
author_email = 'parthivshah33@gmail.com',
packages = find_packages(), 
install_requires = get_requirements('requirements.txt')
    
    
)