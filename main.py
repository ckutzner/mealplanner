import random
from datetime import date, timedelta
from urllib.parse import urlparse

def next_monday_date():
    """ Returns the date of next monday """
    if date.today().weekday() == 0:
        next_monday = date.today()
    else:
        diff = 7 - date.today().weekday()
        next_monday = date.today() + timedelta(diff)
    return next_monday

def seasonal_recipes():
    """ Determines whether it's summer or winter, reads appropriate recipe list; depends on next_monday_date() """     
    mon = next_monday_date().month
    if mon in range(4,10):
        with open('input/summer-meals.txt', 'r') as r:
            recipes = r.readlines()
    else: 
        with open('input/winter-meals.txt','r') as r: 
            recipes = r.readlines()
        
    return recipes

def choose_menus():
    """ Choose random menus from the recipes list """
    full_list = seasonal_recipes()
    food = random.sample(full_list, 6)
    menus = []
    for meal in food:
        m = meal.split('; ')
        if len(m) > 1:
            mealname = m[0].strip
            mealsource = m[1].strip
            if urlparse(m[1]).scheme and urlparse(m[1]).netloc:
                menus.append(f'\\href{{{mealsource}}}{{{mealname}}}\n')
            else:
                menus.append(f'{mealname}\\\\\n{{\\small {mealsource}}}\n')
        else: 
            menus.append(f'{m[0]}\n')
    return menus

def choose_soups():
    """ Choose 2 soups from the soups list """
    with open('input/soups.txt', 'r') as s:
        souplist = s.readlines()
        
    soups = random.sample(souplist, 2)
    return soups

def menuplan():
    """ generate weekdays with date, then string it together with lists nicely and write to a text/tex file """
    date = next_monday_date()
    menus = choose_menus()
    soups = choose_soups()

    menufile = str(f'output/{date.strftime("%Y-%m-%d")}_menus.tex') 
    days = []
    
    for i in range(14):
        days.append(date)
        date += timedelta(1)
     
    with open(menufile, 'w') as meals:
        #copy preamble
        with open('templates/preamble.tex', 'r') as p:
            preamble = p.read()

        meals.write(preamble)    
        # the following line could be made prettier using string formatting
        meals.write(f"{{\\Large Menus for Calendar Week {str(days[0].isocalendar()[1])}}}\\\\ \n{{\\small {str(days[0].strftime("%B %d, %Y"))} - {str(days[6].strftime("%B %d, %Y"))}}}\\\\ \n ~ \\\\")
        
        for day in days: # write the menu order to a tex file
            daystring = str(f"{{\\calligra \\Large {day.strftime("%A, %B %d %Y")}}} \\\\ \n")
            if day.weekday() == 0 or day.weekday() == 3:
                meals.write(f"{daystring} Leftovers (or pasta) for dinner!\n\n")
            elif day.weekday() == 2:
                meals.write(f"{daystring} {soups.pop(0)} \n\n")
            elif day.weekday() == 4:
                meals.write(f"{daystring} Pizza day!\n\n")
            elif day.weekday() == 6:
                if len(soups) > 0:
                    meals.write(f"{daystring} {menus.pop(0)} \\newpage\n{{\\Large Menus for Calendar Week {str(days[7].isocalendar()[1])}}} \\\\ \n{{\\small {str(days[7].strftime("%B %d, %Y"))} - {str(days[-1].strftime("%B %d, %Y"))}}}\\\\ \n ~ \\\\")
                else:
                    meals.write(f"{daystring} {menus.pop(0)} \\end{{center}}\n\\end{{document}}")
            else:
                meals.write(f"{daystring} {menus.pop(0)} \n")

menuplan()
