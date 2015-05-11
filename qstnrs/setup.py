from setuptools import setup, find_packages

setup(
    name='Questionnaire',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    description='Simple questionnaire app.',
    author='Bogdan',
    requires=['django']
)
