from app import app
import util
if __name__ == "__main__":
    print("starting python flask server for prediction....")
    util.load_saved_artifacts()
    app.run()