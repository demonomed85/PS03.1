from bs4 import BeautifulSoup
import requests
from googletrans import Translator

translator = Translator()
def get_eng_words():
    url = 'https://randomword.com/'
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        eng_word = soup.find('div', id='random_word').text.strip()
        eng_discription = soup.find('div', id='random_word_definition').text.strip()
        return {
            'eng_words': eng_word,
            'eng_discription': eng_discription
        }

    except requests.HTTPError: print('HTTPError')
    except requests.ConnectionError: print('ConnectionError')
    except requests.Timeout: print('Timeout')
    except requests.RequestException: print('RequestException')
    except: print("Unexpected error:", sys.exc_info()[0])


def game():
  while True:
    print("Добро пожаловать в игру")
    eng_words = get_eng_words()
    eng_word = eng_words.get('eng_words')
    ru_word = translator.translate(eng_word, src='en', dest='ru').text
    eng_discription = eng_words.get('eng_discription')
    ru_discription = translator.translate(eng_discription, src='en', dest='ru').text
    print(f"Угадай слово по описанию: {ru_discription}")
    user_answer = input("Ваш ответ: ")

    if user_answer == eng_word:
        print("Правильно")
    else:
        print(f"Неправильно. Правильное слово: {ru_word}")

    if input("Хотите сыграть еще? (y/n):") != "y":
        break

game()