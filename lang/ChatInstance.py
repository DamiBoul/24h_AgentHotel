import os

from langfuse.callback import CallbackHandler
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate

import private


class ChatInstance:
    
    def __init__(self, template): 
        if "MISTRAL_API_KEY" not in os.environ:
            os.environ["MISTRAL_API_KEY"] = private.mistral_key()

        self.langfuse_handler = CallbackHandler(
            public_key=private.public_key(),
            secret_key=private.private_key(),
            host="https://cloud.langfuse.com"
        )

        llm = ChatMistralAI(
            model="mistral-large-latest",
            temperature=0,
            max_retries=2,
        )

        prompt = ChatPromptTemplate.from_messages(template)

        self.chain = prompt | llm


    def ask(self, prompt):
        result = self.chain.invoke(prompt, config={"callbacks": [self.langfuse_handler]})
        return result

