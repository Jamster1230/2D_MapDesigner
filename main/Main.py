from helpers.application import app
# Main

if __name__ == "__main__" :

    App = app()
    App.cleanup()
    App.destroy()