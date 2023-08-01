import pygame
import random
import math
pygame.init()

# class to store information about the setup of the visualizer
# creating a class here prevents the need to create unnecessary global 
# variables
class DrawInfo:
    BLACK = 0, 0, 0
    WHITE = 255, 255, 255
    GREEN = 0, 255, 0
    RED = 255, 0, 0
    BACKGROUND_COLOR = WHITE
    SIDE_PAD = 100
    TOP_PAD = 150

    FONT = pygame.font.SysFont('comicsans', 20)
    LARGE_FONT = pygame.font.SysFont('comicsans', 30)

    GRADIENTS = [
        (128, 128, 128), 
        (160, 160, 160),
        (192, 192, 192)
    ]

    def __init__(self, width, height, lst):
        self.width = width
        self.height = height
        
        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption('Sorting Visualizer')
        self.set_list(lst)
    
    def set_list(self, lst):
        self.lst = lst
        self.min_value = min(lst)
        self.max_value = max(lst)

        # calculating the width of the bars

        # this is the total area of each block
        # this calculation allows for the width of each block to dynamically
        # change based on the number of elements in lst
        self.block_width = round((self.width - self.SIDE_PAD) / len(lst))
        # the top pad will be the space needed to set up the navigation
        # bar and other essential material at the top of the screen
        # This gives us the height we have left on the screen, so we divide
        # by the number of values in our range in order to get the height
        # scalar that we want
        self.block_height = math.floor((self.height - self.TOP_PAD) / \
                                  (self.max_value - self.min_value))
        self.start_x = self.SIDE_PAD // 2


def draw(draw_info, algo_name, ascending):
    draw_info.window.fill(draw_info.BACKGROUND_COLOR)

    title = draw_info.LARGE_FONT.render(f'{algo_name}: {"Ascending" if ascending else "Descending"}', 1, (255, 171, 130))
    draw_info.window.blit(title, ( draw_info.width / 2 - \
                                     title.get_width() / 2, 5))

    controls = draw_info.FONT.render('R - Reset | Space - Start Sorting | A - Ascending | D - Descending', 1, draw_info.BLACK)
    draw_info.window.blit(controls, ( draw_info.width / 2 - \
                                     controls.get_width() / 2, 55))

    sorting = draw_info.FONT.render('I - Insertion | B - Bubble'\
                                    ' | S - Selection', 1, draw_info.BLACK)
    draw_info.window.blit(sorting, ( draw_info.width / 2 - \
                                     sorting.get_width() / 2, 85))

    draw_list(draw_info)
    pygame.display.update()

def draw_list(draw_info, color_positions = {}, clear_bg = False):
    lst = draw_info.lst

    if clear_bg:
        clear_rect = (draw_info.SIDE_PAD//2, draw_info.TOP_PAD, \
                        draw_info.width - draw_info.SIDE_PAD, \
                            draw_info.height - draw_info.TOP_PAD)
        pygame.draw.rect(draw_info.window, draw_info.BACKGROUND_COLOR, clear_rect)

    for i, val in enumerate(lst):
        # x coordinate for the current block
        x = draw_info.start_x + i * draw_info.block_width
        # y coordinate
        y = draw_info.height - (val - draw_info.min_value) * \
            draw_info.block_height
        color = draw_info.GRADIENTS[i % 3]

        if i in color_positions:
            color = color_positions[i]

        pygame.draw.rect(draw_info.window, color, (x, y, \
                                draw_info.block_width, draw_info.height))
        
    if clear_bg:
        pygame.display.update()
        

# function to generate the starting array
def generate_list(num_elements, min_val, max_val):
    lst = []

    for _ in range(num_elements):
        lst.append(random.randint(min_val, max_val))
    
    return lst

def bubble_sort(draw_info, ascending = True):
    lst = draw_info.lst
    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1 - i):
            if (lst[j] > lst[j + 1] and ascending) or \
                (lst[j] < lst[j + 1] and not ascending):
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                draw_list(draw_info, {j : draw_info.GREEN, j + 1 : draw_info.RED}, True)
                # yield is a generator that returns control to the calling
                # function. The function will resume after the yield statement
                # when it is called again
                # this allows us to still use our control buttons during the 
                # sorting algorithm
                yield True
    return lst

def insertion_sort(draw_info, ascending=True):
    lst = draw_info.lst

    for i in range(1, len(lst)):
        j = i
        while j > 0 and ((lst[j] < lst[j - 1] and ascending) or \
                         (lst[j] > lst[j - 1] and not ascending)):
            lst[j], lst[j - 1] = lst[j -1], lst[j]
            draw_list(draw_info, {j - 1 : draw_info.GREEN, j : draw_info.RED}, True)
            yield True
            j -= 1
    
    return lst

def selection_sort(draw_info, ascending=True):
    lst = draw_info.lst
    if ascending:
        for i in range(len(lst)):
            curr_min = lst[i]
            min_index = i
            for j in range(i + 1, len(lst)):
                if lst[j] < curr_min:
                    curr_min = lst[j]
                    min_index = j
            lst[i], lst[min_index] = lst[min_index], lst[i]
            draw_list(draw_info, {i : draw_info.GREEN, min_index : draw_info.RED}, True)
            yield True
    else:
        for i in range(len(lst)):
            curr_max = lst[i]
            max_index = i
            for j in range(i + 1, len(lst)):
                if lst[j] > curr_max:
                    curr_max = lst[j]
                    max_index = j
            lst[i], lst[max_index] = lst[max_index], lst[i]
            draw_list(draw_info, {i : draw_info.GREEN, max_index : draw_info.RED}, True)
            yield True
    return lst


def main():
    run = True
    clock = pygame.time.Clock()

    num_elements = 50
    min_val = 0
    max_val = 100

    lst = generate_list(num_elements, min_val, max_val)
    draw_info = DrawInfo(800, 600, lst)

    sorting = False
    ascending = True

    sorting_algo = bubble_sort
    sorting_algo_name = "Bubble Sort"
    sorting_algo_generator = None

    frame_rate = 60

    # pygame event loop
    while run:
        clock.tick(frame_rate)

        if sorting:
            try:
                next(sorting_algo_generator)
            except StopIteration:
                sorting = False
        else:
            draw(draw_info, sorting_algo_name, ascending)

        # rendering the display
        pygame.display.update()

        # handling events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type != pygame.KEYDOWN:
                continue
            if event.key == pygame.K_r:
                lst = generate_list(num_elements, min_val, max_val)
                draw_info.set_list(lst)
                sorting = False
            elif event.key == pygame.K_SPACE and not sorting:
                sorting = True
                sorting_algo_generator = sorting_algo(draw_info, ascending)
            elif event.key == pygame.K_a and not sorting:
                ascending = True
            elif event.key == pygame.K_d and not sorting:
                ascending = False
            elif event.key == pygame.K_i and not sorting:
                sorting_algo = insertion_sort
                sorting_algo_name = "Insertion Sort"
                frame_rate = 60
            elif event.key == pygame.K_b and not sorting:
                sorting_algo = bubble_sort
                sorting_algo_name = "Bubble Sort"
                frame_rate = 60
            elif event.key == pygame.K_s and not sorting:
                sorting_algo = selection_sort
                sorting_algo_name = "Selection Sort"
                # here I am slowing down the frame rate when selection
                # sort is run in order for better visualization
                frame_rate = 20
    
    pygame.quit()


if __name__ == '__main__':
    main()
