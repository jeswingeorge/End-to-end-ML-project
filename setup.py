from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT =   "-e ."

def get_requirements(file_path:str)->List[str]:  # function takes string as input and returns a list of strings
    '''
    This function will return the list of packages which are requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "")  for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)


    return(requirements)



setup(
name = "mlproject",
version = '0.0.1',
author = "Jeswin",
author_email="georgejeswin22@gmail.com",
packages=find_packages(),
install_requires = get_requirements('requirements.txt')  # first the availability of these packages is checked if not available then install
)

