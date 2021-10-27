from instapy import InstaPy, smart_run
from typing import List


class PromotionService:
    def __init__(self, session: InstaPy,
                 shop_name: str,
                 message: str,
                 locations: List[str],
                 tags: List[str]):
        self.__session = session
        self.__shop_name = shop_name
        self.__message = message
        self.__locations = locations
        self.__tags = tags

    def __define_interaction(self):
        self.__session.set_do_like(enabled=True, percentage=25)
        self.__session.set_do_comment(enabled=True, percentage=10)
        self.__session.set_comments([self.__message])
        self.__session.set_simulation(enabled=True, percentage=100)
        self.__session.set_do_story(enabled=True, percentage=40, simulate=False)
        self.__session.set_user_interact(
            amount=4,
            percentage=50,
            randomize=True,
            media='Photo'
        )
        self.__session.set_user_interact(
            amount=3,
            percentage=32,
            randomize=True,
            media='Video'
        )
        self.__session.set_skip_users(
            skip_private=True,
            private_percentage=100,
            skip_business=True,
            business_percentage=100
        )

    def __like(self, amount: int):
        self.__session.like_by_tags(self.__tags, amount=amount, interact=True)
        self.__session.like_by_feed(amount=amount, randomize=True, interact=True)
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
        self.__session.follow_by_locations(
            self.__tags,
            amount=10,
            skip_top_posts=skip_top_posts,
        )
        self.__session.follow_user_following(
            [self.__shop_name],
            amount=10,
            randomize=randomize,
            interact=True,
        )
        self.__session.follow_user_followers(
            [self.__shop_name],
            amount=10,
            randomize=randomize,
            interact=True,
        )
        self.__session.follow_likers(
            [self.__shop_name],
            photos_grab_amount=2,
            follow_likers_per_photo=3,
            randomize=randomize,
            sleep_delay=600,
            interact=True,
        )
        self.__session.follow_commenters(
            [self.__shop_name],
            amount=100,
            daysold=365,
            max_pic=100,
            sleep_delay=600,
            interact=True
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
