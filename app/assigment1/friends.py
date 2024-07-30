# Question 8: Mr. Tony wants to find the person with most friends. You are presented with a users dict of keys=ids and values=usernames and a friendships list of user id tuples expressing a friendship between two users. Find out which user has the most friends. Return a tuple of friend name and his/her friends
# File path for question in repo: app/assignment1/friends.py
# Input:
# friendships = [(0, 1), (0, 2), (0, 4), (0, 5), (1, 3), (2, 4), (4, 5)]
# users={0: 'bob', 1: 'bob', 2: 'tim', 3: 'tim', 4: 'julian', 5: 'julian'}
# Output:
# (‘bob’, ['bob', 'julian', 'julian', 'tim'])
from collections import defaultdict

def most_friends(users, friendships):  

    # Create a dictionary to count the number of friends for each user
    friend_count = defaultdict(list)
    # Populate the friend_count dictionary
    for user1, user2 in friendships:
        friend_count[user1].append(users[user2])
        friend_count[user2].append(users[user1])
    # Find the user with the most friends
    max_friends_user = max(friend_count, key=lambda user: len(friend_count[user]))
    return (users[max_friends_user], friend_count[max_friends_user])

# Example usage
friendships = [(0, 1), (0, 2), (0, 4), (0, 5), (1, 3), (2, 4), (4, 5)]
users = {0: 'bob', 1: 'bob', 2: 'tim', 3: 'tim', 4: 'julian', 5: 'julian'}
result = most_friends(users, friendships)
print(result)  # Output: ('bob', ['bob', 'tim', 'julian', 'julian'])