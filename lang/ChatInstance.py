import os

from langfuse.callback import CallbackHandler
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate

import private


class ChatInstance:
    
    def __init__(self, template, tools): 
        if "MISTRAL_API_KEY" not in os.environ:
            os.environ["MISTRAL_API_KEY"] = private.mistral_key()

        self.langfuse_handler = CallbackHandler(
            public_key=private.public_key(),
            secret_key=private.private_key(),
            host="https://cloud.langfuse.com"
        )

        self.change_template(template, tools)
        
        self.history = []  


    def ask(self, prompt):
        print(prompt)
        prompt["old_messages"]  = ", ".join(self.history)
        result = self.chain.invoke( prompt, config={"callbacks": [self.langfuse_handler]})
        
        self.history.append("user :"+ prompt["input"])
        self.history.append("you :"+ result.content)
        
        return result
    
    
    def change_template(self,template, tools):
        llm = ChatMistralAI(
            model="mistral-large-latest",
            temperature=0,
            max_retries=2,
        )
        
        llm_with_tools = llm.bind_tools(tools)
        
        prompt = ChatPromptTemplate.from_messages(template)
        
        self.chain = prompt | llm_with_tools 
        
        self.template = template

