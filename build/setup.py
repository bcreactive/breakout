import sys
import cx_Freeze
from cx_Freeze import setup, Executable

# base = "Win32GUI" allows your application to open without a console window
executables = [cx_Freeze.Executable('breakout.py', base = "Win32GUI")]

cx_Freeze.setup(
    name = "breakout!",
    options = {"build_exe" : 
        {"packages" : ["pygame"], "include_files" : ["save_file.csv", "breakout.py",
                                                     "button.py", "block.py",
                                                     "ball.py", "pickup.py",
                                                     "scorelabel.py", "highscore.py",
                                                     "player.py", "settings.py",
                                                     "timer.py", 

                                                     "ball.png", "ball_lost.png", 
                                                     "dmg_up.png", "end_screen.png", 
                                                     "levelup.png", "life_up.png", 
                                                     "multiball.png", "title_screen.png",
                                                     "width_up.png", "win_screen.png",

                                                     "balllost.mp3", "blib.mp3", 
                                                     "blib2.mp3", "complete.mp3",
                                                     "fail.mp3", "highscore.mp3",
                                                     "intro.mp3", "level_a.mp3",
                                                     "level_b.mp3", "level_c.mp3", 
                                                     "level_d.mp3", "level_e.mp3",
                                                     "multiball.mp3", "pickupget.mp3",
                                                     "spawn.mp3", "win.mp3" ]}}, 
    executables = executables
)