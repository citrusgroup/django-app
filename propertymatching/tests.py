from django.test import TestCase
from propertymatching.models import Company, Agent, ListingItem, User, UserForm
from django.db import connection

# Create your tests here.
def main():

    data_dict = search_test()

    for i in data_dict['listing_results']:
        print(data_dict['listing_results'][i])
        print(data_dict['user_results'][i])
        print('\n')

    email_ready(data_dict)

def search_test():

    query = queries()

    with connection.cursor() as cursor:
        cursor.execute(query)
        data = cursor.fetchall()

    data_dict = {'listing_results': {}, 'user_results': {}}
    matching_no = 1
    for row in data:
        data_dict['listing_results'][matching_no] = {
            'listing_id': row[0],
            'listing_name': row[1],
            'listing_price': row[2],
            'listing_month_cost': row[3],
            'listing_properties': row[4],
            'listing_area': row[5],
            'listing_envs': row[6]
        }

        data_dict['user_results'][matching_no] = {
            'user_id': row[7],
            'user_min_budget': row[8],
            'user_max_budget': row[9],
            'user_min_month_cost': row[10],
            'user_max_month_cost': row[11],
            'user_properties': row[12],
            'user_areas': row[13],
            'user_envs': row[14]
        }
        matching_no +=1    

    return data_dict

def email_ready(data_dict):

    email_ready = {}

    for entry in data_dict:
        


    return 

def queries():

    search_query = """SELECT
	--property listings results
	listings.id as listing_id,
	listings.name as listing_name,
	listings.price as listing_price,
	listings.monthly_cost as listing_month_cost,
	listings.properties as listing_properties,
	listings.properties ->> 'area' as listing_area,
	listings.properties ->> 'environment' as listing_envs,
	--user requirements results
	user_details.id as user_id,
	user_details.budget_min as user_min_budget,
	user_details.budget_max as user_max_budget,
	user_details.monthly_cost_min as user_min_month_cost,
	user_details.monthly_cost_max as user_max_month_cost,
	user_details.properties as user_properties,
	user_details.properties ->> 'area' as user_areas,
	user_details.properties ->> 'environment' as user_envs
FROM
	propertymatching_userform AS user_details
	JOIN propertymatching_listingitem AS listings ON user_details.budget_max >= listings.price
		AND user_details.budget_min <= listings.price
		AND listings.monthly_cost BETWEEN user_details.monthly_cost_min AND user_details.monthly_cost_max
		
ORDER BY
	user_id"""

    return search_query

if __name__== "__main__":
    main()