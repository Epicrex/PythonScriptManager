back_list = ["back"]
exit_list = ["quit", "exit"]


def trigger_back_or_exit_action(user_inp):
    if user_inp in back_list:
        return True
    elif user_inp in exit_list:
        exit()
