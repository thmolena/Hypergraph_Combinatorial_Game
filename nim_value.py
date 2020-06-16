import copy
def remove_a_step(starting_list_1,i):
    starting_list_2 = copy.deepcopy(starting_list_1)
    print("Remove " , starting_list_1[i])
     
    for j in range(len(starting_list_1)):
        a_letter = starting_list_1[j].find(starting_list_1[i])
        if a_letter != -1:
            starting_list_2.remove(starting_list_1[j])
    return starting_list_2



def get_vertices(starting_list):
    vertices = []
      
    for i in range(len(starting_list)):
        if len(starting_list[i]) == 1:
            vertices.append(starting_list[i])

    print("The list of the vertices: ",vertices)
    return vertices


def get_hyperedges(starting_list):
    hyperedges = []
    
    for i in range(len(starting_list)):
        if len(starting_list[i]) != 1:
            hyperedges.append(starting_list[i])
    print("The list of the hyperedges: ",hyperedges)
    return hyperedges


def oddly_uniform(number_of_vertices, number_of_hyperedges):
    if number_of_vertices %2 == 0 and number_of_hyperedges %2 == 0:
        nim_value = 0
    elif number_of_vertices %2 != 0 and number_of_hyperedges %2 == 0:
        nim_value = 1
    elif number_of_vertices %2 != 0 and number_of_hyperedges %2 != 0:
        nim_value = 2
    else:
        nim_value = 3
    return nim_value

def evenly_uniform(number_of_vertices, number_of_hyperedges):
    if number_of_vertices %2 == 0 and number_of_hyperedges %2 == 0:
        nim_value = 0
    elif number_of_vertices %2 != 0 and number_of_hyperedges %2 == 0:
        nim_value = 1
    elif number_of_vertices %2 == 0 and number_of_hyperedges %2 != 0:
        nim_value = 2
    else:
        nim_value = 3
    return nim_value

def find_nim(number_of_vertices, number_of_hyperedges, the_result_monotype):
    if the_result_monotype == "oddly":
        nim_value = oddly_uniform(number_of_vertices, number_of_hyperedges)
    elif the_result_monotype == "evenly":
        nim_value = evenly_uniform(number_of_vertices, number_of_hyperedges)
    return nim_value

def check_monotype(number_of_hyperedges,hyperedges):
    result_monotype = []
    for i in range(number_of_hyperedges):
        if len(hyperedges[i])%2 == 0:
           result_monotype.append("even")
        else:
           result_monotype.append("odd")
    if "even" not in result_monotype:
        the_result_monotype = "oddly"
    elif "odd" not in result_monotype:
        the_result_monotype = "evenly"
    else:
        the_result_monotype = "mixed"
    return the_result_monotype

def main():
    starting_number = input("Input the number of all vertices and hyperedges to start with? ")
    starting_number = int(starting_number)
    starting_list = []

    for i in range (starting_number):
        starting = input("Input a vertex or a hyperedge: ")
        starting_list.append(starting)

    starting_list_start =copy.deepcopy(starting_list)    
    thy(starting_list_start)


def ahihi(starting_list_1,i):
    starting_list_2 = copy.deepcopy(starting_list_1)
    print("")
    print(i, "i-th level")
    print("Starting with", starting_list_1)
    starting_list_3 = remove_a_step(starting_list_2,i)
    print(starting_list_3)

            
    return starting_list_3

def ahaha(starting_list_1):
    vertices = get_vertices(starting_list_1)
    hyperedges = get_hyperedges(starting_list_1)

    the_result_monotype = check_monotype(len(hyperedges),hyperedges)

    if the_result_monotype != "mixed":
        nim_value = find_nim(len(vertices), len(hyperedges), the_result_monotype)
        print("the nim_value is: ",nim_value)
    else:
        nim_value = 1000
        print("Cannot find the nim value yet since it is mixed.")
    return nim_value

def thy(starting_list_1):
    
    nim_value = ahaha(starting_list_1)
    if nim_value == 1000:

        for i in range(len(starting_list_1)):
            starting_list_3 = ahihi(starting_list_1,i)

            nim_value_5 = ahaha(starting_list_3)

            if nim_value_5 == 1000:
                for i in range(len(starting_list_3)):
                    starting_list_4 = ahihi(starting_list_3,i)

                    nim_value_6 = ahaha(starting_list_4)

                    if nim_value_6 == 1000:
                        for i in range(len(starting_list_4)):
                            starting_list_5 = ahihi(starting_list_4,i)

                            nim_value_7 = ahaha(starting_list_5)
                            
                            if nim_value_7 == 1000:
                                for i in range(len(starting_list_5)):
                                    starting_list_6 = ahihi(starting_list_5,i)

                                    nim_value_8 = ahaha(starting_list_6)

                                    if nim_value_8 == 1000:
                                        for i in range(len(starting_list_6)):
                                            starting_list_7 = ahihi(starting_list_6,i)

                                            nim_value_9 = ahaha(starting_list_7)

                                             
                                        
      
                    

#def thu_nghiem():

main()
