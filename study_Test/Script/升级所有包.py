#coding=UTF-8
'''
Created on 2016��12��5��

@author: ZWT
'''
import pip
from subprocess import call
for dist in pip.get_installed_distributions():
    call("pip install --upgrade " + dist.project_name, shell=True)