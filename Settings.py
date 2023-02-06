import json


def get_default_input():
    with open("settings.json", "r") as f:
        settings = json.load(f)
        return settings["default_input"]


def get_default_output0():
    with open("settings.json", "r") as f:
        settings = json.load(f)
        return settings["default_output0"]


def get_default_output1():
    with open("settings.json", "r") as f:
        settings = json.load(f)
        return settings["default_output1"]


def wirte_default_settings(default_input, default_output0, default_output1):

    file = {
        "default_input": default_input,
        "default_output0": default_output0,
        "default_output1": default_output1,
    }

    with open("settings.json", "w") as f:
        json.dump(file, f, indent=4)
