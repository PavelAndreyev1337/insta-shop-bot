from instapy import InstaPy, smart_run
from typing import List


class PromotionService:
    def __init__(self, session: InstaPy,
                 shop_name: str,
                 message: str,
                 locations: List[str]):
        self.__session = session
        self.__shop_name = shop_name
        self.__message = message
        self.__locations = locations

    def __define_interaction(self):
        self.__session.set_do_like(enabled=True)
        self.__session.set_do_comment(enabled=True)
        self.__session.set_comments([self.__message])
        self.__session.set_do_story(enabled=True)
        self.__session.set_user_interact(
            amount=4,
            randomize=True,
            media='Photo'
        )
        self.__session.set_user_interact(
            amount=3,
            randomize=True,
            media='Video'
        )
        self.__session.set_skip_users(
            skip_private=True,
            skip_business=True,
        )

    def __like(self, amount: int):
        self.__session.like_by_locations(
            self.__locations,
            amount=amount,
            skip_top_posts=True,
            randomize=True
        )

    def __follow(self, amount: int, skip_top_posts: bool, randomize: bool):
        self.__session.follow_by_locations(
            self.__locations,
            amount=10,
            skip_top_posts=skip_top_posts,
        )

    def __add_comment(self, amount: int):
        self.__session.comment_by_locations(
            self.__locations,
            amount=amount,
            skip_top_posts=False
        )

    def start(self, amount: int = 10, skip_top_posts: bool = False, randomize: bool = True):
        with smart_run(self.__session, threaded=True):
            self.__define_interaction()
            self.__like(amount)
            self.__follow(amount, skip_top_posts, randomize)
            self.__add_comment(amount)
        return self
