from setuptools import setup

setup(
    name='pyDocsis',
    version='0.3',
    packages=['pydocsis'],
    url='https://github.com/botheredtodd/pyDocsis',
    license='LGPL-3.0 license',
    author='Todd Balsley',
    author_email='todd.balsley@cox.com',
    description='A library for working with docsis files'
    install_requires=[
        'joblib',
        'requests',
        'ipaddress',
        'urllib3',
        'six',
        "sqlalchemy",
        "sshtunnel",
        "pymysql",
        "sqlalchemy-utils",
        "psycopg",


    ],
    # python_requires='>=3.10',
    scripts=[
        'Scripts/cm_decode',
    ]
)

