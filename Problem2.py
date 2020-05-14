import os
def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    if os.path.isdir(path):
        if len(os.listdir(path))==0:
            return []
        file_elements=os.listdir(path)
        files=[os.path.join(path,file) for file in file_elements if file.endswith(suffix)]
        folders=[folder for folder in file_elements if "." not in folder]
        for each in folders:
            files.extend(find_files(suffix,os.path.join(path,each)))
        return files
    else:
        return "Wrong path"

# Normal Cases:
print(".c files in the whole testdir dir")
print(find_files('.c', "./testdir"))
print("\n\nNo suffix given,thersfore prints all\n")
print(find_files('',"./testdir"))
print("\n\nNo file present therefore in this directory")
print(find_files('.c',"./testdir/subdir2"))
print("\n\nIncorrect path is provided")
print(find_files('.c',"./testdir/user/subdir"))
