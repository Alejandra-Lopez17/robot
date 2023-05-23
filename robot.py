import random

class Card:
    def __init__(self, name, attack_level=0, defense_level=0,status=False,beneficio=False):
        self.name = name
        self.attack_level = attack_level
        self.defense_level = defense_level
        self.status = status
        self.beneficio = beneficio
    
    def print_card(self):
        print(self.name)

    def use(self, card_to_use, part):
        if card_to_use.status == "Berseker":
            part.attack_level = part.attack_level +(part.attack_level*card_to_use.attack_level)
        elif card_to_use.status == "Electrificado":
            part.defense_level = part.defense_level - (part.defense_level*card_to_use.defense_level)
        elif card_to_use.status == "Barrera":
            part.defense_level = part.defense_level +(part.defense_level*card_to_use.defense_level)
        elif card_to_use.status == "Attack Bonus":
            part.defense_level = part.attack_level + card_to_use.attack_level
        elif card_to_use.status == "Invencible":
            part.defense_level = part.defense_level + card_to_use.defense_level
        elif card_to_use.status == "Carta de Confusion":
            confusion_defense = part.attack_level
            confusion_attack = part.defense_level
            part.defense_level = confusion_defense
            part.attack_level = confusion_attack
        elif card_to_use.status == "Carta de Bloqueo":
            part.attack_level = 0

class Part:
    def __init__(self, name, attack_level=0, defense_level=0, energy_consumption=0):
        self.name = name
        self.attack_level = attack_level
        self.defense_level = defense_level
        self.energy_consumption = energy_consumption


    def get_status_dict(self):
        formatted_name = self.name.replace(" ", "_").lower()
        return {
            "{}_name".format(formatted_name): self.name.upper(),
            "{}_status".format(formatted_name): self.is_available(),
            "{}_attack".format(formatted_name): self.attack_level,
            "{}_defense".format(formatted_name): self.defense_level,
            "{}_energy_consump".format(formatted_name): self.energy_consumption,
        }

    def is_available(self):
        return not self.defense_level <= 0

robot_art = r"""
      0: {head_name}
      Is available: {head_status}
      Attack: {head_attack}                              
      Defense: {head_defense}
      Energy consumption: {head_energy_consump}
              ^
              |                  |1: {weapon_name}
              |                  |Is available: {weapon_status}
     ____     |    ____          |Attack: {weapon_attack}
    |oooo|  ____  |oooo| ------> |Defense: {weapon_defense}
    |oooo| '    ' |oooo|         |Energy consumption: {weapon_energy_consump}
    |oooo|/\_||_/\|oooo|          
    `----' / __ \  `----'           |2: {left_arm_name}
   '/  |#|/\/__\/\|#|  \'           |Is available: {left_arm_status}
   /  \|#|| |/\| ||#|/  \           |Attack: {left_arm_attack}
  / \_/|_|| |/\| ||_|\_/ \          |Defense: {left_arm_defense}
 |_\/    O\=----=/O    \/_|         |Energy consumption: {left_arm_energy_consump}
 <_>      |=\__/=|      <_> ------> |
 <_>      |------|      <_>         |3: {right_arm_name}
 | |   ___|======|___   | |         |Is available: {right_arm_status}
// \\ / |O|======|O| \  //\\        |Attack: {right_arm_attack}
|  |  | |O+------+O| |  |  |        |Defense: {right_arm_defense}
|\/|  \_+/        \+_/  |\/|        |Energy consumption: {right_arm_energy_consump}
\__/  _|||        |||_  \__/        
      | ||        || |          |4: {left_leg_name} 
     [==|]        [|==]         |Is available: {left_leg_status}
     [===]        [===]         |Attack: {left_leg_attack}
      >_<          >_<          |Defense: {left_leg_defense}
     || ||        || ||         |Energy consumption: {left_leg_energy_consump}
     || ||        || || ------> |
     || ||        || ||         |5: {right_leg_name}
   __|\_/|__    __|\_/|__       |Is available: {right_leg_status}
  /___n_n___\  /___n_n___\      |Attack: {right_leg_attack}
                                |Defense: {right_leg_defense}
                                |Energy consumption: {right_leg_energy_consump}
                                
"""

print(robot_art)

colors = {
    "Black":   '\x1b[90m',
    "Blue":    '\x1b[94m',
    "Cyan":    '\x1b[96m',
    "Green":   '\x1b[92m',
    "Magenta": '\x1b[95m',
    "Red":     '\x1b[91m',
    "White":   '\x1b[97m',
    "Yellow":  '\x1b[93m',
}

