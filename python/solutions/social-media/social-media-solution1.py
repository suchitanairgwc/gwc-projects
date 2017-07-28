# User Class
# manages user information like id, name, username
# stores a single user's connections
class User:
    # Constructor for user class
    def __init__(self, username, fullname, userid):
        
        self.userName = username
        self.userFullName = fullname
        self.id = userid 
        self.connections = []
   
   # Method to set connections for a given user
   # A user can have multiple connections
    def set_connections(self, userID):
        self.connections.append(userID)

    # Get user's connnections
    def get_connections(self):
        return self.connections
	
    # Get user's full name
    def get_fullname(self):
        return self.userFullName

    # Get user's username
    def get_username(self):
        return userName
    
    # Get user's ID
    def get_id(self):
        return self.id
 
# Network Class
# Keeps a list of all users
# Checks if users to be connected exist and calls each user's set connection method to connect user A to user B     
class Network:

    # Constructor for network class
    def __init__(self):
        self.users = {}
        
    # Add users to the users list
    def add_users(self, user, user_id):
        self.users[user_id] = user

    # Connect user A to user B if they both exist and are not already connected. 
    def add_connections(self, firstUserId, secondUserId):
        firstUserFound = False
        secondUserFound = False 

        if self.users.get(int(firstUserId)):
            user = self.users[int(firstUserId)]
            firstUserFound = True
            firstUser = user
        else:
             print ("User1 specified is invalid")
        if self.users.get(int(secondUserId)):
            user = self.users[int(secondUserId)]
            secondUserFound = True
            secondUser = user
        else:
            print ("User2 specified is invalid")
        if secondUserId in firstUser.get_connections():
            print ("User %s and %s are already connected" %(firstUser.get_fullname(), secondUser.get_fullname()))
        elif firstUserId == secondUserId:
            print ("First user and second user are the same, cannot connect to self")
        else:
            firstUser.set_connections(secondUserId)
            secondUser.set_connections(firstUserId)

	
    # Method to return a user object
    def get_usersList(self):
        return self.users

    # Method to print connections for a given user
    def printConnections(self, userID):
        if self.users.get(int(userID)):
            user = self.users.get(int(userID))
        else:
            print ("This specified user does not exist in the network")
            return -1
        connections = user.get_connections()
        if len(connections) == 0:
            print ("This user is lonely!")
        else:
            for connection in connections:
                connectedUser = self.users[int(connection)]
                print (connectedUser.get_fullname())

    # Method to print users
    def printUsers(self):
        if bool(self.users):
            for id, user in self.users.items():
                print (id, user.get_fullname())
        else:
            print ("Network has 0 users, you need to add users")
    
    


def main():
    input_option = None
    input_value = None
    userid = 0
    list_of_users = []
    
    # Variable that stores the options print list
    cmd_options = """
    \n\
    1. Add User
    2. Add Connections
    3. List all users in this network
    4. List Connections for a given user
    5. Quit
    """ 
    # Network class instance should only be created once, before the while loop
    network = Network()    
    while input_option != 'quit':
        # print options
        print (cmd_options)
        input_value = input('Pick an option number from above: ')
        if input_value == '1':
            username = input('Specify a username for the user: ')
            fullname = input('Specify a full name for the user: ')
            userid += 1
            newUser = User(username, fullname, userid)
            addUserId = newUser.get_id()
            network.add_users(newUser, addUserId)
        elif input_value == '2':
            network.printUsers()
            if not bool(network.get_usersList()):
                print ("You cannot add connections when there are no users in the network.")
            else:
                firstUserID = input("Enter number(ID) for first user: ")
                secondUserID = input("Enter number(ID) for second user: ")
                network.add_connections(firstUserID,secondUserID)
        elif input_value == '3':
            network.printUsers()
        elif input_value == '4':
            network.printUsers()
            userID = input("Enter ID(number) for the user to print connections: ")
            network.printConnections(userID)
        elif input_value == '5':
            input_option = 'quit'
       

if __name__ == '__main__':
    main()
