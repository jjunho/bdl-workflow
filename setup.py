from setuptools import setup, find_packages

setup(
    name='bdlcli',
    version='0.1.0',
    description='CLI para workflow BDL',
    author='Seu Nome',
    author_email='seu@email.com',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'pyyaml',
    ],
    entry_points={
        'console_scripts': [
            'bdlcli=bdlcli.cli:main',
        ],
    },
    package_data={
        '': ['.github/prompts/*.md', 'BDL.yaml'],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)
