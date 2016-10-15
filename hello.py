from flask import Flask
from flask import jsonify, make_response
app = Flask('rodgy-library')

books = {
	'name': 'Harry Potter and the priosoner',
	'auther': 'jk. Rowling',
	'category': 'Magic/Fiction',
	'id': '4325345234'
}

@app.route('/api/category/books/', methods=['GET', 'POST'])
def book_api():
	return jsonify(books)

if __name__ == '__main__':
	app.run()