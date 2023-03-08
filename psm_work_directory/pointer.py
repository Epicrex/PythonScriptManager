"""
This file is used to determine the relative path of every other file, the location of this file must stay un-touched.

This file contains all file/ folder paths that any scripts need. This means that when a file is added or renamed,
one only has to add or rename it here.

Make sure to NEVER reference file/ folder paths or names anywhere, instead ALWAYS ask this pointer file for the path,
and if it doesn't have the path or name you want, add it.
"""


#####################################################################################
# General Folders
#####################################################################################
def paths():
    # PY Scripts Folder
    py_scripts = "py_scripts"

    # Requirements Folder
    requirements = "requirements"

    # Dev and User Log Folders
    user_logs = r"..\User Logs"

    # Resources
    other_resources = "other_resources"


#####################################################################################
# Specific Folders/ Files
#####################################################################################
def specific_paths():
    pass
