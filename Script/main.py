#coding: utf-8

# Put your script (and all resources that it needs for running) in this folder.
# The filename of the main script should be "main.py".
from objc_util import NSBundle

info = NSBundle.mainBundle().infoDictionary()
version = str(info['CFBundleVersion'])
short_version = str(info['CFBundleShortVersionString'])
print(version)
print(short_version)
print('Hello World')
