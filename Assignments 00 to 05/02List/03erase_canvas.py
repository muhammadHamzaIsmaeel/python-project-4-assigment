import tkinter as tk

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 40
ERASER_SIZE = 20

def erase_object(canvas, eraser):
    mouse_x = canvas.winfo_pointerx() - canvas.winfo_rootx()
    mouse_y = canvas.winfo_pointery() - canvas.winfo_rooty()

    overlapping_object = canvas.find_overlapping(
        mouse_x, mouse_y, mouse_x + ERASER_SIZE, mouse_y + ERASER_SIZE
    )

    for obj in overlapping_object:
        if obj != eraser:
            canvas.itemconfig(obj, fill='white')

def main():
    root = tk.Tk()
    canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
    canvas.pack()

    num_rows = CANVAS_HEIGHT // CELL_SIZE
    num_cols = CANVAS_WIDTH // CELL_SIZE

    for row in range(num_rows):
        for col in range(num_cols):
            left_x = col * CELL_SIZE
            top_y = row * CELL_SIZE
            right_x = left_x + CELL_SIZE
            bottom_y = top_y + CELL_SIZE    
            canvas.create_rectangle(left_x, top_y, right_x, bottom_y, fill='blue')
            
    canvas.wait_for_click = lambda: canvas.bind("<Button-1>", lambda e: None)
    canvas.get_last_click = lambda: (canvas.winfo_pointerx() - canvas.winfo_rootx(), canvas.winfo_pointery() - canvas.winfo_rooty())

    canvas.wait_for_click()
    last_click_x, last_click_y = canvas.get_last_click()

    eraser = canvas.create_rectangle(
        last_click_x, last_click_y, last_click_x + ERASER_SIZE, last_click_y + ERASER_SIZE, fill='pink'
    )

    def move_eraser(event):
        canvas.moveto(eraser, event.x, event.y)
        erase_object(canvas, eraser)

    canvas.bind("<Motion>", move_eraser)

    root.mainloop()

if __name__ == '__main__':
    main()