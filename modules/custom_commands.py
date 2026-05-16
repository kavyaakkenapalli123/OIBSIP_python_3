import json

def execute_custom_command(command):

    with open("config/commands.json", "r") as file:

        commands = json.load(file)

    for key in commands:

        if key in command:

            print(commands[key])