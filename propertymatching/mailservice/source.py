from propertymatching.models import Company, Agent, ListingItem, User, UserForm, FormMatches
from django.db import connection

def email_source():

    match_list = source_matches()
    email_reqs = {}
    for match in match_list:
        if match_list[match]['email_sent'] == False:
            customer = source_user(match_list[match]['userform_id'])
            listing = source_listing(match_list[match]['listing_id'])
            agent = source_agent(listing['agent_id'])
            company = source_company(agent['company_id'])

            email_reqs[match] = {
                'customer': customer,
                'listing': listing,
                'agent': agent,
                'company': company
            }

    return email_reqs

def source_matches():

    match_ids = """select * from propertymatching_formmatches"""

    with connection.cursor() as cursor:
        cursor.execute(match_ids)
        form_matches = cursor.fetchall()

    match_dict = {}

    for row in form_matches:
        match_dict[row[0]] = {
            'email_sent': row[1],
            'created_at': row[2],
            'listing_id': row[3],
            'userform_id': row[4]
        }

    return match_dict

def source_user(userform_id):

    cust_details = """SELECT
	propertymatching_user.name as customer_name,
	propertymatching_user.phone_number as phone,
	propertymatching_user.email as email
    FROM
	propertymatching_user
    WHERE
	propertymatching_user.id in(
	SELECT
    user_id FROM propertymatching_userform
    WHERE
    propertymatching_userform.id = %s)""" %(userform_id)

    with connection.cursor() as cursor:
        cursor.execute(cust_details)

        data = cursor.fetchall()

    for row in data:
        customer = {
            'name': row[0],
            'phone': row[1],
            'email': row[2]
        }

    return customer

def source_listing(listing_id):

    listing_details = """SELECT
	propertymatching_listingitem.name AS listing_address,
	propertymatching_listingitem.price as listing_price,
	propertymatching_listingitem.monthly_cost as upkeep,
	propertymatching_listingitem.properties as details,
	propertymatching_listingitem.agent_id as agent
    FROM
	propertymatching_listingitem
    WHERE
	id = %s""" %(listing_id)

    with connection.cursor() as cursor:
        cursor.execute(listing_details)
        data = cursor.fetchall()
    
    for row in data:
        listing = {
            'listing_address': row[0],
            'listing_price': row[1],
            'upkeep': row[2],
            'details': row[3],
            'agent_id': row[4]
        }
    return listing

def source_agent(agent_id):

    agent_details = """SELECT
	propertymatching_agent.name AS agent_name,
	propertymatching_agent.phone_number AS phone,
	propertymatching_agent.email AS email,
	propertymatching_agent.company_id AS company_id
    FROM
	propertymatching_agent
    WHERE
	id = %s""" %(agent_id)

    with connection.cursor() as cursor:
        cursor.execute(agent_details)
        data = cursor.fetchall()

    for row in data:
        agent = {
            'agent_name': row[0],
            'phone': row[1],
            'email': row[2],
            'company_id': row[3]
        }

    return agent

def source_company(company_id):

    company_details = """SELECT
    propertymatching_company.name AS Company,
    propertymatching_company.phone_number AS phone,
    propertymatching_company.email AS email
    FROM
    propertymatching_company
    WHERE
    id = %s""" %(company_id)

    with connection.cursor() as cursor:
        cursor.execute(company_details)
        data = cursor.fetchall()

    for row in data:
        company = {
            'company': row[0],
            'phone': row[1],
            'email': row[2]
        }

    return company

def source_update_matchform():

    return
