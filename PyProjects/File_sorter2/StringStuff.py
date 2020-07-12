import json
import os

def get_destination(filename):
        destination = ""
        index = 0
        taglist = filename.split("#")[0:-1]
        tags = load_json("sorter.json")
        
        for tag in tags:
            if tags[tag]["Index"] == index:
                destination = destination + tags[tag][taglist[index]]
                index += 1
        return destination

def load_json(name):
        with open(name, "r") as f:
            parsed_json = json.load(f)
        return parsed_json

def ensure_dir(file_path):
        if not os.path.exists(file_path):
            os.makedirs(file_path)