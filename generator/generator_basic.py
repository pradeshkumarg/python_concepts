channels = ["HBO", "cnn", "abc", "espn"]


def remote_control():
    for c in channels:
        yield c


r = remote_control()

print(type(r))

print(next(r))
print(next(r))
print(next(r))
print(next(r))
