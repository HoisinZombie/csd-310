
from city_functions import get_city

print("Enter 'q' at any time to quit.")
while True:
    city = input("\nPlease enter the name of a city only: ")
    if city == 'q':
        break
    country = input("Please enter the name of the country the city is located in: ")
    if country == 'q':
        break
    population = input("\nPlease enter the population of the city: ")
    if population == 'q':
        break
    language = input("\nPlease enter the most main language of this city: ")
    if language == 'q':
        break



    location = get_city(city, country, population, language)
    print(f"\tNeatly formatted location: {location}.")
