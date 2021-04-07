import phonenumbers
from phonenumbers import geocoder
pais = str(input('Qual o código do país? ')).strip()
ddd = str(input('Qual o DDD? ')).strip()
tel = str(input('Digite o telefone ')).strip()
phone = '+'+ pais + ddd + tel
phone_number = phonenumbers.parse(phone)
geocode = geocoder.description_for_number(phone_number, 'pt')
print(f'O número citado é de: \033[31m{geocode}\033[m')