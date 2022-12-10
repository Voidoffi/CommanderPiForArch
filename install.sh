#!/bin/sh
echo '##########################################'
echo 'Installing packages for CommanderPi'
echo '##########################################'
sudo pacman -S tk python-pillow python-pip

sudo pip install psutil
sudo chmod +x ${path}/src/start.sh
echo '##########################################'
echo 'Creating a shortcut on the desktop'
echo '##########################################'
sudo python c_desktop.py $USER
if [ -d "$HOME/Desktop" ]
then
    sudo chown $USER ~/Desktop/commanderpi.desktop
    sudo chmod +x ${HOME}/Desktop/commanderpi.desktop
else
    echo "Could not find Desktop path!"
fi
exit 0
