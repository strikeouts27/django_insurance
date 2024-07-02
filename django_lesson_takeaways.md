when i am creating a view I need to specify where the template is located. 
quote/customer.html -> WRONG
quote/templates/customer.html -> WRONG 
DJANGO  will only start its search for templates by looking for the templates folder which i must create. 

# Create your views here.

def customer_page(request):
    return render(request, "customer.html")

When trying to activate a virtual enviornment use the tab key. 
The documentation is wrong you have to use / not \

github -f force pushes changes into the repostiroy 
it takes your changes and does not merge anything it clobbers what isup there. 

the view is the gatekeeper to the model. the view specifies what information the form can access. 
the view is based off of the model in models.py. 

Go to the django docs and look at the built in django views, forms, etc. 
See the example and see how they implemented it by importing it in. 
see the different attributes that are included in the example that are good things to implement. 

highlighting a view and pressing f12 allows us to see what the source code is comming from and how it was built.
my own code and the built in django code.  
this is the definition command. 

right click view page source is helpful for inspecting things. 

block content tags are used to control what code is extended in a extends command. you don't have to extend everything in an extend command. 

extend code will do something to it and show it. 
extended -> 

vs include extension. 

block content and endblock content -> they filter out what is extended on extendes. they over write what is extended in the file. 

instead of making the html myself, django forms will do that for me by utilizing forms.py and views and logic. 

the order would be as the path(url describes)

url takes the string url to be used. than the view logic inside of it orders a template to be called. 
that template is called.
and inside of that template is the order to extended base.html if extendes is used. 

block content and endblock tags have to be placed inside base.html somewhere to tell django where to overwrite the code with whatever is inside the block tag. 

whats inside the block tags is what is being overwritten. 

Createview is a way to create an object that can be stored in a database. 
In laymans terms this is one of the ways you can create and save information in a database. 

Shift Alt is a command that lets you select a column so you can make multichanges to columns. Real style! 

UpdateView requires a template in order to be sent to the browser. a new url will be necessary. 

If we see a FieldError that means a field is in the createview or update view that is not what the model has. one of the possible errors. 

path converters takes a url that you type in the browser and it tries to match that with one the urls with urls.py

if i do not know what to do, try clicking around the django documentation for things. 
