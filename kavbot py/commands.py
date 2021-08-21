import json
def commands_kav():
    pre_commands = {
                    'what is <term>':'  Returns Definitions of term from the dictionary',
                    'hi':'  Returns Hi Ho',
                    'music':'  Try it',
                    'time':'  Returns current time',
                    'weater <city_name>' :'Returns current weather at that place',
                    'meaning <word>' : 'Returns the meaning of the word from an online dictionary',
                    'quote': 'Returns a quote for the day'
                   }
    pre_commands = json.dumps(pre_commands, indent=0)
    return pre_commands