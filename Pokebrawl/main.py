import turtle
import random
import time

def import_pokemon_scoring(filename):
    scoring = {}
    file = open(filename, 'r')
    
    for line in file:
        pokemon, score = line.strip().split(',')
        scoring[pokemon] = int(score)
    
    file.close()
    return scoring


Pokemons = import_pokemon_scoring('pokemon_scoring.txt')

# Global variables
unlocked_levels = 1
shots_taken = 0
shots_scored = 0
score_user = 0
current_pokemon = None
selected_level = 1

level_pokemons = {
    1: "Pikachu.gif",
    2: "Squirtle.gif",
    3: "Meowth.gif",
    4: "Snorlax.gif",
    5: "Charizard.gif"
}

# Initialize the screen
screen = turtle.Screen()
screen.bgpic('Pokebrawl.gif')

def create_level_button(level_num, x, y):
    def create_button():
        button = turtle.Turtle()
        screen.addshape(f"Level{level_num}.gif")
        button.shape(f"Level{level_num}.gif")
        button.penup()
        button.goto(x, y)
        
        if level_num > unlocked_levels:
            button.color("gray")
        
        return button

    def make_click_handler(button):
        def handle_click(click_x, click_y):
            global selected_level
            # Check if click is within button's boundaries
            button_width = 100  # Adjust based on your button image size
            button_height = 50  # Adjust based on your button image size
            button_x, button_y = button.pos()
            
            if (button_x - button_width/2 <= click_x <= button_x + button_width/2 and button_y - button_height/2 <= click_y <= button_y + button_height/2):
                if level_num <= unlocked_levels:
                    selected_level = level_num
                    game(0, 0)
        return handle_click

    button = create_button()
    button.onclick(make_click_handler(button))
    
    return button

def show_message(message, duration=2000):
    msg = turtle.Turtle()
    msg.hideturtle()
    msg.penup()
    msg.goto(0, 0)
    msg.color("white")
    msg.write(message, align="center", font=("Arial", 24, "bold"))
    screen.ontimer(lambda: msg.clear(), duration)
    screen.ontimer(lambda: levels_screen(0, 0), duration)


def levels_screen(x, y):
    screen.clear()
    screen.bgpic("Levels_screen.gif")

    starting_x = -300
    y_pos = 150  # Moved 150 units upwards
    spacing = 150
    
    for i in range(1, 6):
        create_level_button(i, starting_x + (i-1)*spacing, y_pos)

