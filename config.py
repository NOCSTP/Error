import minecraft_launcher_lib


options = minecraft_launcher_lib.utils.generate_test_options();

options = {
    # This is needed
    "username": "NOCST",
    "uuid": "",
    "token": "",
    # This is optional
    "executablePath": "java", # The path to the java executable
    "defaultExecutablePath": "java", # The path to the java executable if the version.json has none
    "jvmArguments": [], #The jvmArguments
    "launcherName": "[BP]launcher", # The name of your launcher
    "launcherVersion": "1.0", # The version of your launcher
    "demo": False, # Run Minecraft in demo mode
    "customResolution": False, # Enable custom resolution
    "resolutionWidth": "854", # The resolution width
    "resolutionHeight": "480", # The resolution heigth
    "server": "example.com", # The IP of a server where Minecraft connect to after start
    "port": "123", # The port of a server where Minecraft connect to after start
    "enableLoggingConfig": False, # Enable use of the log4j configuration file
    "disableMultiplayer": False, # Disables the multiplayer
    "disableChat": False, # Disables the chat
    "quickPlayPath": None, # The Quick Play Path
    "quickPlaySingleplayer": None, # The Quick Play Singleplayer
    "quickPlayMultiplayer": "de8.mineconnect.xyz:25742", # The Quick Play Multiplayer
    "quickPlayRealms": None, # The Quick Play Realms
}