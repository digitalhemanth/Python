#Python PIP

'''
Python pip : 

Python PIP is a package manger, you can use it to install certain libraries to your python 
installation. You can say it is a replacement for easy_install. 
We can use pip to install python modules and their dependency also.

''' 
#Question: Python 2.x Vs Python 3.x :Do I have already PIP?

'''
PIP is there if you are on Python 2 >=2.7.9 or Python 3 >=3.4 binaries downloaded from python.org,
but you’ll need to upgrade pip. Also,pip will be there if you are working in a Virtual Environment 
created by virtualenv or pyvenv.
'''

#Python Install pip

'''
There are many ways to install pip, but my preferred method is the following:

Download the get-pip.py in your system or copy content of the above url in a text file and rename it
to get-pip.py.

Open a CMD window and select the folder location where the file is located. Run python get-pip.py
For verification of a successful installation, open a CMD window and navigate to scripts folder under Python folder (Default is C:\Python27\Scripts).
Type command from this location to launch the Python interpreter.

'''
#Set environment variable for PIP

'''
If you set PATH environment variable then you won’t have to reference the pip install directory again
and again.
Set: (default = C:\Python37\Scripts) in your Windows/Linux “PATH” environment variable.
'''
#How to use Pip and PYPI
'''
PYPI stands for Python Package Index. It’s required for finding a package to install. Packages will be installed from the Python Package Index.
PYPI is a repository of software for the Python programming language.
'''
#Getting Started with PIP

'''
To install a package using PIP, just open up your terminal, and type in a search query using the PIP tool.

'''
#PIP Search packages and modules
             # pip search Flask

#Installing a package

            # pip install Flask

#Pip – Show information

             # pip show Flask

#Uninstalling a package
             
              # pip uninstall Flask


