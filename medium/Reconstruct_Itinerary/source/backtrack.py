class Solution(object):
    def findItinerary(self, tickets):
        # set a map that stores flight as the key and the destinations as the value
        self.flightMap = collections.defaultdict(list)
        # iterate the tickets
        for ticket in tickets:
            # store the key as the origin and the append the possible destinations
            self.flightMap[ticket[0]].append(ticket[1])
        # set a map that tracks the visited flights
        self.visited = dict()
        # sort the destinations in a lexical order and set the visited flights
        for src in self.flightMap:
            # sort the destinations according to the lexical order
            self.flightMap[src].sort()
            # append the visited map with the list of unvisited flights
            self.visited[src] = [0 for _ in self.flightMap[src]]
        # set the total number of airports that needs to be included in the route == tickets + 1
        self.flights = len(tickets) + 1
        # initialize the starting route with JFK
        route = ['JFK']
        # return the complete route from backtracking
        return self.backtrack(route)

    def backtrack(self, route):
        # get the current destination
        src = route[-1]
        # return the route if the all the airports are included in the route
        if len(route) == self.flights:
            return route
        # iterate the destinations from the current flight
        for i, dest in enumerate(self.flightMap[src]):
            # if the destination is not a visited flight
            if not self.visited[src][i]:
                # update the destination flight as visited
                self.visited[src][i] = 1
                # invoke the recursion with the next destination
                ans = self.backtrack(route + [dest])
                # reset the destination flight
                self.visited[src][i] = 0
                # return the route if all the airports are included in the route
                if len(ans) == self.flights:
                    return ans
        # return the empty list if no complete route is found
        return list()