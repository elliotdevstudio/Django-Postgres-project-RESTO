from django.db.models import fields
from django.db.models.fields.related import ForeignKey
from django.shortcuts import render, redirect
from django.urls import reverse

from django.views import View
from django.views.generic.edit import DeleteView, UpdateView, FormView, CreateView
from django.views.generic.base import ContextMixin, TemplateView
from django.views.generic.detail import DetailView


from main_app.models import Job_Post, Business, Review, User

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.forms import ModelForm


from django.http import HttpResponseRedirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# Create your views here.
#=== SIGNUP AND LOGIN FORMS ===

class BusinessProfileForm(ModelForm):
    class Meta:
        model = Business
        fields = ['name', 'description', 'address', 'city', 'state', 'zip_code'] 

class JobPostCreate(ModelForm):
    class Meta:
        model = Job_Post
        fields = ['title', 'pay_type', 'description', 'city', 'state']
        __empty__ = ('(Unknown)')

class UserProfileForm(ModelForm):
    class Meta:
        model = User 
        fields = ['first_name', 'last_name', 'city', 'state', 'zip_code', 'work_preferences', 'description']
        __empty__ = ('(Unknown)')

class ReviewForm(ModelForm):
    class Meta:
        model = Review 
        fields = ['title', 'city', 'state','review', ]

# === BEGINNING WITH LANDING PAGES ===

class Home(TemplateView):
  template_name = "home.html"
    
  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context["user_signup_form"] = UserCreationForm()
      context["login_form"] = AuthenticationForm()
      return context


class About(TemplateView):
  template_name = "about.html"

  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context["user_signup_form"] = UserCreationForm()
      context["login_form"] = AuthenticationForm()
      return context


## == USER CREATE ===
class UserSignup(TemplateView):
  template_name= "user_signup"

  def get(self, request):
      user_form = UserCreationForm()
      context = {"user_form": user_form}
      return render(request, "registration/user_signup.html", context)

  def post(self, request):
      user_form = UserCreationForm(request.POST)
      if user_form.is_valid():
        user = user_form.save()
        user.save()
        login(request, user)
        return render('user_profile_create', kwargs={'pk': self.object.pk})
      else:
        context = {"user_form": user_form}
        return render(request, "registration/user_signup.html", context)


## == BUSINESS CREATE ===
class BusinessSignup(TemplateView):
    template_name = "business_signup"
   
    def get(self, request):
      user_form = UserCreationForm()
      context = {"user_form": user_form}
      context["login"] = True
      return render(request, "registration/business_signup.html", context)

    def post(self, request):
      user_form = UserCreationForm(request.POST)
      if user_form.is_valid():
        user = user_form.save()
        user.save()
        login(request, user)
        return render("business_profile_create.html", kwargs={'pk': self.object.pk})
      else:
        context = {"user_form": user_form}
        return render(request, "registration/business_signup.html", context)


'''
WRITE UP A SIMPLE VIEW (USING THE GIVEN BASE TEMPLATE), BUT MAKE TWO OF THEM, ONE FOR 'INDIVIDUAL'
USERS, AND ANOTHER FOR 'BUSINESS', THE ONLY DIFFERENCE IS THAT EACH PAGE REDIRECTS TO THE SECOND STEP OF 
PROFILE CREATION (WITH CUSTOM FORM FIELDS) FOR EACH ONE, AND SAVE THAT POST DATA FOR EACH USER TYPE

'''
# === USER PROFILE CREATE === 
@method_decorator(login_required, name='dispatch')
class UserProfileCreate(TemplateView):
    template_name = "user_profile_create"
    success_url = "/profile/"

    def get(self, request):
        user_profile_form = UserProfileForm()
        context = {"user_profile_form": user_profile_form}
        context["login"] = True
        return render(request,"registration/user_profile_create.html", context)
    
    def post(self, request):
        user_profile_form = UserProfileForm(request.POST)

        if user_profile_form.is_valid(): 
          user = user_profile_form.save() 
          user.save()
          return render(request, 'user_detail', kwargs={'pk': self.object.pk})
        else:
          context = {"user_profile_form": user_profile_form}
          return render(request, "registration/user_profile_create.html", context) 

