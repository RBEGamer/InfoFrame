#VERISON CHECKER MARCEL OCHSENDORF C OCT 2016
import os
import os.path
import httplib2
from git import Repo
import subprocess
from subprocess import call
import shutil
import glob

#PLEASE SETUP YOUR PATHS HERE
executable_dir = '/home/info_frame/' #the dir where your final compile result was located
executable_name = executable_dir + 'info_frame' #the path and the name of your executable to run it
repo_version_file_path = 'https://raw.githubusercontent.com/RBEGamer/InfoFrame/master/version.txt' #the url to ur version textfile this can be in your repo using the raw mode
repo_source_git_path = 'https://github.com/RBEGamer/InfoFrame.git' #the git project to clone
version_file_path = executable_dir + 'current_version.txt' #path to your local version file
repo_local_clone_dir = './clone_dir/' #temp dir for storing the clone data this can be the /tmp dir
#version_file_path_clone = repo_local_clone_dir + 'version.txt'
src_dir_to_compile = repo_local_clone_dir + 'src/vs_project/info_frame/info_frame/'#the path starting from your repo root for your souce cmake lists.txt
src_dir_to_build = src_dir_to_compile + 'build/' #dont touch it :) because cmake ..
execute_after_compile = 1 #1/0 set this to 1 to run it after compile
execute_if_no_update_required = 1 #1/0 set this to 1 to run it if no update requied
#FLAGS (OPTIONAL, DEFAULT IS '')
cmake_additional_flags = '-G "Unix Makefiles" -DCMAKE_BUILD_TYPE=RELEASE' #additional flags for the cmake call
make_additional_flags = ''#additional flags for the make call
exec_additional_flags = ''#additional flags for executiong og the final compile result

#version vars
current_version = '-1'
current_online_version = '-1'

print "VERSION CHECKER START"


#check if execute folder exists
if not os.path.exists(executable_dir):
    os.mkdir(executable_dir)
    print 'create executable dir'
#check if version file exists
if not os.path.exists(version_file_path):
    current_version = '0'
    f = file(version_file_path, 'w+')
    f.write(current_version)
    f.close()
    print 'create missing local version file ' + version_file_path
else:
    #read version file
    file = open(version_file_path, 'r')
    lines = file.readlines()
    current_version = lines[0]
    file.close()
#read remote version file
try:
    resp, content = httplib2.Http().request(repo_version_file_path)
    #print content
    current_online_version = content #todo add check to valid number
except:
    print 'request failed please check internet connection or repo link'
    current_online_version = '-1'

#check if update required
print current_version + '==' + current_online_version
if not current_version == current_online_version:
    print 'online version different update it'
    try:
        print 'start cloning repo'
        #clean rebo dir
        if os.path.exists(repo_local_clone_dir):
            shutil.rmtree(repo_local_clone_dir)
            print 'remove old clone dir'
        #check version file
        if not os.path.exists(version_file_path):
            f = open(version_file_path, 'w')
            f.write(current_online_version)
            f.close()
            print 'create missing local version file ' + version_file_path
        #write new version to local file
        ft = open(version_file_path, 'w')
        ft.write(current_online_version)
        ft.close()
        #clone
        Repo.clone_from(repo_source_git_path, repo_local_clone_dir)
        #CREATE BUILD DIR
        if not os.path.exists(src_dir_to_build):
            os.mkdir(src_dir_to_build)
            print 'create build folder'
        else:
            print 'clean build dir'
            shutil.rmtree(src_dir_to_build)
        #RUN CMAKE
        print 'run cmake'
        return_code = subprocess.call("cmake .. " + cmake_additional_flags, shell=True, cwd=src_dir_to_build)
        #RUN COMPILE
        print 'run make'
        return_code = subprocess.call("make " + make_additional_flags, shell=True, cwd=src_dir_to_build)
        #COPY FILE TO DEST
        print 'CLEANUP FINAL DIR'
        shutil.rmtree(executable_dir)
        #COPY FINAL FILES
        print 'COPY FILES TO FINAL DIR'
        shutil.copytree(src_dir_to_build, executable_dir)
        #CLEAN GIT CLONE
        shutil.rmtree(repo_local_clone_dir)
        #TEST
        if not os.path.exists(version_file_path):
            f = open(version_file_path, 'w')
            f.write(current_online_version)
            f.close()
            print 'create missing local version file ' + version_file_path

        print 'EXECUTE FINAL RESULT'
        if execute_after_compile == 1:
          subprocess.call(executable_name +  exec_additional_flags, shell=True)

    except:
        print 'cant clone repo'
else:
    print 'no update requied execute'
    if execute_if_no_update_required == 1:
         if os.path.exists(executable_name):
             subprocess.call(executable_name + ' ' + exec_additional_flags, shell=True)
        else:
            print 'execute path not exists'
    #TODO RUN PRODUCT
