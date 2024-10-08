import pygame
import sys
import random
import time
import math

# Inizializza pygame
pygame.init()

running = True
game = True
global diff

#Costanti
WIDTH = 1000
HEIGHT = int(WIDTH*(0.75))

font_style = pygame.font.SysFont("Pixel Army", int(WIDTH/40))
font_style2 = pygame.font.SysFont("Pixel Army", int(WIDTH/20))
font_style3 = pygame.font.SysFont("Pixel Army", int(WIDTH/52))
font_style4 = pygame.font.SysFont("Pixel Army", int(WIDTH/14))
font_style6 = pygame.font.SysFont("Retromoticons", int(WIDTH/40))

# Colori
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
global oscuramento
oscuramento=0
green = (0, 255, 0)
RED =(255, 0, 0)
RED_TRANSP=(255,0,0,128)
RED_darker = (210,0,0)
RED_darker_darker = (180 ,0,0)
blue = (50, 153, 213)
orange = (236, 88, 0)
yellow=(255,211,67)
gray=(152,147,139)
gray_darker=(130, 125, 117)
fucsia=(255,0,255)


# Imposta la finestra
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("In The Space")

GameMenu_active=1

def GameMenu():
    def messagemenu1(msg, color):  # Titolo
        mesg = font_style4.render(msg, True, color)
        text_rect = mesg.get_rect(center=(WIDTH/2, HEIGHT/2-WIDTH/10))
        
        screen.blit(mesg, text_rect)
        
    def messagemenu2(msg, color):  # Inizia o esce
        mesg = font_style.render(msg, True, color)
        text_rect = mesg.get_rect(center=(WIDTH/2, HEIGHT/2))
        
        screen.blit(mesg, text_rect)
    
    def messagemenu3(msg, color):  # Titolo
        mesg = font_style.render(msg, True, color)
        text_rect = mesg.get_rect(center=(WIDTH/2, HEIGHT/2+WIDTH/10))
        
        screen.blit(mesg, text_rect)
    
    while GameMenu_active==1:
        
        screen.fill(BLACK)
        
        messmenu1=str("In The Space") 
        messagemenu1(messmenu1, blue)
        
        messmenu2=str("C   Inizia        Q   Esci") 
        messagemenu2(messmenu2, blue)
        
        messmenu3=str("M   Menu tasti") 
        messagemenu3(messmenu3, blue)
        
        pygame.display.flip()
        pygame.time.delay(20)
        #pygame.display.update()
        
        for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            pygame.quit()
                            sys.exit()
                        if event.key == pygame.K_c:
                            GameMenu_active==0
                            GameSetting()
                        if event.key == pygame.K_m:
                            GameMenu_active==0
                            BindingMenu()

def GameSetting():
    GameSetting_active=1
    global diff
    diff=1
    def settmess1(msg, color):  # Titolo
        mesg = font_style2.render(msg, True, color)
        text_rect = mesg.get_rect(center=(WIDTH/2, HEIGHT/2-WIDTH/10))
        
        screen.blit(mesg, text_rect)
        
    def settmess2(msg, color):  # Inizia o esce
        mesg = font_style.render(msg, True, color)
        text_rect = mesg.get_rect(center=(WIDTH/2, HEIGHT/2))
        
        screen.blit(mesg, text_rect)
    
    def settmess3(msg, color):  # Titolo
        mesg = font_style.render(msg, True, color)
        text_rect = mesg.get_rect(center=(WIDTH/2, HEIGHT/2+WIDTH/10))
        
        screen.blit(mesg, text_rect)
    
    while GameSetting_active==1:
        
        screen.fill(BLACK)
        
        messmenu1=str("Scegli la difficolta'") 
        settmess1(messmenu1, blue)
        
        messmenu2=str("Numero Vite: < "+str(diff)+" >") 
        settmess2(messmenu2, fucsia)
        
        messmenu3=str("C   Inizia     Q   Indietro") 
        settmess3(messmenu3, blue)
        
        for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            GameSetting_active=0
                            GameMenu()
                        if event.key == pygame.K_c:
                            GameSetting_active==0
                            gameloop()
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_d and diff==1:
                            diff=2
                        elif event.key == pygame.K_d and diff==2:
                            diff=3
                        elif event.key == pygame.K_d and diff==3:
                            diff=1
                        elif event.key == pygame.K_a and diff==3:
                            diff=2
                        elif event.key == pygame.K_a and diff==2:
                            diff=1
                        elif event.key == pygame.K_a and diff==1:
                            diff=3
        pygame.display.flip()
        pygame.time.delay(20)
        #pygame.display.update()

