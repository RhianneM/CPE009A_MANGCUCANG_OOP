import random

class Character:
    def __init__(self, name, hp, attack):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.attack = attack

    def is_alive(self):
        return self.hp > 0

    def reset(self):
        self.hp = self.max_hp

    def clamp_hp(self):
        if self.hp > self.max_hp:
            self.hp = self.max_hp

    def deal_damage(self, opponent, bonus_damage=0):
        damage = random.randint(5, self.attack) + bonus_damage

    
        if random.random() < 0.2:
            damage *= 2
            print("💥 CRITICAL HIT!")

        opponent.hp -= damage

        
        if random.random() < 0.1:
            heal = random.randint(5, 10)
            self.hp += heal
            self.clamp_hp()
            print(f"{self.name} heals {heal} HP!")

        print(f"{self.name} deals {damage} damage to {opponent.name}")



class Novice(Character):
    def __init__(self):
        super().__init__("Novice", 90, 15)


class Swordsman(Character):
    def __init__(self):
        super().__init__("Swordsman", 100, 20)


class Archer(Character):
    def __init__(self):
        super().__init__("Archer", 85, 23)


class Magician(Character):
    def __init__(self):
        super().__init__("Magician", 75, 26)


class BossMonster(Character):
    def __init__(self):
        super().__init__("Boss Monster", 110, 22)


class Game:
    def __init__(self):
        self.wins = {"Player 1": 0, "Player 2": 0}
        self.single_wins = 0

    def choose_role(self):
        roles = {
            "1": Swordsman,
            "2": Archer,
            "3": Magician
        }

        print("\nChoose your role:")
        print("1. Swordsman")
        print("2. Archer")
        print("3. Magician")

        choice = input("Enter choice: ")
        return roles.get(choice, Swordsman)()

    def battle(self, player1, player2, single_player_mode=False):
        player1.reset()
        player2.reset()

     
        if single_player_mode:
            player1.max_hp = int(player1.max_hp * 1.1)
            player1.hp = player1.max_hp

            player2.attack = int(player2.attack * 0.9)

        players = [player1, player2]
        random.shuffle(players)

        print("\n--- Battle Start ---")

        while player1.is_alive() and player2.is_alive():
            attacker = players[0]
            defender = players[1]

            bonus = 2 if (single_player_mode and attacker == player1) else 0

            attacker.deal_damage(defender, bonus_damage=bonus)

            print(f"{defender.name} HP: {max(0, defender.hp)}\n")

            players.reverse()

        winner = player1 if player1.is_alive() else player2
        print(f"🏆 {winner.name} wins!\n")
        return winner

    def single_player(self):
        print("\n--- Single Player Mode ---")
        player_wins = 0

        player = Novice()

        while True:
            print("\nNew Match!")
            opponent = BossMonster()

            winner = self.battle(player, opponent, single_player_mode=True)

            if winner == player:
                player_wins += 1
                self.single_wins += 1

                print(f"✔ You won this round!")
                print(f"Wins this run: {player_wins}")
                print(f"Total Single Player Wins: {self.single_wins}")

                
                if player_wins >= 2:
                    print("\n🎉 You unlocked new roles!")
                    player = self.choose_role()
            else:
                print("❌ You lost!")
                break

    def player_vs_player(self):
        print("\n--- Player vs Player Mode ---")

        while True:
            player1 = self.choose_role()
            player2 = self.choose_role()

            winner = self.battle(player1, player2)

            if winner == player1:
                self.wins["Player 1"] += 1
            else:
                self.wins["Player 2"] += 1

            print("\nScore:")
            print(f"Player 1 Wins: {self.wins['Player 1']}")
            print(f"Player 2 Wins: {self.wins['Player 2']}")

            again = input("Play again? (y/n): ")
            if again.lower() != 'y':
                break

    def start(self):
        while True:
            print("\n=== GAME MENU ===")
            print("1. Single Player")
            print("2. Player vs Player")
            print("3. Exit")

            choice = input("Choose mode: ")

            if choice == "1":
                self.single_player()
            elif choice == "2":
                self.player_vs_player()
            elif choice == "3":
                print("Exiting game...")
                break
            else:
                print("Invalid choice!")


if __name__ == "__main__":
    game = Game()
    game.start()