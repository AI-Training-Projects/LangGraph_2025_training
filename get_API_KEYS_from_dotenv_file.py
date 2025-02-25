## Get API KEYS from local .env file in project folder.

# USE `dotenv` to load API KEYS from .env file in project root folder
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
SERPAPI_API_KEY = os.getenv('SERPAPI_API_KEY')
TAVILY_API_KEY = os.getenv('TAVILY_API_KEY')
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
LANGSMITH_API_KEY = os.getenv("LANGSMITH_API_KEY")