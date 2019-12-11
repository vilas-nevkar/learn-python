"""
Listing dirs:
os.listdir()	        Returns a list of all files and folders in a directory
os.scandir()	        Returns an iterator of all the objects in a directory including file attribute information
pathlib.Path.iterdir()	Returns an iterator of all the objects in a directory including file attribute information

Status:
os.stat()
os.scandir()
or pathlib.Path()

Creating dirs:
os.mkdir()	            Creates a single subdirectory
pathlib.Path.mkdir()	Creates single or multiple directories
os.makedirs()	        Creates multiple directories, including intermediate directories

Pattern Match:
startswith()	        Tests if a string starts with a specified pattern and returns True or False
endswith()	            Tests if a string ends with a specified pattern and returns True or False
fnmatch.fnmatch(filename, pattern)	Tests whether the filename matches the pattern and returns True or False
glob.glob()	            Returns a list of filenames that match a pattern
pathlib.Path.glob()	    Finds patterns in path names and returns a generator object

Deletion:
os.remove()	            Deletes a file and does not delete directories
os.unlink()	            Is identical to os.remove() and deletes a single file
pathlib.Path.unlink()	Deletes a file and cannot delete directories
os.rmdir()	            Deletes an empty directory
pathlib.Path.rmdir()	Deletes an empty directory
shutil.rmtree()	        Deletes entire directory tree and can be used to delete non-empty directories

Copying, Moving, Renaming:
shutil.copy(src, dst)
shutil.copy2(src, dst)
shutil.copytree('data_1', 'data1_backup')
shutil.move('dir_1/', 'backup/')
os.rename('first.zip', 'first_01.zip')

Archiving:
zipfile.extract()
zipfile.extractall()
tarfile.getnames()
tarfile.extract()
tarfile.extractfile()
tarfile.extractall()
tarfile.add()
shutil.make_archive()
shutil.unpack_archive()
"""