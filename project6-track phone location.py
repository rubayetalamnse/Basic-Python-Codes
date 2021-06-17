from sys import path_importer_cache
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
my_phone_number= phonenumbers.parse("+8801608635997")
print(my_phone_number)
print(geocoder.description_for_number(my_phone_number,'en'))
print(carrier.name_for_number(my_phone_number,'en'))
mom_phone_number =phonenumbers.parse("+7 495 772 95 90 ")
print(geocoder.description_for_number(mom_phone_number,'en'))



