Reflection Agent

Upon first LLM invocation, the Reflection Agent revisits it's output and critiques it in the context of the system prompt. The agent then regenerates the response with the output and reflection, and presents the updated response to the user. This improves upon an LLM's zero shot prompting by reinforcing the published response.

* Too many iterations dilutes the model's response quality, causing it to create overly safe, rather than objective, responses. *

Paper: (Reflexion: Language Agents with Verbal Reinforcement Learning)[https://arxiv.org/abs/2303.11366]