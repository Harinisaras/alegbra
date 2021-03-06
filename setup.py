from setuptools import setup

with open('README.md', 'r') as file:
     long_description = file.read()

setup(
    name='alegbra',
    version='1.0',
    description='A package that can perform alegbric functions . ',
    long_description=long_description,
    long_description_content_type='text/markdown',
    py_modules=['alegbra'],
    package_dir={'': 'src'},
    classifiers=[

         "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
    ],
    install_requires=[],
    url="https://github.com/Harinisaras/alegbra.git",
    author='Harini.T,Venkateswar.S ',
    author_email='harinisarasv@gmail.com'
)