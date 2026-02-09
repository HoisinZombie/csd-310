def get_city (city, country, population, language):
    """Generate a neatly formatted location"""
    location = f"{city}, {country} - population {population}, {language}"
    return location.title()
