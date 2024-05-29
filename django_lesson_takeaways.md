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