class Robot:
    def __init__(self, name, color_code):
        self.name = name
        self.color_code = color_code
        self.energy = 100
        self.parts = [
            Part("Head", attack_level=5, defense_level=10, energy_consumption=5),
            Part("Weapon", attack_level=15, defense_level=0, energy_consumption=10),
            Part("Left Arm", attack_level=3, defense_level=20, energy_consumption=10),
            Part("Right Arm", attack_level=6, defense_level=20, energy_consumption=10),
            Part("Left Leg", attack_level=4, defense_level=20, energy_consumption=15),
            Part("Right Leg", attack_level=8, defense_level=20, energy_consumption=15),
        ]
        self.magic_cards = []
        self.used_magic_cards = 0

    def greet(self):
        print("Hola, mi nombre es", self.name)

    def print_energy(self):
        print("Nos queda un porcentaje de energía", self.energy, "")

    def attack(self, enemy_robot, part_to_use, part_to_attack):
        enemy_robot.parts[part_to_attack].defense_level -= self.parts[part_to_use].attack_level
        self.energy -= self.parts[part_to_use].energy_consumption

    def is_on(self):
        return self.energy >= 0

    def is_there_available_parts(self):
        for part in self.parts:
            if part.is_available():
                return True
        return False

    def print_status(self):
        print(self.color_code)
        str_robot = robot_art.format(**self.get_part_status())
        self.greet()
        self.print_energy()
        print(str_robot)
        print(colors["Black"])

    def get_part_status(self):
        part_status = {}
        for part in self.parts:
            status_dict = part.get_status_dict()
            part_status.update(status_dict)
        return part_status

    def use_magic_card(self, card_index,part):
        if 0 <= card_index < len(self.magic_cards):
            magic_card = self.magic_cards[card_index]
            magic_card.use(self.magic_cards[card_index],self.parts[part])
            print(f"{self.name} usa {magic_card.name}!")
            if self.used_magic_cards == 2:
                print(f"{self.name} Ha usado todas las cartas mágicas disponibles.")
        else:
            print("Índice de tarjeta mágica no válido.")

def play():
    playing = True
    print("Bienvenid@ al juego")
    robot_one = Robot("Alejandra", colors["Black"])
    robot_two = Robot("Andrea", colors["Red"])
    round_count = 0

    magic_cartas=[
        Card("Berseker", attack_level=0.5, defense_level=0,status="Berseker",beneficio="positivo"),
        Card("Barrera", attack_level=0, defense_level=0.5,status="Barrera",beneficio="positivo"),
        Card("Attack Bonus", attack_level=5, defense_level=0,status="Attack Bonus",beneficio="positivo"),
        Card("Invencible", attack_level=0, defense_level=1000,status="Invencible", beneficio="positivo"),
        Card("Electrificado", attack_level=0, defense_level=0.2,status="Electrificado",beneficio="negativo"),
        Card("Carta de Confusion", attack_level=0, defense_level=0,status="Carta de Confusion",beneficio="negativo"),
        Card("Carta de Bloqueo", attack_level=0, defense_level=1000,status="Carta de Bloqueo",beneficio="negativo"),
    ]

    random.shuffle(magic_cartas)
    
    robot_one.magic_cards.append(magic_cartas[0])
    robot_one.magic_cards.append(magic_cartas[1])

    random.shuffle(magic_cartas)

    robot_two.magic_cards.append(magic_cartas[0])
    robot_two.magic_cards.append(magic_cartas[1])

    while playing:
        if round_count % 2 == 0:
            current_robot = robot_one
            enemy_robot = robot_two
        else:
            current_robot = robot_two
            enemy_robot = robot_one

        current_robot.print_status()
        print("¿Qué parte debería usar para atacar?")
        part_to_use = input("Escoja un número de la parte: ")
        part_to_use = int(part_to_use)

        enemy_robot.print_status()
        print("¿Qué parte del enemigo deberíamos atacar?")
        part_to_attack = input("Escoja una parte del enemigo para atacar: ")
        part_to_attack = int(part_to_attack)

        current_robot.attack(enemy_robot, part_to_use, part_to_attack)
        round_count += 1

        if not enemy_robot.is_on() or not enemy_robot.is_there_available_parts():
            playing = False
            print("¡Felicidades! Tú ganaste.")
            print(current_robot.name)

        if current_robot.used_magic_cards < 2:
            print("¿Quieres usar una carta mágica?")
            use_magic_card = input("Introduzca 'si' o 'no': ")
            if use_magic_card.lower() == "si":
                print("¿Qué carta mágica quieres usar?")
                for i, card in enumerate(current_robot.magic_cards):
                    print(f"{i + 1}. {card.name}")
                card_index = int(input("Elija un número para la tarjeta: ")) - 1
                part = int(input("Elija la parte en la que quiere utilizar la tarjeta: "))
                if current_robot.magic_cards[card_index].beneficio == "positivo":
                    current_robot.use_magic_card(card_index,part)

                elif current_robot.magic_cards[card_index].beneficio == "negativo":
                    enemy_robot.use_magic_card(card_index,part)

play()