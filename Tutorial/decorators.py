## Closures

# def main_welcome(msg):
#
#     def sub_welcome_class():
#         print("welcome to inner function")
#         print(msg)
#         print("hi")
#     return  sub_welcome_class()
# main_welcome("hello")


def main_welcome(func):
    def sub_welcome_class():
        print("welcome to inner function")
        func()
        print("hi")

    return sub_welcome_class()
@main_welcome
def channrl_name():
    print("YouTube")

