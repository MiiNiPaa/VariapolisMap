init -10 python:
    class POI:
        def __init__(self, x, y, icon, name, desc, show_map=True, show_desc=True):
            self.x = x
            self.y = y
            self.icon = icon
            self.name = name
            self.desc = desc
            self.show_map = show_map
            self.show_desc = show_desc

    class District:
        def __init__(self, name, x, y, image):
            self.name = name
            self.x = x
            self.y = y
            self.pos = (x, y)
            self.image = image

screen description(district, selection):
    $ name = getattr(store, district + "_name")
    $ description = getattr(store, district + "_desc")

    vbox:
        xfill True
        label name  style "description_label"
        if not selection:
            text description


style description_label is label:
    xalign 0.5

style description_label_text is label_text:
    font "fonts/blade2rus.ttf"
    size 96
    color "#EEE"
    outlines [(4, "#111", 1, 1)]

style map_text is text:
    justify True


screen poi_screen(district, selection):
    vbox:
        for poi in filter( lambda x: x.show_desc, getattr(store, "poi_list_" + district) ):
            hbox:
                add poi.icon yalign 0.5
                label poi.name yalign 0.5
            if selection:
                hbox:
                    null width 15
                    text poi.desc
            null height 15


screen notes_screen(district, selection):
    vbox:
        for i, note in enumerate(getattr(persistent, "notes_" + district)):
            hbox:
                imagebutton:
                    yalign 0.5
                    idle "mark_set.png"
                    hover "mark_delete.png"
                    if selection:
                        action Function(delete_note, district, i)
                label note[0] yalign 0.5
            if selection:
                hbox:
                    null width 15
                    text note[1]
            null height 15

transform dissolve_appear:
    on show:
        linear 0.2 alpha 1.0
    on hide:
        linear 0.2 alpha 0.0

transform slow_dis_a_pear:
    on idle:
        easeout_cubic 0.2 alpha 0.0
    on hover:
        alpha 1.0




transform empty_one:
    rotate 0

transform map_close_none:
    rotate_pad False
    linear 0.3 zoom 0.9 anchor (0.0 ,0.5) rotate 0

transform map_close_funland:
    linear 0.6 zoom 2.8 anchor (0.03 ,0.1) rotate 0

transform map_close_port:
    linear 0.6 zoom 3.0 anchor (0.03 ,0.26) rotate 0

transform map_close_brainwood:
    linear 0.6 zoom 2.5 anchor (0.15, 0.3) rotate 0

transform map_close_backhall:
    linear 0.6 zoom 2.8 anchor (0.6 ,0.36) rotate 50

transform map_unrotate_backhall:
    rotate -50

transform map_close_gold_hills:
    linear 0.6 zoom 2.5 anchor (0.0 ,0.45) rotate 0

transform map_close_graystone:
    linear 0.6 zoom 1.8 anchor (0.04 ,0.75) rotate 0

transform map_close_loadout:
    linear 0.6 zoom 1.7 anchor (0.35 ,0.62) rotate 60

transform map_unrotate_loadout:
    rotate -60

transform map_close_penolli:
    linear 0.6 zoom 1.9 anchor (0.47 ,0.58) rotate 60

transform map_unrotate_penolli:
    rotate -60

transform map_close_sprawl:
    linear 0.6 zoom 1.5 anchor (0.37 ,0.8) rotate 0

define transform_dict = {
    None: map_close_none,
    "funland": map_close_funland,
    "port": map_close_port,
    "brainwood": map_close_brainwood,
    "backhall": map_close_backhall,
    "gold_hills": map_close_gold_hills,
    "graystone": map_close_graystone,
    "loadout": map_close_loadout,
    "penolli": map_close_penolli,
    "sprawl": map_close_sprawl,
}

define unrotate = {
    None: empty_one,
    "funland": empty_one,
    "port": empty_one,
    "brainwood": empty_one,
    "backhall": map_unrotate_backhall,
    "gold_hills": empty_one,
    "graystone": empty_one,
    "loadout": map_unrotate_loadout,
    "penolli": map_unrotate_penolli,
    "sprawl": empty_one,
}


