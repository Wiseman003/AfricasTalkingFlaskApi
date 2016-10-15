from Flask import Flask

app = Flask('rodgy')

@app.route('/api/categoty/books', methods=['GET', 'POST'])
def book_api():
	return 'some resource'

if __name__ == '__main__':
	app.run()