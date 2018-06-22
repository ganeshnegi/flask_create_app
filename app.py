from project import create_app

if __name__== "__main__":
	app = create_app('config.Config')
	app.run(debug=True)