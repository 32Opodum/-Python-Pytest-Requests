import requests
import pytest

URL= 'https://api.pokemonbattle.ru/v2' 
TOKEN= '24608585cc6559c066a5ff9f9ad01501'
HEADER= {'Content-Type': 'application/json', 'trainer_token' :TOKEN }
TRENER_ID='34696'



def test_status_code():
    response=requests.get(url= f'{URL}/pokemons', params={'trainer_id': TRENER_ID})
    assert response.status_code == 200

def test_part_of_response():
    response_get = requests.get(url= f'{URL}/pokemons', params={'trainer_id': TRENER_ID})
    assert response_get.json()["data"][0]["name"] == 'Буль'

@pytest.mark.parametrize('key, value', [('name', 'Буль'),('trainer_id', TRENER_ID)])
def test_parametrize(key, value):
    response_parametrize = requests.get(url=f'{URL}/pokemons', params={'trainer_id': TRENER_ID})
    assert response_parametrize.json()["data"][0][key] == value


