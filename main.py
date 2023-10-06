import pygame
from sys import exit
pygame.init()

screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Mashapa John The Ripper Development")
clock = pygame.time.Clock()
test_surface = pygame.image.load('Sky.png').convert()
test_surface1 = pygame.image.load('ground.png').convert()
test_font = pygame.font.Font(None , 50)
text_surface = test_font.render('To My Mom Grace , Thank you for everything ', False,'green')

snail_surface = pygame.image.load('snail1.png').convert_alpha()
snail_surface2 = pygame.image.load('snail2.png').convert_alpha()
snail_x_pos = 500
snail_y_pos = 270
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(test_surface,(0,0))
    screen.blit(test_surface1,(0,300))
    screen.blit(text_surface,(50,50))
    screen.blit(snail_surface2,(50,270))
    snail_x_pos -= 1
    if snail_x_pos < -100 : snail_x_pos = 800
    screen.blit(snail_surface,(snail_x_pos,snail_y_pos))


    pygame.display.update()
    clock.tick(80)
