# Common_pattern_python

Yep, This repository will include common patterns in python which I usually encouter when I work on company's project and my pet project :D 

#Patterns

##MVC(Model-View-Controller)

###Description 

We will separate into 3 parts:

1./ Model:

1.1/ Description:
    Handle about database, It provides knowledge : data and how to work with that data.Model will work independently with view and controller.
1.2/ Requirement:
    + Create data models and interface of work with them
    + Validate data and report all errors to the controller
    + Avoid working directly with user interface

2./ View:

2.1/ Description:
    Appearance of knowledge,View receives data from model though the controller and is responsible for it's visualization.It should not contain complex logic, all such logic should goto the models and controllers

2.2/ Requirement:
     + Try to keep them simple, use only simple comparisons and loops
     + Accessing the database directly

3./ Controller : The glue between the model and view

3.1/ Description:

    + Pass data from user requests to model for processing, retrieving and saving the data
    + Pass data to views for rendering
    + Handle all request errors and errors from models
Avoid the following in controllers:
    + Render data
    + Work with the database and businees logic directly
    
=> We need smart models, thin, controllers. and dumb views.
