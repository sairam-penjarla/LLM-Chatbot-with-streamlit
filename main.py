import argparse
from faker import Faker
import random

class Chatbot:
    def __init__(self) -> None:
        self.fake = Faker()

    def __call__(self, prompt: str) -> str:
        response = " ".join([self.fake.sentence() for _ in range(random.randrange(10, 30))])
        return response

chatbot = Chatbot()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("--prompt", type=str, help="The prompt to get a response for")
    args = parser.parse_args()
    prompt = args.prompt
    response = chatbot(prompt)
    print(f"User: {prompt}\nBot: {response}")