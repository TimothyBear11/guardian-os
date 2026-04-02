#!/usr/bin/env bash


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
