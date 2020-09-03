from flask import Flask, jsonify, request

app = Flask(__name__)

books = [{'Name': "The Hunger Games",
	  'book_id': "0",
	  'description': "Depicts the harshness of nation of Panem, North America"
			 "Contains the chronicles of a sixteen year old Katniss Everdeen"
			 "Inorder to win, she will have to make choices that weight survival against humanity and life against love",
	  'author': "Suzanne Collins",
          'price': "$10", 
	  'website': "visit goodreads.com to know more"},
	 {'Name': "Harry Potter and the Order of the Phoenix",
	  'book_id': "1",
	  'description': "Depicts young Harry's fifth year at Hogwarts"
			 "Growing threat of He-Who-Must-Not-Be-Named"
			 "Harry must discover the true depth and strength of his friends, and the shocking price of unbearable sacrifice",
	  'author': "J.K. Rowling",
          'price': "$15",
	  'website': "visit goodreads.com to know more"},
	{'Name': "To Kill a Mockingbird",
	  'book_id': "2",
	  'description': "Depicts childhood in a Southern town"
			 "Compassionate, dramatic and deeply moving"
			 "Takes readers to the roots of human behaviour",
	  'author': "Harper Lee",
          'price': "$9.99",
	  'website': "visit goodreads.com to know more"},
	{'Name': "The Book Thief",
	  'book_id': "3",
	  'description': "Young Liesel's life changes as she stands by her brothers grave"
			 "A love affair begins with books and words, as Liesel, learns to read"
			 "Readers experience a superbly crafted writing that burns with intensity",
	  'author': "Markus Zusak",
          'price': "$4.05",
	  'website': "visit goodreads.com to know more"},
	{'Name': "The Chronicals of Narnia",
	  'book_id': "4",
	  'description': "Contains journeys to the end of the world, fantastic creatures, and epic battles between good and evil"
			 "Draws the reader into a land where magic meets reality"
			 "Captivates fans with adventures, characters, and truths that speak to readers of all ages",
	  'author': "C.S. Lewis",
          'price': "$17",
	  'website': "visit goodreads.com to know more"},
        {'Name': "The Blue Umbrella",
          'book_id': "5",
          'description': "Depicts heroism and redemption"
                         "Short and humorous novel"
                         "Depicts villagers reaction to a girl having a fancy umbrella ",
          'author': "Ruskin Bond",
          'price': "$3.06",
          'website': "visit goodreads.com to know more"},
        {'Name': "Inferno",
          'book_id': "6",
          'description': "It is the first part of Italian writer Dante Alighieri's poem Divine Comedy"
                         "It depicts Purgatorio and Paradiso"
                         "This book tells the journey of Dante through Hell, guided by the ancient Roman poet Virgil",
          'author': "Dan Brown",
          'price': "$17",
          'website': "visit goodreads.com to know more"},
        {'Name': "Sherlock Holmes",
          'book_id': "7",
          'description': "Story of a fictional private detective, Sherlock Holmes"
                         "He solves crimes with his partner Sir Watson"
                         "Holmes is known for his proficiency with observation, deduction, forensic science and logical reasoning",
          'author': "Sir Arthur Conan Doyle",
          'price': "$13",
          'website': "visit goodreads.com to know more"},
        {'Name': "Ulysses",
          'book_id': "8",
          'description': "The novel establishes a series of parallels between the poem Odyssey and novel"
                         "The novel is highly allusive and also imitates the styles of different periods of English literature"
                         "It contains puns, parodies, and allusions- as well as its rich characterisation and broad humour",
          'author': "James Joyce",
          'price': "$8.99",
          'website': "visit goodreads.com to know more"},
        {'Name': "Romeo and Juliet",
          'book_id': "9",
          'description': "Tragedy written by William Shakespeare on two young lovers"
                         "Shakespeare's most popular play"
                         "The play focuses on romantic love, specifically the intense passion between Romeo and Juliet",
          'author': "William Shakespeare",
          'price': "$20",
          'website': "visit goodreads.com to know more"},
        {'Name': "Rhea",
          'book_id': "10",
          'description': "Very intriguing book, the writer takes imagination to the highest level"
                         "Story is refreshingly non-predictable"
                         "The book has a haunting quality the reader wont soon forget",
          'author': "Russ Martin",
          'price': "$35",
          'website': "visit goodreads.com to know more"},
	]

@app.route('/')
def index():
	return "Welcome to the Books API"

@app.route("/books", methods=['GET'])
def get():
	return jsonify({'Books':books})

@app.route("/books/<int:book_id>",methods={'GET'})
def get_book(book_id):
	return jsonify({'book': books[book_id]})

@app.route("/books", methods=['POST'])
def create():
	book = {'Name': "Gone with the Wind",
	        'book_id': "11",
	        'description': "Scarlett O'Hara, the beautiful, spoiled daughter of a well-to-do Georgia plantation owner, must use every means at her disposal to claw her way out of the poverty",
                'author': "Margaret Mitchell",
	        'price': "visit goodreads.com to know more"},
	books.append(book)
	return jsonify({'Created': book})



@app.route("/books/<int:book_id>",methods=['DELETE'])
def delete(book_id):
	books.remove(books[book_id])
	return jsonify({'result': True})


@app.route("/books/price/<float:amount>",methods=['GET'])
def price_in_India(amount):
    sum = (amount) * 73.49
    return jsonify({'cost in Indian Rupees':str(round(sum))})


if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5000, debug=True)
