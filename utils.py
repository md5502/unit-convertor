


def convert_mass(amount, c_from, c_to):
    amount = int(amount)
    units = {
        'milligram': 1,
        'gram': 1000,
        'kilogram': 1000000,
        'ounce': 28349.5,
        'pound': 453592.37
    }

    # Convert the input amount to milligrams
    if c_from in units and c_to in units:
        amount_in_mg = amount * units[c_from]
        
        # Convert from milligrams to the desired unit
        converted_amount = amount_in_mg / units[c_to]
        return converted_amount
    else:
        return "Invalid units"



def convert_length(amount, c_from, c_to):
    amount = int(amount)
    units = {
        'millimeter': 1,
        'centimeter': 10,
        'meter': 1000,
        'kilometer': 1000000,
        'inch': 25.4,
        'foot': 304.8,
        'yard': 914.4,
        'mile': 1609344
    }

    # Convert the input amount to millimeters
    if c_from in units and c_to in units:
        amount_in_mm = amount * units[c_from]
        
        # Convert from millimeters to the desired unit
        converted_amount = amount_in_mm / units[c_to]
        return converted_amount
    else:
        return "Invalid units"


def convert_temperature(amount, c_from, c_to):
    amount = int(amount)

    if c_from == 'celsius':
        if c_to == 'fahrenheit':
            print("\n\n\n", (amount * 9/5) + 32, "\n\n\n")
            return (amount * 9/5) + 32
        elif c_to == 'kelvin':
            return amount + 273.15
        
    elif c_from == 'fahrenheit':
        if c_to == 'celsius':
            return (amount - 32) * 5/9
        elif c_to == 'kelvin':
            return (amount - 32) * 5/9 + 273.15
        
    elif c_from == 'kelvin':
        if c_to == 'celsius':
            return amount - 273.15
        elif c_to == 'fahrenheit':
            return (amount - 273.15) * 9/5 + 32
        
    else:
        return "Invalid units"
