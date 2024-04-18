from app import app
import util2
if __name__ == "__main__":
    print("starting python flask server for prediction....")
    util2.load_saved_artifacts()
    app.run()