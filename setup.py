from setuptools import setup, find_packages

VERSION = '0.0.8' 
DESCRIPTION = 'Python package for creating and deleting zoom meetings'
LONG_DESCRIPTION = 'This package allows for easy scheduling and updating of Zoom meetings within your django app. please visit https://github.com/JoeyAlpha5/django-zoom-meetings for more details'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="django_zoom_meetings", 
        version=VERSION,
        author="Jalome Chirwa",
        author_email="chjalome@gmail.com",
        url = "https://github.com/JoeyAlpha5/django-zoom-meetings",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=['PyJWT','requests'], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python', 'first package','zoom'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)