import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from propertymatching.mailservice import form_source

def mail_exec():



    emails = ['John.holmgren@tmrw.se', 'erikbostrom1@gmail.com', 'magnus.larsen@apoex.se']

    for mail in emails:
        message = Mail(
            from_email = 'sendgrid_email_test@example.com',
            to_emails =mail,
            subject= 'Hello from the Citrus Group Automated email service - please take a ticket',
            html_content='<strong>locked and loaded, watch this space and get excited</strong>')
        print(os.environ.get('SENDGRID_API_KEY'))
        try:
            sg = SendGridAPIClient(api_key='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')

            response = sg.send(message)
            print(mail)
            print(response.status_code)
            print(response.body)
            print(response.headers)
        except Exception as e:
            print(str(e))


def source_mail():
    
    match_data = form_source.email_source()

    for match_no in match_data:
        
        #data on the contact details of the customer
        print(match_no)
        print(match_data[match_no]['customer']['name'])
        print(match_data[match_no]['customer']['phone'])
        print(match_data[match_no]['customer']['email'])

        #data on the listing of the match with aformentioned customer
        print(match_data[match_no]['listing']['listing_address'])
        print(match_data[match_no]['listing']['listing_price'])
        print(match_data[match_no]['listing']['upkeep'])
        print(match_data[match_no]['listing']['details'])
        #print(match_data[match_no]['listing']['environment'])
        #print(match_data[match_no]['listing']['apartment_level'])
        #print(match_data[match_no]['listing']['real_estate_type'])

        #data on the agent details of the match with aformentioned customer
        print(match_data[match_no]['agent']['agent_name'])
        print(match_data[match_no]['agent']['phone'])
        print(match_data[match_no]['agent']['email'])
        
        #data on the compay details of the match with aformentioned customer
        print(match_data[match_no]['company']['company'])
        print(match_data[match_no]['company']['phone'])
        print(match_data[match_no]['company']['email'])
        print('\n')