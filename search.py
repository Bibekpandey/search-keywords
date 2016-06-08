#!/usr/bin/python3

'''
    python3 files_keywords.py -p <path> -k <keywords separated by space> -i <ignore extensions>
'''

import subprocess
import sys
import re

ignore = 'pdf,jpg,tgz,doc,pptx,odt'.split(',')

def isIgnored(name):
    global data 
    for x in data['ignore']:
        if '.'+x in name:
            return True
    return False

def escape(filename):
    lst = [' ', '[', ']']
    ret = filename
    for x in lst:
        ret = ret.replace(x, '\\'+x)
    return ret

def printmsg():
    print('Usage: <command> -k <KEYWORDS> [-p <PATH> [-i <IGNORED EXTENSIONS>]]')
    print('Example: ./search-keywords.py -k include SomeVariableName SomeFunctionName AnyName -p /Some/Path/ -i jpg png etc')
   


if __name__== '__main__':
    keys = {'-k':'keywords', '-i':'ignore', '-p':'path' }
    data = {'path':subprocess.getoutput("pwd").strip()} # default first element
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
    if 'ignore' in data.keys():
        data['ignore'] = data['ignore'].strip().split()
    else:
        data['ignore'] = []

    tmp = set(data['ignore'])
    tmp1 = set(ignore)
    data['ignore'] = list(tmp.union(tmp1))
    
    # populate list of keywords
    data['keywords'] = data.get('keywords', '').strip().split()
    if len(data['keywords'])==0:
        printmsg()
        exit(0)

    # final result is dict
    resultset = {}
    for keyword in data['keywords']:
        resultset[keyword]=[] 
    
    # now iterate over the files and find if any exist
    files = []
    op = subprocess.getstatusoutput('ls '+data['path']+' -p | grep -v /')
    if op[0]==1:
        print("Please Enter a valid directory path")
        printmsg()
        exit(1)
    
    files = [data['path']+'/'+x for x in op[1].strip().split('\n')]
    
    for x in files:
        if isIgnored(x):
            print('Ignoring file:', x)
            continue
        try:
            lines = subprocess.getoutput('cat \''+escape(x)+'\'').strip().split('\n')
            for keyword in data['keywords']:
                l = [i+1 for i,y in enumerate(lines) if keyword in y]     
                if len(l)>0:
                    resultset[keyword].append((x,l))
        except Exception as e:
            print(e)

    # now output
    print()
    for keyword in data['keywords']:
        print('KEYWORD \''+ keyword+ '\' FOUND: ',end='')
        if len(resultset[keyword])==0:
            print('Nowhere')
        else:
            print()
            for filepath in resultset[keyword]:
                print('  in file \''+ filepath[0]+ '\'')
                for l in filepath[1]:
                    print('    at line ', l)
        print()
