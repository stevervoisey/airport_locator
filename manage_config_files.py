import os
import configparser
import json


def load_config_file_from_json(parameter=None):
    example_config = {
        "DEFAULT": {
            "MAPPING_API": "UNDEFINED",
            "SECRET_KEY": "secret-key"},
        "TEST": {
            "MAPPING_API": "UNDEFINED",
            "SECRET_KEY": "secret-key"},
        "PRODUCTION": {
            "MAPPING_API": "UNDEFINED",
            "SECRET_KEY": "secret-key"},
    }

    env_config_file = os.environ.get('LOOKUP_AIRPORT_CONFIG_FILE', None)

    if parameter:
        with open(parameter, 'r') as config_file:
            config = json.load(config_file)

    elif env_config_file:
        with open(env_config_file, 'r') as config_file:
            config = json.load(config_file)

    elif os.path.isfile("config.json"):
        with open("config.json", 'r') as config_file:
            config = json.load(config_file)

    elif os.path.isfile("config_example.json"):
        with open("config_example.json", 'r') as config_file:
            config = json.load(config_file)

    else:
        config = example_config

    return config


def load_config_file(parameter=None):

    example_config = """
[DEFAULT]
MAPPING_API = UNDEFINED
SECRET_KEY = secret-key

[TEST]
MAPPING_API = UNDEFINED
SECRET_KEY = secret-key

[PRODUCTION]
MAPPING_API = UNDEFINED
SECRET_KEY = secret-key
"""
    config = configparser.ConfigParser()
    env_config_file = os.environ.get('LOOKUP_AIRPORT_CONFIG_FILE', None)

    if parameter:
        with open(parameter, 'r') as config_file:
            config.read(config_file)

    elif env_config_file:
        config.read(env_config_file)

    elif os.path.isfile("config.json"):
        config.read("config.json")

    else:
        config.read(example_config)

    return config

