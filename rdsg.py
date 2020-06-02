#!/usr/bin/python3
from pygame.locals import * # pygameイベント処理のため
import pygame               # pygame
import time                 # sleepのため
import random               # シャッフルのため

pygame.init()                #pygameを使う際には必ず最初にinit()を呼びます

filename = 'stereogram.jpg'  #画像のファイルネーム

dummyscreen=pygame.display.set_mode((1,1),0,32) #image.load().convertを先に呼ぶとエラーが出るので、ダミーの呼び出しをします。

img=pygame.image.load(filename).convert() #ファイルの読み込み

xsize = img.get_width() # 画像の幅の取得
ysize = img.get_height() # 画像の高さの取得 

screen=pygame.display.set_mode((xsize,ysize),0,32) # ディスプレイをするスクリーンを、画像の幅、高さで再設定

surface=pygame.Surface((xsize,ysize)) # 元画像を描くサーフェスを設定
surface.blit(img,(0,0)) # 元画像を描く

# 元画像のサーフェスと、ディスプレイするスクリーンのサイズは一致していて、
# それぞれ全ての点が1対1対応します

ns = [i for i in range(xsize*ysize)] # 画面上の全ての点に順番を付けます
random.shuffle(ns) # 点の順番をシャッフルします これで、重複しない乱数列が出来ます

for cnt in range(xsize*ysize): # 画面の点の個数ループ。全部点を打ったら抜けます

    for event in pygame.event.get(): # pygame QUITイベントが出たら、終了
        if event.type == QUIT:
            exit()

    pos=divmod(ns.pop(0),ysize) # 打つ点の座標を、乱数から求めます
    # 幅掛ける高さなので、高さで割り、商と余りをそれぞれ、x,y座標とします

    col=surface.get_at(pos) # 元画像のサーフェスから、(x,y)における色を取得します。ピクセルの色の取得は、surface.get_at()でやります。
    screen.set_at(pos,col) # スクリーンに、位置pos、色colで点を打ちます

    pygame.display.update() # スクリーンをアップデートします

time.sleep( 20 ) # ループを抜けたら、20秒間ウエイトをします

# 終わり
