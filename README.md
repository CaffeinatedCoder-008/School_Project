# School_Project
# Flask Web Application Project

This repository contains a Flask web application project that offers several functionalities, each implemented as a separate Flask application. These functionalities provide various tools and calculators to perform tasks related to mathematics and computation.

## Functionalities

1. **Fibonacci Series Generator**: This application allows users to generate Fibonacci series based on their input. The Fibonacci series is a sequence of numbers where each number is the sum of the two preceding ones, typically starting with 0 and 1.

2. **Marks Calculator**: The Marks Calculator application enables users to calculate the total and average marks for five subjects. Users can input their marks for each subject, and the application will provide the total marks obtained and the average marks.

3. **Circle Calculator**: With the Circle Calculator application, users can compute the circumference and area of a circle based on the input radius. The application utilizes standard mathematical formulas to determine the circumference and area of the circle.

## Getting Started

To run each functionality individually on your local machine, follow these steps:

1. Clone the repository to your local machine: git clone https://github.com/Dev-droid1/School_Project
2. Navigate to the directory of each Flask application (e.g., `fibonacci_app`, `marks_app`, `circle_app`).
3. Install the required dependencies by running: pip install -r requirements.txt
4. Run each Flask application by executing its Python file: python appname.py
5. Each application will be accessible at `http://127.0.0.1:5000/` by default.

## Deployment

To deploy the Flask applications to a production environment, you can use a WSGI server like Gunicorn along with a reverse proxy like Nginx or Apache. Here are the basic steps:

1. Install Gunicorn: pip install gunicorn
2. Run each Flask application with Gunicorn: gunicorn --bind 0.0.0.0:8000 wsgi
3. Set up a reverse proxy (e.g., Nginx) to handle incoming requests and serve static files.

 ## Contributing

Contributions are welcome! If you have any ideas for improvements or new features, feel free to open an issue or submit a pull request.
  
