from setuptools import setup

setup(
    name='pyDocsis',
    version='0.3.39',
    packages=['pydocsis'],
    long_description="pyDocsis: A library for doing things to DOCSIS configs with python.  This library is a work in progress and is not yet ready for production use.  It is being developed by Todd Balsley and Yu X at Cox Communications.",
    url='https://github.com/botheredtodd/pyDocsis',
    license='Apache License 2.0',
    author='Todd Balsley and Yu X',
    author_email='todd.balsley@cox.com',
    description='A library for working with docsis files',
    install_requires=[

    ],
    # python_requires='>=3.10',
    scripts=[
        'Scripts/cm_decode',
        'Scripts/mib-json-builder.py',
        'Scripts/mta_decode',
    ]
)

