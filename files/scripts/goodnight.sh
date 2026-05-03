#!/bin/bash

# --- The Guardian OS Goodnight Script ---
# This babysits Topgrade so you don't have to.

echo "🌙 Starting the Goodnight routine, Tim..."

# 1. Run Topgrade (This will update rpm-ostree, Brew, and Flatpaks)
# We use --non-interactive so it doesn't hang on questions
topgrade --non-interactive

echo "✅ System updates staged."

# 2. Sync any last-minute dotfile changes to GitHub
if command -v chezmoi &> /dev/null; then
    echo "💾 Syncing dotfiles..."
    chezmoi status
fi

echo "🔋 All set. Sleep well, Palmetto."
sleep 3

# 3. Power off
# On Atomic systems, the update applies on the NEXT boot.
systemctl poweroff
