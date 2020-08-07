import os
import xml.etree.ElementTree as ET

from path_util import get_project_root

APK_NAME = "test"

RES_PATH = get_project_root() + "\\sources\\" + APK_NAME + "\\res\\"

DEFAULT_RES = "values"


def get_strings_file(directory):
    return RES_PATH + "\\" + directory + "\\strings.xml"


def is_string_resource(directory):
    return os.path.isfile(get_strings_file(directory))


def get_all_string_resources() -> []:
    languages = []
    res_directories = os.listdir(RES_PATH)
    for directory in res_directories:
        if is_string_resource(directory):
            languages.append(directory)
    return languages


# Check if there all strings are translated
def get_all_strings(directory):
    tree = ET.parse(get_strings_file(directory))
    root = tree.getroot()

    strings = {}
    for child in root:
        strings[child.attrib["name"]] = child.text
    return strings


langs = get_all_string_resources()

default_strings = get_all_strings(DEFAULT_RES)
print(default_strings)
