### ENVIRONMENT VARIABLES ###

fish_add_path "$HOME/.local/bin"

### INTERACTIVE SETTINGS ###
if status is-interactive
    # Disable default greeting
    set -g fish_greeting ""

    # --- Tool Initializations ---
    # Tide does not require an 'init' line here.
    # Just run 'tide configure' once in your terminal to set it up.

    # Initialize Zoxide (smarter cd)
    if type -q zoxide
        zoxide init fish | source
    end

    # Initialize Direnv (automatic env loading)
    if type -q direnv
        direnv hook fish | source
    end

    # --- Fastfetch (System Info) ---
    if type -q fastfetch
        fastfetch \
            --logo "$HOME/Pictures/newlogo1.png" \
            --logo-type auto \
            --logo-width 45 \
            --logo-height 27
    end

    # --- Load Custom Functions ---
    # Note: Fish usually autoloads files in ~/.config/fish/functions/
    # If you prefer your 'functions_extra' subfolder, this loop works:
    if test -d "$HOME/.config/fish/functions_extra"
        for f in $HOME/.config/fish/functions_extra/*.fish
            source $f
        end
    end

    # --- Git Abbreviations ---
    abbr -a gs 'git status'
    abbr -a ga 'git add .'
    abbr -a gc 'git commit -m "'
    abbr -a gp 'git push'
    abbr -a gd 'git diff'
    abbr -a gds 'git diff --staged'
    abbr -a gl 'git pull --rebase'
    abbr -a gco 'git checkout'
    abbr -a gb 'git branch -vv'
    abbr -a gcm 'git checkout main' # Separated the pull for safety
    abbr -a gundo 'git reset --soft HEAD~1'

    # --- Aliases ---
    alias vim='nvim'
    alias vi='nvim'

    # Modern ls replacement (eza)
    if type -q eza
        alias ls='eza --icons --group-directories-first'
        alias ll='eza -l --icons --group-directories-first'
        alias tree='eza --tree --icons'
    end

    # Quick navigation
    alias d='cd ~'
    alias dl='cd ~/Downloads'
    alias dt='cd ~/Documents'
    alias proj='cd ~/projects'
    alias reboot="sudo reboot"
    alias poweroff="sudo poweroff"

end


# Generated for envman. Do not edit.
test -s ~/.config/envman/load.fish; and source ~/.config/envman/load.fish
