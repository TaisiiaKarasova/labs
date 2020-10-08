#refactoring - Taisiia Karasova

import pygame.draw as pgd
import pygame as pg
import math as m

pg.init()

def draw_trunk (screen, x, y, trunk_width, trunk_height, tree_color):
    ''' the center(x,y) of the tree is the point in the middle of its trunk '''
    
    bottom_trunk_y_lower_begin = y + trunk_height // 60
    bottom_trunk_y_lower_end = y + trunk_height // 4
    pgd.line(screen, tree_color,
             [x, bottom_trunk_y_lower_begin], 
             [x, bottom_trunk_y_lower_end], 
             trunk_width // 18)

    bottom_trunk_y_upper_begin = y + 17 * trunk_height // 60
    bottom_trunk_y_upper_end = y + trunk_height // 2
    pgd.line(screen, tree_color,
             [x, bottom_trunk_y_upper_begin], 
             [x, bottom_trunk_y_upper_end], 
             trunk_width // 18)

    top_trunk_coords_lower = [
                        [x, y],
                        [x - trunk_width // 22, y - trunk_height // 80],
                        [x, y - 35 * trunk_height // 232],
                        [x + trunk_width // 22, y - 16 * trunk_height // 116]
                        ]
    top_trunk_coords_upper = [
                        [x + trunk_width // 80, y - trunk_height // 6 + trunk_height // 200],
                        [x - trunk_width // 80, y - 17 * trunk_height // 96],
                        [x + trunk_width // 18, y - trunk_height // 2 + trunk_height // 100],
                        [x + 7 * trunk_width // 86, y - trunk_height // 2 + trunk_height // 200]
                        ]
    pgd.polygon(screen, tree_color,top_trunk_coords_lower)
    
    pgd.polygon(screen, tree_color, top_trunk_coords_upper)

    
def draw_branches (screen, x, y, trunk_width, trunk_height, tree_color):
    ''' the center(x,y) of the tree is the point in the middle of its trunk '''

    right_low_branch_x = x
    right_low_branch_y = y - 5 * trunk_height // 57
    right_low_branch_width = 14 * trunk_width // 35
    right_low_branch_height = trunk_height // 2 + 5 * trunk_height // 57
    right_low_branch_start_ang = 3 * m.pi // 7
    right_low_branch_arc_size = 13 * m.pi // 35
    pgd.arc(screen, tree_color,
            [[right_low_branch_x, right_low_branch_y], 
            [right_low_branch_width, right_low_branch_height]],
            right_low_branch_start_ang, right_low_branch_start_ang + right_low_branch_arc_size,
            4)

    right_top_branch_x = x + trunk_width // 16
    right_top_branch_y = y - trunk_height // 2
    right_top_branch_width = trunk_width - trunk_width // 8
    right_top_branch_height = 6 * trunk_height // 7
    right_top_branch_start_ang = m.pi/2
    right_top_branch_arc_size = 2 * m.pi // 5
    pgd.arc(screen, tree_color,
            [[right_top_branch_x, right_top_branch_y], 
            [right_top_branch_width, right_top_branch_height]],
            right_top_branch_start_ang, right_top_branch_start_ang + right_top_branch_arc_size,
            4)
    
    left_top_branch_x = x - trunk_width
    left_top_branch_y = y - trunk_height // 2
    left_top_branch_width = trunk_width
    left_top_branch_height = trunk_height
    left_top_branch_start_ang = m.pi/10
    left_top_branch_arc_size = 2 * m.pi // 5
    pgd.arc(screen, tree_color,
            [[left_top_branch_x, left_top_branch_y], 
            [left_top_branch_width, left_top_branch_height]],
            left_top_branch_start_ang, left_top_branch_start_ang + left_top_branch_arc_size,
            4)

    left_low_branch_x = x - 11 * trunk_width // 24
    left_low_branch_y = y
    left_low_branch_width = 11 * trunk_width // 24
    left_low_branch_height = trunk_height // 2
    left_low_branch_start_ang =  m.pi/6
    left_low_branch_arc_size = 11 * m.pi // 24
    pgd.arc(screen, tree_color,
            [[left_low_branch_x, left_low_branch_y], 
            [left_low_branch_width, left_low_branch_height]],
            left_low_branch_start_ang, left_low_branch_start_ang + left_low_branch_arc_size,
            4)


def draw_leaves (screen, x, y, trunk_width, trunk_height, tree_color):
    ''' the center(x,y) of the tree is the point in the middle of its trunk '''
    
    dist_from_trunk_to_leave = 5 * trunk_width // 37
    right_low_leaves_y = y - trunk_height // 14
    right_low_leaves_width = trunk_width // 40
    right_low_leaves_height = trunk_height // 7
    dist_between_leaves = trunk_width // 20
    for i in range (3):
        pgd.ellipse(screen, tree_color,
                    [[x + dist_from_trunk_to_leave, right_low_leaves_y], 
                    [trunk_width // 40, trunk_height // 7]])
        dist_from_trunk_to_leave += dist_between_leaves

    
    dist_from_trunk_to_leave = trunk_width // 3
    dist_from_ground_to_leave = 16 * trunk_height // 35
    dist_between_leaves_x = (3 * trunk_width) // 80
    dist_between_leaves_y = trunk_width // 70
    right_top_leaves_width = trunk_width // 40
    right_top_leaves_height = trunk_height // 7
    for i in range (5):
        pgd.ellipse(screen, tree_color,
                    [[x + dist_from_trunk_to_leave, y - dist_from_ground_to_leave], 
                    [right_top_leaves_width, right_top_leaves_height]])
        dist_from_trunk_to_leave += dist_between_leaves_x
        dist_from_ground_to_leave += dist_between_leaves_y

    dist_from_trunk_to_leave = 5 * trunk_width // 16
    dist_from_ground_to_leave = 7 * trunk_height // 16
    dist_between_leaves_x = 3 * trunk_width // 80
    dist_between_leaves_y = trunk_width // 70
    left_top_leaves_width = trunk_width // 40
    left_top_leaves_height = trunk_height // 7
    for i in range (5):
        pgd.ellipse(screen, tree_color,
                    [[x - dist_from_trunk_to_leave, y - dist_from_ground_to_leave], 
                    [left_top_leaves_width, left_top_leaves_height]])
        dist_from_trunk_to_leave += dist_between_leaves_x
        dist_from_ground_to_leave += dist_between_leaves_y

    dist_from_trunk_to_leave = trunk_width // 6
    dist_between_leaves = trunk_width // 20
    left_low_leaves_width = trunk_width // 40
    left_low_leaves_height = trunk_height // 7
    left_low_leaves_y = y
    for i in range (3):
        pgd.ellipse(screen, tree_color,
                    [[x - dist_from_trunk_to_leave, left_low_leaves_y], 
                    [left_low_leaves_width, left_low_leaves_height]])
        dist_from_trunk_to_leave += dist_between_leaves

        
def draw_tree (screen, x, y, trunk_width, trunk_height, tree_color):
    ''' the center(x,y) of the tree is the point in the middle of its trunk '''

    draw_trunk (screen, x, y, trunk_width, trunk_height, tree_color)
    draw_branches (screen, x, y, trunk_width, trunk_height, tree_color)
    draw_leaves (screen, x, y, trunk_width, trunk_height, tree_color)


def draw_paws (screen, x, y, torso_length, torso_height, paws_color, background_color):
    '''the center(x,y) of the panda is its nose'''

    front_left_paw_coords = [
                             [x + 28 * torso_length // 53, y - 23 * torso_height // 60],
                             [x + 28 * torso_length // 53, y + 4 * torso_height // 60],
                             [x + 23 * torso_length // 53, y + 20 * torso_height // 60],
                             [x + 18 * torso_length // 53, y + 27 * torso_height // 60],
                             [x + 4 * torso_length // 53, y + 20 * torso_height // 60],
                             [x + 13 * torso_length // 53, y + 12 * torso_height // 60]
                            ]
                             
    pgd.polygon(screen, paws_color, front_left_paw_coords)

    front_right_paw_coords = [
                              [x - 4 * torso_length // 53, y - 9 * torso_height // 60],
                              [x + 8 * torso_length // 53, y - 3 * torso_height // 60],
                              [x + 10 * torso_length // 53, y + 10 * torso_height // 60],
                              [x + 3 * torso_length // 53, y + 20 * torso_height // 60],
                              [x - 6 * torso_length // 53, y + 15 * torso_height // 60]
                             ]
                              
    pgd.polygon(screen, paws_color, front_right_paw_coords)

    back_paw_coords = [
                       [x + 40 * torso_length // 53, y - 10 * torso_height // 60],
                       [x + 40 * torso_length // 53, y + 8 * torso_height // 60],
                       [x + 30 * torso_length // 53, y + 21 * torso_height // 60],
                       [x + 20 * torso_length // 53, y + 15 * torso_height // 60]
                      ]
    pgd.polygon(screen, paws_color, back_paw_coords)


def draw_ears (screen, x, y, torso_length, torso_height, ears_color):
    '''the center(x,y) of the panda is its nose'''

    left_ear_coords = [x + 15 * torso_length // 53, y - 30 * torso_height // 60]
    left_ear_width = 12 * torso_length // 53
    left_ear_height = 20 * torso_height // 60
    pgd.ellipse(screen, ears_color,
                [left_ear_coords,
                [left_ear_width, left_ear_height]])

    right_ear_coords = [x - 6 * torso_length // 53, y - 32 * torso_height // 60]
    right_ear_width = 16 * torso_length // 53
    right_ear_height = 15 * torso_height // 60
    pgd.ellipse(screen, ears_color,
                [right_ear_coords,
                [right_ear_width, right_ear_height]])


def draw_nose (screen, x, y, torso_length, torso_height, nose_color):
    '''the center(x,y) of the panda is its nose'''

    nose_coors = [x - 3 * torso_length // 50, y - 3 * torso_height // 55]
    nose_width = 3 * torso_length // 25
    nose_height = 4 * torso_height // 55
    pgd.ellipse(screen, nose_color, [nose_coors, 
                [nose_width, nose_height]])


def draw_head (screen, x, y, torso_length, torso_height, head_color, background_color):
    '''the center(x,y) of the panda is its nose'''

    head_coords = [
                    [x, y],
                    [x + 25 * torso_length // 55, y - 7 * torso_height // 65],
                    [x + 25 * torso_length // 55, y - 25 * torso_height // 65],
                    [x + 25 * torso_length // 110, y - 35 * torso_height // 65],
                    [x, y - 30 * torso_height // 65],
                    [x - 5 * torso_length // 55, y - 30 * torso_height // 130]
                  ]
                  
    pgd.polygon(screen, head_color, head_coords)

    above_head_coords = [
                          [x + 25 * torso_length // 110, y - 35 * torso_height // 63],
                          [x + 9 * torso_length // 53, y - 31 * torso_height // 60],
                          [x + 15 * torso_length // 53, y - 30 * torso_height // 60]
                        ]
    pgd.polygon(screen, background_color, above_head_coords)


def draw_eyes (screen, x, y, torso_length, torso_height, eyes_color):
    '''the center(x,y) of the panda is its nose'''

    right_eye_coords = [x - 5 * torso_length // 53, y - 15 * torso_height // 60]
    right_eye_width = 6 * torso_length // 53
    right_eye_height = 7 * torso_height // 60
    pgd.ellipse(screen, eyes_color, [right_eye_coords,
                [right_eye_width, right_eye_height]])

    left_eye_coords = (x + 10 * torso_length // 53, y - 10 * torso_height // 60)
    left_eye_radius = 4 * torso_length // 53
    pgd.circle(screen, eyes_color, left_eye_coords, left_eye_radius)


def draw_torso (screen, x, y, torso_length, torso_height, torso_color):
    '''the center(x,y) of the panda is its nose'''

    torso_coords = [x - 5 * torso_length // 53, y - 25 * torso_height // 60]

    pgd.ellipse(screen, torso_color, [torso_coords,
                [47 * torso_length // 53, 27 * torso_height // 60]])


def draw_panda(screen, x, y,
               torso_length, torso_height,
               torso_color, paws_color, head_color,
               ears_color, eyes_color, nose_color,
               background_color):
    '''the center(x,y) of the panda is its nose'''
    
    draw_torso (screen, x, y, torso_length, torso_height, torso_color)
    draw_paws (screen, x, y, torso_length, torso_height, paws_color, background_color)
    draw_ears (screen, x, y, torso_length, torso_height, ears_color)
    draw_head (screen, x, y, torso_length, torso_height, head_color, background_color)
    draw_nose (screen, x, y, torso_length, torso_height, nose_color)
    draw_eyes (screen, x, y, torso_length, torso_height, eyes_color) 


FPS = 30
background_color = (255, 184, 135)
display_size = (1300, 700)
panda_color_black = (0, 0, 0)
panda_color_white = (255, 255, 255)
tree_color = (0, 80, 31)


screen = pg.display.set_mode(display_size)
screen.fill(background_color)

draw_tree(screen,
          11 * display_size[0] // 26, 9 * display_size[1] // 28,
          6 * display_size[0] // 13, 43 * display_size[1] // 70,
          tree_color)

draw_tree(screen,
          37 * display_size[0] // 130, 3 * display_size[1] // 7,
          23 * display_size[0] // 130, 13 * display_size[1] // 28,
          tree_color)

draw_tree(screen,
          8 * display_size[0] // 65, 31 * display_size[1] // 70,
          3 * display_size[0] // 13, 3 * display_size[1] // 7,
          tree_color)

draw_tree(screen,
          56 * display_size[0] // 65, 9 * display_size[1] // 28,
          27 * display_size[0] // 130, 41 * display_size[1] // 70,
          tree_color)

draw_panda(screen,
           6 * display_size[0] // 13, 4 * display_size[1] // 7,
           5 * display_size[0] // 26, 27 * display_size[1] // 70,
           panda_color_white, panda_color_black, panda_color_white,
           panda_color_black, panda_color_black, panda_color_black,
           background_color)

draw_panda(screen,
           24 * display_size[0] // 65, 5 * display_size[1] // 7,
           display_size[0] // 13, 11 * display_size[1] // 70,
           panda_color_white, panda_color_black, panda_color_white,
           panda_color_black, panda_color_black, panda_color_black,
           background_color)

pg.display.update()
clock = pg.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True

pg.quit()

