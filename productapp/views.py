from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template.loader import get_template
from productapp.models import login_info
from productapp.models import user_info
from productapp.models import category
from productapp.models import product
from productapp.models import comment
from django.db.models import Max
from django import forms

class UploadFileForm(forms.Form):
    image = forms.ImageField()

# Create your views here.

def login(request):
	l=islogedin(request)
	if l:
		return HttpResponseRedirect('/product/dashboard')
	t = get_template('login.html')
	error=''
	if request.method=='POST':
		username=request.POST['username']
		password=request.POST['password']
		chek=login_info.objects.filter(username=username)
		if len(chek)<=0:
			error='No user found'
		elif(chek[0].password==password):
			request.session['username']=username
			#if (chek[0].usertype=='admin'):
			return HttpResponseRedirect('/product/dashboard')
		else:
			error='password not match'
	return HttpResponse(t.render({'error':error}))

def signup(request):
	l=islogedin(request)
	if l:
		return HttpResponseRedirect('/product/dashboard')
	error=''
	t = get_template('signup.html')
	if request.method=='POST':
		name=request.POST['name']
		username=request.POST['username']
		email=request.POST['email']
		password=request.POST['password']
		chek=login_info.objects.filter(username=username)
		if len(chek)>0:
			error='Username already exist'
			return HttpResponse(t.render({'error':error}))
		log=login_info(username=username,password=password)
		log.save()
		user=user_info(name=name,email=email,username=username)
		user.save()
		request.session['username']=username
		return HttpResponseRedirect('/product/dashboard')
	return HttpResponse(t.render())

def islogedin(request):
	if request.session.has_key('username'):
		return True
	else:
		return False


def isadmin(request):
    chek=login_info.objects.get(username=request.session['username'])
    if(chek.usertype=='admin'):
    	return True
    else:
    	return False

def dashboard(request):
	l=islogedin(request)
	if l:
		adm=isadmin(request)
		if adm:
			cat=[]
			cat.append(getCategory('0'))

			t=get_template('admin_dashboard.html')
			products=product.objects.all()
			return HttpResponse(t.render({'name':request.session['username'] , 'category':cat,'par':0,'products':products,'par_name':"Category"}))
		else:
			cat=[]
			cat.append(getCategory('0'))
			products=product.objects.all()
			t=get_template('dashboard.html')
			return HttpResponse(t.render({'name':request.session['username'] , 'category':cat,'par':0,'products':products}))
	else:
		return HttpResponseRedirect('/product/login')

def logout(request):
	l=islogedin(request)
	if l:
		del request.session['username']
	return HttpResponseRedirect('/product/login')

def profile(request):
	l=islogedin(request)
	if l:
		if request.method=='POST':
			name=request.POST['name']
			email=request.POST['email']
			profile=user_info.objects.get(username=request.session['username'])
			profile.name=name
			profile.email=email
			profile.save()
		pf=user_info.objects.filter(username=request.session['username'])[0]
		t=get_template('profile.html')
		return HttpResponse(t.render({'detail':pf}))
	else:
		return HttpResponseRedirect('/product/login')

def getCategory(parent):
	cat=category.objects.filter(parent=parent)
	return cat

def addcategory(request,offset):
	l=islogedin(request)
	if l:
		if request.method=='POST':		
			cname=request.POST['new_category']
			try:
				cid=category.objects.all().aggregate(Max('cat_id'))['cat_id__max']+1
			except:
				cid=1
			path=''
			if offset=='0':
				path='0'
				parent_name="Category"
			else:
				path=getpath(offset)
				parent_name=category.objects.get(cat_id=offset).cat_name
		
			c=category(cat_id=cid,cat_name=cname,parent=offset,pathp=path,parent_name=parent_name)
			c.save()
			return HttpResponseRedirect("/product/dashboard/"+path)
	else:
		return HttpResponseRedirect('/product/login')

def getpath(node):
	path=''
	
	p=category.objects.filter(cat_id=int(node))[0].pathp
	path=p+'/'+node
	return path

