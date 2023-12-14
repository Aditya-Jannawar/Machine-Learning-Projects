from setuptools import find_packages, setup

HYPEN_E_DOT = '-e .'

def get_requirements(file_path):
    '''
    this function will return list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.read()
        requirements = [req.replace("\n", "") for req in requirements.split('\n') if req]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name='Machine-Learning-Projects',
    version='0.0.1',
    author='Aditya',
    author_email='adijannawar@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
