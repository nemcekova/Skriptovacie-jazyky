
def gen_quiz(qpool, *index, altcodes=('ABCDEF'), quiz=None):
    """

    >>> test_qpool5 = [('Question1', ['Answer1', 'Answer2', 'Answer3', 'Answer4']), ('Question2', ['Answer1', 'Answer2', 'Answer3']), ('Question3', ['Answer1', 'Answer2', 'Answer3', 'Answer4']), ('Question4', ['Answer1', 'Answer2'])]
    >>> not_used = gen_quiz(test_qpool5, 0, altcodes = '123456')
    >>> gen_quiz(test_qpool5, 0, altcodes = '123456')
    [('Question1', ['1: Answer1', '2: Answer2', '3: Answer3', '4: Answer4'])]



    >>> test_qpool7 = [('Question1', ['Answer1', 'Answer2', 'Answer3', 'Answer4']), ('Question2', ['Answer1', 'Answer2', 'Answer3']), ('Question3', ['Answer1', 'Answer2', 'Answer3', 'Answer4']), ('Question4', ['Answer1', 'Answer2'])]
    >>> gen_quiz(test_qpool7, 0, 2, 4, altcodes = ['101','201'])
    Ignoring index 4 - list index out of range
    [('Question1', ['101: Answer1', '201: Answer2']), ('Question3', ['101: Answer1', '201: Answer2'])]
    """
    if(quiz is None):
        quiz=[]
    for i in index:
        try:
            question_tmp = qpool[i]
            answers_tmp = question_tmp[1]
            neviem = list(zip(altcodes, answers_tmp))
            answers = [": ".join(pair) for pair in neviem]

            q_n_a = (question_tmp[0], answers)
            quiz.append(q_n_a)
        #    print(quiz)
        except Exception as e:
            print("Ignoring index " + str(i) + " - " + str(e))


    return quiz


if __name__ == "__main__":
    import doctest
    doctest.testmod()
