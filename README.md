# Flask_and_Docker

Deploying Machine Learning and NLP models using Flask and docker
This model can be run in the development server.

This is not configured with the Apache to use in the production enviornment

# Libraries used :

Used flasgger 0.8.1 and sci-kit learn : 0.22.1 
All the required librariesare mentioned in the "requirements.txt" file

# Docker Commands :

Base Image : continuumio/anaconda3:4.4.0

To build the container , run the following command 

      sudo docker build -t rf-api .  ("." stands for current directory)

To check whether the image has been built:

      sudo docker images 

To run the container , use :
     
      sudo docker run -p 5000:5000 rf-api
      
      -p : is a port I have used explicitly 

# To test :

Go to explorer and type the following in the URL box :

localhost:5000/apidocs


  
