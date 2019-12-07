from propertymatching.models import Company, Agent, ListingItem, User, UserForm
from django.contrib.postgres.search import SearchQuery
from faker import Faker
import random

## property arrays for listings and user form ##
real_estate_types = ['Apartment','House','Townhouse','Bungalow']
apartment_level = ['ground_floor', 'top_level']
area = ['costa_del_sol', 'Costa_del_Almeria', 'mallorca', 'costa_de_sur', 'barcelona']
environment = ['beach', 'golf_club', 'night_life', 'city_centre', 'airport', 'family_friendly', 'shopping']


def main():
    
    random_data = pop_randomiser()

    populate_partnerform(random_data[0])

    populate_customerform(random_data[1])

    print('database populated!')

def pop_randomiser():

    data = {}
    data_userform = {}
    fake = Faker()

    fake.random.seed(5467)

    for i in range(10):

        company = fake.company()
        
        data[company] = {
            'company_number': fake.phone_number(),
            'company_email': fake.company_email(),
            'agent_details': {}
        }
        
        for j in range(10):
            
            agent = fake.name()
            data[company]['agent_details'][agent] = {
                'agent_number': fake.phone_number(),
                'agent_email': fake.free_email(),
                'listings': {}
            }

            for k in range(5):
                
                listing = fake.address()
                real_estates = fake.random_element(real_estate_types)
                size = fake.random_int(min=50, max=60, step=1)
                if 'Apartment' in real_estate_types:
                    level = fake.random_element(apartment_level)
                else:
                    level = None

                data[company]['agent_details'][agent]['listings'][listing] = {
                    'price': fake.ean8(),
                    'rent': fake.postalcode(),
                    'properties': {'real_estate_type': real_estates, 'apartment_level': level, 'size': size,
                    'area': fake.random_element(area), 'environment': fake.random_elements(elements=environment, unique=True),
                    'balcony': fake.boolean(chance_of_getting_true=80), 'garden': fake.boolean(chance_of_getting_true=50), 
                    'pool': fake.boolean(chance_of_getting_true=70), 'rent_out': fake.boolean(chance_of_getting_true=50)
                }}

    fake.random.seed(5467)

    for i in range(20):
        
        real_estates = fake.random_elements(elements=real_estate_types, unique=True)
        size = fake.random_int(min=50, max=60, step=1)

        if 'Apartment' in real_estate_types:
            level = fake.random_elements(elements=apartment_level, unique=True)
        else:
            level = None

        user_name = fake.name()
        budget = fake.ean8()
        upkeep = fake.postalcode()

        data_userform[user_name] = {
            'user_number': fake.phone_number(),
            'user_email': fake.free_email(),
            'budget_min': (float(budget)*0.8),
            'budget_max': (float(budget)*1.2),
            'upkeep_min': (float(upkeep)*0.8),
            'upkeep_max': (float(upkeep)*1.2),
            'properties': {'real_estate_type': real_estates, 'apartment_level': level, 'size_min': (size*0.8),
                    'size_max': (size*1.2), 'area': fake.random_elements(elements=area, unique=True), 
                    'environment': fake.random_elements(elements=environment, unique=True),
                    'balcony': fake.boolean(chance_of_getting_true=80), 'garden': fake.boolean(chance_of_getting_true=50), 
                    'pool': fake.boolean(chance_of_getting_true=70), 'rent_out': fake.boolean(chance_of_getting_true=50)
                }}

    return data, data_userform


def populate_partnerform(data):

    for company in data:

        company_id = Company(name=company, phone_number=data[company]['company_number'], email=data[company]['company_email'])
        
        company_id.save()

        for agent in data[company]['agent_details']:
            
            agent_id = Agent(name=agent, phone_number=data[company]['agent_details'][agent]['agent_number'], 
            email=data[company]['agent_details'][agent]['agent_email'], company=company_id)

            agent_id.save()

            for listing in data[company]['agent_details'][agent]['listings']:
                
                listing_id = ListingItem(name=listing, 
                price=data[company]['agent_details'][agent]['listings'][listing]['price'],
                monthly_cost=data[company]['agent_details'][agent]['listings'][listing]['rent'], agent=agent_id,
                properties=data[company]['agent_details'][agent]['listings'][listing]['properties'])

                listing_id.save()
    
    return
def populate_customerform(cust_data):

    fake = Faker()
    fake.random.seed(1000)
    
    for cust_name in cust_data:
        customer_name = fake.name()

        user_id = User(name=customer_name, phone_number=cust_data[cust_name]['user_number'],
        email=cust_data[cust_name]['user_email'])

        user_id.save()

        userform_id = UserForm(budget_min=cust_data[cust_name]['budget_min'], budget_max=cust_data[cust_name]['budget_max'],
        monthly_cost_min=cust_data[cust_name]['upkeep_min'], monthly_cost_max=cust_data[cust_name]['upkeep_max'],
        properties=cust_data[cust_name]['properties'], user=user_id)

        userform_id.save()

    return

if __name__ == "__main__":
    main()