# overlapping-cluster-removal
Welcome to the cluster-removal micro-project repository.

Following is the problem statemet: 
You are given a list of tuples of the form (<float> x, <float> y, <float> r,) (let's call these c-tuples). Each c-tuple represents a circle on a rectangular coordinate space, with x and y being the coordinates of the center and r being the radius. Assume that each c-tuple has a unique radius.
  
 Let a cluster of circles be a group of circles where each circle in the group overlaps with atleast one other circle in that group. Formally, first let a path be formed between two circles when they overlap. Define a cluster as a group of n circles, where each circle is reachable from every other circle through the formed paths. 

Write a python script that does the following: 
Foreachcluster,the circle with the largest area is kept, and all other circles in that cluster are removed.
Return the resulting list of c-tuples.
Some examples are shown.

The solution makes use of Disjoint sets to clearly seperate multiple clusters, which is crucial.
![Cluster example](/cluster.png)
