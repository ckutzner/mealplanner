# mealplanner
A python utility for generating printable weekly meal plans from lists of your favorite recipes (using LaTeX).  
The planner currently uses four lists:  summer meals, winter meals, soups and specials (for when you are feeling fancy and have the extra time to cook a nice meal).

It is currently a bit inflexible; it was invented to scratch a very specific itch in my household, so many things are hardcoded.

## Requirements
 * Python 3
 * pdflatex 

## Usage
This is a commandline utility. I'm not planning to make a GUI for it (but if you find it useful and want to make one, go ahead).

To generate a meal plan, first add recipe names to the input files (summer-meals.txt, winter-meals.txt, soups.txt, specials.txt). Then, from the directory where main.py is located, call: 
    
    python main.py

Then navigate to the output directory and run:

    pdflatex YYYY-MM-DD_menus.tex

(where YYYY-MM-DD corresponds to the start date of the menu plan in year-month-day format).

## Why I made this
My wife and I were looking for a way of organizing our grocery shopping better, having some variety in our meals and using mostly recipes we have tried and tested before. (Who has time to deal with new recipes all the time?) Initially, we just made a list of the stuff we liked to eat and cobbled together a script that picked a random recipe for the next 14 days. Over time, we adjusted it to our working week. For example, we used to get Pizza every Friday, or we'd discover that we regularly skipped cooking the planned meal on Mondays because of a particularly hectic schedule. That inspired me to include "pasta or leftovers" days (substitute your favorite go-to quick meal for pasta) and Wednesday became soup day.
