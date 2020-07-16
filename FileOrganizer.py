import os
import shutil
cdir = os.getcwd()
def listoffiles(dirname):
    listOfFile = os.listdir(dirname)
    allFiles = list()
    for entry in listOfFile:
        fullPath = os.path.join(dirname, entry)
        if os.path.isdir(fullPath):
        	continue
        else:
            allFiles.append(fullPath)
          
    return allFiles
files = listoffiles(cdir)
exts = list()
allexts = list()
for file in files:
	name, ext = os.path.splitext(file)
	exts.append(ext[1:])

occ = dict()
for extension in exts:
	occ[extension] = occ.get(extension, 0) + 1

allexts = list(occ)
dirs = len(allexts)
print("Working...")

for file in files:
	name, ext = os.path.splitext(file)
	for extension in exts:
		if(ext[1:] == extension):
			fullpath = (cdir + "/" + extension)
			if(os.path.isdir(fullpath)):
				continue
			else:
				os.mkdir(extension)

flag = 0
count = 0
for file in files:
	name, ext = os.path.splitext(file)
	for extension in allexts:
		if(ext[1:] == extension):
			fullpath = (cdir + "/" + extension)
			try:
				shutil.move(file, fullpath)	
			except:
				flag = 1
				count = count+1
if flag == 1:
	print("OOPS! It looks like", count, "files already exist(s) in their respective folders. Could not move them. Please check.")
else:
	print("Done!")