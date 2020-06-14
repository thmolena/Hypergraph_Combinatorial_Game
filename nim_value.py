def remove_a_vertex(vertices, hyperedges):
    if len(vertices) >0:
        a_vertex = vertices[0]
        vertices = vertices[1:]
    for i in range(len(hyperedges)):
        a_hyperedge = hyperedges[i]
        a_letter = a_hyperedge.find(a_vertex)
def remove_a_hyperedge(vertices,hyperedges):
    if len(hyperedges) >0:
        hyperedges = hyperedges[1:]
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
    else:
        nim_value = "unknown"
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
    number_of_vertices = input("How many vertices do you start with? ")
    number_of_vertices = int(number_of_vertices)
    vertices = []
    for i in range(number_of_vertices):
        vertex = input("Input a vertex: ")
        vertices.append(vertex)
    number_of_hyperedges = input("How many hyperedges do you start with? ")
    number_of_hyperedges = int(number_of_hyperedges)
    hyperedges = []
    for i in range(number_of_hyperedges):
        hyperedge = input("Input an hyperedge : ")
        hyperedges.append(hyperedge)
    the_result_monotype = check_monotype(number_of_hyperedges,hyperedges)
    print("The list of the vertices: ",vertices)
    print("The list of the hyperedges: ",hyperedges)
    print(the_result_monotype)
    nim_value = find_nim(number_of_vertices, number_of_hyperedges, the_result_monotype)
    print("the nim_value is: ",nim_value)
    new_vertices = remove_a_vertex(vertices, hyperedges)
    print(new_vertices)
main()
