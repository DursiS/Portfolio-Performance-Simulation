""" Prompts to chose preset """
def get_choice():
    choice = int(input("Choose Portfolio Preset (1-3): "))
    while choice not in [1, 2, 3]:
        choice = int(input("Invalid. Choose Portfolio Preset (1-3): "))
    return choice


""" Returns the chosen preset portfolio """
def preset(choice):
    
    if choice == 1:
        return preset_1
    
    if choice == 2:
        return preset_2
        
    if choice == 3:
        return preset_3


preset_1 = {
    "AAPL": 10,
    "GOOGL": 5,
    "AMZN": 5,
    "MSFT": 8,
    "TSLA": 6
}

preset_2 = {
    "NVDA": 12,
    "META": 7,
    "NFLX": 4,
    "INTC": 45,
    "ADBE": 6
}

preset_3 = {
    "BABA": 10,
    "ORCL": 8,
    "UBER": 12,
    "CRM": 5,
    "SHOP": 9
}