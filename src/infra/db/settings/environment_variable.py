import os

import dotenv

dotenv.load_dotenv()

DATABASE_STRING = "postgresql+psycopg2://{}:{}@{}:{}/{}".format(
    os.environ["DATABASE_USER"],
    os.environ["DATABASE_PASSWORD"],
    os.environ["DATABASE_HOST"],
    os.environ["DATABASE_PORT"],
    os.environ["DATABASE_NAME"],
)