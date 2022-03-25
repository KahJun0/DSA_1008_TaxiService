from .Graph import Graph
from datetime import datetime

now = datetime.now()


class Record:

    def __init__(self):
        self.driverRecords = {}
        self.invert = {}
        self.passengerRecords = {}
        self.passengerStartRadius = []
        self.passengerEndRadius = []
        self.drivers = []
        self.passengers = []

    def updateDriver(self, driverID,
                     visitingNodes):  # this function updates this virtual database on which nodes the driver is
        # going to go past
        self.driverRecords[driverID] = visitingNodes
        # print(self.driverRecords) #testing purpose

    def addDriver(self, driver):
        self.drivers.append(driver)

    def updatePassenger(self, accID, vistingNodes, startRadius,
                        endRadius):  # this function updates this db on which nodes the passenger WILL have to go past
        self.passengerRecords[accID] = vistingNodes
        self.passengerStartRadius = startRadius
        self.passengerEndRadius = endRadius

    def invertIndex(
            self):  # this function inverts the index of the driver nodes (to show which nodes will be touched if
        # there are multiple drivers)

        for key, values in self.driverRecords.items():
            for value in values:
                if value not in self.invert:
                    self.invert[value] = []
                self.invert[value].append(key)
        self.splitInvert = [[k, v] for k, values in self.invert.items() for v in
                            values]  # this lines converts the invert dictionary into a list, splitting each
        # idividual nodes with its rider.

    def intersect(self, dict, list):  # AND operation between two sets (for compare function)
        intersectList = []
        for items in list:
            for nodes in dict.keys():
                if nodes == items:
                    intersectList.append(nodes)
        return intersectList

    def compare(
            self):  # this function creates a list of intersected points of a driver and a passenger (both at start
        # point and end point in accordance to the passenger)
        self.startIntersection = self.intersect(self.invert, self.passengerStartRadius)  # Ss = Cs n SP(Xs,Xd)
        self.endIntersection = self.intersect(self.invert, self.passengerEndRadius)  # Sd = Cd n SP(Xs,Xd)
        try:
            if self.startIntersection and self.endIntersection:
                pass
            else:
                raise ValueError('Sorry, there is no driver nearby')
        except ValueError as err:
            print(err.args)
            quit()

    def selectingRides(self, distStart, distEnd):
        self.startTable = {}
        self.endTable = {}
        self.nodeStartList = []
        self.nodeEndList = []
        for nodes in self.startIntersection:
            for i in range(len(self.splitInvert)):
                if nodes == self.splitInvert[i][0]:
                    self.nodeStartList.append(tuple(self.splitInvert[
                                                        i]))  # we insert as tuple because we going to use them as
                    # keys in dict later on

        for nodes in self.endIntersection:
            for i in range(len(self.splitInvert)):
                if nodes == self.splitInvert[i][0]:
                    self.nodeEndList.append(tuple(self.splitInvert[
                                                      i]))  # we insert as tuple because we going to use them as keys
                    # in dict later on

        for keys in self.nodeStartList:  # this table represents Fig 6 in the article
            distanceFromStartNode = distStart[keys[0]]
            self.startTable[keys] = distanceFromStartNode

        for keys in self.nodeEndList:  # this table represents Fig 6 in the article
            distanceFromEndNode = distEnd[keys[0]]
            self.endTable[keys] = distanceFromEndNode

        return self.averageMinDistance(self.startTable, self.endTable)  # algo to select driver for the passenger

    def averageMinDistance(self, Table, Table2):
        if min(Table, key=Table.get)[1] == min(Table2, key=Table2.get)[1]:
            # if the driver of both the minimum distance from start and end nodes are the same, that driver will
            # be selected
            return min(Table, key=Table.get)[1]

        # else compare the two drivers
        else:
            minStart1 = 99999999  # min distance of driver 1 from start point
            minStart2 = 99999999  # min distance of driver 2 from start point
            minEnd1 = 99999999  # min distance of driver 1 from end point
            minEnd2 = 99999999  # min distance of driver 2 from end point
            for key in Table:
                if key[1] == min(Table, key=Table.get)[1]:
                    if Table[key] < minStart1:
                        minStart1 = Table[key]
                elif key[1] == min(Table2, key=Table2.get)[1]:
                    if Table[key] < minStart2:
                        minStart2 = Table[key]

            for key in Table2:
                if key[1] == min(Table, key=Table.get)[1]:
                    if Table2[key] < minEnd1:
                        minEnd1 = Table2[key]
                elif key[1] == min(Table2, key=Table2.get)[1]:
                    if Table2[key] < minEnd2:
                        minEnd2 = Table2[key]

            if ((minStart1 + minEnd1) / 2) < ((minStart2 + minStart2) / 2):
                return min(Table, key=Table.get)[1]

            elif ((minStart1 + minEnd1) / 2) > ((minStart2 + minStart2) / 2):
                return min(Table2, key=Table2.get)[1]

            else:
                return min(Table, key=Table.get)[1]


class Driver:

    def __init__(self, name, driverID):
        self.name = name
        self.driverID = driverID

    def offerRide(self, records, starting, destination, num_freeSeats):
        self.starting = starting
        self.destination = destination
        self.freeSeats = num_freeSeats
        self.time = now.strftime("%H:%M:%S")

        d = Graph(41)
        dist = d.dijkstra(d, self.starting, self.destination)
        self.visitingNodes = d.getSolutions(1, dist)  # gets all the nodes passed by, from starting node to end note
        records.updateDriver(self.driverID, self.visitingNodes)
        records.addDriver(self)


class Passenger:

    def __init__(self, name, accID):
        self.name = name
        self.accID = accID

    def requestRide(self, records, starting, destination):
        self.starting = starting
        self.destination = destination
        self.time = now.strftime("%H:%M:%S")

        d = Graph(41)
        self.dist = d.dijkstra(d, self.starting,
                               self.destination)  # list of the distance from Passenger's starting node to all other
        # node
        self.visitingNodes = d.getSolutions(1, self.dist)
        self.radiusNodesStart = d.getSolutions(3, self.dist)  # this gets radius around starting node Cs
        # following codes is to get radius around end note:
        g = Graph(41)
        self.dist2 = g.dijkstra(g, self.destination, self.starting)
        self.radiusNodesEnd = g.getSolutions(3, self.dist2)  # nodes surround the end point: Cd

        records.updatePassenger(self.accID, self.visitingNodes, self.radiusNodesStart, self.radiusNodesEnd)

        records.invertIndex()
        records.compare()
        match = records.selectingRides(self.dist, self.dist2)
        print(f"Passenger: {self.name} is matched with driver id: {match}")
        return match
