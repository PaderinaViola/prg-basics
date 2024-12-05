import re
fileaaa = "files.txt"
pattern = r"\w+\.\w{4}"


def names(files):
    matching_files = []
    with open(files, 'r') as file:
        content = file.readlines()
        for name in content:
            match = re.search(pattern, name)
            if match:
                matching_files.append(name)
    return(matching_files)

matching_files = names(fileaaa)
for name in matching_files:
    print(name, end='')  


