import openai as ai
def smartai(ques):
    def chat(question,chat_log = None) -> str:
        if(chat_log == None):
            chat_log = start_chat_log
        prompt = f"{chat_log}Human: {question}\nAI:"
        response = completion.create(prompt = prompt, engine =  "davinci", temperature = 0.85,top_p=1, frequency_penalty=0, 
        presence_penalty=0.7, best_of=2,max_tokens=100,stop = "\nHuman: ")
        return response.choices[0].text


    if __name__ == "__main__":
        ai.api_key = "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"

        completion = ai.Completion()

        start_chat_log = """Human: Hello, I am Human.
        AI: Hello, human I am openai gpt3.
        Human: How are you?
        AI: I am fine, thanks for asking. 
        """

        #train = False
        
        
       
        return chat(ques,start_chat_log).split(",")[0]
