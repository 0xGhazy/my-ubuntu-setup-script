import os
import yaml
import json
from pathlib import Path
from termcolor import colored


SOFTWARE_YAML_FILE = "./data/softwares.yaml"
DEPENDENCIES = ["sudo apt-get install curl -y", "sudo apt-get install gnupg -y"]
SERVICE_YAML_FILE = ""
category_path = ""
DOWNLOAD_PATH = "./downloads"

TOOL_VERSION = colored("1.0.0", "yellow")
AUTHOR = colored("Hossam Hamdy", "blue")

def read_dict_from_yaml(software_yaml_path: str) -> dict:
	with open(software_yaml_path, 'r') as file:
		softwares_yaml = yaml.load(file, Loader=yaml.SafeLoader)
	return softwares_yaml


def display_banner():
	software_count = colored(len(read_dict_from_yaml(SOFTWARE_YAML_FILE).keys()), "red")
	print("   __,_,                                           ")
	print("  [_|_/                                            ")
	print("   //                                              ")
	print(" _//    __                                         ")
	print(f"(_|)   |@@|     By: {AUTHOR} aka <0xGhazy>        ")
	print(f" \ \\__ \\--/ __  Version: {TOOL_VERSION}         ")
	print("  \o__|----|  |   __                               ")
	print("      \ }{ /\\ )_ / _\\                            ")
	print("      /\__/\\ \\__O (__                            ")
	print("     (--/\--)    \\__/                             ")
	print("     _)(  )(_                                      ")
	print("    `---''---`                                     \n")
	print("Hello world, How can i help you?                    ")
	print(f"I can install cool [{software_count}] Development Tools, libs, and more :)\n")


def main():
    print(colored("[?] Read softwares yaml file", "green"))
    display_banner()

main()
