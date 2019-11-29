from django.test import TestCase
from propertymatching.models import Company, Agent, ListingItem, User, UserForm

# Create your tests here.

def main():

    search_test()


def search_test():

    user_form_entries = UserForm.objects.filter(user_id=1)

    print(user_form_entries)



if __name__== "__main__":
    main()