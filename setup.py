from setuptools import find_packages, setup

setup(
    name='faceverify',
    packages=find_packages(include=['faceverify']),
    version='0.1.0',
    description='Face verification for web',
    author='Jakub Wielgus',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)