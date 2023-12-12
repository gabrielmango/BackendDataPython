import os

import dotenv

dotenv.load_dotenv()

def get_database_string():
    return 'postgresql+psycopg2://{}:{}@{}:{}/{}'.format(
    os.environ["DATABASE_USER"],
    os.environ["DATABASE_PASSWORD"],
    os.environ["DATABASE_HOST"],
    os.environ["DATABASE_PORT"],
    os.environ["DATABASE_NAME"],
)


if __name__ == '__main__':
    print(get_database_string())