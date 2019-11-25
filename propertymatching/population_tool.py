from propertymatching.models import Company 
from propertymatching.models import Agent
from propertymatching.models import Listing_item
from faker import Faker


def main():
    
    pop_randomiser()

def pop_randomiser():

    data = {}
    fake = Faker()

    fake.random.seed(5467)

    for i in range(1):

        company = fake.company()
        print("data line entry")
        print("\n")
        data[company] = {
            'company_number': [fake.phone_number],
            'company_email': [fake.company_email],
            'agent_details': {}
        }

        print("Company Form")
        print(fake.company())
        print(fake.phone_number())
        print(fake.company_email())
        print("\n")
        
        for j in range(1):
            
            agent = fake.name()
            data[company]['agent_details'] = {
                'agent_name': [agent],
                'agent_number': [fake.phone_number()],
                'agent_email': [fake.free_email()],
                'listings': {}
            }
            print("Agent Form")
            print(fake.name())
            print(fake.phone_number())
            print(fake.free_email())

            for k in range(1):
                
                listing = fake.address()

                data[company]['agent_datails']['listings'] = {

                }

                print("\n")
                print("Listing Form")
                print(fake.address())
                print(fake.ean8())
                print(fake.postalcode())
                print(fake.words(nb=15, ext_word_list=None, unique=False))

    return

def populate(data):
    Listing_item.objects.create(listing_name='', price='', monthly_cost='', properties ='')

    Agent.objects.create(agent_name='', phone_number='', agent_email='')

    Company.objects.create(company_name='', phone_number='', company_email='')
    
    

    return 'populated!'

if __name__ == "__main__":
    main()