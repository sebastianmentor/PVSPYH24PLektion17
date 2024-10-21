class Person:
    def __init__(
        self,
        name: str,
        age: int,
        passport: bool,
        city: str,
        drivers_license: bool,
        shoe_size: int,
        salary: int,
    ):
        self.name = name
        self.age = age
        self.passport = passport
        self.city = city
        self.drivers_license = drivers_license
        self.shoe_size = shoe_size
        self.salary = salary

def valid_name(person:Person) -> bool:
    if person.name in ['Sebastian', 'Kalle', 'Kungen']:
        return True
    return False

def valid_drinking_age(age:int) -> bool:
    return True if age>=18 else False

def has_passport(passport:bool) -> bool:
    return True if passport else False

def lives_in_the_right_city(city:str) -> bool:
    if city not in ['Stockholm', 'Göteborg', 'Uppsala']:
        return True
    return False

def dont_have_drivers_license(license:bool) -> bool:
    return True if not license else False

def right_shoe_size(size:int) -> bool:
    return True if 36 <= size <= 47 else False

def earns_enough(salary:int) -> bool:
    return True if salary > 25000 else False

def serve_drinks(person:Person):
    if (valid_name(person)
        and valid_drinking_age(person.age) 
        and has_passport(person.passport)
        and lives_in_the_right_city(person.city)
        and dont_have_drivers_license(person.drivers_license)
        and right_shoe_size(person.shoe_size)
        and earns_enough(person.salary)
        ):
        
        print(f'Serve this person {person.name} a drink!')
    else:
        print(f'Sorry, you are not welcome here! Fuck off!')

