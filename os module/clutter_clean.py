import os

os.chdir("os module/clutter_clean")
print("Current Dir:", os.getcwd())

all_files = os.listdir(".")
file_name_list = []
file_type_list = []

def seperate_name_ext():
    for file in all_files:
        if os.path.isfile(file) and not file.startswith('.'):  # skip folders & hidden files
            name, ext = os.path.splitext(file)
            file_name_list.append(name)
            file_type_list.append(ext)

seperate_name_ext()

def rename_by_type(file_type):
    def filter_types(file):
        return os.path.splitext(file)[1].lower() == file_type.lower()

    filtered_files = list(filter(filter_types, all_files))

    for index, file in enumerate(filtered_files):
        new_name = f"{index + 1}{file_type.lower()}"
        if not os.path.exists(new_name):  # avoid overwriting
            os.rename(file, new_name)
        else:
            print(f"Skipped {file}: {new_name} already exists")

def rename_all_by_type(types=None):
    if types is None:
        types = list(set(file_type_list))  # remove duplicates

    for file_type in types:
        rename_by_type(file_type)


rename_all_by_type() #no argument means all type will be renamed. pass a list [".txt","py"] argument to rename selected types








