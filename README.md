# GROUP M

Rao,Deepthi

Renich,Vincent

Fernandez, Hanna

Instructions for The Last One

1. Clone this repository
2. Navigate to CardGames
3. run 'python3 theLastOne.py'
4. Follow the prompts specified to set up the Gaming environment
   	PLEASE BE SURE TO ENTER THE EXACT STRINGS SPECIFIED OR BEHAVIOR WILL NOT BE AS EXPECTED
5. Each player places a card from their hand. Their hand and the current card at the top of the pile will be displayed by the program.
	INPUTTING INVALID STRINGS WILL CAUSE THE CURRENT PLAYER TO DRAW A CARD
6. The special cards will show specific instructions to follow.

Instructions for Egyptian Rat Screw

1. Clone this repository on every machine you want to use
2. Navigate to CardGames on every terminal you want to use
3. On one machine/terminal, run 'python3 server.py' or 'python3 server.py -p <PORT>'
For this, <PORT> is the port number to use for connections.
If you don't specify this, the port will be 2222.
4. On a number of other machines/terminals (players) that is a factor of 52, run 'python3 client.py <HOST> <PORT>'
For this, <HOST> is the hostname of the server machine, and <PORT> is the port number that the
server is listening on. Both of these are printed by the server when it starts.
5. On each client terminal, enter the player name for that client.
6. Using the first terminal connected (the Game Master), enter '/start ers'
This will start the game.
7. Using any client terminal, enter any text to proceed to the next play by a player.
8. To exit, type 'exit' on each client terminal, and type CTRL+C on the server terminal until
   the program exits.
