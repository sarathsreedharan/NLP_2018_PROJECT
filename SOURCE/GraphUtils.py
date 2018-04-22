from networkx import Graph
from networkx.drawing.nx_agraph import write_dot
import os
import config

def createGraph(model):
    graph = Graph()

    city_connect_to_map = model.getCityConnectedToMap()
    city_disease_count_map = model.getCityDiseaseCountsMap()

    for key in city_connect_to_map.keys():
        disease_count = city_disease_count_map[key]
        node_name = str(key)+" ["+str(disease_count)+"]"
        graph.add_node(key,label=node_name)


    for key in city_connect_to_map.keys():
        for city in city_connect_to_map[key]:
            graph.add_edge(key, city)

    write_dot(graph, 'foo.dot')
    os.system('dot -Tsvg foo.dot -o '+config.GRAPH_FILE)
    print ("Saved Graph!")

