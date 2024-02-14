import pyglet
import random

window = pyglet.window.Window(width=800, height=200, caption='Linear Search Visualization')
batch = pyglet.graphics.Batch()

numbers = random.sample(range(1, 100), 19) + [46]
shuffled_numbers = numbers.copy()
random.shuffle(shuffled_numbers)

current_index = 0
found_index = -1
search_complete = False

def linear_search():
    global current_index, found_index, search_complete
    if current_index < len(shuffled_numbers):
        if shuffled_numbers[current_index] == 46:
            found_index = current_index
            search_complete = True
        current_index += 1
    else:
        search_complete = True

pyglet.clock.schedule_interval(lambda dt: linear_search(), 1.0)

@window.event
def on_draw():
    window.clear()
    for i, number in enumerate(shuffled_numbers):
    
        x = i * 40 + 10
        y = window.height // 2
        width = 30
        height = 30

        # Draw the box
        if i == current_index and not search_complete:
            color = (200, 100, 255) 
        elif i == found_index:
            color = (0, 255, 0)  
        else:
            color = (255, 0, 255)  
        
        pyglet.shapes.Rectangle(x, y, width, height, color=color, batch=batch).draw()
      
        label = pyglet.text.Label(str(number), x=x+width//2, y=y+height//2, anchor_x='center', anchor_y='center', batch=batch)
        label.draw()

pyglet.app.run()
