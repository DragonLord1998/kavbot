question = 't  how are you? \a i am fine'
if question[0] == 't':
    question =question.replace('t','',1)
    statements = question.split('\a')
    que = statements[0]
    ans = statements[1]
    print(que , ans)