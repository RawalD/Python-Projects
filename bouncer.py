def game():
	userOne = input("UserOne Rock Paper Scissors ")
	msg = 0
	while msg < 10:
		print("NO CHEATING")
		msg += 1

	userTwo = input("UserTwo Rock Paper Scissors ")
	print("Shoot!")

	if userOne == " rock" and userTwo == "scissors":
		print("userOne Wins")
	elif userOne == "rock" and userTwo == "paper":
		print("userTwo wins")
	elif userOne == "paper" and userOne == "rock":
		print("userOne wins")
	elif userOne == "paper" and userTwo == "scissors":
		print("userTwo wins")
	elif userOne == "scissors" and userTwo == "paper":
		print("userOne wins")
	elif userOne == "scissors" and userTwo == "rock":
		print("userTwo wins")
	elif userOne == userTwo:
		print("its a draw")	
	else:
		print("no valid input")			

game()

play = input("Play again y/n")
if play == "y":
	game()
else:
	print("bye")						