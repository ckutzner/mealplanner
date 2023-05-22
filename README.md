# mealplanner
A python utility for generating weekly meal plans from a list of your favorite recipes

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
