# ==============================================================================
# Qtile Config for tbear - Marchborn Guardian Theme (Corrected)
# ==============================================================================

import os
import subprocess

from libqtile import bar, hook, layout
from libqtile.backend.wayland import InputConfig
from libqtile.config import Click, Drag, DropDown, Group, Key, Match, ScratchPad, Screen
from libqtile.lazy import lazy

# NEW IMPORTS FOR CAPSULES
from qtile_extras import widget
from qtile_extras.widget.decorations import RectDecoration

# --- Wayland Input Rules ---
wl_input_rules = {
    "type:keyboard": InputConfig(
        kb_repeat_rate=50,
        kb_repeat_delay=300,
    ),
    "*": InputConfig(
        accel_profile="flat",  # Disables mouse accel for 1:1 snappiness
        pointer_accel=0,
    ),
}

# ==================== THEME VARIABLES ====================
colors = {
    "bg": "#1A2024",  # Dark Slate Base
    "bg_alt": "#22292E",  # Lighter Slate for panels
    "fg": "#D3E0E2",  # Icy White Text
    "primary": "#7FFFD4",  # Bright Aquamarine
    "secondary": "#FF4D4D",  # Bright Bloodstone Red (Glow)
    "inactive": "#34424A",  # Muted Slate for borders/capsules
    "alert": "#8A0303",  # Dark Bloodstone for warnings
}

# ==================== VARIABLES ====================
mod = "mod4"  # Super key
terminal = "kitty"
launcher = "fuzzel"

# ==================== KEYBINDINGS ====================
keys = [
    # --- Window Navigation ---
    Key([mod], "left", lazy.layout.left()),
    Key([mod], "right", lazy.layout.right()),
    Key([mod], "down", lazy.layout.down()),
    Key([mod], "up", lazy.layout.up()),
    # --- Window Movement ---
    Key([mod, "shift"], "left", lazy.layout.shuffle_left()),
    Key([mod, "shift"], "right", lazy.layout.shuffle_right()),
    Key([mod, "shift"], "down", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "up", lazy.layout.shuffle_up()),
    # --- Window Controls ---
    Key([mod], "f", lazy.window.toggle_fullscreen()),
    Key([mod, "shift"], "space", lazy.window.toggle_floating()),
    Key([mod], "q", lazy.window.kill()),
    # --- MonadTall Specifics ---
    Key([mod], "m", lazy.layout.maximize()),  # Toggle between 70% and 100%
    Key(
        [mod, "shift"], "Return", lazy.layout.swap_main()
    ),  # Swap current window to the 70% slot
    Key([mod], "equal", lazy.layout.grow()),  # Increase the 70% area
    Key([mod], "minus", lazy.layout.shrink()),  # Decrease the 70% area
    # Use your existing arrow keys to move focus between the main and stack
    # --- Layout Cycling ---
    Key([mod], "space", lazy.next_layout()),  # Cycle Forward
    Key([mod, "shift"], "space", lazy.prev_layout()),  # Cycle Backward (Reverse)
    # --- Qtile Controls ---
    Key([mod, "shift"], "r", lazy.reload_config()),
    Key([mod, "shift"], "e", lazy.shutdown()),
    # --- Applications ---
    Key([mod], "d", lazy.spawn(launcher)),
    Key([mod], "Return", lazy.spawn(terminal)),
    Key([mod], "n", lazy.spawn(f"{terminal} -e nvim")),
    Key([mod], "k", lazy.spawn("kate")),
    Key([mod], "z", lazy.spawn("zeditor")),
    Key([mod], "b", lazy.spawn("floorp")),
    Key([mod], "m", lazy.spawn("spotify")),
    Key([mod], "v", lazy.spawn("vesktop")),
    Key([mod], "s", lazy.spawn("steam")),
    Key([mod], "h", lazy.spawn("heroic")),
    Key([mod], "e", lazy.spawn("thunar")),
    Key([mod], "j", lazy.spawn("joplin-desktop")),
    Key([mod], "p", lazy.spawn("positron")),
    # --- Scratchpad ---
    Key([mod], "t", lazy.group["scratchpad"].dropdown_toggle("term")),
]

# ==================== WORKSPACES ====================
groups = [Group(str(i)) for i in range(1, 10)]

for i in groups:
    keys.extend(
        [
            Key([mod], i.name, lazy.group[i.name].toscreen()),
            Key([mod, "control"], i.name, lazy.window.togroup(i.name)),
        ]
    )

# ==================== SCRATCHPAD ====================
groups.append(
    ScratchPad(
        "scratchpad",
        [
            DropDown(
                "term",
                "kitty --class=scratchpad",
                opacity=0.95,
                height=0.7,
                width=0.8,
                x=0.1,
                y=0.2,
            )
        ],
    )
)

# ==================== LAYOUTS ====================
layouts = [
    layout.MonadTall(
        border_focus=colors["primary"],
        border_normal=colors["inactive"],
        border_width=2,
        margin=8,
        ratio=0.7,  # This sets the Master window to 70% of the screen
        new_client_position="after_current",  # New windows go into the 30% stack
    ),
    layout.Columns(
        border_focus=colors["primary"],
        border_normal=colors["inactive"],
        border_width=2,
        margin=8,
        insert_position=1,
    ),
    layout.Max(),
    layout.Floating(
        border_focus=colors["secondary"],
        border_normal=colors["inactive"],
        border_width=2,
    ),
]

# ==================== BAR WIDGETS & CAPSULES ====================
widget_defaults = dict(
    font="FiraCode Nerd Font",
    fontsize=14,
    padding=6,
    foreground=colors["fg"],
)
extension_defaults = widget_defaults.copy()


