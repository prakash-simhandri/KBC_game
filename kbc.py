import pyttsx3
print("________Welcome to the KBC game_________\n")
def spech(text):
	engine = pyttsx3.init()
	engine.setProperty("rate",140)
	engine.setProperty("volume",2)
	engine.say(text)
	engine.runAndWait()
spech("Welcome to the KBC game!")


question		=['Which of these following Hindi Idioms means to promise someone','In which month are the harvest festivals Pongal, Magh Bihu and Lohri celebrated ','Which of these following is also the name of a popular Microsoft program','Who is the singer of Makhna ( Audio question)','In which state did the Bharatiya Janata Party from their government for the first time','The weight of diamonds is usually measured in what?','Who of these politicians is this person talking about?','Which state of India has the shortest coastline?','(mere samne wali khidki) This song is from which film?','Vasant, Vinod, Mahasukh, Gautam and Rajesh are brothers related to whih of these business families?','Who is the first Indian woman wrestler to win a gold medal at the Asian Games?','Which of these viruses takes it\'s name from a place in Malaysia?','Which of these planets has a solid surface?','Who holds the Guinness Wole Record for the oldest person to be elected for the first time as PM of a nation?','According to the Mahabharata, who was the father of Chitrasena, Vrishasena and Satyasena?']
first_options	=['1) Give your Word',		'1) February',	'1) Paragraph',	'1) Raftaar',		'1) Himachal Pradesh',	'1)Tola',	'1) Mohammad Azharuddin',		'1) Goa',			'1) Raabta',				'1) Hinduja',	'1) Sakshi Malik',	'1) Nipah',		'1) Mars',		'1) P V Narasimha Rao',		'1) Arjuna']
second_options	=['2) Giving your hand',	'2) March',		'2) Sentence',	'2) Honey Singh',	'2) Sikkim',			'2) Carat',	'2) Kirti Azad',				'2) Maharashtra',	'2) Hindi Medium',			'2) Adani',		'2) Babita Kumari',	'2) Ebola',		'2) Saturn',	'2) Chaudhary Charan Singh','2) Karna']
third_options	=['3) Giving your heart',	'3) April',		'3) Word',		'3) Badshah',		'3) Tripura',			'3) Maund',	'3) Imran Khan',				'3) Odisha',		'3) Padosan',				'3) Ambani',	'3) Vinesh Phogat',	'3) Influenza',	'3) Jupiter',	'3) Morarji Desai',			'4) Dhritarashtra']
fourth_options	=['4) Giving your shoulder','4) January',	'4) Statement',	'4) Mika Singh',	'4) Assam',				'4) Troy',	'4) Mansoor Ali Khan Pataudi',	'4) West Bengal',	'4) Badrinath Ki Dulhania',	'4) Ruia',		'4) Kavita Devi',	'4) HIV',		'4) Uranus',	'4) H D Deve Gowda',		'4) Yudhishthira']
all_options		=[first_options,second_options,third_options,fourth_options]
ans_key			=[1,4,3,2,4,2,3,1,3,2,3,1,1,3,2]
price			=[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,10000000]
question_level  =["first", "second", "third", "fourth", "fifth"]
i=0
padhav=0
question_level_num=0
Total_Amount = 0
while i < len(question):
	print("Your {} question is:".format(question_level[question_level_num]))
	spech("Your {} question is:".format(question_level[question_level_num]))
	print (question[i],"\n")
	spech(question[i])

	print("Your options are:")
	spech("Your options are:")
	print (first_options[i],"\n")
	spech(first_options[i])

	print (second_options[i],"\n")
	spech(second_options[i])

	print (third_options[i],"\n")
	spech(third_options[i])

	print (fourth_options[i],"\n")
	spech(fourth_options[i])

	spech("input your option number")
	user=int(input("input your option number  >"))
	

	if user!=ans_key[i]:
		print ("Your answer is wrong")
		spech("Your answer is wrong")
		break
	print ("Your answer is correct! and you also wined {} rupees.".format(price[i]),"\n")
	spech("Your answer is correct! and you also wined {} rupees.".format(price[i]))

	Total_Amount+=price[i]
	i+=1	
	question_level_num+=1
	if i %5==0:
		print ("Congrats! Your {} stop is complete.".format(question_level[padhav]))
		spech("Congrats! Your {} stop is complete.".format(question_level[padhav]))
		question_level_num=0
		padhav+=1
if Total_Amount == 0:
	print("sorry! You lost the game")
	spech("sorry! You lost the game")
else:
	print("Congrates! you win Total Amount is {} rupayes".format(Total_Amount))
	spech("Congrates! you win Total Amount is {} rupayes".format(Total_Amount))
	print("thank you")
	spech("thank you! by by")
