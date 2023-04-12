import os
import json
import openai
import logging
from datetime import datetime
from tenacity import retry, stop_after_attempt, wait_random_exponential # type: ignore # see https://github.com/openai/openai-cookbook for instructions 

# Configure the logging level for the openai library
logging.getLogger("openai").setLevel(logging.ERROR)

class GPT: 
    
    def __init__(self,openai_api_type,openai_api_base,openai_api_version,openai_api_key,log_dir,engine,system_prompt,temperature): 
        openai.api_type = openai_api_type
        openai.api_base = openai_api_base
        openai.api_version = openai_api_version
        openai.api_key = openai_api_key
        self.log_dir = log_dir
        self.engine = engine
        self.temperature = temperature
        self.chat = [{"role": "system", "content": system_prompt},]

    @retry(wait=wait_random_exponential(min=1, max=60), stop=stop_after_attempt(7))
    def ask(self, question, verbose=False, store_chat_history=True): 
        messages = self.chat + [{"role": "user", "content": question}]
        response = openai.ChatCompletion.create(engine=self.engine, messages=messages, temperature=self.temperature)
        if response['choices'][0]['finish_reason'] != 'stop':
            reply = response['choices'][0]['finish_reason']
        else: 
            reply = response['choices'][0]['message']['content']
        updated_chat = messages + [{"role": "assistant", "content": reply},]
        self.log(updated_chat)
        if store_chat_history: self.chat = updated_chat
        if verbose: print(reply)
        return reply
    
    def log(self, chat): 
        current = datetime.now()
        savepath = self.log_dir+'/'+str(current)+'.txt'
        with open(savepath,'w') as f: 
            f.write(json.dumps(chat))