def game(x, y):
    global shots_taken, shots_scored, score_user, current_pokemon
    screen.clear()
    screen.title("Soccer Game")
    screen.bgpic("stadium.gif")
    game_loop = False
    
    while game_loop == False:
        # Initialize game variables
        score_user = 0
        attempts = 5
        max_level = 5
        shots_taken = 0
        shots_scored = 0
        last_click_time = 0
        click_cooldown = 2.0
        current_pokemon = level_pokemons[selected_level]

        pokeballs = []


        # Create the turtle objects
        pokemon = turtle.Turtle()
        soccer_ball = turtle.Turtle()
        goal_celebration = turtle.Turtle()

        def setup_pokeballs():
            for i in range(5):
                ball = turtle.Turtle()
                screen.addshape(f"Pokeball_unused{i+1}.gif")
                screen.addshape(f"Pokeball_goal{i+1}.gif")
                screen.addshape(f"Pokeball_miss{i+1}.gif")
                ball.shape(f"Pokeball_unused{i+1}.gif")
                ball.penup()
                x_pos = -100 + (i * 50)
                ball.goto(x_pos, 300)
                pokeballs.append(ball)

        def update_pokeball(index, result):
            if 0 <= index < len(pokeballs):
                if result == "goal":
                    pokeballs[index].shape(f"Pokeball_goal{index+1}.gif")
                elif result == "miss":
                    pokeballs[index].shape(f"Pokeball_miss{index+1}.gif")

        def reset_pokeballs():
            for i in range(len(pokeballs)):
                pokeballs[i].shape(f"Pokeball_unused{i+1}.gif")

        def level_complete():
            global unlocked_levels
            screen.clear()
            if selected_level == unlocked_levels and unlocked_levels < 5:
                unlocked_levels += 1
                show_message(f"Level {selected_level} Complete!\nNew level unlocked!")
            elif selected_level == 5:
                screen.bgpic("Win.gif")
            else:
                show_message(f"Level {selected_level} Complete!")

        def setup(pokemon_name):
            global shots_taken, shots_scored, score_user
            shots_taken = 0
            shots_scored = 0
            score_user = 0

            reset_pokeballs()

            screen.addshape(pokemon_name)
            pokemon.shape(pokemon_name)
            pokemon.penup()
            pokemon.speed(100000)
            pokemon.goto(-20, -20)
            
            screen.addshape("Soccerball.gif")
            soccer_ball.shape("Soccerball.gif")
            soccer_ball.penup()
            soccer_ball.goto(-20, -300)
            print(f"New Pokémon: {pokemon_name} - Score 3 times to move on!")
        
        def move_to_click(x, y):
            global shots_taken, shots_scored, current_pokemon

            current_time = time.time()
            if current_time - move_to_click.last_click_time < click_cooldown:
                print("Please wait before clicking again!")
                return

            move_to_click.last_click_time = current_time

            if shots_taken < attempts:
                result = None
                shots_taken += 1
                move_ball_and_pokemon(x, y)

                if check_score():
                    shots_scored += 1
                    result = "goal"
                    update_pokeball(shots_taken - 1, "goal")
                else:
                    result = "miss"
                    update_pokeball(shots_taken - 1, "miss")

                print(f"Shots Taken: {shots_taken} | Shots Scored: {shots_scored} | Misses: {shots_taken - shots_scored}")

                if shots_scored >= 3:
                    print(f"Good job! Level complete!")
                    screen.ontimer(lambda: level_complete(), 1500)
                    return
                elif shots_taken - shots_scored >= 3:
                    print(f"Try again! You need at least 3 scores to move on.")
                    show_message("Try again! You need at least 3 scores to move on.")
                    return

            if shots_taken >= attempts:
                print(f"Try again! You need at least 3 scores to move on.")
                show_message("Try again! You need at least 3 goals to move on.")


        def smooth_interpolation(start, end, t):
            t = max(0, min(1, t))
            t = t * t * (3 - 2 * t)
            return start + (end - start) * t

        def move_ball_and_pokemon(x, y):
            original_ball_pos = (-20, -300)
            original_pokemon_pos = (-20, -20)
            
            start_ball_x, start_ball_y = soccer_ball.pos()
            start_pokemon_x, start_pokemon_y = pokemon.pos()
            
            end_pokemon_x = random.randint(-400, 400)
            end_pokemon_y = random.randint(-100, 100)
            
            total_frames = 30
            
            for frame in range(total_frames + 1):
                t = frame / total_frames
                
                curr_ball_x = smooth_interpolation(start_ball_x, x, t)
                curr_ball_y = smooth_interpolation(start_ball_y, y, t)
                soccer_ball.goto(curr_ball_x, curr_ball_y)
                
                curr_pokemon_x = smooth_interpolation(start_pokemon_x, end_pokemon_x, t)
                curr_pokemon_y = smooth_interpolation(start_pokemon_y, end_pokemon_y, t)
                pokemon.goto(curr_pokemon_x, curr_pokemon_y)
                
                screen.update()
                turtle.delay(10)
            
            screen.ontimer(lambda: reset_positions(original_ball_pos, original_pokemon_pos), 1000)

        def reset_positions(ball_pos, pokemon_pos):
            soccer_ball.goto(ball_pos)
            pokemon.goto(pokemon_pos)

        def goal_scored():
            goal_celebration.hideturtle()
            goal_celebration.penup()
            
            screen.addshape("goal.gif")
            goal_celebration.shape("goal.gif")
            goal_celebration.showturtle()
            goal_celebration.goto(0, 0)
            screen.ontimer(clear_celebration, 1000)

        def clear_celebration():
            goal_celebration.clear()
            goal_celebration.hideturtle()

        def check_score():
            dist_to_win = Pokemons[current_pokemon]
            distance_target = soccer_ball.distance(pokemon)
            
            goalpost_left = -470
            goalpost_right = 470
            goalpost_bottom = -200
            goalpost_top = 200

            if not (goalpost_left <= soccer_ball.xcor() <= goalpost_right and goalpost_bottom <= soccer_ball.ycor() <= goalpost_top):
                update_pokeball(shots_taken - 1, "miss")
                print("Miss! The soccer ball went outside the goalpost!")
                miss_turtle = turtle.Turtle()
                miss_turtle.hideturtle()
                miss_turtle.penup()
                screen.addshape("Miss.gif")
                miss_turtle.shape("Miss.gif")
                miss_turtle.goto(0, 0)
                miss_turtle.showturtle()
                screen.ontimer(miss_turtle.clear(), 2000)
                screen.ontimer(miss_turtle.hideturtle(), 2000)
                return False

            if distance_target > dist_to_win:
                print(f"Score! Soccer ball is over {current_pokemon}.")
                goal_scored()
                return True
            else:
                update_pokeball(shots_taken - 1, "miss")
                miss_turtle = turtle.Turtle()
                miss_turtle.hideturtle()
                miss_turtle.penup()
                screen.addshape("Miss.gif")
                miss_turtle.shape("Miss.gif")
                miss_turtle.goto(0, 0)
                miss_turtle.showturtle()
                
                print(f"No score. Soccer ball is not over {current_pokemon}.")
                screen.ontimer(miss_turtle.clear(), 3000)
                screen.ontimer(miss_turtle.hideturtle(), 3000)
                return False

        move_to_click.last_click_time = 0
        setup_pokeballs()
        setup(current_pokemon)
        screen.onscreenclick(move_to_click)
        screen.listen()
        screen.mainloop()

# Create play button
play = turtle.Turtle()
screen.addshape("Play.gif")
play.shape("Play.gif")
play.penup()
play.goto(0, -300)

# Connect the play button to the levels screen
play.onclick(levels_screen)

screen.mainloop()