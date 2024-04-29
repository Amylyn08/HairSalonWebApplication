from hairsalon_app._init_ import create_app

app = create_app()

if __name__== '__main__':
    app.run(port=5010, debug=True)
else:
    app.run(port=5010, debug=True)
