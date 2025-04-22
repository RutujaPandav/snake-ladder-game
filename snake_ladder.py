import random
import time

# 🐍 Snakes (some are helpful!)
snakes = {16: 6, 47: 26, 62: 19, 64: 60, 93: 68, 97: 76, 99: 80}
friendly_snakes = {11: 33, 55: 77}  # Reverse snakes 😈➡️😇

# 🪜 Ladders
ladders = {3: 22, 5: 8, 20: 38, 27: 56, 43: 66, 50: 91, 70: 92}

# 🌀 Portals (teleporters!)
portals = [10, 25, 45, 67, 89]

# Starting positions
players = {"🔴 Player 1": 0, "🔵 Player 2": 0}

def roll_dice():
    return random.randint(1, 6)

def print_board():
    print("\n🎲 Game Board Snapshot:")
    for name, pos in players.items():
        print(f"{name} is at 📍 {pos}")
    print("-" * 40)

def move_player(name, position):
    input(f"{name}, press Enter to roll the dice...")
    dice = roll_dice()
    print(f"{name} rolled a 🎲 {dice}!")
    position += dice
    if position > 100:
        print("⚠️ You need an exact number to land on 100.")
        position -= dice
    time.sleep(0.5)

    if position in snakes:
        print(f"{name} got bitten by 🐍! Going down from {position} to {snakes[position]}")
        position = snakes[position]
    elif position in friendly_snakes:
        print(f"{name} found a friendly 🐍! Climbing up from {position} to {friendly_snakes[position]}")
        position = friendly_snakes[position]
    elif position in ladders:
        print(f"{name} climbed a 🪜! Up from {position} to {ladders[position]}")
        position = ladders[position]
    elif position in portals:
        teleport = random.randint(1, 100)
        print(f"{name} entered a 🌀 PORTAL! Teleporting to {teleport}")
        position = teleport

    print(f"{name} moved to 📍 {position}")
    return position

# 🎮 Game loop
print("✨ Welcome to Snakes & Portals! ✨\n")
while True:
    for player in players:
        players[player] = move_player(player, players[player])
        print_board()
        if players[player] == 100:
            print(f"🎉🎉 {player} WINS THE GAME! 🎉🎉")
            exit()
