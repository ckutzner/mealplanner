# mealplanner
A python utility for generating printable weekly meal plans from lists of your favorite recipes (using LaTeX).  
The planner currently uses four lists:  summer meals, winter meals, soups and specials (for when you are feeling fancy and have the extra time to cook a nice meal).

It is currently a bit inflexible; it was invented to scratch a very specific itch in my household, so many things are hardcoded.

## Requirements
 * Python
 * pdflatex 

## Usage
This is a commandline utility. I'm not planning to make a GUI for it.

To generate a meal plan, first add recipe names to the input files (summer-meals.txt, winter-meals.txt, soups.txt, specials.txt). Then, from the directory where main.py is located, call: 
    
    python main.py

Then navigate to the output directory and run:

    pdflatex YYYY-MM-DD_menus.tex

(where YYYY-MM-DD corresponds to the start date of the menu plan in year-month-day format).
