import requests

URL= 'https://api.pokemonbattle.ru/v2' 
TOKEN= '24608585cc6559c066a5ff9f9ad01501'
HEADER= {'Content-Type': 'application/json', 'trainer_token' :TOKEN }

NEW_NAME = 'PUPS'
TRAINER_ID = 34696
POKEMON_ID = '273618'
# Формирование URL
full_url = f'{URL}/trainers/{TRAINER_ID}/add_pokeball'






body_registration = {
    "trainer_token": TOKEN ,
    "email": "makeeva.ali@yandex.ru",
    "password": "32Opodum"
}

body_confirmation={
    "trainer_token": TOKEN
}

body_create= {
    "name": "Буль",
    "photo_id": 1
}
body_update = {
    "pokemon_id": POKEMON_ID,
    "name": NEW_NAME,
    "photo_id": 1
}



'''response=requests.post(url= f'{URL}/trainers/reg', headers= HEADER ,json= body_registration )
print(response.text)'''


'''response_confirmation= requests.post(url= f'{URL}/trainers/confirm_email',headers= HEADER ,json= body_create )
print(response_confirmation.text)'''

'''response_create=requests.post(url= f'{URL}/pokemons',headers= HEADER ,json= body_create )
print(response_create.text)'''

'''pokenon_id= response_create.json() ['id']
print(pokenon_id)'''




'''response = requests.put(url= f'{URL}/pokemons', headers=HEADER, json=body_data)

if response.status_code == 200:
    print("Имя покемона успешно обновлено.")
    print(response.json())
else:
    print(f"Ошибка: {response.status_code}")
    print(response.text)'''



data = {"pokemon_id": POKEMON_ID}

# Выполнение POST-запроса
response = requests.post(
    url=f'{URL}/trainers/add_pokeball',
    headers=HEADER,
    json=data
)

# Проверка результата
if response.status_code == 200:
    print("Покемон пойман в покебол!")
    print(response.json())
else:
    print(f"Ошибка при поимке покемона: {response.status_code}")
    print(response.text)