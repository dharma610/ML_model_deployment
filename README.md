## ML-Model-Flask-Deployment(Locally)

Project Details:
This project has four major parts :

1) **02-Linear Regression Project.ipynb** - This is a jupyter notebook containing model to be implemented
2) **app.py** - This contains Flask APIs that receives details through GUI or API calls, computes the precited value based on our model and returns it.
3) **request.py** - This uses requests module to call APIs already defined in app.py and dispalys the returned value.
4) **templates** - This folder contains the HTML template to allow user to enter required details and displays the predicted value.

Running the jupyter notebook containing model, would create a serialized version of our model into a file **lm_model.pkl**

Run app.py using below command to start Flask API
**python app.py**

By default, flask will run on port 5000.

Navigate to URL http://localhost:5000
You should be able to view the homepage.

Now fill the required details and click on predict button and you can see the prediction.
