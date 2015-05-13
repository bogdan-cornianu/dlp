from setuptools import setup

setup(
    name='Questionnaire',
    version='0.1',
    packages=['questionnaire'],
    include_package_data=True,
    description='Simple questionnaire app.',
    author='Bogdan Cornianu',
    install_requires=[
        'Django==1.4.20',
        'MySQL-python==1.2.5',
        'South==1.0.2',
        'pytest==2.7.0',
        'pytest-django==2.8.0',
        'tox==1.9.2'
    ]
)
