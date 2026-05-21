import tkinter as tk
import random

WIDTH = 400
HEIGHT = 600
CAR_SPEED = 20
GAME_SPEED = 50 

def move_left(event):
    car_pos = canvas.coords(car)
    if car_pos[0] > 0:
        canvas.move(car, -CAR_SPEED, 0)

def move_right(event):
    car_pos = canvas.coords(car)
    if car_pos[2] < WIDTH:
        canvas.move(car, CAR_SPEED, 0)

def game_loop():
    global score, game_running
    
    if not game_running:
        return

    # Move the enemy car down
    canvas.move(enemy, 0, 10)

    enemy_pos = canvas.coords(enemy)
    car_pos = canvas.coords(car)


    if enemy_pos[3] > HEIGHT:
        x = random.randint(20, WIDTH - 60)  
        canvas.coords(enemy, x, 0, x + 40, 80)
        score += 1
        window.title(f"Car Racing Game | Score: {score}")


    if (car_pos[2] > enemy_pos[0] and
        car_pos[0] < enemy_pos[2] and
        car_pos[3] > enemy_pos[1] and
        car_pos[1] < enemy_pos[3]):
        
        game_running = False
        canvas.create_text(WIDTH // 2, HEIGHT // 2, text="GAME OVER", fill="white", font=("Arial", 30, "bold"))
        return

    window.after(GAME_SPEED, game_loop)

window = tk.Tk()
window.title("Car Racing Game | Score: 0")

canvas = tk.Canvas(window, width=WIDTH, height=HEIGHT, bg="gray")
canvas.pack()

car = canvas.create_rectangle(180, 500, 220, 580, fill="blue")
enemy = canvas.create_rectangle(180, 0, 220, 80, fill="red")

score = 0
game_running = True


window.bind("<Left>", move_left)
window.bind("<Right>", move_right)

game_loop()

window.mainloop()
