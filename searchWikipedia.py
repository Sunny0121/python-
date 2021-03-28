# First open terminal and type 'pip install wikipedia' for install wikipedia module
# Wikipedia is a Python library that makes it easy to access and parse data from Wikipedia.

import wikipedia  # importing wikipedia

try:
    while True:
        print("Type 'exit' for exit")

        # search variable takes: what user is want to know about
        search = input("What do you want to know:\nType here:-")

        # Here i use if: statement for exiting the code if user do not intrested
        if search == 'exit':
            print("Exiting ...")
            print("Done ...")
            print("Thanks for using ...")

            #break  for break the loop
            break

        # In else: statement second variable lines takes integer value for lines
        else:
            lines = int(
                input(
                    "How many lines are enough:\n Type here(input must be a natural number):-"
                ))
            #  Search Wikipedia, get article summaries, get data like links and images from a page, and more.
            result = wikipedia.summary(search, sentences=lines)
            print(result)
except Exception as e:
    #  Wikipedia wraps the MediaWiki API so you can focus on using Wikipedia data, not getting it.
    print(e, "\n \t \t####   Retry/check your inputs  #####")
