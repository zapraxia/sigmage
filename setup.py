from setuptools import find_packages, setup

with open('README.rst', 'r') as long_description_file:
    long_description = long_description_file.read()

setup(
    name='sigmage',
    version='0.0.1.dev3',
    author='Juho Kim et al.',
    author_email='juho-kim@outlook.com',
    description='A package for signing images to mark the original creators',
    long_description=long_description,
    long_description_content_type='text/x-rst',
    url='https://github.com/Zapraxia/sigmage',
    packages=find_packages(),
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    python_requires='>=3.7',
    install_requires=['stegano'],
)
