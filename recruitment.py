def main():
	#write your code here
	print("Welcome to the special recruitment program, please answer the following questions:")
	skills = ["Python", "C++", "JavaScript", "Meeting", "Leeting", "Eating"]
	cv = {}

	cv["name"] = input("What's your name? ")
	cv["age"] = int(input("How old are you? "))
	cv["experience"] = int(input("How many years of experience do you have? "))
	cv["skills"] = []

	counter = 1
	print("Skills:")
	for skill in skills:
		print(str(counter) + ". " + skill)
		counter += 1
	
	user_skill_1 = int(input("Choose a skill from above by entering its number: "))
	cv["skills"].append(skills[user_skill_1 - 1])
	user_skill_2 = int(input("Choose another skill from above by entering its number: "))
	cv["skills"].append(skills[user_skill_2 - 1])

	
	if (cv["age"] >= 25 and cv["age"] <= 40 and cv["experience"] > 5 and skills[5] in cv["skills"]):
		print("You have been accepted, " + cv["name"])
	else:
		print("You have been rejected, " + cv["name"])
	print(cv)

	
if __name__ == '__main__':
	main()