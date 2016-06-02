#!/usr/bin/python3

'''
    python3 files_keywords.py -p <path> -k <keywords separated by space>
'''

import os
import sys
import re

def isIgnored(name):
    global ignore
    for x in ignore:
        if '.'+ignore in name:
            return True
    return False


if __name__== '__main__':
    # global data
    keys = {'-k':'keywords', '-i':'ignore', '-p':'path' }
    data = {'path':os.popen("pwd").read().strip()} # default first element
    ignore = []
    keywords = []

    args = sys.argv
    
    
    allargs = ' '.join(args)

    params = re.findall(r'-[a-z]', allargs)
    splitted = re.split(r'-[a-z]', allargs)[1:] # first one is filename

    # fill dict data
    for i, parm in enumerate(params):
        data[keys[parm]] = splitted[i].strip()
    
    # take care of trailing / in path
    if data['path'][-1]== '/': data['path'] = data['path'][:-1]

    # populate list of ignore extensions
    data['ignore'] = data['ignore'].strip().split()
    
    # populate list of keywords
    data['keywords'] = data.get('keywords', '').strip().split()
    if len(data['keywords'])==0:
        print('ERROR IN FORMAT')
        assert False

    print(data)
    # final result is dict
    resultset = {}
    for keyword in data['keywords']: resultset[keyword]=[]
    
    print(resultset)
    
    # now iterate over the files and find if any exist
    
    files = [data['path']+'/'+x for x in os.popen('ls '+data['path']+' -p | grep -v /').read().strip().split()]
    
    for x in files:
        if isIgnored(x):continue
        try:
            print(os.popen('cat '+x).read().strip().split('\n'))
        except:
            pass
        assert False
    
    
    
    
    
