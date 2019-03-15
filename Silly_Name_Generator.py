"""Generates "funny" names by randomly combining names from 2 separated lists."""
import sys
import random


def main():
    """Choose names at random from 2 tuples of names and prints them to screen"""
    first = ('Baby Oil', 'Bad News', 'Big Burps', "Bill 'Beenie-Weenie'",
             "Bob 'Stinkbug'", 'Bowel Noises', 'Boxelder', "Bud 'Lite' ",
             'Butterbean', 'Buttermilk', 'Buttocks', 'Chad', 'Chesterfield',
             'Chewy', 'Chigger', 'Cinnabuns', 'Cleet', 'Cornbread', 'Crab Meat',
             'Crapps', 'Dark Skies', 'Dennis Clawhammer', 'Dicman', 'Elphonso',
             'Fancypants', 'Figgs', 'Foncy', 'Gootsy', 'Greasy Jim', 'Huckleberry',
             'Huggy', 'Ignatious', 'Jimbo', "Joe 'Pottin Soil'", 'Johnny',
             'Lemongrass', 'Lil Debil', 'Longbranch', '"Lunch Money"', 'Mergatroid',
             '"Mr Peabody"', 'Oil-Can', 'Oinks', 'Old Scratch', 'Ovaltine',
             'Pennywhistle', 'Pitchfork Ben', 'Potato Bug', 'Pushmeet',
             'Rock Candy', 'Schlomo', 'Scratchensniff', 'Scut',
             "Sid 'The Squirts'", 'Skidmark', 'Slaps', 'Snakes', 'Snoobs',
             'Snorki', 'Soupcan Sam', 'Spitzitout', 'Squids', 'Stinky',
             'Storyboard', 'Sweet Tea', 'TeeTee', 'Wheezy Joe',
             "Winston 'Jazz Hands'", 'Worms')

    last = ('Appleyard', 'Bigmeat', 'Bloominshine', 'Boogerbottom',
            'Breedslovetrout', 'Butterbaugh', 'Clovenhoof', 'Clutterbuck',
            'Cocktoasten', 'Endicott', 'Fewhairs', 'Gooberdapple', 'Goodensmith',
            'Goodpasture', 'Guster', 'Henderson', 'Hooperbag', 'Hoosenater',
            'Hootkins', 'Jefferson', 'Jenkins', 'Jingley-Schmidt', 'Johnson',
            'Kingfish', 'Listenbee', "M'Bembo", 'McFadden', 'Moonshine', 'Nettles',
            'Noseworthy', 'Olivetti', 'Outerbridge', 'Overpeck', 'Overturf',
            'Oxhandler', 'Pealike', 'Pennywhistle', 'Peterson', 'Pieplow',
            'Pinkerton', 'Porkins', 'Putney', 'Quakenbush', 'Rainwater',
            'Rosenthal', 'Rubbins', 'Sackrider', 'Snuggleshine', 'Splern',
            'Stevens', 'Stroganoff', 'Sugar-Gold', 'Swackhamer', 'Tippins',
            'Turnipseed', 'Vinaigrette', 'Walkingstick', 'Wallbanger', 'Weewax',
            'Weiners', 'Whipkey', 'Wigglesworth', 'Wimplesnatch', 'Winterkorn',
            'Woolysocks')

    print("Welcome to the Psych 'Sidekick Name Picker.'")
    print("A name just like Sean would pick for Gus:\n")

    while True:
        first_name = random.choice(first)  # Picks a random item from the first array
        last_name = random.choice(last)  # Picks a random item from the last array
        print(first_name, last_name)

        continue_question = input("Type 'n' to generate a new name and 'e' to exit\n")

        if continue_question.lower() == "n":
            break
        elif continue_question.lower() == "e":
            for i in range(20):
                print("")
            continue


main()
