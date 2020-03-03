import os

class Config:
    api_user = os.getenv('HW_USER')
    api_password = os.getenv('HW_PASSWORD')
    api_url = os.getenv('HW_API_URL', 'https://api.sandbox.hyperwallet.com')
    program_token = os.getenv('HW_PROGRAM_TOKEN')
    user_token = os.getenv('HW_USER_TOKEN')
    cors_origins= os.getenv('HW_DOMAIN_ORIGIN', '*')
    
