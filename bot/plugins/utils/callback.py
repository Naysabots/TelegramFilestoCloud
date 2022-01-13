from logging import fatal
from ...filetocloud import CloudBot
from pyrogram.types import CallbackQuery
from ...helpers import download_media
from ...helpers.servers import upload_handler


@CloudBot.on_callback_query()
async def selecting_server(client: CloudBot, message: CallbackQuery) -> None:
    callback_data = message.data
    if callback_data.startswith('transfersh'):
        await upload_handler(client, message, callback_data)
    elif callback_data.startswith('fileio'):
        await upload_handler(client, message, callback_data)
    elif callback_data.startswith('gofileio'):
        await upload_handler(client, message, callback_data)
    elif callback_data.startswith('anonyfiles'):
        await upload_handler(client, message, callback_data)
    elif callback_data.startswith('mixdrop'):
        await upload_handler(client, message, callback_data)
    elif callback_data.startswith('ufile'):
        await upload_handler(client, message, callback_data)
    elif callback_data.startswith('tninja'):
        await upload_handler(client, message, callback_data
    elif callback_data.startswith('bayfiles'):
        await upload_handler(client, message, callback_data
