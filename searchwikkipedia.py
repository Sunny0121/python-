import wikipedia
try:
    while True:
        print("type 'exit' for exit")
        search = input("What do you want to know:\nType here:-")
        if search == 'exit' :
            print("Exiting ...")
            print("Done ...")
            print("Thanks for using ...")
            break
        else:
            lines = int(input("How many lines are enough:\n Type here(input must be a natural number):-"))
            result = wikipedia.summary(search,sentences = lines)
            print(result)
except Exception as e:
    print(e,"\n \t \t####    this is error    #####")