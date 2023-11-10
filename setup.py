from setuptools import setup, find_packages

setup(
    name='math_quiz_game',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'random',  # No need to specify 'random' as it's part of the standard library
    ],
    entry_points={
        'console_scripts': [
            'math_quiz = your_module_name:math_quiz',  # Replace with the actual name of your module
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
