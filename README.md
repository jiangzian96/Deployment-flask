## ML-Model-Flask-Deployment
This is a demo project to elaborate how machine learning models can be containerized and deployed using Flask API both locally and on cloud.

### Prerequisites
You must have the packages listed in ```requirements.txt``` installed.

### Project Structure
This project has five major parts :
1. ```model.py``` - A simple linear regression model that predicts employee salary based on training data in ```hiring.csv``` file.
2. ```app.py``` - Flask APIs that receives employee details through API calls and then the model makes a prediction and return in JSON format.
3. ```make_prediction.sh``` and ```make_prediction_aws.sh``` - Two shell scripts that send a sample input through a POST request and then return the model prediction both locally and on cloud (AWS ECS).
4. ```Makefile``` - for setting up the project with virtual environment and the required packages.
5. ```Dockerfile``` - for containerizing the application and deploy it on cloud.

### Running the project locally
1. Create a Python virtual environment by running 
```
python3 -m venv ~/.venv
```
and activate the virtual environment
```
source ~/.venv/bin/activate
```

2. Install the required packages by running
```
make install
```

3. Ensure that you are in the project home directory. Train the machine learning model
```
python model.py
```
This would create a serialized version of our model into a file ```model.pkl```

2. Run app.py using below command to start Flask API
```
python app.py
```
By default, flask will run on port 5000.

3. Change the input data in ```make_prediction.sh``` and run it.
