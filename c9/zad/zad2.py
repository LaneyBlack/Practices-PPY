import errno
import os


def rmtree(path):
    for file in os.listdir(path):
        rmtree(os.path.join(path, file))
    os.rmdir(path)

try:
    with open("configuration.txt", mode="r", encoding="UTF-8") as fileconfig:
        isDeleteMode = fileconfig.readline().strip() == "delete"
        current_path = fileconfig.readline().strip()
        config = fileconfig.readline().strip()
    folder_name = ""
    if not isDeleteMode:
        for symbol in config:
            if symbol == '{':
                current_path = os.path.join(current_path, folder_name)
                os.mkdir(current_path)
                folder_name = ""
            elif symbol == ',':
                if folder_name != "":
                    tmp_dir = os.path.join(current_path, folder_name)
                    os.mkdir(tmp_dir)
                folder_name = ""
            elif symbol == '}':
                if folder_name!="":
                    tmp_dir = os.path.join(current_path, folder_name)
                    os.mkdir(tmp_dir)
                    current_path = os.path.split(current_path)[0]
                folder_name=""
            else:
                folder_name += symbol
    else:
        wasDeleted = False
        for symbol in config:
            if symbol == '}':
                wasDeleted = False
            elif wasDeleted:
                continue
            if symbol == '{':
                rmtree(os.path.join(current_path, folder_name))
                wasDeleted = True
                folder_name = ""
            elif symbol == ',':
                rmtree(os.path.join(current_path, folder_name))
                folder_name = ""
            else:
                folder_name += symbol
except OSError as exc:
        print(exc)
        #ToDo return all the changes