def capsule(color):
    return dict(
        decorations=[
            RectDecoration(
                colour=color,
                radius=12,
                filled=True,
                padding_y=4,
                group=False,
            )
        ],
        padding=12,
    )


def init_widgets_left():
    return [
        widget.GroupBox(
            active=colors["primary"],
            inactive=colors["inactive"],
            highlight_method="line",
            highlight_color=[colors["bg_alt"], colors["bg_alt"]],
            this_current_screen_border=colors["secondary"],
            borderwidth=3,
            disable_drag=True,
        ),
        widget.Spacer(length=10),
        # --- The Layout Indicator Capsule ---
        widget.CurrentLayout(
            foreground=colors["primary"],
            # Left Click = Next, Right Click = Previous
            mouse_callbacks={
                "Button1": lazy.next_layout(),
                "Button3": lazy.prev_layout(),
            },
            **capsule(colors["inactive"]),
        ),
        widget.Spacer(length=10),
        widget.WindowName(foreground=colors["primary"]),
    ]


def init_widgets_center():
    return [
        # FIXED: Forces Fahrenheit more explicitly via ?u& format
        widget.GenPollCommand(
            cmd='curl -s "wttr.in/Brandon,FL?u&format=%c+%t" | sed "s/+//" | tr -d "\n"',
            shell=True,
            update_interval=600,
            foreground=colors["primary"],
            **capsule(colors["inactive"]),
        ),
        widget.Spacer(length=6),
        widget.Clock(
            format="%a %b %d  |  %I:%M %p",
            foreground=colors["primary"],
            **capsule(colors["inactive"]),
        ),
        widget.Spacer(length=6),
        # FIXED: Added initial_timeout to allow network sync on boot
        widget.CheckUpdates(
            distro="Arch_checkupdates",
            display_format="󰚰 {updates}",
            no_update_string="󰚰 0",
            update_interval=1800,
            initial_timeout=15,
            colour_no_updates=colors["primary"],
            colour_have_updates=colors["secondary"],
            **capsule(colors["inactive"]),
        ),
    ]


def init_widgets_right_primary():
    return [
        widget.CPU(
            format="󰍛 {load_percent}%",
            foreground=colors["secondary"],
            **capsule(colors["inactive"]),
        ),
        widget.Spacer(length=6),
        widget.Memory(
            format="󰘚 {MemUsed: .0f}{mm}",
            foreground=colors["secondary"],
            **capsule(colors["inactive"]),
        ),
        widget.Spacer(length=6),
        widget.StatusNotifier(**capsule(colors["inactive"])),  # Tray
        widget.Spacer(length=6),
        widget.Notify(**capsule(colors["inactive"])),
        widget.Spacer(length=6),
        widget.QuickExit(
            default_text=" ⏻ ",
            countdown_format=" [{}] ",
            foreground=colors["secondary"],
            **capsule(colors["inactive"]),
        ),
    ]


def init_widgets_right_secondary():
    return [
        widget.CPU(
            format="󰍛 {load_percent}%",
            foreground=colors["secondary"],
            **capsule(colors["inactive"]),
        ),
        widget.Spacer(length=6),
        widget.Memory(
            format="󰘚 {MemUsed: .0f}{mm}",
            foreground=colors["secondary"],
            **capsule(colors["inactive"]),
        ),
        widget.Spacer(length=10),
        widget.Notify(**capsule(colors["inactive"])),
        widget.Spacer(length=6),
        widget.QuickExit(
            default_text=" ⏻ ",
            foreground=colors["secondary"],
            **capsule(colors["inactive"]),
        ),
    ]


# ==================== BAR BUILDERS ====================
def create_primary_bar():
    return bar.Bar(
        [
            *init_widgets_left(),
            widget.Spacer(),
            *init_widgets_center(),
            widget.Spacer(),
            *init_widgets_right_primary(),
        ],
        size=32,
        background=colors["bg_alt"],
        opacity=0.95,
        margin=[4, 8, 0, 8],
    )


def create_secondary_bar():
    return bar.Bar(
        [
            *init_widgets_left(),
            widget.Spacer(),
            *init_widgets_center(),
            widget.Spacer(),
            *init_widgets_right_secondary(),
        ],
        size=32,
        background=colors["bg_alt"],
        opacity=0.95,
        margin=[4, 8, 0, 8],
    )


# ==================== SCREENS ====================
screens = [
    Screen(top=create_primary_bar()),  # Main Monitor (OMEN)
    Screen(top=create_secondary_bar()),  # Secondary
    Screen(top=create_secondary_bar()),  # Tertiary
]

# ==================== MOUSE BINDINGS ====================
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button1", lazy.window.bring_to_front()),
]

# ==================== FLOATING RULES ====================
floating_layout = layout.Floating(
    border_focus=colors["secondary"],
    border_normal=colors["inactive"],
    border_width=2,
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class="fuzzel"),
        Match(wm_class="scratchpad"),
        Match(title="pinentry"),
    ],
)


# ==================== AUTOSTART ====================
@hook.subscribe.startup_once
def autostart():
    script = os.path.expanduser("~/.config/qtile/autostart.sh")
    subprocess.Popen([script])


# ==================== BEHAVIOR SETTINGS ====================
follow_mouse_focus = True
bring_front_click = False
cursor_warp = True
focus_on_window_activation = "focus"  # Forced focus
auto_minimize = True
reconfigure_screens = True
wmname = "Qtile"
