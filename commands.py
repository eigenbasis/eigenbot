import string


def get_user(line):  # get user who typed msg
    separate = line.split(":", 2)
    user = separate[1].split("!", 1)[0]
    return user


def get_message(line):
    separate = line.split(":", 2)
    message = separate[2]
    return message