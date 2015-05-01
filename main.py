'''
CS51 Final CS51_Final_Project
main.py

This is the umbrella function that implements the entire algorithm
'''
import training_data as td
import take_in_txt as tit
import CART_tree as cart
import rf as rf

if __name__ == "__main__":
	instruction = raw_input('enter 1 for spam filtering' + "\n"
		+ 'enter 2 for pima classification' + "\n"
		+ 'enter 3 for titanic classification' + "\n"
		+ 'enter 4 for prostate cancer classification' + "\n")
	if (instruction == "1"):
		f = raw_input('enter your email text' + "\n")
		row = []
		row.append(tit.count(f))
		row.append(tit.numbercount(f))
		row.append(tit.keyword_freq(f))
		row.append(tit.bigram_freq(f))
		row.append(tit.bigram_freq(f))

		spam_predict = row
		rf_result = rf.build_rf(td.spam, 500, 200, spam_predict)
		print(rf.rf_vote(rf_result))

	elif (instruction == "2"):
		input_list = raw_input('enter the following categories in a list format' 
			+ "\n" + "[glucose, diastolic, insulin, bmi, diabetes, age, 'ignored']"
			+ "\n"
			+ "ex. [89, 66, 94, 28.1, 0.167, 21, 'ignored']" + "\n")
		pima_predict = eval(input_list)
		check = rf.build_rf(td.pima, 100, 100, pima_predict)
		print(rf.rf_vote(check))

	elif (instruction == "3"):
		input_list = raw_input('enter the following categories in a list format'
			+ "\n" + "['class', 'sex', age, 'ignored']"
			+ "\n"
			+ "ex. ['3rd', 'male', 26, 'ignored'])" + "\n")
		titanic_predict = eval(input_list)
		check = rf.build_rf(td.titanic, 392, 300, titanic_predict)
		print(rf.rf_vote(check))
	
	elif (instruction == "4"):
		input_list = raw_input('enter the following categories in a list format'
			+ "\n" + "[pgtime, age, eet, g2, grade, gleason, 'ploidy', 'ignored']"
			+ "\n"
			+ "ex. [6.1, 64, 2, 10.26, 2, 4, 'diploid, 'ignored']" + "\n")
		stagec_predict = eval(input_list)
		check = rf.build_rf(td.stagec, 134, 300, stagec_predict)
		print(rf.rf_vote(check))

	else:
		print ("that was not an option")


''' code below was used to test the accuracy

	#pima_accuracy = test_accuracy(td.pima_training, td.pima_testing)
	#print (pima_accuracy)

	#titanic_accuracy = test_accuracy(td.titanic_training, td.titanic_testing)
	#print (titanic_accuracy)

	#stagec_accuracy = test_accuracy(td.stagec_training, td.stagec_testing)
	#print (stagec_accuracy)

	#spam_accuracy = test_accuracy(td.spam_training, td.spam_testing)
	#print (spam_accuracy)

'''




