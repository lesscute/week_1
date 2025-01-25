##### ASSIGNMENT STARTS HERE #####


#%%
# First Assignment
'''
1: Please create a program which inputs two years and outputs the years as well as the difference
between them!

Your output should look like:

Year 1: 2025
Year 2: 2028
Difference: 3
'''
#user input
year_input = int(input("Enter a year: "))
# takes input and adds 2
new_year = year_input + 2
# takes the difference
difference = new_year - year_input
#shows results 
print(f"Year 1: {year_input}")
print(f"Year 2: {new_year}")
print(f"Difference: {difference} years")


# I don't know what i'm doing. I thought day 1 was on 1/27/2025
#%%
# Second Assignment

'''
2: Please create a program which collects an input as fahrenheit and outputs the 
temperature in celsius

Your output should look like:

Fahrenheit: 25
Celsius: -3.89
'''
##researched on how to find solutions
#How cold is it in the us
fahrenheit = float(input("Enter temp in Fahrenheit: "))
#does canadian math
celsius = (fahrenheit - 32) * 5/9
#provides output
print(f"{fahrenheit}F is equal to {celsius:.2f}C")

#%%

# Third Assignment

'''

3: Please create a program which collects an input as US Dollars and converts the output to Euros 
given the exchange rate on 1/19/25 as 1 USD = 0.97 Euro

Your output should look like:
USD: 1
EU: 0.97

'''

#convertion rate
usd_to_euro_rate = 0.97
#input USD
usd_amount = float(input("Enter USD: "))
#converts to Euro
euro_amount = usd_amount * usd_to_euro_rate
#displays output
print(f"{usd_amount} USD is equal to {euro_amount:.2f} EUR")


##### ASSIGNMENT ENDS HERE #####
