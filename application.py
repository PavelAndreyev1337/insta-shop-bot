import os
from instapy import InstaPy
from services.promotion_service import PromotionService
from consts import LOCATIONS, INSTA_SHOP_NAME, MESSAGE


class Application:
    def __init__(self, is_headless_browser: bool = False):
        print(os.getenv('INSTA_USERNAME'))
        self.__session = InstaPy(
            username=os.getenv('INSTA_USERNAME'),
            password=os.getenv('INSTA_PASSWORD'),
            headless_browser=is_headless_browser
        )
        self.__promotion_service = PromotionService(
            self.__session,
            INSTA_SHOP_NAME,
            MESSAGE,
            LOCATIONS
        )

    def start_promotion(self):
        self.__promotion_service.start()
        return self
