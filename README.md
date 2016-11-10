# Version-Compiler
## Easy autoupdate of your program with the rpi!

The Version-Compiler is a python script that checks at run a set git repo and at change it will
with the help of cmake create a project depends of your OS and then it will compile (make, nmake) it.

# SETUP
* Download the python file located at `/src/python/version_checker.py`
* Edit the variables in the head of the script to your git repo (please see the NOTE section)
* Save the script and add it to your autostart (`rc.local`) with sudo permission

### NOTE
* The `version.txt` file in the root dir of the repo (url can be specified in the script) is important to check the version! This must exists!
* The system builds your files with cmake, so our sourcecode must contain a valid `CMakeLists.txt`

# TEST
The default configuration, clones this repo and compile the test project located at `/src/vs_project/`

# BUILD STATE
![Gopher image](https://travis-ci.org/RBEGamer/Version-Compiler.svg?branch=master)
The Travis Build config is currently  not up to date but the script is working
