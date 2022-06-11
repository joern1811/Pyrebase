from setuptools import setup, find_packages

setup(
    name='Pyrebase',
    version='3.0.27',
    url='https://github.com/thisbejim/Pyrebase',
    description='A simple python wrapper for the Firebase API',
    author='James Childs-Maidment',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.4',
    ],
    keywords='Firebase',
    packages=find_packages(exclude=['tests']),
    install_requires=[
        'requests==2.28.0',
        'gcloud==0.18.3',
        'oauth2client==4.1.3',
        'requests_toolbelt==0.9.1',
        'python_jwt==3.3.2',
        'pycryptodome==3.14.1'
    ]
)
