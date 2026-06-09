import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img_trans = pg.transform.flip(bg_img, True, False)
    img_3 = pg.image.load("fig/3.png")
    img_3_trans = pg.transform.flip(img_3, True, False)
    tmr = x = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        screen.blit(bg_img, [x, 0])
        x -= 1
        tmr += 1
        screen.blit(bg_img_trans, [x + 1600, 0])
        screen.blit(bg_img, [x + 3200, 0])
        if x <= -3199:
            x = 0
        screen.blit(img_3_trans, [300,200])
        pg.display.update()
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()