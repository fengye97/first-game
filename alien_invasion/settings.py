class Settings():  #创建一个存储alien_invasion所有设置的类
    def __init__(self):
        self.screen_width=800
        self.screen_height=600
        self.bg_color=(230,230,230)
        
        self.ship_speed_factor=1.5  #飞船速度的设置
        self.ship_limit=3

        self.alien_speed_factor=1

        self.bullet_speed_factor=1
        self.bullet_width=3
        self.bullet_height=15
        self.bullet_color=0,250,0

        self.speedup_scale=1.1
        self.score_scale=1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):  #重置速度设置
        self.ship_speed_factor=1.5
        self.bullet_speed_factor=1
        self.alien_speed_factor=1

        self.alien_points=50


    def increase_speed(self):
        self.ship_speed_factor*=self.speedup_scale
        self.bullet_speed_factor*=self.speedup_scale
        self.alien_speed_factor*=self.speedup_scale
        self.alien_points=int(self.alien_points*self.score_scale)
        
