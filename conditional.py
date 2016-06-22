name = raw_input("what's your name?")


def is_long(name):
    return len(name) > 10

if is_long(name) or name == "Clinton":
    print "Wow, that's a long name"
    if len(name) > 30:
        print "Now, that's crazy."
elif len(name) > 2:
    print "Cool, that's about average."
else:
    print "Are you sure those aren't your initials?"
