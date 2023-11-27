from setuptools import setup, find_packages

# get version
#with open('VERSION.md', 'r') as in_file:
#    VERSION = in_file.read()
#    in_file.close()
VERSION = "0.0.2"

setup(
    name='mkslides',
    version=VERSION,
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