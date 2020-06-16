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

def thy(starting_list_1):
    
    vertices = get_vertices(starting_list_1)
    hyperedges = get_hyperedges(starting_list_1)

    the_result_monotype = check_monotype(len(hyperedges),hyperedges)

    if the_result_monotype != "mixed":
        nim_value = find_nim(len(vertices), len(hyperedges), the_result_monotype)
        print("the nim_value is: ",nim_value)
    
    else:
        for i in range(len(starting_list_1)):
            starting_list_3 = ahihi(starting_list_1,i)
            vertices_5 = get_vertices(starting_list_3)
            hyperedges_5 = get_hyperedges(starting_list_3)
            
            the_result_monotype_5 = check_monotype(len(hyperedges_5),hyperedges_5)
        
            if the_result_monotype_5 != "mixed":
                nim_value = find_nim(len(vertices_5), len(hyperedges_5), the_result_monotype_5)
                print("the nim_value is: ",nim_value)
    
            else:
                for i in range(len(starting_list_3)):
                    starting_list_4 = ahihi(starting_list_3,i)
                    vertices_6 = get_vertices(starting_list_4)
                    hyperedges_6 = get_hyperedges(starting_list_4)
            
                    the_result_monotype_6= check_monotype(len(hyperedges_6),hyperedges_6)            

                    if the_result_monotype_6 != "mixed":
                        nim_value = find_nim(len(vertices_6), len(hyperedges_6), the_result_monotype_6)
                        print("the nim_value is: ",nim_value)

                    else:
                        for i in range(len(starting_list_4)):
                            starting_list_5 = ahihi(starting_list_4,i)
                            vertices_7 = get_vertices(starting_list_5)
                            hyperedges_7 = get_hyperedges(starting_list_5)
            
                            the_result_monotype_7= check_monotype(len(hyperedges_7),hyperedges_7)           

                            if the_result_monotype_7 != "mixed":
                                nim_value = find_nim(len(vertices_7), len(hyperedges_7), the_result_monotype_7)
                                print("the nim_value is: ",nim_value)

                            else:
                                for i in range(len(starting_list_5)):
                                    starting_list_6 = ahihi(starting_list_5,i)
                                    vertices_8 = get_vertices(starting_list_6)
                                    hyperedges_8 = get_hyperedges(starting_list_6)
            
                                    the_result_monotype_8 = check_monotype(len(hyperedges_8),hyperedges_8)           
            
                                    if the_result_monotype_8 != "mixed":
                                        nim_value = find_nim(len(vertices_8), len(hyperedges_8), the_result_monotype_8)
                                        print("the nim_value is: ",nim_value)

                                    else:
                                        for i in range(len(starting_list_6)):
                                            starting_list_7 = ahihi(starting_list_6,i)
                                            vertices_9 = get_vertices(starting_list_7)
                                            hyperedges_9 = get_hyperedges(starting_list_7)
            
                                            the_result_monotype_9 = check_monotype(len(hyperedges_9),hyperedges_9)
                                             
                                            if the_result_monotype_9 != "mixed":
                                                nim_value = find_nim(len(vertices_9), len(hyperedges_9), the_result_monotype_9)
                                                print("the nim_value is: ",nim_value)
                                           

"""
            if the_result_monotype != "mixed":
                nim_value = find_nim(len(vertices_5), len(hyperedges_5), the_result_monotype)
                print("the nim_value is: ",nim_value)
        
            if the_result_monotype == "mixed":
                for i in range(len(hyperedges_1)):
                    print("")
                    print(j, "j-th level")
                    print("Starting with ", hyperedges_1)
                    hyperedges_2 =(remove_a_step(hyperedges_1,i))
                    hyperedges_3=copy.deepcopy(hyperedges_2)
                    print(hyperedges_3)
                    vertices_6 = get_vertices(hyperedges_2)
                    hyperedges_6 = get_hyperedges(hyperedges_2)
                    the_result_monotype= check_monotype(len(hyperedges_6),hyperedges_6)            
   """                 
      
                    

#def thu_nghiem():

main()
