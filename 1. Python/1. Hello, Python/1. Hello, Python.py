
#! Hello, Python!
# ? Python was named for the British comedy troupe Monty Python,
# ? so we'll make our first Python program an homage to their skit about Spam?
# ? Just for fun, try reading over the code below and predicting what it's going to do when run.
# ? (If you have no idea, that's fine!)
# ? Then click the "output" button to see the results of our program.


spam_amount = 0
print(spam_amount)

# Ordering Spam, egg, Spam, Spam, bacon and Spam (4 more servings of Spam)
spam_amount = spam_amount + 4

if spam_amount > 0:
    print("But I don't want ANY spam!")

viking_song = "Spam " * spam_amount
print(viking_song)

# ? There's a lot to unpack here!
# ? This silly program demonstrates many important
# ? aspects of what Python code looks like and how it works.
# ?  Let's review the code from top to bottom.


# * Variable assignment: Here we create a variable called spam_amount and
# *assign it the value of 0 using =, which is called the assignment operator.
# * Aside: If you've programmed in certain other languages
# * (like Java or C++), you might be noticing some things Python
# * doesn't require us to do here:
# * we don't need to "declare" spam_amount before assigning to it
# * we don't need to tell Python what type of value spam_amount
# *  is going to refer to. In fact,
# * we can even go on to reassign spam_amount
# * to refer to a different sort of thing like a string or a boolean.
