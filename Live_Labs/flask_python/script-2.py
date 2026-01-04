from flask import Flask  

app = Flask(__name__) #creating the Flask class object   

@app.route('/home') #decorator    
def home():  
    return "hello, welcome to our website.";  

if __name__ =='__main__':  
    app.run(debug = True)  

"""Initial we get
Not Found
The requested URL was not found on the server. If you entered the URL manually 
please check your spelling and try again.

when we change url by adding /home we get:
hello, welcome to our website."""