# Pokebrawl 🥅⚽  
A Pokémon-themed soccer minigame built in Python using the Turtle graphics module.  
Shoot the ball, score goals, unlock levels, and face off against Pokémon goalkeepers with increasing difficulty!

---

## 📚 Table of Contents
- Features
- Demo
- Installation
- Usage
- Project Structure
- Technologies Used
- Configuration
- Roadmap
- Contributing
- License
- Credits

---

## 🚀 Features
- 5 unique Pokémon goalie levels  
- Unlock new levels by scoring 3 goals  
- Smooth animations using custom interpolation  
- Pokémon difficulty controlled via `pokemon_scoring.txt`  
- Pokéball HUD shows goal / miss / unused  
- Custom sprites and GIF-based animations  
- Score tracking and fail/retry logic

---

## 📂 Project Structure

```

Pokebrawl
│
├── main.py
├── pokemon_scoring.txt
│
├── Play.gif
├── Levels_screen.gif
├── stadium.gif
├── goal.gif
├── Win.gif
├── Miss.gif
│
├── Pikachu.gif
├── Squirtle.gif
├── Meowth.gif
├── Snorlax.gif
├── Charizard.gif
│
├── Pokeball_unused1.gif
├── Pokeball_unused2.gif
├── Pokeball_unused3.gif
├── Pokeball_unused4.gif
├── Pokeball_unused5.gif
│
├── Pokeball_miss1.gif
├── Pokeball_miss2.gif
├── Pokeball_miss3.gif
├── Pokeball_miss4.gif
├── Pokeball_miss5.gif
│
├── Pokeball_goal1.gif
├── Pokeball_goal2.gif
├── Pokeball_goal3.gif
├── Pokeball_goal4.gif
└── Pokeball_goal5.gif
```

---

## 🚀 How to Run the Game

### **1. Install Python**
This project uses Python 3.x.  
Download it from: https://www.python.org/

### **2. Clone or Download the Repo**

```bash
git clone https://github.com/Satyansh-alt/Pokebrawl.git
cd Pokebrawl

```

### **3. Ensure All GIF Files Are in the Same Folder as main.py**

The game relies heavily on these sprite files.

### **4. Run the Game**
python main.py

---

### **🕹 How to Play**

Click Play on the title screen.

Choose an unlocked level.

Click anywhere on the field to shoot the soccer ball.

Score 3 out of 5 goals to beat the level.

Beat a level to unlock the next one!

Beat level 5 to win the game.

---

### **🔧 Game Logic Summary**

Each Pokémon has a scoring distance defined in pokemon_scoring.txt

A “goal” happens if:

Your click lands inside the goal area and

The ball is far enough away from Pokémon’s position based on difficulty

Misses are tracked visually using Pokéballs

Cooldown between shots prevents spam clicking

When 3 goals are scored → Level Complete

When 3 misses occur → Try Again

---

### **📜 pokemon_scoring.txt Format**
Pikachu.gif,200
Squirtle.gif,250
Meowth.gif,300
Snorlax.gif,350
Charizard.gif,400

Higher numbers = harder Pokémon (you must shoot farther from them to score).

---

### **🛠 Technologies Used**

Python

Turtle Graphics

GIF-based sprite animation

Simple game state + level progression system

---

### **🤝 Contributing**

Pull requests are welcome!
If you’d like to improve the visuals, performance, or add new mechanics, feel free to open an issue.
