import io
from django.contrib.auth import REDIRECT_FIELD_NAME, login
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render,redirect
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from orders.forms import OrderCreateForm
from orders.models import OrderItem,Order
from django.contrib.auth import logout as auth_logout
from parts.models import Product
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from .forms import OrderForm, SignUpForm
from django.contrib.auth.views import LoginView    
from .models import Category, Product, Profile, Slider
from django.views.generic import TemplateView, ListView
from django.db.models import Q
from fpdf import FPDF
from django.http import FileResponse
from xhtml2pdf import pisa
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from django.core.mail import BadHeaderError, send_mail
from reportlab.pdfgen    import canvas
from reportlab.lib.utils import ImageReader
from io import StringIO
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from html import escape
from .render import Render
from django.views.generic import View

# Create your views here.
 


class SearchResultsView(ListView):
    model = Product
    template_name = 'search/search_results.html'
    def get_queryset(self): 
        query = self.request.GET.get('q')
        object_list = Product.objects.filter(
            Q(name__iregex=query) 
        )
        return object_list

def product_list(request, category_slug=None,):
    last_four = Product.objects.all().order_by('-id')[:12]
    slider = Slider.objects.all().order_by('-id')[:3]
    category = None
    
    categorys = Category.objects.all()
    products = Product.objects.filter(available=True)
    
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category_id=category)
    return render(request,
                  'product/list.html',
                  {'category': category,
                   'categorys': categorys,
                   'products': products,'last_four':last_four,'slider':slider})



def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    
    return render(request, 'product/detail.html', {'product': product,})


def signup(request):
    
    
    
    
    
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        
        if form.is_valid () :
            form.save()
            username = form.cleaned_data.get('username')
            
            
            raw_password = form.cleaned_data.get('password1')
            response = redirect('/')
            return response
            
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})



def index(request):
    slider = Slider.objects.all().order_by('-id')[:6]
    return render(request,'index.html',{'slider':slider})

def contact(request):
    return render(request,'contact.html',)


def about(request):
    return render(request,'about.html',)

@login_required
def personal(request):
    
    context ={}
    userid = request.user
 
    
    context["dataset"] = Order.objects.filter(userid = userid)
         
    

    return render(request,'personal.html',context)

class Pdf(View):
    def get(self, request , id):
        order = get_object_or_404(Order, id=id)
        if order.userid_id == request.user.id and order.paid == 1:
            order = get_object_or_404(Order, id=id)
            
            
            
            
            params = {
                'order': order,
                'request': request,
                
                }

            
            return Render.render('pdf.html', params)
        else:
            return redirect('/')
        
            

def detail_view(request, id):
    
    
    order = get_object_or_404(Order, id=id)

    
        
        
        
    
    

    if order.userid_id == request.user.id:

        obj = get_object_or_404(Order, id = id)
        form = OrderCreateForm(request.POST or None, instance = obj) 
        if request.method =="POST" and 'cancel' in request.POST :
            obj.delete()
            return HttpResponseRedirect("person") 
        if request.method =="POST" and 'pay' in request.POST :
            
        
            obj.paid = True
            obj.save()
            
    
    
            
            
            
        return render(request, "detail_view.html",{'order': order})
    else:
        return redirect('/')
    
 
    
    
def logout(request):
    auth_logout(request)
    return redirect('/')
   

   


    
         
    


def updateimage(request):
    username = None
    if request.method == 'POST':
        if request.user.is_authenticated:
            username = request.user
            
            
            
            if Profile.objects.filter(user=username):
                obj = get_object_or_404(Profile, user = username)
                if obj.user == request.user:
                    obj.image.delete()
                    obj.image = request.FILES.get('image')
                    fs = FileSystemStorage(location='/profile_pics/')
                    filename = fs.save('image',obj.image)
                    uploaded_file_url = fs.url(request.user)
                    obj.save()
                    return redirect('http://127.0.0.1:8000/personal')
                else:
                    image = request.FILES.get('image')
                    Profile.objects.create(user = username,image = image)
                    return redirect('http://127.0.0.1:8000/personal')
    return render(request,'updateimg.html',)