def subcategory(request,offset):
	l=islogedin(request)
	if l:
		subids=offset.split('/')
		per=subids[-1]
		cat=[]
		for p in subids:
			cat.append(getCategory(p))
		products=[]
		parent=[int(per),]
		products=list(product.objects.filter(product_cat=per))
		for pare in parent: 
			cats=category.objects.filter(parent=pare)
			for cts in cats:
				pds=product.objects.filter(product_cat=cts.cat_id)	
				products+=list(pds)
				parent+=[cts.cat_id,]
		adm=isadmin(request)
		parent_name=category.objects.get(cat_id=per).cat_name
		noitem=""
		if len(products)==0:
			noitem="No item found..."
		if adm:
			t=get_template('admin_dashboard.html')			
			return HttpResponse(t.render({'name':request.session['username'] , 'category':cat, 'par':per,'products':products,'par_name':parent_name,'noitem':noitem}))
		else:
			t=get_template('dashboard.html')			
			return HttpResponse(t.render({'name':request.session['username'] , 'category':cat, 'par':per,'products':products,'par_name':parent_name,'noitem':noitem}))
	else:
		return HttpResponseRedirect('/product/login')	
	
def addproduct(request):
	l=islogedin(request)
	if l:
		adm=isadmin(request)
		if adm:
			if request.method=='POST':				
				pname=request.POST['productname']
				pcat=request.POST['productcat']
				features=request.POST['feature']
				try:
					pid=product.objects.all().aggregate(Max('product_id'))['product_id__max']+1
				except:
					pid=1
				pro=product(product_id=pid,product_name=pname,product_cat=pcat,product_features=features)
				pro.save()
				form = UploadFileForm(request.POST, request.FILES)
				if form.is_valid():
					handle_uploaded_file(request.FILES['image'],pid)								
			form = UploadFileForm()
			cats=category.objects.all()
			categorys=[]
			t=get_template('add_product.html')
			for cat in cats:
				categ=cat.pathp.split('/')
				for c in categ:
					if c=='0':
						cn=''
					else:
						cn+=category.objects.filter(cat_id=c)[0].cat_name+'/'
				cn+=cat.cat_name
				pth=cat.pathp
				categorys.append({'cat_id':cat.cat_id,'cat_path':cn})
			return HttpResponse(t.render({'cat':categorys,'form':form}))
	return HttpResponseRedirect('/product/login')	
		
def showproduct(request,offset):
	l=islogedin(request)
	if l:
		if request.method=='POST':
			comment_dis=request.POST['cmnt']
			username=request.session['username']
			pid=offset
			try:
				cid=comment.objects.all().aggregate(Max('comment_id'))['comment_id__max']+1
			except:
				cid=1
			cmt=comment(comment_id=cid,product_id=pid,username=username,comment_discription=comment_dis)
			cmt.save()
		t=get_template('product_view.html')
		if not product.objects.filter(product_id=offset):
			return HttpResponseRedirect("/product/dashboard")
		products=product.objects.filter(product_id=offset)[0]
		ctr=category.objects.filter(cat_id=products.product_cat)[0]
		categ=ctr.pathp.split('/')
		for c in categ:
			if c=='0':
				cn=''
			else:
				cn+=category.objects.filter(cat_id=c)[0].cat_name+'/'
		cn+=ctr.cat_name
		cmnt=comment.objects.filter(product_id=offset)
		admin=False
		adm=isadmin(request)
		fe=product.objects.filter(product_id=offset)[0].product_features
		features=fe.split('\n')
		if adm:
			admin=True
		return HttpResponse(t.render({'products':products,'category':cn,'coment':cmnt,'pid':offset,'admin':admin,'features':features}))

def handle_uploaded_file(f,pid):
	with open('/home/user/mysite/productapp/static/product_images/'+str(pid)+'.jpg', 'wb+') as destination:
		for chunk in f.chunks():
			destination.write(chunk)

def delete_product(request,offset):
	l=islogedin(request)
	if l:
		adm=isadmin(request)
		if adm:
			pdct=product.objects.filter(product_id=offset)
			pdct.delete()
			cmnt=comment.objects.filter(product_id=offset)
			cmnt.delete()
	return HttpResponseRedirect('/product/dashboard')

def not_found(request):
	t=get_template('404.html')			
	return HttpResponse(t.render())
def search(request):
	l=islogedin(request)
	if l:
		if request.method=='POST':
			search_word=request.POST['word']
			items=product.objects.filter(product_name__icontains=search_word)
			noitem=""
			if len(items)==0:
				noitem="No item found..."
			t=get_template('search.html')
			return HttpResponse(t.render({'products':items,'noitem':noitem}))
	return HttpResponseRedirect('/product/dashboard')