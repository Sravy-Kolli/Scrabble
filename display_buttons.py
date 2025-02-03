import turtle
import time
import pygame
from pygame.locals import *

pygame.init()


screen_width = 600
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Scrabble')

font = pygame.font.SysFont('Constantia', 30)

#define colours
bg = (204, 102, 0)
red = (255, 0, 0)
black = (0, 0, 0)
white = (255, 255, 255)
#define global variable
clicked = False
counter = 0

class button():

        #colours for button and text
        button_col = (255, 0, 0)
        hover_col = (75, 225, 255)
        click_col = (50, 150, 255)
        text_col = black
        width = 180
        height = 70

        def __init__(self, x, y, text):
                self.x = x
                self.y = y
                self.text = text
        def draw_button(self):

                global clicked
                action = False

                #get mouse position
                pos = pygame.mouse.get_pos()

                #create pygame Rect object for the button
                button_rect = Rect(self.x, self.y, self.width, self.height)

                #check mouseover and clicked conditions
                if button_rect.collidepoint(pos):
                        if pygame.mouse.get_pressed()[0] == 1:
                                clicked = True
                                pygame.draw.rect(screen, self.click_col, button_rect)
                        elif pygame.mouse.get_pressed()[0] == 0 and clicked == True:
                                clicked = False
                                action = True
                        else:
                                pygame.draw.rect(screen, self.hover_col, button_rect)
                else:
                        pygame.draw.rect(screen, self.button_col, button_rect)

                 #add shading to button
                pygame.draw.line(screen, white, (self.x, self.y), (self.x + self.width, self.y), 2)
                pygame.draw.line(screen, white, (self.x, self.y), (self.x, self.y + self.height), 2)
                pygame.draw.line(screen, black, (self.x + self.width, self.y), (self.x + self.width, self.y + self.height), 2)

                #add text to button
                text_img = font.render(self.text, True, self.text_col)
                text_len = text_img.get_width()
                screen.blit(text_img, (self.x + int(self.width / 2) - int(text_len / 2), self.y + 25))
                return action



play = button(75, 200, 'Play Now :)')
quit = button(325, 200, 'Quit?')
Help = button(75, 350, 'Help')



run = True
while run:

        #screen.fill(bg)
        
        if play.draw_button():
            import turtle
            import time
            turtle.screensize(canvwidth=4000, canvheight=4000,
                    bg="brown")
            turtle.title("Scrabble")
            t = turtle.Turtle()
            def box(ln):
                for i in range(4):
                    t.forward(ln)
                    t.rt(90)
            t.speed(0)
            x = 0
            y = 0
            while True:
                t.goto(x,y)
                t.pendown()
                x += 50
                box(50)
                if x >= 50*15:
                    x = 0
                    y += 50
                    t.penup()
                if y>= 50 * 15:
                    break
            turtle.done()
        if quit.draw_button():
            run = False

        if Help.draw_button():
            from PIL import Image

            image = Image.open('/home/chandana/Downloads/HelpScrabble.png')
            image.show()


        counter_img = font.render(str(counter), True, red)
        screen.blit(counter_img, (280, 450))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()

pygame.quit()

