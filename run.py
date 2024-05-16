from hairsalon_app.__init__ import create_app

app = create_app()

if __name__== '__main__':
    app.run(port=5010, debug=True)
else:
    app.run(port=5010, debug=True)
