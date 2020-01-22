import random
import math


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
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        # last_id is the num on the outside (1, 2, 3, 4, 5, etc)
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME
        for i in range(0, num_users):  # loop thru users
            self.add_user(i)  # add each user
        # Add users
        possible_friendships = []
        # Create friendships
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
        # !!!! IMPLEMENT ME
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
