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
    img_3_trans_rct = img_3_trans.get_rect()
    img_3_trans_rct.center = 300, 200
    tmr = dx = dy = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        x = -(tmr % 3200)
        tmr += 1

        Key_lst = pg.key.get_pressed()
        if not any(Key_lst):
            img_3_trans_rct.move_ip((-1, 0))
        if Key_lst[pg.K_UP]:
            img_3_trans_rct.move_ip((0, -1))
        if Key_lst[pg.K_DOWN]:
            img_3_trans_rct.move_ip((0, 1))
        if Key_lst[pg.K_LEFT]:
            img_3_trans_rct.move_ip((-1, 0))
        if Key_lst[pg.K_RIGHT]:
            img_3_trans_rct.move_ip((2, 0))

        screen.blit(bg_img, [x, 0])
        screen.blit(bg_img_trans, [x + 1600, 0])
        screen.blit(bg_img, [x + 3200, 0])
        screen.blit(img_3_trans, img_3_trans_rct)
        pg.display.update()
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()