#!/usr/bin/env python
# coding: utf-8
# # get pageviews with AWS

import os, requests, bz2

def download_file(url, dirpath='./'):
    local_filename = dirpath + url.split('/')[-1]
    # NOTE the stream=True parameter below
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=131072):   #8192
                # If you have chunk encoded response uncomment if
                # and set chunk_size parameter to None.
                #if chunk: 
                f.write(chunk)
    return local_filename
# https://stackoverflow.com/questions/16694907/download-large-file-in-python-with-requests


# ##### download many files
urlpath = 'https://dumps.wikimedia.org/other/pageview_complete/2019/2019-10/'
filenames = ['pageviews-20191001-user.bz2', 'pageviews-20191002-user.bz2']
dirpath = '../data/raw/pageviews/'

for filename in [filenames[0]]:
    download_file(url=urlpath+filename, dirpath=dirpath)
    filepath = os.path.join(dirpath, filename)
    newfilepath = os.path.join(dirpath, filename + '.decompressed')
    with open(newfilepath, 'wb') as new_file, bz2.BZ2File(filepath, 'rb') as file:
        for data in iter(lambda : file.read(100 * 1024), b''):
            new_file.write(data)



