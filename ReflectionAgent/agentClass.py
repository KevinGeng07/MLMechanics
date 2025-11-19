### Remixed from https://github.com/neural-maze/agentic-patterns-course/blob/main/src/agentic_patterns/reflection_pattern/reflection_agent.py.
### TODO: CLEAN THIS CODE BY A LOT.
from dotenv import load_dotenv
from groq import Groq
from agentClassUtils import *
from time import time
load_dotenv()

GEN_SYS_PROMPT = """
    You are a machine learning engineer tasked with teaching the user about LLM context limits.
    Your task is to generate the best content possible for the user\'s request. If the user provides critique,
    respond with a revised version of your previous attempt.
"""

REF_SYS_PROMPT = """
    You are an experienced machine learning engineer who has previously directed at many top AI companies (think OpenAI, MoonshotAI, Baidu, etc). You are tasked with constructively criticizing
    the provided response and citations, ensuring the model is summarizing real, credible papers and producing a response that audiences in industry can interpret without fail.
"""

class ReflectionAgent:
    def __init__(self, model:str='llama-3.3-70b-versatile'):
        self.client = Groq()
        self.model = model

    def _request_completion(self, history:list, log_title:str='COMPLETION', log_color:str=''):
        response = self.client.chat.completions.create(messages=history, model=self.model)
        return str(response.choices[0].message.content)
    
    def generate(self, gen_history:list[dict]) -> str:
        response = self.client.chat.completions.create(messages=gen_history, model=self.model)
        return str(response.choices[0].message.content)

    def reflect(self, ref_history:list[dict]) -> str:
        response = self.client.chat.completions.create(messages=ref_history, model=self.model)
        return str(response.choices[0].message.content)

    def run(self, user_msg:str, gen_sys_prompt:str='', ref_sys_prompt:str='', steps=10) -> str:
        gen_sys_prompt = GEN_SYS_PROMPT
        ref_sys_prompt = REF_SYS_PROMPT

        t_start = time()

        gen_history = FixedFirstChatHistory(
            [
                build_prompt(prompt=gen_sys_prompt, role='system'),
                build_prompt(prompt=user_msg, role='user')
            ],
            total_length=3
        )

        ref_history = FixedFirstChatHistory(
            [build_prompt(prompt=ref_sys_prompt, role='system')],
            total_length=3
        )
        print(f'Iteration 1 complete. Time Elapsed: {time() - t_start}')

        for i in range(steps-1):
            t_start = time()
            generation = self.generate(gen_history)
            update_history(gen_history, generation, 'assistant')
            update_history(ref_history, generation, 'user')

            critique = self.reflect(ref_history)

            update_history(gen_history, critique, 'user')
            update_history(ref_history, critique, 'assistant')

            print(f'Iteration {i + 2} complete. Time Elapsed: {time() - t_start}')
        
        return generation
    

if __name__ == '__main__':
    # agent = Groq()
    agent = ReflectionAgent()
    print(agent.run('Evaluate the levels of model hallucinations and proposed their solutions. DO NOT CITE ANY PAPERS.'))
