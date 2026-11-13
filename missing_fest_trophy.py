class Player:
    def __init__(self, name):
        self.name = name
        self.bag = []

    def collect_item(self, item):
        self.bag.append(item)
        print(f"{self.name} collected: {item}")

class Place:
    def __init__(self, name, required_item=None):
        self.name = name
        self.required_item = required_item
        self.is_locked = required_item is not None

    def unlock(self, player):
        if self.is_locked:
            if self.required_item in player.bag:
                print(f"Success: {player.name} unlocked the {self.name} using the {self.required_item}!")
                self.is_locked = False
                return True
            else:
                print(f"Failed: {self.name} is locked! {player.name} needs a {self.required_item} to enter.")
                return False
        else:
            print(f"{self.name} is already unlocked.")
            return True

class Chest:
    def __init__(self, correct_code):
        self.correct_code = correct_code
        self.is_open = False

    def open_chest(self, entered_code):
        if entered_code == self.correct_code:
            self.is_open = True
            print("Success: The code was correct! The chest is open. You found the Missing Fest Trophy!")
        else:
            print(f"Failed: Code '{entered_code}' is incorrect. The chest remains locked.")

# --- STORY EXECUTION ---

print("=== STARTING THE FAILED ROUTE ===")
player1 = Player("Alice")
secret_room = Place("Secret Room", required_item="Silver Key")
trophy_chest = Chest(correct_code="1234")

# Player tries to enter without the key
room_accessed = secret_room.unlock(player1)
if room_accessed:
    trophy_chest.open_chest("0000")


print("\n=== STARTING THE SUCCESSFUL ROUTE ===")
player2 = Player("Bob")
secret_room = Place("Secret Room", required_item="Silver Key")
trophy_chest = Chest(correct_code="1234")

# Player collects the required item first
player2.collect_item("Silver Key")

# Player successfully enters the room
room_accessed = secret_room.unlock(player2)

# Player uses the correct code to open the chest
if room_accessed:
    trophy_chest.open_chest("1234")
