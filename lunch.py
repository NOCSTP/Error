import subprocess

import config

import minecraft_launcher_lib
print(minecraft_launcher_lib.command.get_minecraft_command("1.20.1-forge-47.2.7", "BP_minecraft", config.options))
subprocess.call(minecraft_launcher_lib.command.get_minecraft_command("1.20.1-forge-47.2.7", "BP_minecraft", config.options))
