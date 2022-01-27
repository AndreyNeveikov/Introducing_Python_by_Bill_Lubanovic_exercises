def good():
    return ['Harry', 'Ron', 'Hermione']


print(good())


def get_odds():
    for number in range(10):
        if number % 2 != 0:
            yield number


counter = 1
for odd in get_odds():
    counter += 1
    if counter == 3:
        print('The third odd number is:', counter)
        break


def test(func):
    def prints_start_and_end():
        print('start')
        func()
        print('end')
        return
    return prints_start_and_end


@test
def say_hello():
    print('Hello')


say_hello()
# test_hello = test(say_hello)
# test_hello()


class OopsException(Exception):
    pass


if 1 == 1:
    raise OopsException('Caught an oops')


