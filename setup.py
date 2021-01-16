from setuptools import find_packages, setup

setup(
    name='sigmage',
    version='0.0.1.dev0',
    author='Juho Kim, Hshmat Sahak',
    author_email='juho-kim@outlook.com',
    description='A package for signing images to mark original creator',
    long_description=open('README.md', 'r').read(),
    long_description_content_type='text/markdown',
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
