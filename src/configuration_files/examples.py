import os
from dotenv import load_dotenv, dotenv_values

# access envi vars by using the os.environ
# print(os.environ)

# access an env var - raise an exception if the key does not exist
print(os.environ["USER"])

# get() method is best practice
print(os.environ.get("DATABASE_URL"))

# add default value for missing var that is not None
database_url = os.environ.get("DATABASE_URL", "sqlite:///")

# getenv() === os.environ.get()
user = os.getenv("USER")
database_url = os.getenv('DATABASE_URL', 'sqlite://')  # set default for missing vars

config = dotenv_values('.env.staging')
print(config['BASE_URL'])


print(os.getenv("BASE_URL"))



