import random
import math

class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)


class User:
    def __init__(self, name):
        self.name = name


class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {} 

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
            return False
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
            return False
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)
            return True

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name) #User from class User ^
        #self.users is the dict then mapping ID to username (id 1-10)
        self.friendships[self.last_id] = set()
        # friendships also a dict {nums inside here 3, 4, 6,}
        # mapping the ID to the friendship


    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        ## graph = social network
        ## node = users/people
        ## edge = friendships
        ## connected components = user's extended social network
        ## BFS == (queue) find the shortest path hint in directions someone in extended network

        # Reset graph
        self.last_id = 0
        # last_id is the num on the outside (1, 2, 3, 4, 5, etc)
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME
        for i in range(num_users):  # loop thru users
            self.add_user(f"User {i + 1}")  # add each user
        # Add users
        possible_friendships = []

        # Create friendships

        ## NOTE: FROM CLASS below
        # target_friendships = (num_users * avg_friendships)
        # total_friendships = 0
        # collisions = 0
        # while total_friendships < target_friendships:
        #     #create a random friendship
        #     user_id = random.randint(1, self.last_id)
        #     friend_id = random.randint()




        for userID in self.users:
            # add 1 to look next to it
            for friendID in range(userID + 1, self.last_id + 1):
                # append to possible_friendships array and add USERID and FRIENDID
                # creates the empty SET()
                possible_friendships.append((userID, friendID))
        random.shuffle(possible_friendships)  # built in python function
        # .floor rounds down a float
        for i in range(0, math.floor(num_users * avg_friendships / 2)):
            # ^ finds the average
            friendships = possible_friendships[i] # [i] is index as you're looping thru
            self.add_friendship(friendships[0],friendships[1]) # goes into array and gets first index
            # and then the second index in friendships array (which is a list of random possible friendships)



    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # 1:[1] currently in visited
        # 3:[1, 3] will be in visited too if you pass in 3
        # !!!! IMPLEMENT ME
        ## NOTE: every means TRAVERSAL 
        # 1. create queue
        # 2. enqueue enque starting point in a list to start the path
        # 3. while queue not empty.. Dequeue the path, then find the last vertex
        # in path, and then DO THE THING but only if we haven't visited this
        # vertex before. THEN add to visited, then make new paths(copy) and enqueue
        # for each vertex. 
        ## NOTE: FROM CLASS below
        #create queue
        queue = Queue()
        queue.enqueue([user_id]) # equeue starting point in list to start path
        # while queue not empty
        while queue.size() > 0:
            #dequeue the path
            path = queue.dequeue()
            #find the last vertex in the path
            current_friend = path[-1]
            # if we havent visited that vertex
            if current_friend not in visited:
                # do the thing, add to visited dictionary path value
                visited[current_friend] = path
                #make new path(copy) and enqueue for
                for friend_id in self.friendships[current_friend]:
                    # ^ this is adjacency list
                    new_path = list(path)
                    new_path.append(friend_id)
                    queue.enque(new_path)

        return visited

                
## NOTE: below is from my own code
        q = Queue()
        # import queue above
        q.enqueue([user_id]) # pass in as a list 
        # path = [] # will be a dict
        # print("size:", q.size())
        while q.size() >= 1:
            # print("size:", q.size())
            path = q.dequeue()
            # print("path", path)
            current_user = path[-1] # CU will be last index of that path
            # first item added to the list, is also the first one removed
            if current_user not in visited: # if you haven't been there yet 
                # path.append(current_user)
                visited[current_user] = path.copy() #built in python method
                # if not, add current user to visited dictions, value will be path
                # print("self.friendships", self.friendships)
                # print("currentuser:", current_user)
                # print("Q:", q.queue)
                # print("wholething:", self.friendships[current_user])
                for friend in self.friendships[current_user]:
                    newpath = path.copy()
                    newpath.append(friend)
                    # print("path2", path)
                    q.enqueue(newpath)
                    # enqueue is like append

        #   friendships: {1: {3, 7}, 2: {8, 9}, 3: {1, 10}, 4: {10}, 5: {6, 7}, 6: {5}, 7: {8, 1, 5}, 8: {9, 2, 7}, 9: {8, 2}, 10: {3, 4}}          
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print("friendships:", sg.friendships)
    connections = sg.get_all_social_paths(1)
    print("connections:", connections)
