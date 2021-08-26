import os
import openai as ai
def smartai(ques):
    def chat(question,chat_log = None) -> str:
        if(chat_log == None):
            start_chat_log = """Human: Hello, I am Human.
                             AI: Hello, human I am KavBot.
                             Human: How are you?
                             AI: I am fine, thanks for asking. 
                             """ 
            start_chat_log = start_chat_log + question
            chat_log = start_chat_log 
        prompt = f"{chat_log}Human: {question}\nAI:"
        response = completion.create(prompt = prompt, engine =  "davinci", temperature = 0.85,top_p=1, frequency_penalty=0, 
        presence_penalty=0.7, best_of=1,max_tokens=100,stop = "\nHuman: ")
        return response.choices[0].text


   
    ai.api_key = os.environ.get("AITOKEN")
    
    completion = ai.Completion()

    

        #train = False
        
        
       
    return chat(ques,start_chat_log).split(",")[0].split(".")[0]

#print(smartai("How old are you?"))

