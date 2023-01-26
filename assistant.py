import os
import openai
import sys
from sr import listen
from tts import speak

# Load your API key from an environment variable or secret management service
openai.api_key = os.getenv("OPENAI_API_KEY")

def run():
    query = listen()
    response = openai.Completion.create(model="text-davinci-003", prompt="You are a very intelligent voice assistant. Respond to this query: " + query, temperature=0, max_tokens=3000)
    speak(response.choices[0].text)

if __name__ == "__main__":
    while True:
        try:
            # Wait for sparcebar to be pressed
            print("Press return to start the assistant")
            input()

            # Run the assistant
            run()

        except KeyboardInterrupt:
            print("\nLater nerd!")
            sys.exit(0)
