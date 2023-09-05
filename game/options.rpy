## This file contains options that can be changed to customize your game.
##
## Lines beginning with two '#' marks are comments, and you shouldn't uncomment
## them. Lines beginning with a single '#' mark are commented-out code, and you
## may want to uncomment them when appropriate.


## Basics ######################################################################

## A human-readable name of the game. This is used to set the default window
## title, and shows up in the interface and error reports.
##
## The _() surrounding the string marks it as eligible for translation.

define config.name = _("Карта Вариополиса")


## Determines if the title given above is shown on the main menu screen. Set
## this to False to hide the title.

define gui.show_name = True


## The version of the game.

define config.version = "1.3"


## Text that is placed on the game's about screen. Place the text between the
## triple-quotes, and leave a blank line between paragraphs.

define gui.about = _p("""
""")


## A short name for the game used for executables and directories in the built
## distribution. This must be ASCII-only, and must not contain spaces, colons,
## or semicolons.

define build.name = "VariopolisMap"


## Sounds and music ############################################################

## These three variables control, among other things, which mixers are shown
## to the player by default. Setting one of these to False will hide the
## appropriate mixer.

define config.has_sound = True
define config.has_music = True
define config.has_voice = True


## To allow the user to play a test sound on the sound or voice channel,
## uncomment a line below and use it to set a sample sound to play.

# define config.sample_sound = "sample-sound.ogg"
# define config.sample_voice = "sample-voice.ogg"


## Uncomment the following line to set an audio file that will be played while
## the player is at the main menu. This file will continue playing into the
## game, until it is stopped or another file is played.

# define config.main_menu_music = "main-menu-theme.ogg"


## Transitions #################################################################
##
## These variables set transitions that are used when certain events occur.
## Each variable should be set to a transition, or None to indicate that no
## transition should be used.

## Entering or exiting the game menu.

define config.enter_transition = dissolve
define config.exit_transition = dissolve


## Between screens of the game menu.

define config.intra_transition = dissolve


## A transition that is used after a game has been loaded.

define config.after_load_transition = None


## Used when entering the main menu after the game has ended.

define config.end_game_transition = None


## A variable to set the transition used when the game starts does not exist.
## Instead, use a with statement after showing the initial scene.


## Window management ###########################################################
##
## This controls when the dialogue window is displayed. If "show", it is always
## displayed. If "hide", it is only displayed when dialogue is present. If
## "auto", the window is hidden before scene statements and shown again once
## dialogue is displayed.
##
## After the game has started, this can be changed with the "window show",
## "window hide", and "window auto" statements.

define config.window = "auto"


## Transitions used to show and hide the dialogue window

define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)


## Preference defaults #########################################################

## Controls the default text speed. The default, 0, is infinite, while any other
## number is the number of characters per second to type out.

default preferences.text_cps = 0


## The default auto-forward delay. Larger numbers lead to longer waits, with 0
## to 30 being the valid range.

default preferences.afm_time = 15


## Save directory ##############################################################
##
## Controls the platform-specific place Ren'Py will place the save files for
## this game. The save files will be placed in:
##
## Windows: %APPDATA\RenPy\<config.save_directory>
##
## Macintosh: $HOME/Library/RenPy/<config.save_directory>
##
## Linux: $HOME/.renpy/<config.save_directory>
##
## This generally should not be changed, and if it is, should always be a
## literal string, not an expression.

define config.save_directory = "CITY_MAP-1679518401"


## Icon ########################################################################
##
## The icon displayed on the taskbar or dock.

define config.window_icon = "gui/window_icon.png"


## Build configuration #########################################################
##
## This section controls how Ren'Py turns your project into distribution files.

init python:

    ## The following functions take file patterns. File patterns are case-
    ## insensitive, and matched against the path relative to the base directory,
    ## with and without a leading /. If multiple patterns match, the first is
    ## used.
    ##
    ## In a pattern:
    ##
    ## / is the directory separator.
    ##
    ## * matches all characters, except the directory separator.
    ##
    ## ** matches all characters, including the directory separator.
    ##
    ## For example, "*.txt" matches txt files in the base directory, "game/
    ## **.ogg" matches ogg files in the game directory or any of its
    ## subdirectories, and "**.psd" matches psd files anywhere in the project.

    ## Classify files as None to exclude them from the built distributions.

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    ## To archive files, classify them as 'archive'.

    # build.classify('game/**.png', 'archive')
    # build.classify('game/**.jpg', 'archive')
    build.classify('game/descriptions/**', 'all')
    build.classify('game/images/logo_**', 'all')
    build.classify('game/**', 'archive')
    ## Files matching documentation patterns are duplicated in a mac app build,
    ## so they appear in both the app and the zip file.

    build.documentation('*.html')
    build.documentation('*.txt')


## A Google Play license key is required to perform in-app purchases. It can be
## found in the Google Play developer console, under "Monetize" > "Monetization
## Setup" > "Licensing".

# define build.google_play_key = "..."


## The username and project name associated with an itch.io project, separated
## by a slash.

