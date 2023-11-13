import os
import requests

ENDPOINT = 'http://127.0.0.1:8000/api/v1/songs/1'
# HEADERS = {'Authorization': f'OAuth {PRACTICUM_TOKEN}'}
BOOK_PATH = 'book/book.txt'
PAGE_SIZE = 1050

book: dict[int, str] = {}


# Функция, возвращающая строку с текстом страницы и ее размер
def _get_part_text(text, start, page_size):
    symbols = [',', '.', '!', ':', ';', '?']
    end = start+page_size
    if end > len(text):
        end = len(text)
        return text[start:end], len(text[start:end])
    if len(text) == page_size and text[-1] in symbols:
        return text, page_size
    for i in reversed(range(start, end)):
        if text[i] in symbols and text[i+1] not in symbols and (
                                        i+1 - start <= page_size):
            return text[start:i+1], i-start+1


# Функция, формирующая словарь книги
def prepare_book(path: str) -> None:
    request_params = {
            'url': ENDPOINT,
        }
    response = requests.get(**request_params)
    response = response.json()
    text = response['text']
    print(text)
    START = 0
    i = 0
    end = 0
    while START < len(text) - 1:
        i += 1
        book[i] = _get_part_text(text, START, PAGE_SIZE)[0].lstrip()
        end = _get_part_text(text, START, PAGE_SIZE)[1]
        START += end


# Вызов функции prepare_book для подготовки книги из текстового файла
prepare_book(os.path.join(os.getcwd(), BOOK_PATH))
