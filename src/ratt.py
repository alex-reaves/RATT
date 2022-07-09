import os
import yaml # https://pynative.com/python-yaml/

userHome = f"/home/{os.getlogin()}"

# Get status of `.cache/RATT-cache.yaml`, `.config/RATT-config.yaml`, and `RATT-tasklist.yaml` #
if os.path.isfile(f"{userHome}/.cache/RATT-cache.yaml") == 0:
    pass
if os.path.isfile(f"{userHome}/.config/RATT-config.yaml") == 0:
    pass

#Need to look for cached location of `RATT-tasklist.yaml`
taskfile = open(f"{userHome}/.cache/RATT-cache.yaml","a")
################################################################################################

print("Put the stuff here")