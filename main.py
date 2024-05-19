from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.animation import *
from PPlay.collision import *

janela = Window(1200,600)
janela.set_title("")
bola=Sprite("PongBall_1_50x50.png",1)
bola.x=janela.width/2-bola.width/2
bola.y=janela.height/2-bola.height/2
fundo=GameImage("fundo.jpg")
pad1=Sprite("pad1.jpg",1)
pad2=Sprite("pad2.jpg",1)
pad1.x=janela.width/12-pad1.width/2
pad1.y=janela.height/2-pad1.height/2
pad2.x=(janela.width-janela.width/12)-pad2.width/2
pad2.y=janela.height/2-pad2.height/2
velx=200
vely=200
vpad=300
teclado = Window.get_keyboard()
placar1=0
placar2=0

while True:
    if teclado.key_pressed("ESC"):
        break
    if teclado.key_pressed("P"):
        velx/=100000000
        vely/=100000000
    if teclado.key_pressed("R"):
        placar1=0
        placar2=0
        bola.x=janela.width/2-bola.width/2
        bola.y=janela.height/2-bola.height/2
        velx=0
        vely=0
        pad1.y = janela.height / 2 - pad1.height / 2
        pad2.y = janela.height / 2 - pad2.height / 2
    if teclado.key_pressed("W") and pad1.y>0:
        pad1.move_y(-vpad * janela.delta_time())
    if teclado.key_pressed("S") and pad1.y<(janela.height-pad1.height):
        pad1.move_y(vpad * janela.delta_time())
    if teclado.key_pressed("UP") and pad2.y>0:
        pad2.move_y(-vpad * janela.delta_time())
    if teclado.key_pressed("DOWN") and pad2.y<(janela.height-pad2.height):
        pad2.move_y(vpad * janela.delta_time())
    if teclado.key_pressed("SPACE") and vely>=0 and velx>=0:
        vely=100
        velx=100
    elif teclado.key_pressed("SPACE") and vely<0 and velx>0:
        vely=-100
        velx=100
    elif teclado.key_pressed("SPACE") and vely<0 and velx<0:
        vely=-100
        velx=-100
    elif teclado.key_pressed("SPACE") and vely>0 and velx<0:
        vely=100
        velx=-100
    if teclado.key_pressed("V") and vely>0 and velx>0:
        vely+=20
        velx+=20
    if teclado.key_pressed("V") and vely<0 and velx>0:
        vely-=20
        velx+=20
    if teclado.key_pressed("V") and vely<0 and velx<0:
        vely-=20
        velx-=20
    if teclado.key_pressed("V") and vely>0 and velx<0:
        vely+=20
        velx-=20

    if Collision.collided(bola,pad1):
        if velx<0:
            velx*=-1.1

    if Collision.collided(bola,pad2):
        if velx>0:
            velx*=-1.1

    if bola.y<0:
        vely*=-1
        bola.y=0
    if bola.y > janela.height - bola.height:
        vely*=-1
        bola.y= janela.height - bola.height
    if bola.x<=0:
        placar2+=1
        bola.x=janela.width/2-bola.width/2
        bola.y=janela.height/2-bola.height/2
        velx=0
        vely=0
    if bola.x>=(janela.width-bola.width):
        placar1+=1
        bola.x=janela.width/2-bola.width/2
        bola.y=janela.height/2-bola.height/2
        velx=0
        vely=0

    if (bola.y > janela.height/2 + pad2.height/2 or bola.y>pad2.y) and velx>0 and pad2.y<(janela.height-pad2.height):
        pad2.move_y(vpad*janela.delta_time())
    if (bola.y < janela.height/2 - pad2.height/2 or bola.y<pad2.y) and velx>0 and pad2.y>0:
        pad2.move_y(-vpad*janela.delta_time())

    bola.x= bola.x+ velx * janela.delta_time()
    bola.y= bola.y+ vely * janela.delta_time()
    fundo.draw()
    bola.draw()
    pad1.draw()
    pad2.draw()
    janela.draw_text(str(placar1), 10,4, 20,(255,255,255))
    janela.draw_text(str(placar2), janela.width-20,4 , 20, (255,255,255))
    janela.update()

