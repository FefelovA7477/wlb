import requests
from typing import Dict, Any

from .constants import TG_BOT_TOKEN, NOTIFICATION_MSG_TEXT, NOTIFICATION_BTN_TEXT

def send_notification_tg(chat_id: int | str) -> None:
    keyboard = _get_notiifcation_keyboard()
    try:
        send_msg_tg(chat_id=chat_id,
                    text=NOTIFICATION_MSG_TEXT,
                    keyboard=keyboard)
    except requests.exceptions.HTTPError:
        raise


def _get_notiifcation_keyboard() -> Dict[str, Any]:
    return {
        'reply_markup': {
            'inline_keyboard':[[{
                "text": NOTIFICATION_BTN_TEXT, 
                "callback_data": "start_save_scores"
            }]]
        }
    }


def send_msg_tg(chat_id: int | str, text: str, keyboard: Dict[str, Any] = None) -> None:
    url = f'https://api.telegram.org/bot{TG_BOT_TOKEN}/sendMessage'
    data = {
        'chat_id': chat_id,
        'text': text,
        'keyboard': keyboard
    }
    response = requests.post(url=url, json=data)
    if not response.ok:
        raise requests.exceptions.HTTPError(f'TgSendMessage failed. Reason - {response.text}')
    
    