import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from form_source import email_source

def mail_exec():

    match_data = email_source()
    
    
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

