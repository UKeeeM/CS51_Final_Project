# CS51_Final_Project
# Sean Cha, You-myeong Kim, Jiahui Huang

1) Please go to the terminal and set the directory to our final project folder

2) Type in “python main.py”

3) It should give you a list of options to choose from. Type in the option you desire. 
(Disclaimer: spam filtering option will take a LONG time. So we encourage you to try the other options first!)

4) The input for options 2~4 should be in the form of a list. If the input is non-numerical, please make sure to put ‘ ’ around it. The example (ex.) shows you the correct format to input. Also, the last element of the list is where the response (predicted result) would normally lie. You can put any NUMBER or just put ‘ignored’ in it. It will be ignored.

5) Once you type in the list and press enter, it will take a few seconds (more for spam filtering because we have much more data the random forest has to traverse through).

6) How to interpret the output:
	- first number is the random forest’s predicted outcome
	 (for example, in the titanic data, 0 means the person with such 
	  predictor variables would likely have died)
	- second number is the proportion of trees in the forest 
	  that voted on that outcome 