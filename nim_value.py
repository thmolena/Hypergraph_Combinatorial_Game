import copy
def remove_a_step(starting_list_1,i):
    starting_list_2 = copy.deepcopy(starting_list_1)
    print("Remove " , starting_list_1[i])
     
    for j in range(len(starting_list_1)):
        a_letter = starting_list_1[j].find(starting_list_1[i])
        if a_letter != -1:
            starting_list_2.remove(starting_list_1[j])
    return starting_list_2

def abc(starting_list_2):
    vertices = []
    hyperedges = []
    
    for i in range(len(starting_list_2)):
        if len(starting_list_2[i]) == 1:
            vertices.append(starting_list_2[i])
        else:
            hyperedges.append(starting_list_2[i])
    number_of_vertices = len(vertices)
    number_of_hyperedges = len(hyperedges)
    print("The list of the vertices: ",vertices)
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

    starting_list_1=copy.deepcopy(starting_list)
    vertices = []
    hyperedges = []
    
    for i in range (starting_number):
        if len(starting_list[i]) == 1:
            vertices.append(starting_list[i])
        else:
            hyperedges.append(starting_list[i])
    number_of_vertices = len(vertices)
    number_of_hyperedges = len(hyperedges)
    the_result_monotype = check_monotype(number_of_hyperedges,hyperedges)
    print("The list of the vertices: ",vertices)
    print("The list of the hyperedges: ",hyperedges)


    if the_result_monotype != "mixed":
        nim_value = find_nim(number_of_vertices, number_of_hyperedges, the_result_monotype)
        print("the nim_value is: ",nim_value)
        
    else:
        for i in range(len(starting_list)):
            print(remove_a_step(starting_list_1,i))
            
        
main()
