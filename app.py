#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install flask


# In[2]:


from flask import Flask, request, render_template


# In[ ]:


app = Flask(__name__)
# indicates that this website belongs to you

@app.route("/", methods = ["GET","POST"])
# decorator is a function that runs before the actual function
def index():
    # flask framework
    if request.method == "POST":
        rate = float(request.form.get("rate")) # rate that is input by user
        print(rate)
        
        # It outputs the value of rate to the console or terminal where the Flask application is running. 
        # This can be helpful for developers to see what data is being received and processed by the server
        
        return(render_template("index.html", result = -50.6 * rate + 90.2))
        # return(render_template("index.html", result = "Machine Model not ready"))
    else:
        return(render_template("index.html", result = "waiting for FX rate..."))
     # result should reference the ML model
    
if __name__ == "__main__":
    app.run()
   

