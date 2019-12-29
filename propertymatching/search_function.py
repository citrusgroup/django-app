from django.test import TestCase
from propertymatching.models import Company, Agent, ListingItem, User, UserForm
from django.db import connection
from operator import eq

# Create your tests here.
def main():

    data_dict = search_test()

    #for i in data_dict['listing_results']:
        #for j in data_dict['listing_results'][i]['listing_envs']:
            #print(data_dict['listing_results'][i]['listing_envs'][j])
    matches(data_dict)

def search_test():

    query = queries()

    with connection.cursor() as cursor:
        cursor.execute(query[1])
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
            'listing_area': [row[5]],
            'listing_envs': string_fixer(row[6])
        }

        data_dict['user_results'][matching_no] = {
            'user_id': row[7],
            'user_min_budget': row[8],
            'user_max_budget': row[9],
            'user_min_month_cost': row[10],
            'user_max_month_cost': row[11],
            'user_properties': row[12],
            'user_areas': string_fixer(row[13]),
            'user_envs': string_fixer(row[14])
        }
        matching_no +=1    

    return data_dict

def matches(data_dict):

    matching_dict = {}
    matches = 1
    for entry in data_dict['listing_results']:
        area_listing = data_dict['listing_results'][entry]['listing_area']
        user_areas = data_dict['user_results'][entry]['user_areas']

        env_listing = data_dict['listing_results'][entry]['listing_envs']
        env_user = data_dict['user_results'][entry]['user_envs']

        if any(elm in user_areas for elm in area_listing):

            user_envs = len(env_user)
            listing_envs = len(env_listing)

            env_matching = 0
            for i in env_user:
                for j in env_listing:
                    if i==j:
                        env_matching +=1
            if (env_matching/user_envs)*100>=80:
                print(data_dict['listing_results'][entry])
                print(data_dict['user_results'][entry])

                matches += 1

    print('total matches: ', matches)
    return 

def queries():

    search_light = """SELECT
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

    search_medium ="""SELECT
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
            AND user_details.properties -> 'pool' = listings.properties -> 'pool'
            AND user_details.properties -> 'garden' = listings.properties -> 'garden'
            AND user_details.properties -> 'balcony' = listings.properties -> 'balcony'
            AND user_details.properties -> 'rent_out' = listings.properties -> 'rent_out'
            
        ORDER BY
            user_id"""

    return search_light, search_medium

def string_fixer(entity):
    rem_01 = entity.strip('[]')
    rem_02 = rem_01.replace('"', '')
    rem_03 = rem_02.replace(' ', '')
    rem_04 = rem_03.split(',')
    return rem_04
if __name__== "__main__":
    main()