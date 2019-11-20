from propertymatching.models import Company 
from propertymatching.models import Agent
from propertymatching.models import Listing_item
from faker import Faker

fake = Faker()


def main():
    
def pop_randomiser():

    data = {}

    entries = input("enter number of entries to be written: ")
    loops = range(int(entries))
    seeds = fake.seeds(20)

    fake.company()
    for i in loops:
        name_company = fake.company()
        number_phone = fake.phone_number()
        email_company = 


    for i in loops:
        print(fake.name())



def populate(data):
    seeds = 
    Listing_item.objects.create(listing_name='', price='', monthly_cost='', properties ='')

    Agent.objects.create(agent_name='', phone_number='', agent_email='')

    Company.objects.create(company_name='', phone_number='', company_email='')
    
    

    return 'populated!'

if __name__ == "__main__":
    main()