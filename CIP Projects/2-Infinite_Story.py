import json
from ai import call_gpt

def main():
    story_data = json.load(open('data/original_small.json'))
    print(type(story_data))

def process_response(response):
    """Converts a `call_gpt` JSON response string into a Python dictionary.""" 
    if response.startswith("```json"):
        # Remove triple ticks at the start and end of the string.
        return json.loads(response[7:-3])
    return json.loads(response)

if __name__ == "__main__":
    main()
  