# === BUSINESS-PROFILE-CREATE ===  
@method_decorator(login_required, name='dispatch')
class BusinessProfileCreate(TemplateView):
    model = Business
    template_name = "business_profile_create"
    success_url= "/profile/"

    def get(self, request):
        business_profile_form = BusinessProfileForm()
        context = {"business_profile_form": business_profile_form}
        context["login"] = True
        return render(request,"registration/business_profile_create.html", context)
    
    def post(self, request):
        business_profile_form = BusinessProfileForm(request.POST)
        if business_profile_form.is_valid(): 
           business = business_profile_form.save(commit=False)  
           business.save()
           return render(request, 'business_detail', kwargs={'pk': self.object.pk})
        else:
          context = {"business_profile_form": business_profile_form}
          return render(request, "registration/business_profile_create.html", context)  
''' 
class BusinessProfileCreate(CreateView):
  template_name = "business_signup.html"
  success_url = "/profile/"

  def get(self, request):
      user_form = UserCreationForm()
      business_form = BusinessSignupForm()
      context = {"user_form": user_form, "business_form": business_form}
      context["login"] = True
      return render(request, "registration/business_signup.html", context)
    
  def post(self, request):
      user_form = UserCreationForm(request.POST)
      business_form = BusinessSignupForm(request.POST)
      if  user_form.is_valid() and business_form.is_valid():
          user = user_form.save()
          business = business_form.save(commit=False)
          business.user = user
          business.save()
          return render(request,'business_detail', kwargs={'pk': self.object.pk})
      else:
          context = {"user_form": user_form, "business_form": business_form}
          return render(request, "registration/business_signup.html", context) 

 '''

@method_decorator(login_required, name='dispatch')
class BusinessDetail(DetailView):
    model = Business
    template_name = "business_profile_create.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
  

@method_decorator(login_required, name='dispatch')
class BusinessRedirect(View):
    def get(self, request):
    
        return redirect('business_detail', request.user.business.pk)

# === JOB LISTING -CREATE- ==== #

@method_decorator(login_required, name='dispatch')
class JobPostCreate(CreateView):
  model = Job_Post
  fields = ['title', 'pay_type', 'description', 'city', 'state']
  template_name = "job_listing_create.html"
  success_url = "/new_listing/"

  def _valid(self, form): 
      form.instance.business = self.request.user.business
      return super(JobPostCreate, self).form_valid(form)
       

# ===== JOB LISTING  -READ- ==== #

@method_decorator(login_required, name='dispatch')
class JobPostDetail(DetailView):
    model = Job_Post
    template_name = "job_post_detail.html"
  
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

@method_decorator(login_required, name='dispatch')
class JobPostUpdate(UpdateView):
    model = Job_Post
    fields = ['title', 'pay_type', 'description']
    template_name = "job_listing_update.html"
    
    def get_success_url(self):
        return reverse('job_listing_detail', kwargs={'pk': self.object.pk})

@method_decorator(login_required, name='dispatch')
class JobPostDelete(DeleteView):
    model = Job_Post
    template_name = "job_listing_delete_confirmation.html"
   
    def get_success_url(self):
        return reverse('business_detail', kwargs={'pk': self.object.business_id})




# === USER DETAIL VIEW ===  READ

@method_decorator(login_required, name='dispatch')
class UserDetail(DetailView):
  model = User
  template_name = "user_detail.html"

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    return context
  

@method_decorator(login_required, name='dispatch')
class UserRedirect(View):
  def get(self, request):

    return redirect('user_detail', request.user.pk)


# === REVIEW -CREATE- ==== #

@method_decorator(login_required, name='dispatch')
class ReviewCreate(CreateView):
  model = Review
  fields = ['business','title', 'review']
  template_name = "review_create.html"
  success_url = "/new_review/"

  def post(self, request, pk): 
    name_of_business=request.POST.get('name_of_business')
    city=request.POST.get('city')
    state=request.POST.get('state')
    description=request.POST.get('description')
    review=Review.objects.create(name_of_business=name_of_business, city=city, state=state, description=description)
    return redirect('review_detail', pk=review.pk)
    

# ==== REVIEW -- READ, UPDATE, DELETE  =======

@method_decorator(login_required, name='dispatch')
class ReviewDetail(DetailView):
  model=Review
  template_name='review_detail.html'

  def get_context_data(self, **kwargs):
      context = super().get_context_data(self, **kwargs)
      return context 


















        

