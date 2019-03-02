import pyglet as pig
from pyglet.window import key
from player import *
from pyglet.sprite import Sprite
class game(pig.window.Window):
    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)# getting the constructor for the windows  
        self.height = 960
        self.width = 640
        self.frame_rate = 1/60.0
        self.move = load_files('move.gif')
        self.bg = load_files('bg.jpg')
        self.attack = load_files('attack.gif')
        self.melee = load_files('melee.gif')
        self.player = object((self.height/2),(self.width/2),Sprite(self.move))
        self.map_List = []
        self.enemy_list = []
        #for i in range():
            #self.enemy_list.append(0,)
        for i in range(4):
            self.map_List.append(object(0,i*960, Sprite(self.bg)))
        for tile in self.map_List:
            tile.acceration = -200
    def on_key_press(self,symbol, modifiers):
        player_x = self.player.x_position
        player_y = self.player.y_postion
        if symbol == key.RIGHT:
            self.player.sideways_acceleration = 90
        if symbol == key.LEFT:
            self.player.sideways_acceleration = -90
        if symbol == key.UP:
            self.player.acceration = 100
        if symbol ==key.DOWN:
            self.player.acceration = -100
        if symbol == key.SPACE:
            self.player = object(player_x,player_y,Sprite(self.attack))
        if symbol == key.M:
            self.player = object(player_x,player_y,Sprite(self.melee))
    
    def on_key_release(self, symbol,modifiers):
        player_x = self.player.x_position
        player_y = self.player.y_postion
        if symbol in(key.RIGHT,key.LEFT):
            self.player.sideways_acceleration  = 0
        if symbol in(key.UP,key.DOWN):
            self.player.acceration = 0
        if symbol in (key.SPACE,key.M):
            self.player = object(player_x,player_y,Sprite(self.move))
    #def get_bounds(self):

    def on_draw(self):
        self.clear()
        for tile in self.map_List:
            tile.draw()
        self.player.draw()
    def map_update(self,dt):
        for tile in self.map_List:
            tile.update(dt)
            if tile.y_postion <= -1000:
                self.map_List.remove(tile)
                self.map_List.append(object(0, 900, Sprite(self.bg)))
            tile.acceration = -200
    def update(self,dt):
        print('X-position:',self.player.x_position,'Y-position',self.player.y_postion)
        self.player.update(dt)
        self.map_update(dt)

if __name__ == "__main__":
    win = game(width =640, height =960 ,resizable=False)
    pig.clock.schedule_interval(win.update , win.frame_rate)
    pig.app.run()
        
