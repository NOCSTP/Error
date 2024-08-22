import minecraft_launcher_lib as mine
import Directory
from git import Repo

import os
progress = 0


repo_url = 'https://github.com/NOCSTP/Launcher_BP.git'

clone_dir = 'BP_minecraft'


# Get the path to the downloads directory
downloads_dir = os.path.join(os.path.expanduser('~'), 'Downloads')

# Name of the folder to create
folder_name = 'BP_minecraft'

# Create the folder



Repo.clone_from(repo_url, clone_dir)