transform map_close(target):
    transform_dict[target]

style map_image_button is image_button:
    focus_mask True

define districts = [
    District( "funland",    30,  -2, "map_funland_%s.png"    ),
    District( "port",       30, 161, "map_port_%s.png"       ),
    District( "brainwood", 152, 260, "map_brainwood_%s.png"  ),
    District( "backhall",  266, 159, "map_backhall_%s.png"   ),
    District( "gold_hills", 30, 423, "map_gold_hills_%s.png" ),
    District( "graystone",  30, 754, "map_graystone_%s.png"  ),
    District( "loadout",   310, 564, "map_loadout_%s.png"    ),
    District( "penolli",   280, 369, "map_penolli_%s.png"    ),
    District( "sprawl",    338, 860, "map_sprawl_%s.png"     ),
]

screen map():
    style_prefix "map"
    default real_tooltip = 'none'
    default selection = None
    key 'game_menu' action SetScreenVariable('selection', None)
    $ tooltip = GetTooltip()
    if tooltip:
        $ real_tooltip = tooltip
    fixed:
        fit_first True
        align (0.0, 0.5)
        at map_close(selection)

        add "map_background.png"
        showif not (tooltip or selection):
            add "map_overlay" at dissolve_appear

        imagebutton:
            focus_mask None
            sensitive not selection
            pos 349, 73
            idle "map_name.png"
            tooltip "city"
            action NullAction()
            at slow_dis_a_pear

        for district in districts:
            imagebutton:
                sensitive not selection
                pos district.pos
                auto district.image
                tooltip district.name
                action SetScreenVariable('selection', district.name)
                at slow_dis_a_pear

        showif selection:
            for poi in filter( lambda x: x.show_map, getattr(store, "poi_list_" + (selection or real_tooltip)) ):
                add poi.icon anchor (0.5, 0.5) pos (poi.x, poi.y) zoom 0.5 at dissolve_appear, unrotate[selection]

    showif tooltip or selection:
            frame:
                at dissolve_appear
                xalign 1.0
                xsize 1100
                viewport:
                    mousewheel True
                    scrollbars "vertical"
                    vscrollbar_unscrollable "hide"
                    vbox:
                        use description(real_tooltip, selection)
                        null height 15
                        use poi_screen(real_tooltip, selection)
                        null height 15
                        use notes_screen(real_tooltip, selection)
                        null height 20
                if selection:
                    textbutton "Добавить заметку" align (0.97, 1.01) background "#000" action Show("add_note", district=selection)


screen add_note(district):
    modal True
    default NameText = "Заметка"
    default NameInput = ScreenVariableInputValue("NameText")
    default DescText = "Текст заметки"
    default DescInput = ScreenVariableInputValue("DescText")
    frame:
        align (0.5, 0.5)
        padding (50, 50, 50, 50)
        has vbox
        label "Название:"
        button:
            action NameInput.Toggle()
            input value NameInput copypaste True
        null height 10
        label "Текст заметки:"
        button:
            action DescInput.Toggle()
            input value DescInput copypaste True multiline True
        null height 33
        hbox:
            textbutton "Отмена" text_xalign 0.5 size_group "btns" action Hide()
            textbutton "Ок" text_xalign 0.5 size_group "btns" action Function(write_note, district, NameText, DescText), Hide()

init python:
    def write_note(district, name, desc):
        getattr(persistent, "notes_" + district).append( (name, desc) )

    def delete_note(district, pos):
        del getattr(persistent, "notes_" + district)[pos]

default persistent.notes_none = []
default persistent.notes_city = []
default persistent.notes_backhall = []
default persistent.notes_brainwood = []
default persistent.notes_funland = []
default persistent.notes_gold_hills = []
default persistent.notes_graystone = []
default persistent.notes_loadout = []
default persistent.notes_penolli = []
default persistent.notes_port = []
default persistent.notes_sprawl = []


label main_menu:
    return
label start:
    python:
        _game_menu_screen = None
        _confirm_quit = False
        _rollback = False
        quick_menu= False
    show screen map
    while True:
        $ ui.interact()
    return
