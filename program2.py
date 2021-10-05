f = open("edges_l3.txt",'r')
all_nodes = {}
for line in f:
 nodes = line.split("\t")
 node1 = nodes[0].strip()
 node2 = nodes[1].strip()
 if node1 not in all_nodes:
 all_nodes[node1] = node1

 if node2 not in all_nodes:
 all_nodes[node2] = node2
print ("Total unique nodes %d"%len(all_nodes))
count = 0
nodes_and_ids = {}
rev_nodes_and_ids = {}
for node in all_nodes:
 if node not in nodes_and_ids:
 count = count + 1
 nodes_and_ids[count] = node
 rev_nodes_and_ids[node] = count
print ("Found %d nodes"%len(all_nodes.keys()))
f = open("graph_l3_test.net",'w')
f.write("*Vertices %d\n"%len(nodes_and_ids.keys()))
for node_id in nodes_and_ids:
 f.write('%s "%s"\n'%(node_id, nodes_and_ids[node_id]))
f2 = open("edges_l3.txt",'r')
f.write("\n*Edges\n")
for arc in f2:
 nodes = arc.split("\t")
 node1 = rev_nodes_and_ids[nodes[0].strip()]
 node2 = rev_nodes_and_ids[nodes[1].strip()]
 f.write("%s %s\n"%(node1,node2))
f.close()
f2.close()