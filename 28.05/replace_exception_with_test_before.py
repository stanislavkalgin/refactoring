# before
def remake_indices(a):
    # code code code
    try:
        return int(a)
    except Exception as ex:
        print("Bad a: {local_a}, {local_ex}".format(local_a=a, local_ex=ex))
    # code code code

# after
def remake_indices(a):
    # code code code
    if a in "123456789":
        return int(a)
    else:
        print("Bad a:", a)
    # code code code
