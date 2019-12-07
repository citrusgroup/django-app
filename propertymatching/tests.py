from django.test import TestCase
from propertymatching.models import Company, Agent, ListingItem, User, UserForm

# Create your tests here.
def main():

    search_test()

#### search function testing, see read me file in Django-app for details
def search_test():

    user_form_entries = User.objects.filter(UserForm__user_id=1).values()

    return user_form_entries

if __name__== "__main__":
    main()