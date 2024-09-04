def myfun(x, *pos_param, **key_param):
    print(x)
    for each_arg in pos_param:
        print(each_arg)
    for key, value in key_param.items():
        print(key, value)

    # Correctly indented line
    modified_pos_param = pos_param + (50,)

    # Call the correct function name
    myfun2(*modified_pos_param, **key_param)


def myfun2(*args, **kwargs):
    print(args)
    print(kwargs)


myfun(10, 20, 30, 40, name="Deva", salary=10000000)
