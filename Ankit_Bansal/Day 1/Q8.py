first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
company_name = input("Enter your company name: ")

## Extract the required portions for the email alias
Alias_First_name= first_name[:2].lower()
Alias_second_name= last_name[-3:].lower()

email_alias = Alias_First_name + Alias_second_name + "@" + company_name.lower() + ".com"
print("Email alias:", email_alias)

