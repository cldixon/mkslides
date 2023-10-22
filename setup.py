from setuptools import setup, find_packages

setup(
    name='mkslides',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'rich',
        'PyYAML'
    ],
    entry_points={
        'console_scripts': [
            'mkslides = mkslides.main:mkslides',
        ],
    },
)