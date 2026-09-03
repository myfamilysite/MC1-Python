#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Create a superclass called Account with a method called account_type
class Account:
    def account_type(self):
        return "Some account type"

# Create a subclass called SavingsAccount
class SavingsAccount(Account):
    def account_type(self):
        # Override the method for SavingsAccount
        return "Savings Account"       

# Create a subclass called CheckingAccount
class CheckingAccount(Account):
    def account_type(self):
        # Override the method for CheckingAccount
        return "Checking Account"       

# Call the functions
my_savings = SavingsAccount()
print(my_savings.account_type())

my_checking = CheckingAccount()
print(my_checking.account_type())

