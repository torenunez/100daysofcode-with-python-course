# https://github.com/torenunez/100daysofcode-with-python-course/blob/master/days/22-24-decorators/decorators.ipynb
# https://gist.github.com/Zearin/2f40b7b9cfc51132851a

def decorator_maker_with_arguments(decorator_arg1, decorator_arg2):
    print
    'I make decorators! And I accept arguments:', decorator_arg1, decorator_arg2

    def my_decorator(func):
        # The ability to pass arguments here is a gift from closures.
        # If you are not comfortable with closures, you can assume it’s ok,
        # or read: http://stackoverflow.com/questions/13857/can-you-explain-closures-as-they-relate-to-python
        print
        'I am the decorator. Somehow you passed me arguments:', decorator_arg1, decorator_arg2

        # Don’t confuse decorator arguments and function arguments!
        def wrapped(function_arg1, function_arg2):
            print('I am the wrapper around the decorated function.\n'
                  'I can access all the variables\n'
                  '\t- from the decorator: {0} {1}\n'
                  '\t- from the function call: {2} {3}\n'
                  'Then I can pass them to the decorated function'
                  .format(decorator_arg1, decorator_arg2,
                          function_arg1, function_arg2))
            return func(function_arg1, function_arg2)

        return wrapped

    return my_decorator

c1 = 'Penny'
c2 = 'Leslie'

@decorator_maker_with_arguments('Leonard', c1)
def decorated_function_with_arguments(function_arg1, function_arg2):
    print ('I am the decorated function and only knows about my arguments:'
           ' {0} {1}'.format(function_arg1, function_arg2))


decorated_function_with_arguments(c2, 'Howard')


def make_html(decorator_arg1):

    def my_decorator(func):

        def wrapped(function_arg1):
            return '<{0}><{1}></{0}>'.format(decorator_arg1, func(function_arg1))

        return wrapped

    return my_decorator


@make_html('p')
@make_html('strong')
def get_text(text):
    return text

get_text('I code with PyBites')