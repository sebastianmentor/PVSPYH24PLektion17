################## Bad  ###################
# Vi har 10 studenter
x = 10

################## Good ###################
# Vi har 10 studenter
number_of_students = 10

################## Bad  ###################
# Mycket som ska hända i koden
def does_it_all():
    # Gör allt som måste ske
    ...

################## Good ###################
def does_some_part():
    ...

def does_some_other_part():
    ...

def make_it_happen():
    does_some_part()
    does_some_other_part()
    # maybe one more thing here

################## Bad  ###################
def process_data(data):
    # Många operationer på data sker här
    ...

################## Good ###################
# Bättre att dela upp operationerna
def parse_data(data):
    ...

def clean_data(parsed_data):
    ...

def analyze_data(clean_data):
    ...

################## Bad  ###################
def p():
    ...

################## Good ###################
def print_report():
    ...

################## Bad  ###################
price = 29.90
total = price * 0.08

################## Good ###################
TAX_RATE = 0.08
total = price * TAX_RATE

################## Bad  ###################
i = 0

################## Good ###################
attempts = 0
