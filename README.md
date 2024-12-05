# Pathfinding Starter Code

Random Function Methodology:
First, the get_random_path method creates variables that will be used throughout the function. The start_node is set to 0 and the current_node is set to start_node. Then the last_node is set to the last node in the data set. The target is set to the target node and the destination is set to target. Then an empty list called path is created which will track the nodes hit.
The algorithm is set within a while loop that runs first until the target is hit. Inside the loop, first, the neighbors list is created which gets all the next nodes of the current_node. Then the neighbors list is filter so the node can not move to the start node if it is contained in neighbors list. Next a random node is chosen from the list under the name next_node and appended to the path. This runs until the target is met. Once that occurs the new condition for the while loop is set to run until the current_node is equal to the last_node. This then runs til the condition is no longer met and the function will then return path.

The statistic I created was a time spent statistic which tracks how long it takes for the node to reach the exit. This uses the variable dt in the update function and gives the user a better sense of comparison between the quickest path and the random path.

I attempted the extra credit to implement the Floyd Warshall method into the scoreboard by creating a get_f_w_path in pathing and then replacing the dijsktra call with it.