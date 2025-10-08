from setuptools import setup, find_packages


def get_requirements_from_file():
    with open("./requirements.txt") as f_in:
        requirements = f_in.read().splitlines()
    return requirements


setup(
    name="thorlabs-cam",
    version="0.0.1",
    author="Yamato Ishii",
    author_email="yamato.ishii2001@gmail.com",
    description="Tools for thorlabs scientific camera sdk",
    install_requires=get_requirements_from_file(),
    python_requires=">=3.11",
    packages=find_packages(),
)