import psutil
from flask import Flask, render_template

#The Flask module is used to create a web application. The app object represents the Flask application
#The __name__ argument is passed to the Flask constructor, which helps Flask determine the root path for the application
app = Flask(__name__) 

@app.route("/")
def index():

#The index function calculates the CPU utilization percentage and the memory usage percentage
    cpu_percent = psutil.cpu_percent()
    mem_percent = psutil.virtual_memory().percent
    Message = None
    if cpu_percent > 75 or mem_percent > 75:
        Message = "High CPU or High Memory Utilisation detected. Please scale up!"
    return render_template("index.html", cpu_percent=cpu_percent, mem_percent=mem_percent, message=Message)


#this used to execute code only if the file was run directly as a script, and not imported
if __name__ == '__main__':
    #Flask will run in debug mode andcan be accessible from any IP address
    app.run(debug=True, host='0.0.0.0')
