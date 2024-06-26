for i in range( 1,10):
    if i%2==0:
        print(i)




##################################



def outer_fun():
    def inner_fun():
        print("*****")
        outer_fun()
        print("#####")

    return inner_fun


@outer_fun
def fun_test():
    print("Inside func")