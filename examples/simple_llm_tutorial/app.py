# examples/simple_llm_tutorial/app.py

from dotenv import load_dotenv

# Load environment variables (e.g., OPENAI_API_KEY from .env)
load_dotenv()

import time
import traceback

from examples.simple_llm_tutorial.model import SimpleModel
from examples.simple_llm_tutorial.agents import SimpleLLMAgent


def banner() -> None:
    print("\n" + "=" * 54)
    print("         🧠 Mesa-LLM Simple Tutorial Example")
    print("=" * 54 + "\n")


def main() -> None:
    banner()

    # Create minimal model and one LLM-powered "agent"
    model = SimpleModel()
    agent = SimpleLLMAgent(unique_id=1, model=model)

    for step in range(1, 4):
        print(f"🔄 Step {step}")
        try:
            agent.step()
        except Exception as exc:
            print("❌ Error during agent.step():", exc)
            traceback.print_exc()
            break
        time.sleep(0.7)
        print("-" * 54)

    print("\n📌 Tutorial complete! "
          "Try editing the prompt, number of steps, or adding more agents.\n")


if __name__ == "__main__":
    main()