# define build.itch_project = "renpytom/test-project"
define config.keymap = dict(

    # Bindings present almost everywhere, unless explicitly
    # disabled.
    rollback = [ ],
    screenshot = [ ],
    toggle_afm = [ ],
    toggle_fullscreen = [ 'alt_K_RETURN', 'alt_K_KP_ENTER', 'K_F11', 'noshift_K_f' ],
    game_menu = [ 'K_ESCAPE', 'K_MENU', 'K_PAUSE', 'mouseup_3' ],
    hide_windows = [ 'mouseup_2', 'noshift_K_h' ],
    launch_editor = [ ],
    dump_styles = [ ],
    reload_game = [ 'alt_K_r', 'shift_K_r' ],
    inspector = [ 'alt_K_i', 'shift_K_i' ],
    full_inspector = [ 'alt_shift_K_i' ],
    developer = [ 'alt_K_d', 'shift_K_d', ],
    quit = [ ],
    iconify = [ ],
    help = [ ],
    choose_renderer = [ ],
    progress_screen = [ ],
    accessibility = [ ],

    # Accessibility.
    self_voicing = [ ],
    clipboard_voicing = [ ],
    debug_voicing = [ ],

    # Say.
    rollforward = [ ],
    dismiss = [ 'K_RETURN', 'K_SPACE', 'K_KP_ENTER', 'K_SELECT', 'mouseup_1' ],
    dismiss_unfocused = [ ],

    # Pause.
    dismiss_hard_pause = [ ],

    # Focus.
    focus_left = [ 'any_K_LEFT', 'any_KP_LEFT' ],
    focus_right = [ 'any_K_RIGHT', 'any_KP_RIGHT' ],
    focus_up = [ 'any_K_UP', 'any_KP_UP' ],
    focus_down = [ 'any_K_DOWN', 'any_KP_DOWN' ],

    # Button.
    button_ignore = [ 'mousedown_1' ],
    button_select = [ 'K_RETURN', 'K_KP_ENTER', 'K_SELECT', 'mouseup_1',  ],
    button_alternate = [ 'mouseup_3' ],
    button_alternate_ignore = [ 'mousedown_3' ],

    # Input.
    input_backspace = [ 'any_K_BACKSPACE' ],
    input_enter = [ 'K_RETURN', 'K_KP_ENTER' ],
    input_next_line = [ 'shift_K_RETURN', 'shift_K_KP_ENTER' ],
    input_left = [ 'any_K_LEFT', 'any_KP_LEFT' ],
    input_right = [ 'any_K_RIGHT', 'any_KP_RIGHT' ],
    input_up = [ 'any_K_UP', 'any_KP_UP' ],
    input_down = [ 'any_K_DOWN', 'any_KP_DOWN' ],
    input_delete = [ 'any_K_DELETE', 'any_KP_DELETE' ],
    input_home = [ 'K_HOME', 'KP_HOME', 'meta_K_LEFT' ],
    input_end = [ 'K_END', 'KP_END', 'meta_K_RIGHT' ],
    input_copy = [ 'ctrl_noshift_K_INSERT', 'ctrl_noshift_K_c', 'meta_noshift_K_c' ],
    input_paste = [ 'shift_K_INSERT', 'ctrl_noshift_K_v', 'meta_noshift_K_v' ],
    input_jump_word_left = [ 'osctrl_K_LEFT', 'osctrl_KP_LEFT' ],
    input_jump_word_right = [ 'osctrl_K_RIGHT', 'osctrl_KP_RIGHT' ],
    input_delete_word = [ 'osctrl_K_BACKSPACE' ],
    input_delete_full = [ 'meta_K_BACKSPACE' ],

    # Viewport.
    viewport_leftarrow = [ 'any_K_LEFT', 'any_KP_LEFT' ],
    viewport_rightarrow = [ 'any_K_RIGHT', 'any_KP_RIGHT' ],
    viewport_uparrow = [ 'any_K_UP', 'any_KP_UP' ],
    viewport_downarrow = [ 'any_K_DOWN', 'any_KP_DOWN' ],
    viewport_wheelup = [ 'mousedown_4' ],
    viewport_wheeldown = [ 'mousedown_5' ],
    viewport_drag_start = [ 'mousedown_1' ],
    viewport_drag_end = [ 'mouseup_1' ],
    viewport_pageup = [ 'any_K_PAGEUP', 'any_KP_PAGEUP'],
    viewport_pagedown = [ 'any_K_PAGEDOWN', 'any_KP_PAGEDOWN' ],

    # These keys control skipping.
    skip = [ ],
    stop_skipping = [ ],
    toggle_skip = [ ],
    fast_skip = [ ],

    # Bar.
    bar_activate = [ 'mousedown_1', 'K_RETURN', 'K_KP_ENTER', 'K_SELECT' ],
    bar_deactivate = [ 'mouseup_1', 'K_RETURN', 'K_KP_ENTER', 'K_SELECT' ],
    bar_left = [ 'any_K_LEFT', 'any_KP_LEFT' ],
    bar_right = [ 'any_K_RIGHT', 'any_KP_RIGHT' ],
    bar_up = [ 'any_K_UP', 'any_KP_UP' ],
    bar_down = [ 'any_K_DOWN', 'any_KP_DOWN' ],

    # Delete a save.
    save_delete = [],

    # Draggable.
    drag_activate = [ 'mousedown_1' ],
    drag_deactivate = [ 'mouseup_1' ],

    # Debug console.
    console = [ 'shift_K_o', 'alt_shift_K_o' ],
    console_older = [ 'any_K_UP', 'any_KP_UP' ],
    console_newer = [ 'any_K_DOWN', 'any_KP_DOWN' ],

    # Director
    director = [ ],

    # Ignored (kept for backwards compatibility).
    toggle_music = [ ],
    viewport_up = [ ],
    viewport_down = [ ],

    # Profile commands.
    performance = [ ],
    image_load_log = [ ],
    profile_once = [ ],
    memory_profile = [ ],

)
