#  Copyright Joel de Guzman 2002-2007. Distributed under the Boost
#  Software License, Version 1.0. (See accompanying file LICENSE_1_0.txt
#  or copy at http://www.boost.org/LICENSE_1_0.txt)
#  Hello World Example from the tutorial

import ibfs_ext
graph = ibfs_ext.IBFSGraph()
graph.initSize(10, 9)
graph.addNode(0,3,0)
graph.addNode(1,0,0)
graph.addNode(2,0,0)
graph.addNode(3,0,0)
graph.addNode(4,0,0)
graph.addNode(5,0,0)
graph.addNode(6,0,0)
graph.addNode(7,0,0)
graph.addNode(8,0,0)
graph.addNode(9,0,3)
graph.addEdge(0,1,1,0)
graph.addEdge(1,2,2,0)
graph.addEdge(2,3,2,0)
graph.addEdge(3,4,2,0)
graph.addEdge(4,5,2,0)
graph.addEdge(5,6,2,0)
graph.addEdge(6,7,2,0)
graph.addEdge(7,8,2,0)
graph.addEdge(8,9,2,0)
graph.initGraph()
mf = graph.computeMaxFlow()
print(mf)
print(graph.isNodeOnSrcSide(0))