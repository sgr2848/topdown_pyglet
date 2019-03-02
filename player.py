import pyglet as pig

from random import randint
def load_files(sprite_img):
    if (sprite_img[-3:]=='gif'):
       return pig.image.load_animation('media/'+sprite_img)
    else:
        return pig.image.load('media/'+sprite_img)
class object():
    def __init__(self, x_position, y_position,sprite= None):
        self.x_position = x_position
        self.y_postion = y_position 
        self.speed = 0.0
        self.max_speed = 10.0
        self.min_speed = 2.0
        self.acceration = 0.0
        self.sideways_acceleration = 0.0
        if sprite is not None:
            self.sprite = sprite
            self.sprite.x = x_position
            self.sprite.y = y_position 
           
    def draw(self):
        self.sprite.draw()
    def update(self,dt):
        self.y_postion += dt * self.acceration
        self.x_position += dt * self.sideways_acceleration
        self.sprite.x = self.x_position 
        self.sprite.y = self.y_postion
                               
    
        
        

        


        
    
    
