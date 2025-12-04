# examples/simple_llm_tutorial/agents.py

from mesa_llm.reasoning.react import ReActReasoning


class SimpleLLMAgent:
    """
    Very small 'agent' that uses Mesa-LLM's ReActReasoning directly.
    It is not a Mesa Agent subclass to keep the tutorial simple.
    """

    def __init__(self, unique_id, model):
        self.unique_id = unique_id
        self.model = model
        self.reasoning = None  # created lazily in step()

    def _call_reasoning(self, prompt: str) -> str:
        """
        Call the ReActReasoning object in a way that works with
        different Mesa-LLM versions.
        """
        r = self.reasoning

        # 1) Newer style: dedicated method
        if hasattr(r, "generate_response"):
            return r.generate_response(prompt)

        # 2) Common alt: run()
        if hasattr(r, "run"):
            return r.run(prompt)

        # 3) If it's callable, just call it
        if callable(r):
            return r(prompt)

        # 4) Fallback: at least return something string-like
        return str(r)

    def step(self):
        """
        Ask the LLM for a short, friendly reply and store it in the model.
        """
        # Lazily create reasoning engine, passing this agent instance
        if self.reasoning is None:
            self.reasoning = ReActReasoning(agent=self)

        prompt = (
            "You are a short, friendly AI agent. "
            "Reply in 3–6 words. No punctuation at the end."
        )

        response = self._call_reasoning(prompt).strip()
        print(f"🤖 Agent {self.unique_id}: {response}")
        self.model.history.append(response)
