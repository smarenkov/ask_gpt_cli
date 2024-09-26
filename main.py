import argparse

from lib.ask_gpt import ask_gpt


def main():
    parser = argparse.ArgumentParser(description="Ask GPT a question.")
    parser.add_argument("question", type=str, help="The question you want to ask GPT.")

    args = parser.parse_args()
    question = args.question
    response = ask_gpt(question)
    print(f"GPT's Response: {response}")


if __name__ == "__main__":
    main()
