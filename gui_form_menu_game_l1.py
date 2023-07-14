import pygame
from pygame.locals import *
from constantes import *
from gui_form import Form
from gui_button import Button
from gui_textbox import TextBox
from gui_progressbar import ProgressBar
from player import Player
from enemigo import Enemy
from plataforma import Plataform
from background import Background
from bullet import Bullet
from botin import Botin

class FormGameLevel1(Form):
    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,active):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,active)

        self.game_paused = False
        self.game_over = False
        self.win = False

        # --- GUI WIDGET --- 
        self.boton1 = Button(master=self,x=0,y=0,w=120,h=40,color_background=None,color_border=None,image_background="images/gui/set_gui_01/Comic_Border/Buttons/Button_M_02.png",on_click=self.on_click_boton1,on_click_param="form_menu_B",text="BACK",font="Verdana",font_size=22,font_color=C_WHITE)
        self.boton2 = Button(master=self,x=200,y=0,w=120,h=40,color_background=None,color_border=None,image_background="images/gui/set_gui_01/Comic_Border/Buttons/Button_M_02.png",on_click=self.on_click_boton1,on_click_param="form_menu_B",text="PAUSE",font="Verdana",font_size=22,font_color=C_WHITE)
        #self.boton_shoot = Button(master=self,x=400,y=0,w=140,h=40,color_background=None,color_border=None,image_background="images/gui/set_gui_01/Comic_Border/Buttons/Button_M_02.png",on_click=self.on_click_shoot,on_click_param="form_menu_B",text="SHOOT",font="Verdana",font_size=22,font_color=C_WHITE)
        
       
        self.pb_lives = ProgressBar(master=self,x=500,y=50,w=200,h=50,color_background=None,color_border=None,image_background="images/gui/set_gui_01/Comic_Border/Bars/Bar_Background01.png",image_progress="images/gui/set_gui_01/Comic_Border/Bars/Bar_Segment05.png",value = 5, value_max=5)
        self.widget_list = [self.boton1,self.boton2,self.pb_lives]

        # --- GAME ELEMNTS --- 
        self.static_background = Background(x=0,y=0,width=w,height=h,path="images/locations/set_bg_01/forest/all.png")
        
        self.player_1 = Player(x=0,y=575,speed_walk=35,speed_run=50,gravity=25,jump_power=30,frame_rate_ms=100,move_rate_ms=100,jump_height=140,p_scale=0.2,interval_time_jump=300)

        #objetos
        self.key = Botin(x=700, y=700, image_path=r"C:\\Users\\blair\\Desktop\\juego\\images\\tileset\\forest\\Objects\\mios\\17.png", scale=1)
        self.extra_life = Botin(x=750, y=750, image_path=r"C:\\Users\\blair\\Desktop\\juego\\images\\tileset\\forest\\Objects\\0.png", scale=1)
        self.coin = Botin(x=85, y=125, image_path=r"C:\\Users\\blair\\Desktop\\juego\\images\\tileset\\forest\\Objects\\mios\\0.png", scale=1.5)
        
        self.objetos_list = []
        self.objetos_list.append(self.key)
        self.objetos_list.append(self.extra_life)
        self.objetos_list.append(self.coin)

        self.enemy_list = []
        self.enemy_list.append (Enemy(x=450,y=575,speed_walk=2,speed_run=5,gravity=14,jump_power=30,frame_rate_ms=150,move_rate_ms=50,jump_height=140,p_scale=0.1,interval_time_jump=300))
        self.enemy_list.append (Enemy(x=900,y=400,speed_walk=2,speed_run=5,gravity=14,jump_power=30,frame_rate_ms=150,move_rate_ms=50,jump_height=140,p_scale=0.1,interval_time_jump=300))
        
        
        
        self.plataform_list = []
        self.plataform_list.append(Plataform(x=50, y=180, width=50, height=40, type=12))
        self.plataform_list.append(Plataform(x=100, y=180, width=50, height=40, type=14))
        

        self.plataform_list.append(Plataform(x=120,y=270,width=50,height=40,type=12))
        self.plataform_list.append(Plataform(x=170,y=270,width=50,height=40,type=13))
        self.plataform_list.append(Plataform(x=220, y=270, width=50, height=40, type=14))

        self.plataform_list.append(Plataform(x=280,y=350,width=50,height=40,type=12))
        self.plataform_list.append(Plataform(x=330,y=350,width=50,height=40,type=14))

        self.plataform_list.append(Plataform(x=200,y=580,width=50,height=40,type=12))
        self.plataform_list.append(Plataform(x=250,y=580,width=50,height=40,type=13))
        self.plataform_list.append(Plataform(x=300,y=580,width=50,height=40,type=14))

        self.plataform_list.append(Plataform(x=450,y=500,width=50,height=40,type=12))
        self.plataform_list.append(Plataform(x=500,y=500,width=50,height=40,type=14))

        self.plataform_list.append(Plataform(x=600,y=500,width=50,height=40,type=12))
        self.plataform_list.append(Plataform(x=650,y=500,width=50,height=40,type=14))

        self.plataform_list.append(Plataform(x=950,y=460,width=50,height=40,type=12))
        self.plataform_list.append(Plataform(x=1000,y=460,width=50,height=40,type=13))
        self.plataform_list.append(Plataform(x=1050,y=460,width=50,height=40,type=13))
        self.plataform_list.append(Plataform(x=1100,y=460,width=50,height=40,type=14))

        self.enemy_bullet_list = []
        self.player_bullet_list = []
            
        
    def colision_player(self, enemy):
        if self.player_1.rect.colliderect(enemy):
            current_time = pygame.time.get_ticks()
            if not enemy.collision_cooldown or current_time >= enemy.collision_cooldown_end_time:
                if self.player_1.lives > 0:
                    self.player_1.lives -= 1
                    enemy.collision_counter += 1
                    enemy.collision_cooldown = True
                    enemy.collision_cooldown_end_time = current_time + enemy.collision_cooldown_time
                    if enemy.collision_counter >= 2:
                        enemy.collision_counter = 0

                    
    def on_click_boton1(self, parametro):
        self.set_active(parametro)

    def update(self, lista_eventos,keys,delta_ms):
        for aux_widget in self.widget_list:
            aux_widget.update(lista_eventos)

        for bullet_element in self.enemy_bullet_list:
            bullet_element.update(delta_ms,self.plataform_list,self.enemy_list,self.player_1)

        for enemy_element in self.enemy_list:
            self.enemy_bullet_list.append(Bullet(enemy_element,enemy_element.rect.centerx,enemy_element.rect.centery,self.player_1.rect.centerx,self.player_1.rect.centery,20,path="images/gui/set_gui_01/Comic_Border/Bars/Bar_Segment05.png",frame_rate_ms=100,move_rate_ms=20,width=10,height=10))
            enemy_element.update(delta_ms,self.plataform_list)
            self.colision_player(enemy_element)  # le pasamos los enemigos de la lista al metodo

        
        self.player_1.events(delta_ms,keys)
        self.player_1.update(delta_ms,self.plataform_list)

        self.pb_lives.value = self.player_1.lives
        
        current_time = pygame.time.get_ticks()
        for enemy_element in self.enemy_list:
            enemy_element.update(delta_ms, self.plataform_list)
            self.colision_player(enemy_element)  # le pasamos los enemigos de la lista al método
        
         
        
    def draw(self): 
        super().draw()
        self.static_background.draw(self.surface)

        for aux_widget in self.widget_list:    
            aux_widget.draw()

        for plataforma in self.plataform_list:
            plataforma.draw(self.surface)

        for enemy_element in self.enemy_list:
            enemy_element.draw(self.surface)
        
        self.player_1.draw(self.surface)

        for objetos in self.objetos_list:
            objetos.draw(self.surface)
        
        for bullet_element in self.enemy_bullet_list:
            bullet_element.draw(self.surface)

        for bullet in self.player_bullet_list:
            bullet.update(self, self.plataform_list,self.enemy_list,self.player_1)
            bullet.draw(self.surface)   
           