import pyglet
import random


window = pyglet.window.Window(width=800, height=200, caption='Binary Search Visualization')
batch = pyglet.graphics.Batch()


numbers = sorted(random.sample(range(1, 100), 19) + [46])


left, right = 0, len(numbers) - 1
mid = (left + right) // 2
found = False
search_complete = False

def binary_search():
    global left, right, mid, found, search_complete
    if left <= right and not found:
        mid = (left + right) // 2
        if numbers[mid] == 46:
            found = True
        elif numbers[mid] < 46:
            left = mid + 1
        else:
            right = mid - 1
    else:
        search_complete = True


pyglet.clock.schedule_interval(lambda dt: binary_search(), 1.0)

@window.event
def on_draw():
    window.clear()
    for i, number in enumerate(numbers):
        
        x = i * 40 + 10
        y = window.height // 2
        width = 30
        height = 30

        
        if left <= i <= right and not search_complete:
            color = (200, 100, 255)  # Blue for the current search interval
        elif i == mid and not search_complete:
            color = (255, 0, 0)  
        elif found and i == mid:
            color = (0, 255, 0)  
        else:
            color = (255,0, 255)  
        
        pyglet.shapes.Rectangle(x, y, width, height, color=color, batch=batch).draw()
        
        label = pyglet.text.Label(str(number), x=x+width//2, y=y+height//2, anchor_x='center', anchor_y='center', batch=batch)
        label.draw()

pyglet.app.run()
