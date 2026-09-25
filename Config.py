from google import genai
import os


def getkey():
    '''
    This function  returns the key
    '''
    return os.environ['google_api_key']
