# BulletinBoard

#### Requirements:

#### part 1

- Client:
  - a client joins by connecting to a dedicated server
  - Need to input a non-existent user name
  - not required to implement any user authentication mechanisms

- Server:

  - listens on a specific non-system port endlessly

  - keeps track of all users that join or leave the group

- When a user joins or leave,all other connected clients get notified by the server.

-  When a user (or client) joins the group, he/she can only see the last 2 messages that were posted on the board
-  A list of users belonging to the group is displayed once a new user joins

- When a user posts a new message, other users in the same group should see the posted message
  - Message ID
  - Sender
  - Post Date
  - Subject
- A user can retrieve the content of a message by contacting the server and providing the message ID as a parameter.
- provide the option to leave the group
- Once a user leaves the group, the server notifies all other users in the same group of this event.

#### part 2

- 5 groups

- The user can select the desired group by id or by name

- A user can join multiple groups at the same time

- user in one group cannot see users in other groups as well as the messages they have posted.