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
    if len(os.listdir(path))==0:
        return []
    file_elements=os.listdir(path)
    files=[path+"/"+file for file in file_elements if file.endswith(suffix)]
    folders=[folder for folder in file_elements if "." not in folder]
    for each in folders:
        files.extend(find_files(suffix,path+"/"+each))
    return files


# Normal Cases:
print(find_files('.c', "./testdir"))
print("\n\nNo suffix given,thersfore prints all\n")
print(find_files('',"./testdir"))