def BindingMenu():
    bind_menu=1
    def bindingmessage1(msg, color):  # Titolo
        mesg = font_style2.render(msg, True, color)
        text_rect = mesg.get_rect(center=(WIDTH/2, HEIGHT/2-WIDTH/5))
        
        screen.blit(mesg, text_rect)
        
    def bindingmessage2(msg, color):  # Inizia o esce
        mesg = font_style.render(msg, True, color)
        text_rect = mesg.get_rect(center=(WIDTH/2, HEIGHT/2-WIDTH/10))
    
        screen.blit(mesg, text_rect)
    
    def bindingmessage3(msg, color):  # Inizia o esce
        mesg = font_style.render(msg, True, color)
        text_rect = mesg.get_rect(center=(WIDTH/2, HEIGHT/2))
        
        screen.blit(mesg, text_rect)
        
    def bindingmessage4(msg, color):  # Inizia o esce
        mesg = font_style.render(msg, True, color)
        text_rect = mesg.get_rect(center=(WIDTH/2, HEIGHT/2+WIDTH/10))
        
        screen.blit(mesg, text_rect)
        
    def bindingmessage5(msg, color):  # Inizia o esce
        mesg = font_style3.render(msg, True, color)
        text_rect = mesg.get_rect(center=(WIDTH/2, HEIGHT/2+WIDTH/5))
        
        screen.blit(mesg, text_rect)
    
    while bind_menu==1:
        
        screen.fill(BLACK)
        
        bindmess1=str("Menu tasti") 
        bindingmessage1(bindmess1, blue)
        
        bindmess2=str("Usa WASD per muoverti") 
        bindingmessage2(bindmess2, fucsia)
        
        bindmess3=str("L   Potenziamento alla velocita'") 
        bindingmessage3(bindmess3, fucsia)
        
        bindmess4=str("Istruzioni su punti e scudo") 
        bindingmessage4(bindmess4, fucsia)
        
        bindmess5=str("Q   Torna al menu") 
        bindingmessage5(bindmess5, blue)
        
        pygame.display.flip()
        pygame.time.delay(20)
        #pygame.display.update()
        
        for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            GameMenu_active==1
                            GameMenu()

