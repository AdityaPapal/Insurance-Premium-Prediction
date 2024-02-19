from setuptools import setup,find_packages
from typing import List

HYPEN_E_DOT="-e ."

def get_requirements(file_path:str)->List['str']:
    requrements = []

    with open(file_path) as f:
        requrements = f.readlines()
        requrements = [req.replace("\n","") for req in requrements]
        if HYPEN_E_DOT in requrements:
            requrements.remove(HYPEN_E_DOT)
        return requrements

setup(

    name = "Insurance Prediction",
    version = "0.0.1",
    author = "Aditya Papal",
    author_email = "papaladitya@gmail.com",
    install_require = get_requirements("requirements.txt"),
    packages = find_packages()
)
