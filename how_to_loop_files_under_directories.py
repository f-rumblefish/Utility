# This code is used in the following blog
# https://medium.com/@franky07724_57962/using-keras-pre-trained-models-for-feature-extraction-in-image-clustering-a142c6cdf5b1

# Assume that you have two directories, cats and dogs. The directory of 'cats' 
# has all the pictures of cats, and the directory of dogs has all the pictures 
# of dogs. The following code loops the directory of cats to get the file names 
# of all the cat pictures, then loops the directories of dogs to get the file 
# names of all the dog pictures.
#
# Please also check flow_from_directory in Keras 
# https://medium.com/@vijayabhaskar96/tutorial-image-classification-with-keras-flow-from-directory-and-generators-95f75ebe5720 

from os import listdir
from os.path import isfile, join

rootpath = "C:/Users/Frank/Desktop/RD/mypython/data-dc/dc/train/"
subdir = ['cats', 'dogs']

for idx, item in enumerate(subdir):
    pathname = rootpath + item
    print("[dir] ", pathname)
    filenames = [f for f in listdir(pathname) if isfile(join(pathname, f))]
    for i, fname in enumerate(filenames):
        print("[file] ", fname)