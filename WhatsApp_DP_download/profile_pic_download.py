# region IMPORTS
from pathlib import Path

from wplay.utils import browser_config
from wplay.utils import target_search
from wplay.utils import target_select
from wplay.utils.helpers import profile_photos_path
from wplay.utils.helpers import whatsapp_selectors_dict
from wplay.utils.Logger import Logger
# endregion


# region LOGGER
__logger = Logger(Path(__file__).name)
# endregion


async def get_profile_picture(target):
    page, _ = await browser_config.configure_browser_and_load_whatsapp()

    if target is not None:
        try:
            await target_search.search_and_select_target(page, target)
        except Exception as e:
            print(e)
            await page.reload()
            await target_search.search_and_select_target_without_new_chat_button(page, target)
    else:
        target = await target_select.manual_select_target(page)
    # Getting Profile picture url
    selector = '#main > header > div > div > img'
    await page.waitForSelector(selector, timeout=2000)
    image_url = await page.evaluate(f'document.querySelector("{selector}").getAttribute("src")')
    try:
        viewSource = await page.goto(image_url)
        f = open(profile_photos_path / f'{target}.jpg', 'wb')
        f.write(await viewSource.buffer())
        f.close()
    except Exception as e:
        print("Error saving image")
