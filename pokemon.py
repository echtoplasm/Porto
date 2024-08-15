from typing import Any
from collections import namedtuple

Pokemon_types = ('fire', 'dark', 'fairy', 'poison', 'electric', 'ice', 'base', 'water')

base_damage_types = {'slash': 10,
                     'bite' : 15,
                     'tackle': 20}

dark_damage_types = {'plague': 10,
                     'hex': 15,
                     'possess':30}

fairy_damage_type = {'phase': 10,
                     'stun' : 20,
                     'moonlight' : 30
                     }

grass_damage_type = {'leaf blade': 15,
                     'dirt clod' : 20,
                     'limb smack' : 30}

fire_damage_type = {'burn' : 10,
                    'singe' : 15,
                    'inferno' : 30}

fire_type_damage_rebuff = {}
fire_type_damage_vulnerability = {}

for dam in grass_damage_type:
    fire_type_damage_rebuff.append(dam * .75 )

for dam in dark_damage_types:
    fire_type_damage_vulnerability.append(dam * 1.25)






class Pokemon:
    def __init__(self, name, level, type, maximum_health, current_health, is_ko, damage_type, vulnerability):
        self.name = name
        self.level = level
        self.type = type
        self.maximum_health = maximum_health
        self.current_health = current_health
        self.is_ko = is_ko
        self.damage_type = damage_type
        self.vulnerability = vulnerability
    


            
        


    
    def level_up(self, level, current_xp, xp_to_next_level, xp_gained):
        self.current_xp = current_xp
        self.xp_to_next_level = xp_to_next_level
        self.level = level
        self.xp_gained = xp_gained
        
        level = []
        
        if current_xp == range(int(0, 1000)):
            level = 1
            print('Your current level is: ', level)
        elif current_xp == range(int(1001, 2000)):
            level = 2
            print('Your current level is: ', level)
        elif current_xp == range(int(2001, 3000)):
            level = 3
            print('Your current level is: ', level)
        elif current_xp == range(int(3001, 4000)):
            level = 4
            print('Your current level is: ', level)
        elif current_xp == range(int(4001, 5000)):
            level = 5
            print('Your current level is: ', level)
        else:
            level = 5
            print('You have reached the max level and xp! Congratulations')
        
        
        if xp_gained > xp_to_next_level:
            level += 1



    
    def lose_health(self, current_health, maximum_health, damage_taken, is_ko, damage_recieved):
        self.current_health = current_health
        self.max_health = maximum_health
        self.damage_taken = damage_taken
        self.is_ko = is_ko
        self.damage_recieved = damage_recieved

        for key, value in base_damage_types, :
            if damage_recieved == key:
                current_health - value
            print('The damage type: ', key, ' inficted ', value, ' to your pokemon!')
            print('Your pokemons current health is: {}').format(self.current_health)

        for health in current_health:
            if current_health == maximum_health:
                print('Your pokemon is happy and healthy!')
            elif current_health <= maximum_health / 2:
                print('Your pokemon is in dire need of healing!')
            elif current_health < maximum_health / 4:
                print('Your pokemon is on the brink of passing out')
            elif current_health == 0:
                self.is_ko == True
                print('Your pokemon is knocked out, use a healing item on them to bring them back!')
    
    def attack_dealt(self, attack, damage_dealt):
        
        self.damage_dealt = damage_dealt
        self.attack_input = attack
        
    Flag = True
    def attack_input(self, attack, damage_type):
        print('Your pokemon has access to Dark Type Damage')
        print('plague = 1', 'hex = 2', 'possess = 3')
        attack_response = input('What attack would you like to use?')
        if self.type == 'Dark':
            self.damage_type = damage_type
            damage_type = 'Dark'
        
        
        if attack_response == '1':
            print(f'{self.name} used Plague and hit the enemy for 10 hit points')
        elif attack_response == '2':
            print(f'{self.name} used Hex and hit the enemy for 20 hitpoints!')
        elif attack_response == '3':
            print(f'{self.name} used possess and hit the enemy for 30 hitpoints!')
        else:
            print('Invalid option. Please choose 1, 2, or 3.')


     
                


    
class Dark_Pokemon(Pokemon):
        def __init__(self, name, level, type, maximum_health, current_health, is_ko, damage_type,):
            self.damage_type = 'Dark'
            self.type = 'Dark'
           
            super().__init__(name, level, type, maximum_health, current_health, is_ko, damage_type)
        def attack_input(self, attack, damage_type):
            super().attack_input(attack, damage_type)



    
class Grass_Pokemon(Pokemon):
    def __init__(self, ):
        super().__init__()

class Fire_Pokemon(Pokemon):
    def __init__(self, name, level, type, maximum_health, current_health, is_ko, damage_type, attack_input):
        super().__init__(self, name, level, type, maximum_health, current_health, is_ko, damage_type, attack_input)

    def  vulnerability(self, type, weak_to, strong_against):

        self.type = type
        self.weak_to = weak_to
        self.strong_against = strong_against
        
        if type == 'fire':
            weak_to == 'dark'
            strong_against == 'grass'


            
            



class Fairy_Pokemon(Pokemon):
    def __init__(self, name, level, type, maximum_health, current_health, is_ko, damage_type):
        super().__init__(self, name, level, type, maximum_health, current_health, is_ko, damage_type)    

class Trainer:

    def __init__(self, level, name, num_of_pokemon, current_pokemon):
        self.name = name
        self.num_of_pokemon = num_of_pokemon
        self.current_pokemon = current_pokemon
        self.level = level
    
    def catching_pokemon(self, pokemon, type_of_pokeball, chance_to_catch, number_of_pokeballs):
        pokemon = Pokemon()
        self.type_of_pokeball = type_of_pokeball 
        self.chance_to_catch = chance_to_catch
        self.number_of_pokeballs = number_of_pokeballs

        def chance_to_catch(chance_to_catch):
            chance_to_catch = 0
            if self.level > 3:
                chance_to_catch = 50
            if self.level == 5:
                chance_to_catch = 75










    
            



            





    
    