from setuptools import setup

setup(
    name='pyDocsis',
    version='0.3.25',
    packages=['pydocsis'],
    url='https://github.com/botheredtodd/pyDocsis',
    license='Apache License 2.0',
    author='Todd Balsley',
    author_email='todd.balsley@cox.com',
    description='A library for working with docsis files',
    install_requires=[

    ],
    # python_requires='>=3.10',
    scripts=[
        'Scripts/cm_decode',
        'Scripts/mib-json-builder.py',
    ]
)

