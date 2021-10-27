from dotenv import load_dotenv
from application import Application


if __name__ == "__main__":
    load_dotenv()  # load .env from root folder
    Application().start_promotion()
