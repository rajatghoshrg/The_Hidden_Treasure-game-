# Adventure Game - "THE HIDDEN TREASURE"
# Made by - Rajat Ghosh
name = input("What is your name: ")
gender = input("Are you a man or woman: ").lower()
print("\n")
print(f"Welcome to the Adventure Game, {name}!")

def start():
    print(f'''
{name}, a young {gender}, wakes up in the dark forest named 'Itachuna Woods'. 
In your pocket, you find a rusty 'key'. This key unlocks the gate to an Hidden treasure..🏴‍☠️

You stand beneath an ancient Banyan tree with two different paths:

- To your LEFT: a narrow, muddy slippy path with deep, strange footprints..👣
- To your RIGHT: a grassy road under the sunlight with wildflowers..🌼

Choose wisely; your journey depends on your choise..💭
''')

    path = input("Which way do you want to go? (left/right): ").lower()

    if path == "left":
        print(f'''
You step into the muddy path. The weather is cold. You hear rustling sounds behind the trees...
Suddenly, a wild wolf jumps out, howling..🐺
        ''')
        decision = input("Do you want to FIGHT or RUN? (fight/run): ").lower()

        if decision == "fight":
            print('''
You grab a branch and face the wolf...
But it’s too strong! It bites your legs, and you collapse..☠️
GAME OVER!!😔
            ''')
        elif decision == "run":
            print('''
You slip and fall into the mud but somehow escape the wolf.You are dirty, full of mud with a scratch in your hand..
Ahead, you reach a long, misty river..🌊
            ''')
            river_choice = input("Do you want to SWIM or SEARCH around for help? (swim/search): ").lower()

            if river_choice == "swim":
                print('''
The current is stronger than expected. You get dragged underwater..☠️
GAME OVER!!
                ''')
            elif river_choice == "search":
                print('''
You walk along the river and find a small old wooden boat..
You also got a long brancn to sail it across the river..🚣

On the other side, there's a dark cave with strange symbols on the entrance..🏛️
                ''')
                cave_choice = input("Do you want to ENTER the cave or REST nearby? (enter/rest): ").lower()

                if cave_choice == "enter":
                    print(f'''
Inside the cave, you discover a rusted metal door. The key fits perfectly!
The door creaks open to reveal the long-lost Hidden Treasure!

CONGRATULATIONS, {name} YOU WIN !!🤩
                    ''')
                elif cave_choice == "rest":
                    print('''
You fall asleep near the cave... but a poisonous snake bites you during the night..🐍
GAME OVER!!😔
                    ''')
                else:
                    print("Invalid choice. Game ends.")
            else:
                print("Invalid choice. Game ends.")
        else:
            print("Invalid choice. Game ends.")

    elif path == "right":
        print('''
The grassy road leads you peacefully toward a crystal-clear, pleasent river.
Birds chirp, and you feel at ease..🌊
        ''')
        choice = input("Do you want to SWIM across or BUILD a raft? (swim/build): ").lower()

        if choice == "swim":
            print('''
You dive in, but the water is freezing and there is a whirlpool..🌪️
You get pulled under..☠️
GAME OVER!!😔
            ''')
        elif choice == "build":
            print('''
You build a raft using nearby logs..
After hours, you reach the other side safely..🚣‍♂️

There you find a small village of kind people..👨‍🦳🧑‍🦳👩‍🦳🧑‍🦳
They offer you food and guidance to the final location..🎯
            ''')
            village_choice = input("Do you TRUST the villagers or EXPLORE alone? (trust/explore): ").lower()

            if village_choice == "trust":
                print('''
The villagers guide you to a temple hidden in the jungle..🛕
Using your key, you unlock the inner chamber... and there it is — the Hidden Treasure!

YOU WIN!!🤩
                ''')
            elif village_choice == "explore":
                print('''
You wander into the jungle alone, but get lost in the thick vegetation.
Night falls. You are never seen again..☠️
GAME OVER!!😔
                ''')
            else:
                print("Invalid choice. Game ends.")
        else:
            print("Invalid choice. Game ends.")

    else:
        print("Invalid path. Game ends.")

start()
