def build_prompt(prompt:str, role:str, tag:str='') -> dict:
    return {'role': role, 'content': f'<{tag}>{prompt}</{tag}>' if tag else prompt}

def update_history(history:list[dict], msg:str, role:str):
    history.append(build_prompt(prompt=msg, role=role))


class ChatHistory(list): # allow all list methods to be applied to ChatHistory instances.
    def __init__(self, messages:list[dict]|None=None, total_length:int=-1):
        if messages is None:
            messages = []
        
        super().__init__(messages)
        self.total_length = total_length

    def append(self, msg:str):
        # Soft limit model context and ensure response generation speed.
        if len(self) == self.total_length:
            self.pop(0)
        super().append(msg)


class FixedFirstChatHistory(ChatHistory):
    def __init__(self, messages:list[dict]|None=None, total_length:int=-1):
        super().__init__(messages, total_length)
    
    def append(self, msg:str):
        if len(self) == self.total_length:
            self.pop(1)
        super().append(msg)
