#take email adress from a user
email = input("enter your email adress here: ").strip()
#strip() function removes any extra space 
username= email[0:email.index('@')]
domain_name=email[email.index('@')+1:]

slice_result = "username = {0}, domain name ={1}".format(username,domain_name)

print(slice_result)