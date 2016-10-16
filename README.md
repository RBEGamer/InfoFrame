# Version-Compiler
The Version-Compiler is a python script that checks at run a set git repo and at change it will
with the help of cmake create a project depends of your OS and then it will compile (make, nmake) it.
#Easy autoupdate of your program with the rpi!
#SETUP
download and change the variables to your git and storage paths in the scriptfile located at
src/python/version_checker.py 

The version.txt file in the root dir of the repo (url can be specified in the script) is important to check the version!

and run
sudo python version_checker.py
#TEST
The default configuration, clones this repo and compile the test project located at /src/vs_project/
