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


## ML-Model-Flask-Deployment(Heroku Cloud)
we need two extra things which is 
1) **Procfile** - For Heroku to be able to run our application like it should, we need to define a set of processes/commands that it should run beforehand. These commands are        located in the Procfile:<br>
     web: gunicorn app:app 

2) **requirements.txt** - we need to define which libraries our application uses. That way, Heroku knows which ones to provide for us, similar to how we install them locally          when developing the app.

     This way we end up with a requirements.txt file that contains the libraries we're using and their versions:<br>

     Flask==1.1.1<br>
     gunicorn==19.9.0<br>
     itsdangerous==1.1.0<br>
     Jinja2==2.10.1<br>
     MarkupSafe==1.1.1<br>
     Werkzeug==0.15.5<br>
     numpy>=1.9.2<br>
     scipy>=0.15.1<br>
     scikit-learn>=0.18<br>
     matplotlib>=1.4.3<br>
     pandas>=0.19<br>
