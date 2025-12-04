# Simple Mesa-LLM Tutorial Example

This tutorial introduces Mesa-LLM using a minimal, console-based example:
a single LLM-powered agent running in a very small Mesa model.

The goal is to give new users a fast, end-to-end path:

1. Install dependencies  
2. Configure an API key  
3. Run a working example  
4. Understand what the code is doing  

---

## 1. Installation

Make sure `mesa`, `mesa-llm`, and supporting packages are installed in your environment:

```bash
pip install mesa mesa-llm "mesa[rec]" python-dotenv
