import pyglet as pig
from pyglet.window import key
from player import *
from pyglet.sprite import Sprite
from random import randint
import time
 
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
        self.bullet = load_files('bullet.png')
        self.enemy = load_files('run.gif')
        self.player = object((self.height/2),(self.width/2),Sprite(self.move))
        self.player_x = self.player.x_position
        self.player_y = self.player.y_postion


        
        self.bullet_list = []
        self.map_List = []
        self.enemy_list = []      
        for i in range(4):
            self.map_List.append(object(0,i*960, Sprite(self.bg)))
        for tile in self.map_List:
            tile.acceration = -100
    
    def on_key_press(self,symbol, modifiers):

        if symbol == key.RIGHT:
            self.player.sideways_acceleration = 90
        if symbol == key.LEFT:
            self.player.sideways_acceleration = -90
        if symbol == key.UP:
            self.player.acceration = 100
        if symbol ==key.DOWN:
            self.player.acceration = -100
        if symbol == key.SPACE:
            self.player = object(self.player_x,self.player_y,Sprite(self.attack))
            self.bullet_list.append(object(self.player_x+32,self.player_y+32,Sprite(self.bullet)))
        if symbol == key.M:
            self.player = object(self.player_x,self.player_y,Sprite(self.melee))
    
    def on_key_release(self, symbol,modifiers):

        if symbol in(key.RIGHT,key.LEFT):
            self.player.sideways_acceleration  = 0
        if symbol in(key.UP,key.DOWN):
            self.player.acceration = 0
        if symbol in (key.SPACE,key.M):
            self.player = object(self.player_x,self.player_y,Sprite(self.move))
    

    def on_draw(self):
        self.clear()
          
        for tile in self.map_List:
            tile.draw()
        self.player.draw()
        for enemy in self.enemy_list:
            enemy.draw()
            self.y_pos = enemy.y_postion
            print(self.y_pos)
        for bullet in self.bullet_list:
            bullet.draw()
            self.y_pos = bullet.y_postion
            print(self.y_pos)

    def make_enemy(self):
        selector = randint(0,20)
        if selector == 1:
            self.enemy_list.append(object(randint(150,450),1000,Sprite(self.enemy)))      
       
    def bullet_update(self,dt):
        for bullet in self.bullet_list:
            bullet.update(dt)
            bullet.acceration = 300
            
            if bullet.y_postion > 1000:
                self.bullet_list.remove(bullet)
            
                
    def enemy_update(self,dt):
        for enemy in self.enemy_list:
            enemy.update(dt)
            enemy.acceration = -300
            if enemy.y_postion < -1000:
                self.enemy_list.remove(enemy)
        if(len(self.enemy_list)<10):
            self.make_enemy()                    
    def map_update(self,dt):
        for tile in self.map_List:
            tile.update(dt)
            if tile.y_postion <= -1000:
                self.map_List.remove(tile)
                self.map_List.append(object(0, 900, Sprite(self.bg)))
            tile.acceration = -200
    def update(self,dt):
        #print('X-position:',self.player.x_position,'Y-position',self.player.y_postion)
        print(self.enemy_list)
        self.player.update(dt)
        self.map_update(dt)
        self.enemy_update(dt)
        self.bullet_update(dt)


        
        

        self.player_x = self.player.x_position
        self.player_y = self.player.y_postion


if __name__ == "__main__":
    win = game(width =640, height =960 ,resizable=False)
    pig.clock.schedule_interval(win.update , win.frame_rate)
    pig.app.run()
        
