import pygame as pg
from time import sleep
from const import *
from InputBox import InputBox
from Box import BOX
from Text import Text
# draw ruler
def drawvachthuoc(screen, h, x, y_min, y_max,rect4):
    # if h==0 then retunr 0
    if h <=  0:
        return 0
    else:
        mid = (y_max+y_min)/2
        drawline(screen, x, mid, x+h*INCREASE_H, mid)
        # display ruler on display
        pg.display.flip()
        sleep(0.25)
        # if have event click mouse on poision rect4
        for event in pg.event.get():
            if event.type ==pg.MOUSEBUTTONDOWN:
                #break draw
                if rect4.collidepoint(event.pos):
                    return 1
        # draw ruler from y min to mid
        check1=drawvachthuoc(screen, h-1, x, y_min, mid,rect4)
        if check1==1:
            return 1
        #draw ruler for mid to y max
        check2=drawvachthuoc(screen, h-1, x, mid, y_max,rect4)
        if check2==1:
            return 1
        return 0

# draw line
def drawline(screen, x, y, w, h):
    pg.draw.line(screen, COLOR_BLACK, (x, y), (w, h))

# draw box ruler
def drawthuoc(screen, x, y, w, h):
    rect = pg.Rect(x, y, w, h)
    pg.draw.rect(screen, COLOR_RED,rect)
def main():
    #khởi tạo các box input
    input_box1 = InputBox(BOX_INPUT_LEN['X'],BOX_INPUT_LEN['Y'],BOX_INPUT_LEN['W'],BOX_INPUT_LEN['H'])
    input_box2 = InputBox(BOX_INPUT_HEIGHT['X'],BOX_INPUT_HEIGHT['Y'],BOX_INPUT_HEIGHT['W'],BOX_INPUT_HEIGHT['H'])
    input_boxes = [input_box1, input_box2]
    # khỏi tạo các box điều khiển
    box_quit=BOX(COLOR_INACTIVE,RECT_QUIT)
    box_draw=BOX(COLOR_INACTIVE,RECT_DRAW)
    boxs=[box_quit, box_draw]
    #khỏi tạo các text
    text_len=Text(TEXT_LEN,FONT,COLOR_BLACK,POIN_TEXT_INPUT_LEN)
    text_height=Text(TEXT_HIGHT,FONT,COLOR_BLACK,POIN_TEXT_INPUT_HEIGHT)
    text_draw=Text(TEXT_DRAW,FONT,COLOR_BLACK,POIN_DRAW)
    text_stopdraw=Text(TEXT_STOPDRAW,FONT,COLOR_BLACK,POIN_DRAW)
    text_quit=Text(TEXT_QUIT,FONT,COLOR_BLACK,POIN_QUIT)
    texts=[text_len, text_height,text_quit]
    
    #các biến điều khiển
    h = ""
    l = ""
    x = 0
    y = 0
    flag=1
    done = False
    while not done:
        for event in pg.event.get():
            #nếu sự kiện bấm close
            if event.type == pg.QUIT:
                done = True
            for box in input_boxes:
                #xử lí các sự kiện input box
                box.handle_event(event)
            #lấy chiều cao vạch thước
            h = input_boxes[1].gettext()
            #lấy chiều dài thước
            l = input_boxes[0].gettext()
            #sự biện bấm chuột
            if event.type ==pg.MOUSEBUTTONDOWN:
                # if click Quit will quit game
                if RECT_QUIT.collidepoint(event.pos):
                    done=True
                # if click Draw will draw or stop draw
                if RECT_DRAW.collidepoint(event.pos):
                    if flag==0:
                        flag=1
                    else:
                        flag=0
        #fill color on sreen
        screen.fill(COLOR_ORANGE,POIN_ORANGE)
        screen.fill(COLOR_INACTIVE, POIN_INACTIVE)
        #update box input
        for box in input_boxes:
            box.update()
        if l != "":
            x = 150
            y = int(l)
            if y<=0:
                y=0
            l = ""
        #draw box input on screen
        for box in input_boxes:
            box.draw(screen)
        drawline(screen, 100, 5, 250, 5)
        drawthuoc(screen, 100, 6, x, y)
        #display box
        for box in boxs:
            box.draw(screen)
        # display tex
        for text in texts:
            text.draw(screen)
        # display draw or stop draw
        if flag==0:
            text_stopdraw.draw(screen)
        else:
            text_draw.draw(screen)
        # 
        screen.blit(image,POIN_IMAGE)
        if h != "" :
            if flag==0:
                # draw rulers
                flag=drawvachthuoc(screen, int(h), 100, 6, y+6,RECT_DRAW)
        pg.display.flip()
        # sleep(0.5)
        screen.fill(COLOR_INACTIVE, POIN_INACTIVE)


if __name__ == '__main__':

    pg.init()
    screen = pg.display.set_mode([WIDTH_SCREEN, HEIGHT_SCREEN])
    image=pg.transform.scale(IMAGE,SIZE_IMAGE)
    main()
    pg.quit()
