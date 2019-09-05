from Algorithm import AlgorithmClass

my_alg = AlgorithmClass()

while True:
    result = ""
    print("select your algorithm : \n"
          "1.bfs\n2.dfs\n3.dls\n4.ids\n5.bidirectional\n6.ucs\n7.a*\n8.exit")
    user_input = input()
    if user_input not in ["1", "2", "3", "4", "5", "6", "7", "8"]:
        print("wrong input")
        continue

    if user_input == "1":
        result = my_alg.bfs()
    elif user_input == "2":
        result = my_alg.dfs()
    elif user_input == "3":
        print("please enter your iterations :")
        iter = int(input())
        result = my_alg.dls(iter)
    elif user_input == "4":
        result = my_alg.ids()
    elif user_input == "5":
        result = my_alg.bidirectional()
    elif user_input == "6":
        result = my_alg.ucs()
    elif user_input == "7":
        result = my_alg.a_star()
    elif user_input == "8":
        break

    print(result)



