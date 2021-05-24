from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Python package for creating and deleting zoom meetings'
LONG_DESCRIPTION = 'This package allows for easy scheduling and updating of Zoom meetings within your django app.'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="django-zoom-meetings", 
        version=VERSION,
        author="Jalome Chirwa",
        author_email="chjalome@gmail.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=['PyJWT','requests'], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python', 'first package'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)