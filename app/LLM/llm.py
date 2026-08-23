import requests

OLLAMA_RUL = "http://localhost:11434/api/generate"

MODEL_NAME ="qwen3:8b"

def generate_answer(prompt):
    response = requests.post(
        OLLAMA_RUL,
        json = {
            "model":MODEL_NAME,
            "prompt":prompt,
            "stream": False
        }
    )

    response.raise_for_status()

    data = response.json()

    return data['response']