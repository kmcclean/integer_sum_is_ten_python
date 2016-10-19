import random
import time

if __name__ == '__main__':
    def main():

        #testing for 10s.
        list = problem(10)
        #solution_linear(list, 10)
        #list = [7, 5, 5, 3]
        solution_quad(list, 10, len(list))
        #
        #testing for 100s.
        list = problem(100)
        #solution_linear(list, 10)
        solution_quad(list, 10, len(list))

        # testing for 1000s.
        list = problem(1000)
        #solution_linear(list, 10)
        solution_quad(list, 10, len(list))

        # testing for 10000s.
        list = problem(10000)
        #solution_linear(list, 10)
        solution_quad(list, 10, len(list))

#This creates the list of random integers, with numbers between one and ten.
def problem(list_length):
    list = []
    #this randomly inserts a number between 1 and 9 into the list. it stops when the list length is reached.
    while len(list) < list_length:
        list.append(random.randint(1, 9))
    return list


#Still working on this solution
# def solution_linear(list, number):
#     start_time = time.time()
#     list_of_solutions = []
#     for item1 in list:
#         search_number = number - item1
#         if search_number > 0:
#             while len(list_of_solutions) < list.count(search_number):
#                 list_of_solutions.append([item1, search_number])
#     print(list_of_solutions)
#     print("Linear time for " + str(len(list)) + ": " + str(time.time() - start_time))


#This is a simple but inelegant solution to the problem.
def solution_quad(list, number, list_length):
    #print(list)
    #This sets a start time, so we can keep track of how long it takes.
    start_time = time.time()
    list_of_solutions = []

    #This loops through the list twice, and checks the results against one another to see if they add up to the number being looks for.
    for item in list:
        for item2 in list:
            if item + item2 == number:
                list_of_solutions.append([item, item2])

    print(list_of_solutions)
    print("Quadratic time for " + str(list_length) + ": " + str(time.time() - start_time))
    print("")

main()





