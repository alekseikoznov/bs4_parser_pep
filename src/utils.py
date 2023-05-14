import logging

from requests import RequestException
from exceptions import ParserFindTagException

from constants import EXPECTED_STATUS


def get_response(session, url):
    try:
        response = session.get(url)
        response.encoding = 'utf-8'
        return response
    except RequestException:
        logging.exception(
            f'Возникла ошибка при загрузке страницы {url}',
            stack_info=True
        )


def find_tag(soup, tag, attrs=None):
    searched_tag = soup.find(tag, attrs=(attrs or {}))
    if searched_tag is None:
        error_msg = f'Не найден тег {tag} {attrs}'
        logging.error(error_msg, stack_info=True)
        raise ParserFindTagException(error_msg)
    return searched_tag


def find_status(key):
    try:
        preview_status = EXPECTED_STATUS[key]
    except KeyError:
        preview_status = ('Unexpected', )
        logging.exception(
            f'Возникла ошибка при поиске статуса {key}',
            stack_info=True
        )
    return preview_status
