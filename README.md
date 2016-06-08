# search-keywords

This is a very simple program that finds out the keywords we want to search in files inside a directory.

## Requirements
* python3
* linux (using bash)

## Usage
Very very easy.  
* If you have made the `search.py` file executable, just do  
`./search.py -k <your desired keywords> -p <path of the directory> -i <extensions to be ignored>`    
  
* If `search.py` is not executable do  
`python3 search.py -k <your desired keywords> -p <path of the directory> -i <extensions to be ignored>`  
  
NOTE: 
* If `-p` not provided, it searches in the current directory
* If `-i` not provided, it has default set of ignore extensions (pdf,jpg,tgz,doc,pptx,odt) [more will be added, don't worry!!]
* `-k` is a must.
* Keywords and ignore extensions need to be separated by comma
