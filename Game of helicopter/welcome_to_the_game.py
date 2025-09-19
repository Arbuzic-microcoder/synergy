
from map import Map
import time
import os
from helicoptrer import Helicoter as Helico
from pynput import keyboard

TIME_TICKS = 0.1

TREE_UPDATE = 50
FIRE_UPDATE = 100
MAP_W, MAP_H = 20,10



field = Map(MAP_W, MAP_H)
field.genetate_forest(3, 10)
field.genetate_river(8)
field.genetate_uphraaid_shop()
field.genetate_mpp()



MOVES = {'w': (-1, 0), 'd':(0, 1), 's':(1, 0), 'a':(0, -1)}
def on_releas(key):
    global helico
    c = key.char
    if c in MOVES.keys():
        dx, dy = MOVES[c][0], MOVES[c][1]
        helico.move(dx, dy)



listener = keyboard.Listener(
    on_press=None,
    on_release=on_releas)
listener.start()


helico = Helico(MAP_W, MAP_H)

tick = 1
while True:
    os.system('cls')
    print('TICK', tick)
    helico.print_menu()
    field.print_map(helico)
    field.prosses_helico(helico)

    
    tick += 1
    
    time.sleep(TIME_TICKS)
    if (tick % TREE_UPDATE == 0):
        field.genetare_tree()
    if (tick % FIRE_UPDATE == 0):
        field.update_fire()