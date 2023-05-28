from dotenv import load_dotenv
import os

load_dotenv()

valid_email = os.getenv('valid_email')
valid_password = os.getenv('valid_password')

invalid_email = valid_email