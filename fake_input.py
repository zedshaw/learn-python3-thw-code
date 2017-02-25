def create(replies):
    """Used for faking out scripts so they can run like
    the book needs but be sectioned to appear to be normal.
    """

    def input(prompt=None):
        reply = replies.pop(0)
        if prompt: print(prompt, end=' ')
        print(reply)
        return reply

    return input, input

