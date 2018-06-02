import os
from nltk.corpus import reuters

def createDocumentFolder():
	directory_document = os.getcwd() + '/Document'
	directory_test_data = directory_document + '/test-data'
	directory_training_data = directory_document + '/training-data'
	if not os.path.exists(directory_document):
		os.makedirs(directory_document)
	if not os.path.exists(directory_test_data):
		os.makedirs(directory_test_data)
	if not os.path.exists(directory_training_data):
		os.makedirs(directory_training_data)

def createCategoriesFolder(path, category):
	directory = path + category
	if not os.path.exists(directory):
		os.makedirs(directory)

def createNewDoc(filename, doc_id):
	f = open(filename,"w+")
	f.write(reuters.raw(doc_id))
	f.close()

def extractNews():
	createDocumentFolder()
	test_data_path = os.getcwd() + '/Document/test-data/'
	training_data_path = os.getcwd() + '/Document/training-data/'
	total_doc_training = 0
	total_doc_test = 0
	for category in reuters.categories():
		createCategoriesFolder(test_data_path, category)
		createCategoriesFolder(training_data_path, category)
		id_doc_training = 1
		id_doc_test = 1
		for doc_id in reuters.fileids(category):
			if doc_id.startswith("train"):
				filename = training_data_path + category + '/Categories_' + category + 'Doc_' + str(id_doc_training) + ".csv"
				createNewDoc(filename, doc_id)
				id_doc_training += 1
				total_doc_training += 1
				print("Category : " + category + " | Doc_Id : ",total_doc_training + " | Type : Training_data")
			else:
				filename = test_data_path + category + '/Categories_' + category + 'Doc_' + str(id_doc_test) + ".csv"
				createNewDoc(filename, doc_id)
				id_doc_test += 1
				total_doc_test += 1
				print("Category : " + category + " | Doc_Id : ",total_doc_test + " | Type : Test_data")
	print("Total document on training dataset : ", total_doc_training)
	print("Total document on test dataset : ", total_doc_test)
	print("Total document : ", total_doc_training+total_doc_test)

extractNews();
