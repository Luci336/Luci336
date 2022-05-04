













define config.name = _("Scarlet Law")





define gui.show_name = False




define config.version = "0.2.9"





define gui.about = _p("""
""")






define build.name = "ScarletLaw"







define config.has_sound = True
define config.has_music = True
define config.has_voice = True














define config.main_menu_music = "audio/main.mp3"











define config.enter_transition = dissolve
define config.exit_transition = dissolve




define config.intra_transition = dissolve




define config.after_load_transition = None




define config.end_game_transition = None
















define config.window = "auto"
define config.windows_icon = "icon.ico"



define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)







default preferences.text_cps = 50





default preferences.afm_time = 15
















define config.save_directory = "ScarletLaw-1600436419"






define config.window_icon = "gui/window_icon.png"






init python:




















    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('game/images/**.webp', 'archive')
    build.classify('game/images/**.jpg', 'archive')
    build.classify('game/images/**.webp', 'archive')
    build.classify('game/**.rpy', 'archive')
    build.classify('game/**.rpyc', 'archive')
    build.classify('game/**.jpeg', 'archive')
    build.classify('game/**.mp3', 'archive')
    build.classify('game/**.ttf', 'archive')
    build.classify('game/**.txt', 'archive')
    build.classify('game/**.webm', 'archive')










    build.documentation('*.html')
    build.documentation('*.txt')
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
