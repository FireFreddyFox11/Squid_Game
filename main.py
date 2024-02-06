import random
import time
import math

num_players = 456
players_list = []
rand_player_count = 21
Next = False


for i in range(1, 30, 5):
    time.sleep(1)
    for j in range(1, rand_player_count):
        players_per_round = random.randint(0, 456)
        players_list.append(players_per_round)
    players_in_round = random.sample(players_list, random.randint(2, 21))
    num_moved = math.ceil((len(players_in_round) * 0.8))
    num_static = math.ceil((len(players_in_round) * 0.2))
    moved_players = random.sample(players_in_round, num_moved)
    for n in moved_players:
        del n
    static_players = random.sample(players_in_round, num_static)
    print("Green Light")
    print("Moved: ", end='')
    print(', '.join(map(str, moved_players)))
    print("Static: ", end='')
    print(', '.join(map(str, static_players)))
    print("Eliminated: None.")
    Next = True
    if Next:
        for j in range(1, rand_player_count):
            players_per_round = random.randint(0, 456)
            players_list.append(players_per_round)
        players_in_round = random.sample(players_list, random.randint(2, 21))
        num_moved = math.ceil((len(players_in_round) * 0.05))
        num_static = math.ceil((len(players_in_round) * 0.95))
        moved_players = random.sample(players_list, num_moved)
        for k in players_list:
            del k
        static_players = random.sample(players_list, num_static)
        eliminated_players = moved_players
        print("Red Light")
        print("Moved: ", end='')
        print(', '.join(map(str, moved_players)))
        print("Static: ", end='')
        print(', '.join(map(str, static_players)))
        print("Eliminated: ", end='')
        print(', '.join(map(str, eliminated_players)))
        print("\n")
        Next = False
