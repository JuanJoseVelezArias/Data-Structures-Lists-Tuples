def multiple_returns(sentence):
    if len(sentence) == 0:
        return (0, "none")
    else:
        return(len(sentence), sentence[0])