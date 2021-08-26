
def run():
    start_chat_log = """
        Human: Hello, I am Human.
        AI: Hello, human I am KavBot.
        Human: How are you?
        AI: I am fine, thanks for asking. 
        """ 
    question = '''thow are you \ai am fine '''
    if question[0] == 't':
        question =question.replace('t','',1)
        statements = question.split('\a')
        que = statements[0]
        ans = statements[1]
        start_chat_log += f"Human: {que}\nAI: {ans}\n"
        print(start_chat_log)


run()