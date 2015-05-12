from setuptools import setup

setup(
    name='Questionnaire',
    version='0.1',
    packages=['questionnaire'],
    include_package_data=True,
    description='Simple questionnaire app.',
    author='Bogdan Cornianu',
    install_requires=['Django==1.4.20', 'MySQL-python==1.2.5', 'South==0.7.6']
)
