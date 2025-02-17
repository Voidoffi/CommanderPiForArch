#!/usr/bin/python
import sys
import os
from os.path import expanduser

user = sys.argv[1]
home_path = expanduser(f"~{user}")

dir_path = os.path.dirname(os.path.realpath(__file__))

print(dir_path)
f_content = \
f"""[Desktop Entry]
Name=CommanderPi
Comment=System info and overclocking
Exec={dir_path}/src/start.sh
Icon={dir_path}/src/icons/Icon.png
Categories=Utility;
Version=1.0
Type=Application
Terminal=true
StartupNotify=true"""
print(f_content)

d_dir = home_path+"/Desktop/commanderpi.desktop"
x_dir = "/usr/share/applications/commanderpi.desktop"

print(f"Save desktop shortcut to {d_dir}")
try:
    f = open(d_dir, "w")
except FileNotFoundError:
    print("Couldn't create desktop shortcut!")
else:
    with f:
        f.write(f_content)


print(f"Save menu shortcut to {x_dir}")
try:
    f2 = open(x_dir, "w")
except FileNotFoundError:
    print("Couldn't create menu shortcut!")
else:
    with f2:
        f2.write(f_content)
