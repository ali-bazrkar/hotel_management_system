import re


class Validator:
    @classmethod
    def name_validator(cls, name, message):
        if isinstance(name, str) and re.match(r"^[a-zA-Z\s]{2,20}$", name):
            return name.title()
        else:
            raise ValueError(message)

    @classmethod
    def username_validator(cls, username, message):
        if re.match(r"^[\w]{2,20}$", username):
            return username.lower()
        else:
            raise ValueError(message)

    @classmethod
    def password_validator(cls, password, message):
        if re.match(r"^[\w@!#$%^&*\s]{8,20}$", password):
            return password
        else:
            raise ValueError(message)

    @classmethod
    def digit_validator(cls, digit, message):
        if re.match(r"^[0-9]{,9}$", str(digit)) and (int(digit) > 0):
            return int(digit)
        if (digit == None):
            return digit
        else:
            raise ValueError(message)

    @classmethod
    def numeric_validator(cls, numeric, message):
        if re.match(r"^[0-9]{1,3}$", str(numeric)) and (int(numeric) > 0) and isinstance(numeric, str):
            numeric = "{:03}".format(int(numeric))
            return numeric
        else:
            raise ValueError(message)

    @classmethod
    def address_validator(cls, address, message):
        if isinstance(address, str) and re.match(r"^[\.\w\s,()-]{2,255}$", address):
            return address
        else:
            raise ValueError(message)

    @classmethod
    def hotel_name_validator(cls, hotel_name, message):
        if isinstance(hotel_name, str) and re.match(r"^[a-zA-Z0-9 .'\-]{2,20}$", hotel_name):
            return hotel_name
        else:
            raise ValueError(message)

