import os.path
import httplib2
from git import Repo
#import urllib.request
#import requests
#from pathlib import Path
repo_version_file_path = 'https://raw.githubusercontent.com/RBEGamer/InfoFrame/master/version.txt'
repo_source_git_path = 'https://github.com/RBEGamer/InfoFrame.git'
version_file_path = './current_version.txt'
current_version = '-1'
current_online_version = '-1'
repo_local_clone_dir = './clone_dir/'
version_file_path_clone = './clone_dir/version.txt'
print "INFO FRAME VERSION CHECKER START"
#read locl version file // if not exists create one
if not os.path.exists(version_file_path):
    current_version = '0'
    f = file(version_file_path, 'w+')
    f.write(current_version)
else:
    #read version file
    file = open(version_file_path, 'r')
    lines = file.readlines()
    current_version = lines[0]
    
#read remote version file    
try:
    resp, content = httplib2.Http().request(repo_version_file_path)
    print content
    current_online_version = content #todo add check to valid number
except err:
    print 'request failed please check internet connection or repo link'
    current_online_version = '-1'
    
#check if update required
if not current_version == current_online_version:
    print 'online version different update it'
    try:
        print 'start cloning repo'
        Repo.clone_from(repo_source_git_path, repo_local_clone_dir)
        #check version file
        if not os.path.exists(version_file_path):
            current_version = '0'
        else:
        #read version file
            file = open(version_file_path_clone, 'r')
            lines = file.readlines()
            current_version = lines[0]
            #write new version to file
            f = file(version_file_path, 'w+')
            f.write(current_version)
            
            
            #RUN CMAKE
            #RUN COMPILE
            #EXECUTE FILE
        
        
    except err:
        print 'cant clone repo'
else:
    print 'no update requied'
    
    #TODO RUN PRODUCT
