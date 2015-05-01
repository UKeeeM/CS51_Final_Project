# This is a function to help us with preprocessing data in a format
# that our random tree will follow

import os 
import string
import rf as rf
import training_data as td

#counts the number of words in a file
def count(f):
	words = string.split(f)
	wordCount = len(words)
	return wordCount

#list of key words we took from spam filter tool website spam assasin
key_word = ["money", "adult", "movie","download" "win", "free", "shipping" , "today", "here", "avaliable"
			"fingertip", "cheap","erection", "rock","online", "as seen on", "buy","clearance", "singles", 
			"satisfied", "viagra", "ad", "amazing","avoid", "single","singles",
			"billion","beverage","bonus","get","hidden","only","open","opportunity",
			"order","password","price","phone","cash","check","click","collect",
			"loans","subscibe","stock", "lega","life","insurance","income","instant",
			"remove","sex","hookup","sample","satisfaction", "earn", "$","medium","penis","enlarge","lengthen",
			"medicine","urgent","vicodin", "fees", "XXX", "offer","winner","xanax", "investment"
			"crisis","miracle","age", "doctor","aging", "shipping", "lottery",
			"boss","fitness","pain","injury","premature","date", "enlargement", "pills", "pill",
			"diet", "quick", "fast", "now", "cash", "nigerian", "prince", "fantastic", "wife",
			"bride", "single", "area", "neighborhood", "close", "satisfied", "opportunities",
			"loving", "sexual", "fantasy", "huge", "enormous", "bed", "tonight", "beloved",
			"boost", "invited", "more", "benefits", "benefit", "reminder", "pleasant",
			"pleasance", "vigorous", "alternative"]

def keyword_freq(f):
	frequency = 0
	words = string.split(f)
	for word in words:
		word_l = word.lower()
		if word_l in key_word:
			frequency += 1 
		else:
			frequency
	return frequency 

def numbercount(f):
	frequency = 0
	words = string.split(f)
	for word in words:
		frequency += sum(c.isdigit() for c in word)
	return frequency

# this is a function that tells us whether the email has 
#top 10 most common words used in spams. 
#def has_top_10(f):

# Function creates a dictionary of key = Bigram and value = frequency
def bigram(f):
	words = string.split(f)
	output = {}
	for i in range(len(words)-2+1):
		g = ' '.join(words[i:i+2])
		output.setdefault(g, 0)
		output[g] += 1
	return output
# also some trigger words from spam filter website spam assasin 
bigram_triggers = ["reverse aging","reverses againg","hidden assets",
"stop snoring","free investment","dig up", "dirt on","stock disclaimer",
"multi leve","level marketing","compare rates", "cable converter", 
"remove wrinkles", "meet singles","free money","free grant","bank account", 
"amazing stuff", "cash bonus","free preview", "no investment","serious cash", 
"free installation","stay strong","free membership", "meet singles", 
"meet single", "your area", "extra income","fantastic deal","for free",
"for only","from","free access", "order now", "order status","please read",
"great offer","real thing", "refinance home","laying around","call now",
"call free","lose weight","fas viagra","easy terms","don't delete","work at",
"limited time", "free dvd","been selected","bad credit","to earn","fantastic deal", "online pharmacy", "join millions","get paid", "its legal","own boss"]

def bigram_freq(f):
	frequency = 0
	words = bigram(f)
	for word in words.keys():
		word_l = word.lower()
		if word_l in bigram_triggers:
			frequency += words[word] 
		else:
			frequency
	return frequency 


if __name__ == "__main__":
	f = raw_input('enter your email text' + "\n")
	row = []
	row.append(count(f))
	row.append(numbercount(f))
	row.append(keyword_freq(f))
	row.append(bigram_freq(f))
	row.append(bigram_freq(f))

	spam_predict = row
	rf_result = rf.build_rf(td.spam, 500, 200, spam_predict)
	print(rf.rf_vote(rf_result))



#Below were the codes that we used to export the spam and ham training data 	
'''
# here we assign a value to indicate whether it is a spam or not, 1 for spam 
def spam_indicator(f):
	return "1"

#here we assign a value 0 to indicate ham	
def ham_indicator(f):
	return"0"

def get_filepaths(directory):
	file_paths = []  # List which will store all of the full filepaths.

	# Walk the tree.
	for root, directories, files in os.walk(directory):
		for filename in files:
			# Join the two strings in order to form the full filepath.
			filepath = os.path.join(root, filename)
			file_paths.append(filepath)  # Add it to the list.
	return file_paths  # Self-explanatory.

# Run the above function and store its results in a variable.   
full_file_paths = get_filepaths("/Users/Jiahui/CS51_Final_Project/spam")
full_file_paths_2 = get_filepaths("/Users/Jiahui/CS51_Final_Project/ham")


if __name__ == "__main__":
	files = []
	files_2 = []
#	path = '/Users/Jiahui/CS51_Final_Project/spam'
#	listing = os.listdir(path)
	
	for fname in full_file_paths:
		file_object = open(fname)
		files.append(file_object.read())

	for fname in full_file_paths_2:
		file_object_2 = open(fname)
		files_2.append(file_object_2.read())


	result = []

	for f in files:
		row = []
		row.append(count(f))
		row.append(numbercount(f))
		row.append(keyword_freq(f))
		row.append(bigram_freq(f))
		row.append(spam_indicator(f))
		result.append(row)

	for f in files_2:
		row = []
		row.append(count(f))
		row.append(numbercount(f))
		row.append(keyword_freq(f))
		row.append(bigram_freq(f))
		row.append(ham_indicator(f))
		result.append(row)

	with open ("spam.csv", "wb") as f:
		writer = csv.writer(f)
		writer.writerows(result)
'''








