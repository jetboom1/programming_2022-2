import re


class Validator:
    """validating data"""
    def validate_name_surname(self, name_surname: str):
        """validating name and surname"""
        if re.search(r'^[A-Z][a-z]{2,30} [A-Z][a-z]{2,30}$', name_surname):
            return True
        return False
    def validate_age(self, age: str):
        """validating age"""
        if age.isdigit() and 16 < int(age) < 66:
            return True
        return False
    def validate_country(self, country: str):
        """Return True if country is valid"""
        if 2<len(country)<10 and country.isalpha() and country[0].isupper():
            return True
        return False
    def validate_region(self, region: str):
        '''Return True if region is valid'''
        if 2<len(region)<10 and region[0].isupper():
            return True
        return False
    def validate_living_place(self, living_place: str):
        '''Return True if living place is valid'''
        if re.search('([A-Z][a-zA-Z]{2,19}) (st.|av.|prosp.|rd.) \d([a-z]|\d)', living_place):
            return True
        return False
    def validate_index(self, index: str):
        '''Return True if index is valid'''
        if len(index) == 5 and index.isdigit():
            return True
        return False
    def validate_phone(self, phone: str):
        '''Return True if phone is valid'''
        if re.search('([+]\d{1,2}0{1}\d{7,10})|([+]\d{2} [(]\d{3}[)] \d{3}-\d{2}-\d{2})', phone):
            return True
        return False
    def validate_email(self, email: str):
        '''Return True if email is valid'''
        if re.search('^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z-.]*?(com|org|edu|gov|net|ua)$', email):
            return True
        return False
    def validate_id(self, id: str):
        '''Return True if id is valid'''
        if len(id) == 6 and id.isdigit() and id.count('0') == 1:
            return True
        return False
    def validate(self, data: str):
        '''Return True if data is valid'''
        if ',' in data:
            data = list([a.strip() for a in data.split(',')])
        elif ';' in data:
            data = list([a.strip() for a in data.split(';')])
        if len(data) == 9:
            if self.validate_name_surname(data[0]) and self.validate_age(data[1]) and self.validate_country(data[2]) \
                    and self.validate_region(data[3]) and self.validate_living_place(data[4]) \
                    and self.validate_index(data[5]) and self.validate_phone(data[6]) and self.validate_email(data[7])\
                    and self.validate_id(data[8]):
                return True
        return False



if __name__ == '__main__':
    valid = Validator()

    # name and surname


