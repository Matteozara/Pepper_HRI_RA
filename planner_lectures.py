from collections import defaultdict, deque
import time

class PepperPlanner:
    def __init__(self, schedule, mappa):
        self.lecture_rooms = schedule
        self.mappa = mappa

    def add_lecture_room(self, lecture_name, room_path):
        self.lecture_rooms[lecture_name] = room_path

    def get_room_path(self, lecture_name):

        try:
            # Get the current time in seconds since the epoch
            current_time_seconds = time.time()

            # Convert the time to a readable format
            #current_time_readable = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(current_time_seconds))
            p = int(time.strftime("%H", time.localtime(current_time_seconds)))

            if ((p >= 16) or (p < 8)): #if the time is later than 16, DIAG is closed
                return {"speak": "DIAG is closed now, it will open at 8:00"}

            if (lecture_name == "free"): #return the list of free rooms
                rooms = "library"
                for i in self.lecture_rooms[lecture_name]:
                    for j in self.lecture_rooms[lecture_name][i]:
                        if (j <= p <= j+1):
                            rooms += " " + i 
                return {"speak": "The rooms free to study are: " + str(rooms)}

            if (self.lecture_rooms[lecture_name] == []):    #go to the room specified
                return {"speak": "Come with me, i will show you where is the room " + lecture_name, "go": self.bfs("S", lecture_name)}


            if(p < self.lecture_rooms[lecture_name][1]):
                #show room
                return {"speak": "you are early for your lesson, the lesson of " + lecture_name + " strats at: " + str(self.lecture_rooms[lecture_name][1]) + " in room " + self.lecture_rooms[lecture_name][0] +". In any case I show you the room, come with me", "go" : self.bfs("S", self.lecture_rooms[lecture_name][0]) }
            elif(self.lecture_rooms[lecture_name][1] <= p <= self.lecture_rooms[lecture_name][1]+1):
                #show room
                return {"speak": "The lesson of " + lecture_name + " is happening now in the room " + self.lecture_rooms[lecture_name][0] +", come with me! I show you the room", "go" : self.bfs("S", self.lecture_rooms[lecture_name][0]) }
            
            return {"speak": "you are late, the lesson of " + lecture_name + " ened at: " + str(self.lecture_rooms[lecture_name][1] + 2)}
        except:
            return {"speak": "I didn't understand, I think you are in the wrong place!"}
    
    def bfs(self, start, end):
        visited = set()
        queue = deque([(start, [start])])

        while queue:
            node, path = queue.popleft()
            if node == end:
                return path
            if node not in visited:
                visited.add(node)
                for neighbor in self.mappa[node]:
                    queue.append((neighbor, path + [neighbor]))
        
        return None


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
    
    def get_graph(self):
        return self.graph
    


#create timetable (dict)
lecture_rooms = {   "nn": ["A1", 8],
                    "robotics": ["A1", 10],
                    "vision": ["A1", 14],
                    "ml": ["A2", 10],
                    "nlp": ["A2", 12],
                    "ai": ["B1", 10],
                    "social": ["B1", 12],
                    "rl": ["B1", 14],
                    "dl": ["B2", 8],
                    "neuro": ["B2", 12],
                    "free": {"A1" : [12], "A2" : [8, 14], "B1": [8], "B2" : [10, 14]},
                    "library": [],
                    "A1": [],
                    "A2": [],
                    "B1": [],
                    "B2": []
                    }

#create map (graph)
mappa = Graph()
mappa.add_edge('S', 'C')
mappa.add_edge('C', 'D1')
mappa.add_edge('D1', 'D2')
mappa.add_edge('D1', 'A1')
mappa.add_edge('D2', 'A2')
mappa.add_edge('C', 'S1')
mappa.add_edge('S1', 'S2')
mappa.add_edge('S1', 'B1')
mappa.add_edge('S2', 'B2')
mappa.add_edge('S2', 'library')


#EXECUTOR
class Executor:
    def __init__(self, states):
        self.states = states

    def execute_plan(self, plan):
        for action in plan:
            if action == "speak":
                print(plan[action])
            else:
                for state in plan[action]:
                    print("Executing action: ", state, "that is go to a: ", self.states[state])

states = {  "S": "start",
            "library": "room",
            "A1": "room",
            "A2": "room",
            "B1": "room",
            "B2": "room",
            "C": "pass point",
            "S1": "pass point",
            "S2": "pass point",
            "D1": "pass point",
            "D2": "pass point",
            }




planner = PepperPlanner(lecture_rooms, mappa.get_graph())
executor = Executor(states)

while True:
    lecture_name = input("Enter the name of the lecture (or 'quit' to exit): ")

    if lecture_name.lower() == 'quit':
        break
    
    plan = planner.get_room_path(lecture_name)
    
    print("START EXECUTION")
    executor.execute_plan(plan)


