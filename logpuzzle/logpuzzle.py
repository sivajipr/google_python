#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib
def sort_url(files):
	for line in files:
		match=re.search(r'a-(\w+)',line)
		if match:
			path1=match.group(1)
		return path1
	return sorted(files,key=path1)
def read_urls(filename):
	url=[]
	files=open(filename)
	for line in files:
		match = re.search(r'GET (\S+)',line)
		if match:
			path=match.group(1)
			if 'puzzle' in path:
				url.append(path)
	print url
#	def sort_url(url):
 #       	for line in url:
  #              	match=re.search(r'a-(\w+)',line)
   #             	if match:
    #                    	path1=match.group(1)
#	                	return path1
#		print sorted(url,key=sort_url)

def main():
  args = sys.argv[1:]

  if not args:
    print 'usage: [--todir dir] logfile '
    sys.exit(1)

  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  img_urls = read_urls(args[0])

  if todir:
    download_images(img_urls, todir)
  else:
    print '\n'.join(img_urls)

if __name__ == '__main__':
  main()
