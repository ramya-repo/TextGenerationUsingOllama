#this is a sample notes. can be replaced to actual content.
import requests
import json

def summarize_meeting_notes(notes):
    ollama_url = 'http://localhost:11434/api/generate'
    model_name = 'llama3.1:latest'  # Replace with the actual model name
    prompt = f"Based on the following meeting notes and business requirement discussions, write detailed functional specifications and user stories: {notes}"
    response = requests.post(ollama_url, json={'model': model_name, 'prompt': prompt}, stream=True)

    if response.status_code == 200:
        functional_specifications = ""
        for line in response.iter_lines():
            if line:
                try:
                    line_json = json.loads(line.decode('utf-8'))
                    token = line_json.get('response', '')
                    functional_specifications += token
                    #print(token, end='', flush=True)
                    print(token, end='', flush=True)
                except json.JSONDecodeError as e:
                    print(f"Failed to decode JSON: {e}")
        return functional_specifications

    else:
        print(f"Failed to connect to Ollama. Status code: {response.status_code}")
        return(response.content)

#summarize_meeting_notes("TESTING")