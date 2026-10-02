# flags: --minimum-version=3.9
# A parenthesized tuple is a single context manager. Removing its brackets would
# turn it into several context managers, which changes the meaning of the code
# (even though the code will always trigger a runtime error).
with c, (a, b):
    pass


with c, (a, b), d:
    pass


with c, ((a, b)):
    pass


with (((a, b))), c:
    pass


with (c, (a, b)):
    pass


# On Python 3.9+, `with (a, b):` has two context managers, so neither pair of
# brackets can go here.
with ((a, b)):
    pass


async def f():
    async with c, (a, b):
        pass


def test_tuple_as_contextmanager():
    from contextlib import nullcontext

    try:
        with nullcontext(), (nullcontext(), nullcontext()):
            pass
    except TypeError:
        # test passed
        pass
    else:
        # this should be a type error
        assert False

# output

# A parenthesized tuple is a single context manager. Removing its brackets would
# turn it into several context managers, which changes the meaning of the code
# (even though the code will always trigger a runtime error).
with c, (a, b):
    pass


with c, (a, b), d:
    pass


with c, (a, b):
    pass


with (a, b), c:
    pass


with c, (a, b):
    pass


# On Python 3.9+, `with (a, b):` has two context managers, so neither pair of
# brackets can go here.
with ((a, b)):
    pass


async def f():
    async with c, (a, b):
        pass


def test_tuple_as_contextmanager():
    from contextlib import nullcontext

    try:
        with nullcontext(), (nullcontext(), nullcontext()):
            pass
    except TypeError:
        # test passed
        pass
    else:
        # this should be a type error
        assert False
