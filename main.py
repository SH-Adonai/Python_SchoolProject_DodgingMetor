import pygame
from player import Player
import random as rnd
from bullet import Bullet
from lifeblock import Lifeblock
import time

def collision(obj1, obj2):
    dist = ((obj1.pos[0] - obj2.pos[0])**2 + (obj1.pos[1] - obj2.pos[1])**2)**0.5
    return dist < 15

def draw_text(txt, size, pos, color):
    font = pygame.font.Font('freesansbold.ttf', size)
    r = font.render(txt, True, color)
    screen.blit(r, pos)

pygame.init()
width, height = 1000,600 

#음악넣기
pygame.mixer.music.load('C:\이선휘\Programming\Python\GuaSoSa\PYGAME\\bgm.wav')
pygame.mixer.music.play(-1)

# 폭팔사진
explode = pygame.image.load('C:\이선휘\Programming\Python\GuaSoSa\PYGAME\\explode.jpg')
explode = pygame.transform.scale(explode, (150,150))

# 배경 우주사진
bg = pygame.image.load('C:\이선휘\Programming\Python\GuaSoSa\PYGAME\\bg.jpg')
bg = pygame.transform.scale(bg, (2000,1200))

# 위너
winner = []

#시간 관련
ptime = 0
playtime = 0

# 화면, 플레이어 생성
pygame.display.set_caption("총알피하기")
screen = pygame.display.set_mode((width, height))
p1 = Player(width/2, height/2)

#총알 만들기
bullets = []
for _ in range(10):
    bullets.append(Bullet(0,rnd.random(), rnd .random()-0.5,rnd.random()-0.5 , rnd.randint(0,3)))

#배경 설정
bg_pos = [-400,-400]
bgx, bgy = 0,0

#생명력 및 무적 설정
life = 5
neverdie = False
ndt = 0
lbx = 870
lifeblocks = []
for _ in range(5):
    lifeblocks.append(Lifeblock((lbx,50,15,15),0))
    lbx += 25


clock = pygame.time.Clock()
FPS = 60

running = True
gameover = False



time.sleep(1)

while running:
    #fps가 변화해도 속도가 바뀌지 않기 위해서 dt값 저장하여 사용
    dt = clock.tick(60)
    
    #총알개수 추가
    if gameover ==False:
        ptime += dt
    if ptime >= 1000:
        bullets.append(Bullet(0, rnd.random(), rnd .random()-0.5, rnd.random()-0.5, rnd.randint(0,3) ))
        ptime -= 1000

    if gameover == False:
        playtime += dt

    #검은 배경
    screen.fill((0,0,0))

    # 배경우주사진
    screen.blit(bg, (bg_pos))
    bg_pos[0] += bgx*dt*0.05
    bg_pos[1] += bgy*dt*0.05
    
    #스크린에 총알그리기
    for b in bullets:
        b.update_and_drawb(dt, screen)




    
    #키보드 입력
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
            break
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                p1.goto(-1,0)
                bgx += 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                p1.goto(1,0)
                bgx += -1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                p1.goto(1,0)
                bgx += -1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                p1.goto(-1,0)
                bgx += 1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                p1.goto(0,1)
                bgy += -1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                p1.goto(0,-1)
                bgy += 1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                p1.goto(0,-1)
                bgy += 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                p1.goto(0,1 ) 
                bgy += -1
                

    # p1움직임 업데이트
    p1.update(dt,screen)


    # 그리기
    if neverdie:
        if (ndt - playtime)//200 in (1,4,7,10,13):
            p1.indraw(screen)
        else:
            p1.draw(screen)
    else:
        p1.draw(screen)
    

    # 무적 취소
    if gameover == False:    
        if playtime > ndt:
            neverdie = False

    #총맞았을 때
    for b in bullets:
        if collision(p1, b):
            if neverdie == False:
                # 폭팔음, 폭팔사운드
                nlife = life - (b.type + 1)
                neverdie = True
                bombsound = pygame.mixer.Sound('C:\이선휘\Programming\Python\GuaSoSa\PYGAME\\bomb.mp3')
                pygame.mixer.Sound.play(bombsound)
                screen.blit(explode, (p1.pos[0]- explode.get_width()/2, p1.pos[1] - explode.get_height()/2))
                # 라이프가 0일때
                if nlife <= 0 :
                    life = 0
                    gameover = True
                    f = open('C:\이선휘\Programming\Python\GuaSoSa\PYGAME\\winner_winner_chicken_dinner.txt','r')
                    winner = f.readlines()
                    f.close()
                    winner = list(map(int, winner))
                    winner.append(playtime)
                    winner.sort(reverse = True)
                    winner = winner[0:min(10, len(winner))]
                    f = open('winner_winner_chicken_dinner.txt','w')
                    for i in range(len(winner)):
                        w = str(winner[i]) + '\n'
                        f.write(w)
                    f.close()
                    
                else :
                    life = nlife
                    ndt = playtime + 3000   
    # 게임오버 문구
    if gameover:
        over = f"Game Over"
        score = f"You scored {playtime}"
        draw_text(over,60,(width/2 -180,height/2-80), (225,225,225))
        draw_text(score,60,(width/2 -250,height/2 -20), (225,225,225))
        
        #순위 보여주기
        for i in range(len(winner)):
            if playtime == winner[i]:
                draw_text(str(winner[i]), 20, (800,100+30*i), (225,30,200))   
            else:
                draw_text(str(winner[i]), 20, (800,100+30*i), (225,225,225))

    
    #시간 및 총알 수 정보 출력
    txt = f"Time: {playtime/1000:.1f}, Bullets: {len(bullets)}"
    draw_text(txt,32,(10,10), (255,255,255))

    # 생명력 정보 출력
    ltxt = f"life: {life}"
    draw_text(ltxt,32,(900,10), (255,255,255))    
    
    #생명력 블록

    for i in range(life):
        lifeblocks[i].update_and_drawl(screen)

    pygame.display.update()
