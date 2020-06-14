

def call_twice(some_func, *args, **kwargs):
    error_mess = "Function should be called twice with same arguments!" 
    try:
        return (some_func(*args, **kwargs), some_func(*args, **kwargs))
    except TypeError:
        return (some_func(*args), some_func(*args)), (error_mess)
    

def push_and_count(target, *, value):
    target.append(target)
    return len(target)


def shoot():
    return 'Bang!'


def test_call_twice():
    assert call_twice(shoot) == ('Bang!', 'Bang!')
    assert call_twice(push_and_count, [], value=42) == (1, 2), (
        "Function should be called twice with same arguments!"
    )



if __name__ == '__main__':
    test_call_twice()
    print('Tests passed')
