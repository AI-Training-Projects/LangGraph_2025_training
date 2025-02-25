import os
from dotenv import load_dotenv
from pathlib import Path
from typing import Dict, Optional

def load_api_keys() -> Dict[str, Optional[str]]:
    """
    Load API keys from local .env file in project root directory
    Returns a dictionary of API keys
    """
    
    # # Get the project root directory (2 levels up from current notebook)
    # # This is used for .py files, not inside Jupyter NBs.
    # project_root = Path(__file__).resolve().parent.parent
    # env_path = project_root / '.env'
    

    # Alternative path resolution for Jupyter notebooks
    project_root = Path(os.getcwd()).parent
    env_path = project_root / '.env'


    # Load environment variables from specific .env file
    if not env_path.exists():
        raise FileNotFoundError(f".env file not found at {env_path}")
    
    load_dotenv(dotenv_path=env_path)
    
    # Dictionary to store API keys
    api_keys = {
        'OPENAI_API_KEY': os.getenv('OPENAI_API_KEY'),
        'SERPAPI_API_KEY': os.getenv('SERPAPI_API_KEY'),
        'PINECONE_API_KEY': os.getenv('PINECONE_API_KEY'),
        'TAVILY_API_KEY': os.getenv('TAVILY_API_KEY'),
        'GOOGLE_API_KEY': os.getenv('GOOGLE_API_KEY'),
        'LANGSMITH_API_KEY': os.getenv("LANGSMITH_API_KEY"),
        'TEST_API_KEY': os.getenv('TEST_API_KEY'),
        # Add other API keys as needed
    }
    
    # Validate required keys
    missing_keys = [k for k, v in api_keys.items() if v is None]
    if missing_keys:
        print(f"Warning: Missing API keys: {', '.join(missing_keys)}")
        
    return api_keys


# Usage Example: 
# API_KEYS_Dict = load_api_keys()