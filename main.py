# website is now a Python package so functions cna be imported from it
from website import create_app

app = create_app()

# The web server is only launched when the main file is run
if __name__ == '__main__':
    # Everytime there is a change in the code, the web server will be rerun
    app.run(debug=True)