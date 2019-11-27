from propertymatching.models import Company, Agent, ListingItem
from faker import Faker


def main():
    
    random_data = pop_randomiser()

    populate_partnerform()(random_data)

def pop_randomiser():

    data = {}
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

                data[company]['agent_details'][agent]['listings'][listing] = {
                    'price': fake.ean8(),
                    'rent': fake.postalcode(),
                    'properties': fake.words(nb=15, ext_word_list=None, unique=False)
                }

    return data

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
    
    

    return 'Partner Form populated!'

if __name__ == "__main__":
    main()