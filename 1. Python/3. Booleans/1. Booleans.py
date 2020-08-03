
#! Booleans
# ? Python has a type of variable called bool.
# ? It has two possible values: True and False.

x = True

print(x)
print(type(x))


def can_run_for_president(age):
    """Can someone of the given age run for president in the US?"""
    # The US Constitution says you must be at least 35 years old
    return age >= 35


print("Can a 19-year-old run for president?", can_run_for_president(19))
print("Can a 45-year-old run for president?", can_run_for_president(45))
