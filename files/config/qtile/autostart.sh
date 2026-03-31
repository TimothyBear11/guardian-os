#!/usr/bin/env bash

# 1. Start the D-Bus session and export it to the environment
dbus-update-activation-environment --systemd --all &

# 2. Initialize the Gnome Keyring (The "Login Memory" Fix)
eval $(gnome-keyring-daemon --start --components=pkcs11,secrets,ssh) &
export SSH_AUTH_SOCK

# 3. Start the wallpaper daemon early
swww-daemon &

# 4. Force monitor layout IMMEDIATELY
kanshi &
sleep 2 # Give Kanshi 2 full seconds to snap the OMEN to Primary

# 5. Now start the applets that live in the tray
nm-applet &
kdeconnect-indicator &
/usr/lib/polkit-kde-authentication-agent-1 &

# 6. Set the wallpaper
sleep 1
swww img ~/Pictures/Wallpapers/tealTile.png &
