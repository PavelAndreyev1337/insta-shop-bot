from instapy import InstaPy, smart_run
from typing import List


class PromotionService:
    def __init__(self, session: InstaPy,
                 shop_name: str,
                 message: str,
                 locations: List[str],
                 amount: int = 1):
        self.__session = session
        self.__shop_name = shop_name
        self.__message = message
        self.__locations = locations
        self.__amount = amount

    def __define_interaction(self):
        self.__session.set_do_like(enabled=True)
        self.__session.set_do_comment(enabled=True)
        self.__session.set_comments([self.__message])
        self.__session.set_do_story(enabled=True)
        self.__session.set_user_interact(
            amount=self.__amount,
            randomize=True,
            media='Photo'
        )
        self.__session.set_user_interact(
            amount=self.__amount,
            randomize=True,
            media='Video'
        )
        self.__session.set_skip_users(
            skip_private=True,
            skip_business=True,
        )

    def __like(self, location: str):
        self.__session.like_by_locations(
            [location],
            amount=self.__amount,
            skip_top_posts=True,
            randomize=True
        )

    def __follow(self, location: str):
        self.__session.follow_by_locations(
            [location],
            amount=self.__amount,
            skip_top_posts=False,
        )

    def __add_comment(self, location: str):
        self.__session.comment_by_locations(
            [location],
            amount=self.__amount,
            skip_top_posts=False
        )
        self.__session.join_pods(topic='fashion')

    def start(self):
        with smart_run(self.__session, threaded=True):
            self.__define_interaction()
            for location in self.__locations:
                self.__like(location)
                self.__follow(location)
                self.__add_comment(location)
        return self