def gameloop():
    # Ripristino valori
    PUNTI = 0
    
    # Variabili della palla
    x, y = WIDTH // 2, HEIGHT // 2
    firex, firey = x, y
    speed_o = 0
    speed_v = 0
    global diff
    Vite=diff
    Last_Vite=diff
    BALL_RADIUS = int(WIDTH/71)
    COLL_RADIUS = int(WIDTH/135)
    SHIELD_RADIUS = int(WIDTH/91)
    MAX_SPEED = int(WIDTH/111.11)
    ACCELERATION = (WIDTH/2000)
    DECELERATION = (WIDTH/3333.33)
    
    flash = 0
    activable_flash = True
    start_flash = False
    flash_time = 0.25
    tot_flashtime = 1.5
    super_o = 0
    super_v = 0

    power=1
    barra_potere=1500
    clock = pygame.time.Clock()
    dt = clock.tick(60)
    
    shield=1
    active_shield=2000
    cooldown_shield =5000
    inv=0
    raccoglibile=1

    bomb_raccoglibile = False
    bomb_coll_radius = int(WIDTH/91)
    bomb_activable = False
    boom_radius=WIDTH/10
    boom=False
    boom_tot_time=0.6
    boom_start=time.time()
    darkening = 100

    # Coordinate per i punti
    foodx = int(random.randrange(0, WIDTH - BALL_RADIUS))
    foody = int(random.randrange(0, HEIGHT - BALL_RADIUS))
    R_change = 0
    G_change = 255
    B_change = 0
    
    R_change_dir=1
    G_change_dir=(-1)
    B_change_dir=1
    
    
    # Dati temporali per le sfere
    last_generation_time = time.time()
    cluster_time=10000
    spheres = []
    
    # Loop principale
    running = True
    game= True
    game_over = False
    game_start=time.time()
    
    # Messaggi
    def message(msg, color):  # Punteggio
        mesg = font_style.render(msg, True, color)
        screen.blit(mesg, [WIDTH / 10, HEIGHT / 10])
    
    def message2(msg, color):  # Game over
        mesg = font_style2.render(msg, True, color)
        text_rect = mesg.get_rect(center=(WIDTH/2, HEIGHT/2-WIDTH/10))
        
        screen.blit(mesg, text_rect)
        
    def message3(msg, color):  # Show punteggio
        mesg = font_style.render(msg, True, color)
        text_rect = mesg.get_rect(center=(WIDTH/2, HEIGHT/2))
        
        screen.blit(mesg, text_rect)
        
    def message4(msg, color):  # C o Q
        mesg = font_style.render(msg, True, color)
        text_rect = mesg.get_rect(center=(WIDTH/2, HEIGHT/2+WIDTH/10))
        
        screen.blit(mesg, text_rect)
        
    def message5(msg, color):
        mesg = font_style6.render(msg, True, color)
        screen.blit(mesg, [WIDTH / 7, HEIGHT / 10.15])
        
    def message6(msg, color):
        mesg = font_style.render(msg, True, color)
        text_rect = mesg.get_rect(center=(WIDTH/2, HEIGHT/11-WIDTH/25))
        screen.blit(mesg, text_rect)

    

    # Modulo generazione sfere casuali
    class Sphere:
        def __init__(self):
            self.SPHERE_RADIUS = random.randint(int(WIDTH/80), int((WIDTH/80)*3))  # Raggio casuale tra 10 e 30
            self.randchoicesphere=random.choice([1,2,3,4])
            if self.randchoicesphere==1:
                self.x = -2*self.SPHERE_RADIUS #Start destra
                self.y = random.randint(0, HEIGHT)
                self.speedx = random.randint(2, 4)
                self.speedy = random.randint(-2, 2)
            elif self.randchoicesphere==2:
                self.x = WIDTH+2*self.SPHERE_RADIUS  # Start sinistra
                self.y = random.randint(0, HEIGHT)
                self.speedx = random.randint(-4, -2)
                self.speedy = random.randint(-2, 2)
                
            elif self.randchoicesphere==3:
                self.x = random.randint(0,WIDTH) # Start in alto
                self.y = -2*self.SPHERE_RADIUS
                self.speedx = random.randint(-2, 2)
                self.speedy = random.randint(2, 4)
            else:
                self.x = random.randint(0, WIDTH)  # Start in basso
                self.y = HEIGHT+2*self.SPHERE_RADIUS
                self.speedx = random.randint(-2, +2)
                self.speedy = random.randint(-4, -2)

        def move(self):
            self.x += self.speedx
            self.y += self.speedy

        def draw(self):
            pygame.draw.circle(screen, gray, (self.x, self.y), self.SPHERE_RADIUS)
    
    def rettangolo_danno():
        rect_width, rect_height = WIDTH, HEIGHT
        rect_surface = pygame.Surface((rect_width, rect_height), pygame.SRCALPHA)
        rect_surface.fill(RED_TRANSP)
        screen.blit(rect_surface, (0, 0))
        pygame.display.flip()
        pygame.time.delay(20)  
        
    # Gioco partito
    while game:
        while running:
            keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
            # Riempie lo schermo di bianco
            screen.fill(BLACK)


            # limito velocità diagonale
            if (keys[pygame.K_d] and keys[pygame.K_w]) or (keys[pygame.K_d] and keys[pygame.K_s]) or (keys[pygame.K_a] and keys[pygame.K_w]) or (keys[pygame.K_a] and keys[pygame.K_s]):
                if MAX_SPEED == int(WIDTH/111.11):
                    MAX_SPEED=MAX_SPEED/(2**(1/2))
            else:
                MAX_SPEED=int(WIDTH/111.11)
            
            # velocità orizzontale
            
            if keys[pygame.K_d]:
                speed_o += ACCELERATION
                if speed_o >= MAX_SPEED:
                    speed_o = MAX_SPEED
            
            elif keys[pygame.K_a]:
                speed_o -= ACCELERATION
                if speed_o <= (-MAX_SPEED):
                    speed_o = (-MAX_SPEED)
                    
            
            if abs(speed_o)>DECELERATION:
                if speed_o >0 and (not(keys[pygame.K_d])):
                    speed_o -= DECELERATION
                elif speed_o <0 and (not(keys[pygame.K_a])):
                    speed_o += DECELERATION
            else:
                speed_o =0
            
            x += speed_o
                
            # velocità verticale
            
            if keys[pygame.K_s]:
                speed_v += ACCELERATION
                if speed_v >= MAX_SPEED:
                    speed_v = MAX_SPEED
            
            elif keys[pygame.K_w]:
                speed_v -= ACCELERATION
                if speed_v <= (-MAX_SPEED):
                    speed_v = (-MAX_SPEED)
            
            if abs(speed_v)>DECELERATION:
                if speed_v >0 and (not(keys[pygame.K_s])):
                    speed_v -= DECELERATION
                elif speed_v <0 and (not(keys[pygame.K_w])):
                    speed_v += DECELERATION
            else: 
                speed_v=0
            
            y += speed_v
            
            # Coordinate fuoco
            firex = x-2*speed_o
            firey = y-2*speed_v
            
            # Potere: bomba
            if bomb_raccoglibile==True:
                pygame.draw.circle(screen, RED, (bomb_coll_x+5*math.sin(time.time()*8), bomb_coll_y+5*math.cos(time.time()*8)), bomb_coll_radius)
                pygame.draw.circle(screen, RED_darker_darker, (bomb_coll_x+5*math.sin(time.time()*8), bomb_coll_y+5*math.cos(time.time()*8)), bomb_coll_radius, 5)
                if ((x-bomb_coll_x+5*math.sin(time.time()*8))**2+(y-bomb_coll_y+5*math.cos(time.time()*8))**2)**(1/2)<=(BALL_RADIUS+bomb_coll_radius+1) and activable_flash==True and raccoglibile ==1:
                    bomb_raccoglibile=False
                    bomb_activable=True
            elif bomb_activable==True:
                pygame.draw.polygon(screen, blue, [(x,y-25),(x+6,y-6),(x+25,y),(x+6,y+6),(x,y+25),(x-6,y+6),(x-25,y),(x-6,y-6)])
                if keys[pygame.K_k]:
                    boom=True
                    bomb_activable=False
                    boom_x=x
                    boom_y=y
                    darkening = 0
                    boom_radii=5
                    boom_start=time.time()
            
            if darkening <0.99:
                boom_radii +=(1/((time.time()-boom_start)+0.01))*0.5
                if boom_radii>110:
                    darkening+=0.02
                pygame.draw.circle(screen, (25-25*darkening, 76-76*darkening, 106-106*darkening), (boom_x, boom_y), boom_radii)
                pygame.draw.circle(screen, (50-50*darkening, 153-153*darkening, 213-213*darkening), (boom_x, boom_y), boom_radii, 10)

            if time.time()-boom_start>boom_tot_time:
                boom=False
                
            if boom==False and bomb_raccoglibile==False and bomb_activable==False and time.time()-boom_start>boom_tot_time+3:
                bomb_coll_x = int(random.randint(int(WIDTH/10), int(WIDTH*9/10)))
                bomb_coll_y = int(random.randint(int(HEIGHT/10), int(HEIGHT*9/10)))
                bomb_raccoglibile=True



            # Aggiornamento asteroidi per aumento difficoltà:
            gentime=2/((PUNTI//5)+1)
            
            #Generazione cluster di asteroidi e nuovo cooldown:
            if cluster_time>0:
                cluster_time -=dt
            else:
                for num in range(1, 10):
                    spheres.append(Sphere())
                    cluster_time=random.randint(7000,12000)
            
            #ASTEROIDI
            if time.time() - last_generation_time > gentime:
                spheres.append(Sphere())
                last_generation_time = time.time()
            
            for sphere in spheres[:]:  # Loop through a copy of the list
                sphere.move()
                sphere.draw()
                if sphere.randchoicesphere==1:
                    if sphere.x > WIDTH+sphere.SPHERE_RADIUS or sphere.y > HEIGHT+sphere.SPHERE_RADIUS or sphere.y < -sphere.SPHERE_RADIUS:
                        spheres.remove(sphere)
                elif sphere.randchoicesphere== 2:
                    if sphere.x < -sphere.SPHERE_RADIUS or sphere.y > HEIGHT+sphere.SPHERE_RADIUS or sphere.y < -sphere.SPHERE_RADIUS:
                        spheres.remove(sphere)
                elif sphere.randchoicesphere== 3:
                    if sphere.x > WIDTH+sphere.SPHERE_RADIUS or sphere.y > HEIGHT+sphere.SPHERE_RADIUS or sphere.x < -sphere.SPHERE_RADIUS:  # Check if the sphere is out of sight
                        spheres.remove(sphere)  # Completely delete the sphere
                else:
                    if sphere.x < -sphere.SPHERE_RADIUS or sphere.y < -sphere.SPHERE_RADIUS or sphere.x > WIDTH+sphere.SPHERE_RADIUS:
                        spheres.remove(sphere)
                
                if boom==True:
                    if ((boom_x-sphere.x)**2+(boom_y-sphere.y)**2)**(1/2)<=(boom_radii+sphere.SPHERE_RADIUS+1):
                        spheres.remove(sphere)
                
                if ((x-sphere.x)**2+(y-sphere.y)**2)**(1/2)<=(BALL_RADIUS+sphere.SPHERE_RADIUS+1):
                    if inv==0 and Vite==Last_Vite:
                        Vite-=1
                        if Vite!=0:
                            rettangolo_danno()
                            time.sleep(0.25)

            
            
            
            # Lista poteri

            # Potere del game_dev
            if keys[pygame.K_p]:
                PUNTI=PUNTI+10
                
            
                
                
            #   Supervelocità
                
            # Dati relativi alla carica del potere
            
            if not(keys[pygame.K_l]):
                barra_potere += dt
            if barra_potere >=1500:
                barra_potere=1500
                if power==0:
                    power=1
                
            if keys[pygame.K_l] and power==1:
                barra_potere -= 4.5*dt
                if shield!=0:
                    raccoglibile=0
                inv=1
                ship_color=blue
                super_o=3*speed_o
                super_v=3*speed_v                
                ACCELERATION=MAX_SPEED
                #DECELERATION=9
            else:
                if shield!=0:
                    inv=0
                if flash==0:
                    raccoglibile=1
                super_o=0
                super_v=0
                ACCELERATION = (WIDTH/2000)
                # DECELERATION = (WIDTH/3333.33)
            
            if barra_potere <=0:
                power=0
                ship_color=WHITE
            else:
                if not keys[pygame.K_l]:
                    ship_color=yellow
                
                                
            x += super_o
            y += super_v

            # Limita il movimento ai bordi della finestra
            if x - BALL_RADIUS < 0:
                x = BALL_RADIUS
            if x + BALL_RADIUS > WIDTH:
                x = WIDTH - BALL_RADIUS
                
            if y - BALL_RADIUS < 0:
                y = BALL_RADIUS
            if y + BALL_RADIUS > HEIGHT:
                y = HEIGHT - BALL_RADIUS
                
            # Dati relativi allo scudo
            
            #Scudo attivo/inattivazione
            if shield==0:
                active_shield -= dt
                pygame.draw.circle(screen, fucsia, (int(x),int(y)), BALL_RADIUS+int(WIDTH/200),int((WIDTH/1000)*3))
                
                center_rectx, center_recty = WIDTH // 2, HEIGHT // 10
                top_left_x = center_rectx - ((active_shield/10) // 2)
                top_left_y = center_recty - (5)
                pygame.draw.rect(screen,fucsia, pygame.Rect(top_left_x, top_left_y, active_shield/10, int(WIDTH/100)))
                
                if active_shield<=0:
                    inv=0
                    shield=1
                    active_shield=2000
            
            #cooldown ricompars scudo
            elif shield==1:
                cooldown_shield -=dt
                if cooldown_shield<=0:
                    shield=2
                    cooldown_shield =random.randint(2500, 7500)
            
            # scelta posizione scudo:
            elif shield==2:
                scudx = random.randint(int(WIDTH/10) , int(WIDTH*9/10))
                scudy = random.randint(int(HEIGHT/10), int(HEIGHT*9/10))
                shield = 3
            
            
            #scudo da raccogliere/raccolto
            else:
                pygame.draw.circle(screen, fucsia, (int(scudx), int(scudy)), SHIELD_RADIUS+(math.sin(3*time.time()))*4, int((WIDTH/1000)*3))
                if ((x-scudx)**2+(y-scudy)**2)**(1/2)<=(BALL_RADIUS+SHIELD_RADIUS+1) and raccoglibile==1 and activable_flash==True:
                    inv=1
                    shield=0
                    
                    
                    
            R_change += R_change_dir*dt/2
            G_change += G_change_dir*dt/2
            B_change += B_change_dir*dt/3
            if R_change>=255 and R_change_dir==1:
                R_change=255
                R_change_dir=(-1)
            elif R_change<=0 and R_change_dir==(-1):
                R_change=0
                R_change_dir=1
            
            if G_change>=255 and G_change_dir==1:
                G_change=255
                G_change_dir=(-1)
            elif G_change<=0 and G_change_dir==(-1):
                G_change=0
                G_change_dir=1
                
            if B_change>=255 and B_change_dir==1:
                B_change=255
                B_change_dir=(-1)
            elif B_change<=0 and B_change_dir==(-1):
                B_change=0
                B_change_dir=1
            
            palline=(R_change, G_change, B_change)
            
            # disegna i punti
            pygame.draw.circle(screen, palline, (foodx, foody), COLL_RADIUS)
            
            # Raccolta del punteggio
            if ((x-foodx)**2+(y-foody)**2)**(1/2)<=(BALL_RADIUS+COLL_RADIUS+1) and raccoglibile==1 and activable_flash==True:
                foodx = int(random.randint(int(WIDTH/10), int(WIDTH*9/10)))
                foody = int(random.randint(int(HEIGHT/10), int(HEIGHT*9/10)))
                PUNTI = PUNTI+1


            # Flash effect per il danno
            if activable_flash==True:
                start_flashtime=time.time()
            
            if  Vite<Last_Vite and activable_flash==True:
                last_flash_time = time.time()
                start_flashtime = time.time()
                start_flash=True
                activable_flash=False
                raccoglibile=0
            
            if start_flash==True:
                if time.time() - last_flash_time > flash_time:
                    if flash==1:
                        flash=0
                    else:
                        flash=1
                        
            if time.time() - start_flashtime > tot_flashtime:
                start_flash=False
                activable_flash=True
                flash=0
                Last_Vite=Vite
                raccoglibile=1
            
            # Disegna la palla
            if flash==0:
                pygame.draw.circle(screen, orange, (int(firex), int(firey)), (BALL_RADIUS/2))
                pygame.draw.circle(screen, ship_color, (int(x), int(y)), BALL_RADIUS)
                
                
            # Punteggio aggiornato a schermo
            PUNTIstr=str(PUNTI)
            message(PUNTIstr, blue)
            
            if diff!=1:
                if Vite==3:
                    str_vite=str("$ $ $")
                elif Vite==2:
                    str_vite=str("$ $")
                elif Vite==1:
                    str_vite=str("$")
            else:
                str_vite=str(" ")
            message5(str_vite, RED)
            
            mins=str(int((time.time()-game_start)//60))
            secs=str(int(time.time()-game_start-60*int(mins)))
            str_tempo=str(mins + " : " + secs)
            message6(str_tempo, blue)
            
            pygame.draw.rect(screen,blue, pygame.Rect(WIDTH/10, HEIGHT/6.5, barra_potere/10, int(WIDTH/100)))
            if power==1:
                if shield==0:
                    contorno_potere=fucsia
                else:
                    contorno_potere=blue
                pygame.draw.rect(screen,contorno_potere, pygame.Rect(int(WIDTH/10-WIDTH/200), int(HEIGHT/6.5-WIDTH/200), int(barra_potere/10+WIDTH/100), int(WIDTH/100+WIDTH/100)), int(WIDTH/500))

                
            if Vite ==0:
                rettangolo_danno()
                time.sleep(0.25)
                running=False
            
            # Aggiorna lo schermo
            pygame.display.flip()
            pygame.time.delay(20)
        
        pygame.display.flip()
        pygame.time.delay(20)
        
        global oscuramento    
        while oscuramento<100 and game_over==False:
            oscuramento += 0.1*dt
            if oscuramento >= 255:
                oscuramento=255
            rect_width2, rect_height2 = WIDTH, HEIGHT
            rect_surface2 = pygame.Surface((rect_width2, rect_height2), pygame.SRCALPHA)
            rect_surface2.fill((0,0,0,oscuramento))
            screen.blit(rect_surface2, (0, 0))
            pygame.display.flip()
            pygame.time.delay(20)
        if oscuramento >=100:
            game_over=True
        
        if game_over==True:
            while running == False and game_over==1:
                screen.fill(BLACK)
                mess2=str("GAME OVER!!!") 
                message2(mess2, RED)
                
                mess3=str("Il tuo punteggio e': "+ PUNTIstr)
                message3(mess3, fucsia)
                
                mess4=("Premi C per riprovare o Q per uscire")
                message4(mess4, blue)
                
                # pygame.display.update()
                pygame.display.flip()
                pygame.time.delay(20)   

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            pygame.quit()
                            sys.exit()
                        if event.key == pygame.K_c:
                            game_over=False
                            oscuramento=0
                            GameMenu()

        
        
        # Termina pygame
        pygame.quit()
        sys.exit()
        
GameMenu()
