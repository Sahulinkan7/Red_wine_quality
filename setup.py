from setuptools import setup,find_packages

HYPHEN_E_DOT="-e ."
project_name="redwine_quality_prediction"
version="0.0.1"
def requirement_list(file_path):
    with open(file_path) as file:
        requirements=file.readlines()
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
        requirements=[r.replace("\n","") for r in requirements]
        return requirements
setup(
    name=project_name,
    author="Linkan kumar sahu",
    author_email="sahulinkan7@gmail.com",
    install_requires=requirement_list("requirements.txt"),
    packages=find_packages()
)