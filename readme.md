ead the readme.md on the things we will have to update, some of em changes were
  made and some are left in the readme.md you will get all the info, use that and
  complete the updates

○ Thought for 3.5s (Let me start by reading the README.md file to understand w...)
● Explored 1 file (README.md)
● Ran 2 commands (+1 · ls -la /home/shwetank/khaana_khazana/)
● Explored 1 file (readme.md) (ctrl+o to expand)
▸ Thought for 9s

  Let me explore the current state of the codebase to understand what's been    
  done and what's left.                                                         

● Ran 2 commands (find /home/shwetank/... ×2) (ctrl+o to expand)

  Now let me read all the key files to understand the current state. I'll       
  dispatch a research agent for a comprehensive codebase read.

● Spawned 1 subagent (ctrl+o to expand)

  I've dispatched a research agent to read the entire codebase. I'll wait for   
  the results to understand the current state and then complete all remaining   
  updates.

● Scheduling 1 timer (120s: Check if the research subagen...) (ctrl+o to expand)
  Waiting for the codebase analysis to complete...                              
  
  [Subagent a82f6236-853a-4ac9-9aa9-d37df24708ff (Codebase Analyzer)]           
  
  Here are the complete contents of every file in the project:
  ──────
  ### 1. config/settings.py
  
    from pathlib import Path                                                    
    import os                                                                   
  
    BASE_DIR = Path(__file__).resolve().parent.parent
  
    SECRET_KEY = 'django-insecure-abc123xyz456'
  
    DEBUG = True                                                                
  
    ALLOWED_HOSTS = ['*']
  
    INSTALLED_APPS = [                                                          
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'recipes',
        'accounts',
        'reviews',
        'favorites',
        'planner',
    ]
  
    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]
  
    ROOT_URLCONF = 'config.urls'
  
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',       
            'DIRS': [BASE_DIR / 'templates'],                                   
            'APP_DIRS': True,                                                   
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',      
                ],
            },
        },
    ]
  
    WSGI_APPLICATION = 'config.wsgi.application'
  
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
                                                                                
    AUTH_PASSWORD_VALIDATORS = [                                                
        {'NAME':
        'django.contrib.auth.password_validation.UserAttributeSimilarityValidato
        r'},
        {'NAME':
        'django.contrib.auth.password_validation.MinimumLengthValidator'},      
        {'NAME':
        'django.contrib.auth.password_validation.CommonPasswordValidator'},     
        {'NAME':
        'django.contrib.auth.password_validation.NumericPasswordValidator'},    
    ]
  
    LANGUAGE_CODE = 'en-us'                                                     
    TIME_ZONE = 'Asia/Kolkata'                                                  
    USE_I18N = True                                                             
    USE_TZ = True                                                               
  
    STATIC_URL = '/static/'                                                     
    STATICFILES_DIRS = [BASE_DIR / 'static']
    MEDIA_URL = '/media/'                                                       
    MEDIA_ROOT = BASE_DIR / 'media'                                             
  
    DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
                                                                                
    LOGIN_URL = '/accounts/login/'                                              
    LOGIN_REDIRECT_URL = '/'                                                    
    LOGOUT_REDIRECT_URL = '/'                                                   
  ──────                                                                        
  ### 2. config/urls.py                                                         
  
    from django.contrib import admin                                            
    from django.urls import path, include
    from django.conf import settings                                            
    from django.conf.urls.static import static
  
    urlpatterns = [
        path('admin/', admin.site.urls),                                        
        path('', include('recipes.urls')),
        path('accounts/', include('accounts.urls')),
        path('reviews/', include('reviews.urls')),
        path('favorites/', include('favorites.urls')),
        path('planner/', include('planner.urls')),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)           
  ──────
  ### 3. recipes/models.py
  
    from django.db import models                                                
    from django.contrib.auth.models import User                                 
  

    class Category(models.Model):                                               
        name = models.CharField(max_length=100)
        slug = models.SlugField(unique=True)                                    
        icon = models.CharField(max_length=50, default='🍽️')                    
  
        class Meta:
            verbose_name_plural = 'Categories'                                  
            ordering = ['name']
  
        def __str__(self):                                                      
            return self.name
  

    class Recipe(models.Model):                                                 
        DIFFICULTY_CHOICES = [                                                  
            ('easy', 'Easy'),
            ('medium', 'Medium'),
            ('hard', 'Hard'),
        ]
  
        title = models.CharField(max_length=200)
        slug = models.SlugField(unique=True)
        author = models.ForeignKey(User, on_delete=models.CASCADE,
        related_name='recipes')
        description = models.TextField()                                        
        image = models.ImageField(upload_to='recipes/', blank=True, null=True)  
        category = models.ForeignKey(Category, on_delete=models.SET_NULL,       
        null=True, related_name='recipes')                                      
        difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES,
        default='medium')                                                       
        prep_time = models.PositiveIntegerField(help_text='Minutes')            
        cook_time = models.PositiveIntegerField(help_text='Minutes')
        servings = models.PositiveIntegerField(default=4)
        calories_per_serving = models.PositiveIntegerField(null=True,           
        blank=True)                                                             
        protein = models.DecimalField(max_digits=6, decimal_places=1, null=True,
        blank=True, help_text='grams')                                          
        carbs = models.DecimalField(max_digits=6, decimal_places=1, null=True,  
        blank=True, help_text='grams')                                          
        fat = models.DecimalField(max_digits=6, decimal_places=1, null=True,    
        blank=True, help_text='grams')                                          
        is_vegetarian = models.BooleanField(default=False)                      
        is_vegan = models.BooleanField(default=False)                           
        created_at = models.DateTimeField(auto_now_add=True)                    
        updated_at = models.DateTimeField(auto_now=True)                        
  
        class Meta:                                                             
            ordering = ['-created_at']
  
        def __str__(self):
            return self.title
  
        @property
        def total_time(self):                                                   
            return self.prep_time + self.cook_time                              
  
        @property                                                               
        def average_rating(self):                                               
            reviews = self.reviews.all()                                        
            if reviews:
                return round(sum(r.rating for r in reviews) / len(reviews), 1)  
            return 0
  

    class Ingredient(models.Model):                                             
        recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE,
        related_name='ingredients')
        name = models.CharField(max_length=200)                                 
        quantity = models.DecimalField(max_digits=8, decimal_places=2)          
        unit = models.CharField(max_length=50)                                  
        order = models.PositiveIntegerField(default=0)
  
        class Meta:
            ordering = ['order']
  
        def __str__(self):
            return f"{self.quantity} {self.unit} {self.name}"                   
  

    class Step(models.Model):                                                   
        recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE,
        related_name='steps')                                                   
        order = models.PositiveIntegerField()                                   
        instruction = models.TextField()                                        
        duration_minutes = models.PositiveIntegerField(null=True, blank=True)   
  
        class Meta:                                                             
            ordering = ['order']                                                
  
        def __str__(self):                                                      
            return f"Step {self.order}: {self.instruction[:50]}"
  ──────
  ### 4. recipes/views.py                                                       
                                                                                
    from django.shortcuts import render, get_object_or_404, redirect            
    from django.contrib.auth.decorators import login_required
    from django.db.models import Q, Avg
    from django.http import JsonResponse                                        
    from .models import Recipe, Category, Ingredient, Step
    from .forms import RecipeForm                                               
    from reviews.models import Review                                           
    from reviews.forms import ReviewForm                                        
  

    def home(request):
        featured =                                                              
        Recipe.objects.annotate(avg_rating=Avg('reviews__rating')).order_by('-av
        g_rating')[:6]
        categories = Category.objects.all()                                     
        latest = Recipe.objects.order_by('-created_at')[:6]                     
        context = {                                                             
            'featured_recipes': featured,
            'categories': categories,
            'latest_recipes': latest,                                           
        }
        return render(request, 'recipes/home.html', context)                    
  

    def recipe_list(request):
        recipes = Recipe.objects.all()                                          
        categories = Category.objects.all()                                     
                                                                                
        query = request.GET.get('q', '')
        category = request.GET.get('category', '')
        difficulty = request.GET.get('difficulty', '')
        sort = request.GET.get('sort', '-created_at')
        diet = request.GET.get('diet', '')
  
        if query:
            recipes = recipes.filter(
                Q(title__icontains=query) | Q(description__icontains=query) |   
                Q(ingredients__name__icontains=query)                           
            ).distinct()                                                        
        if category:                                                            
            recipes = recipes.filter(category__slug=category)
        if difficulty:
            recipes = recipes.filter(difficulty=difficulty)
        if diet == 'vegetarian':                                                
            recipes = recipes.filter(is_vegetarian=True)                        
        elif diet == 'vegan':                                                   
            recipes = recipes.filter(is_vegan=True)
  
        recipes = recipes.order_by(sort)                                        
  
        context = {                                                             
            'recipes': recipes,                                                 
            'categories': categories,
            'current_query': query,
            'current_category': category,
            'current_difficulty': difficulty,
            'current_sort': sort,
            'current_diet': diet,
        }
        return render(request, 'recipes/recipe_list.html', context)
  

    def recipe_detail(request, slug):
        recipe = get_object_or_404(Recipe, slug=slug)                           
        reviews = recipe.reviews.all().order_by('-created_at')
        is_favorited = False
        if request.user.is_authenticated:                                       
            is_favorited = 
            recipe.favorited_by.filter(user=request.user).exists()              
  
        review_form = ReviewForm()                                              
        if request.method == 'POST' and request.user.is_authenticated:          
            review_form = ReviewForm(request.POST)                              
            if review_form.is_valid():                                          
                review = review_form.save(commit=False)
                review.recipe = recipe
                review.user = request.user                                      
                review.save()                                                   
                return redirect('recipe_detail', slug=slug)                     
  
        context = {                                                             
            'recipe': recipe,
            'reviews': reviews,
            'review_form': review_form,
            'is_favorited': is_favorited,
        }
        return render(request, 'recipes/recipe_detail.html', context)           
  

    @login_required
    def recipe_create(request):                                                 
        if request.method == 'POST':                                            
            form = RecipeForm(request.POST, request.FILES)
            if form.is_valid():                                                 
                recipe = form.save(commit=False)                                
                recipe.author = request.user                                    
                recipe.save()                                                   
                # Save ingredients
                ingredient_names = request.POST.getlist('ingredient_name[]')    
                ingredient_qtys = request.POST.getlist('ingredient_qty[]')      
                ingredient_units = request.POST.getlist('ingredient_unit[]')    
                for i, name in enumerate(ingredient_names):                     
                    if name.strip():                                            
                        Ingredient.objects.create(                              
                            recipe=recipe,
                            name=name,
                            quantity=ingredient_qtys[i] or 0,                   
                            unit=ingredient_units[i],                           
                            order=i
                        )
                # Save steps
                step_instructions = request.POST.getlist('step_instruction[]')  
                step_durations = request.POST.getlist('step_duration[]')        
                for i, instruction in enumerate(step_instructions):
                    if instruction.strip():                                     
                        Step.objects.create(
                            recipe=recipe,
                            instruction=instruction,                            
                            duration_minutes=step_durations[i] or None,         
                            order=i + 1                                         
                        )
                return redirect('recipe_detail', slug=recipe.slug)              
        else:
            form = RecipeForm()                                                 
        return render(request, 'recipes/recipe_form.html', {'form': form,       
        'editing': False})                                                      
  

    @login_required
    def recipe_edit(request, slug):                                             
        recipe = get_object_or_404(Recipe, slug=slug, author=request.user)      
        if request.method == 'POST':
            form = RecipeForm(request.POST, request.FILES, instance=recipe)     
            if form.is_valid():                                                 
                form.save()
                recipe.ingredients.all().delete()                               
                recipe.steps.all().delete()                                     
                ingredient_names = request.POST.getlist('ingredient_name[]')    
                ingredient_qtys = request.POST.getlist('ingredient_qty[]')      
                ingredient_units = request.POST.getlist('ingredient_unit[]')    
                for i, name in enumerate(ingredient_names):                     
                    if name.strip():                                            
                        Ingredient.objects.create(                              
                            recipe=recipe,
                            name=name,
                            quantity=ingredient_qtys[i] or 0,
                            unit=ingredient_units[i],
                            order=i
                        )
                step_instructions = request.POST.getlist('step_instruction[]')  
                step_durations = request.POST.getlist('step_duration[]')        
                for i, instruction in enumerate(step_instructions):             
                    if instruction.strip():                                     
                        Step.objects.create(                                    
                            recipe=recipe,                                      
                            instruction=instruction,
                            duration_minutes=step_durations[i] or None,         
                            order=i + 1
                        )
                return redirect('recipe_detail', slug=recipe.slug)
        else:                                                                   
            form = RecipeForm(instance=recipe)                                  
        return render(request, 'recipes/recipe_form.html', {'form': form,       
        'recipe': recipe, 'editing': True})
  

    @login_required
    def recipe_delete(request, slug):                                           
        recipe = get_object_or_404(Recipe, slug=slug, author=request.user)      
        if request.method == 'POST':                                            
            recipe.delete()                                                     
            return redirect('recipe_list')                                      
        return render(request, 'recipes/recipe_confirm_delete.html', {'recipe': 
        recipe})
  ──────
  ### 5. recipes/urls.py
  
    from django.urls import path
    from . import views
  
    urlpatterns = [
        path('', views.home, name='home'),
        path('recipes/', views.recipe_list, name='recipe_list'),
        path('recipes/new/', views.recipe_create, name='recipe_create'),        
        path('recipes/<slug:slug>/', views.recipe_detail, name='recipe_detail'),
        path('recipes/<slug:slug>/edit/', views.recipe_edit,
        name='recipe_edit'),                                                    
        path('recipes/<slug:slug>/delete/', views.recipe_delete,
        name='recipe_delete'),
    ]
  ──────
  ### 6. recipes/forms.py
  
    from django import forms
    from .models import Recipe                                                  
  

    class RecipeForm(forms.ModelForm):
        class Meta:                                                             
            model = Recipe                                                      
            fields = ['title', 'slug', 'description', 'image', 'category',      
            'difficulty',                                                       
                      'prep_time', 'cook_time', 'servings',                     
                      'calories_per_serving',
                      'protein', 'carbs', 'fat', 'is_vegetarian', 'is_vegan']   
            widgets = {
                'title': forms.TextInput(attrs={'class': 'form-control',        
                'placeholder': 'Recipe Title'}),
                'slug': forms.TextInput(attrs={'class': 'form-control',         
                'placeholder': 'recipe-slug'}),
                'description': forms.Textarea(attrs={'class': 'form-control',   
                'rows': 4}),
                'category': forms.Select(attrs={'class': 'form-select'}),       
                'difficulty': forms.Select(attrs={'class': 'form-select'}),     
                'prep_time': forms.NumberInput(attrs={'class': 'form-control',  
                'placeholder': 'Minutes'}),
                'cook_time': forms.NumberInput(attrs={'class': 'form-control',  
                'placeholder': 'Minutes'}),
                'servings': forms.NumberInput(attrs={'class': 'form-control'}), 
                'calories_per_serving': forms.NumberInput(attrs={'class':       
                'form-control'}),
                'protein': forms.NumberInput(attrs={'class': 'form-control',    
                'step': '0.1'}),                                                
                'carbs': forms.NumberInput(attrs={'class': 'form-control',      
                'step': '0.1'}),
                'fat': forms.NumberInput(attrs={'class': 'form-control', 'step':
                '0.1'}),
            }
  ──────
  ### 7. recipes/admin.py
  
    from django.contrib import admin                                            
    from .models import Recipe, Category, Ingredient, Step
  

    class IngredientInline(admin.TabularInline):
        model = Ingredient
        extra = 3                                                               
                                                                                
                                                                                
    class StepInline(admin.TabularInline):                                      
        model = Step
        extra = 3
  

    @admin.register(Category)
    class CategoryAdmin(admin.ModelAdmin):                                      
        list_display = ['name', 'slug', 'icon']
        prepopulated_fields = {'slug': ('name',)}                               
  

    @admin.register(Recipe)
    class RecipeAdmin(admin.ModelAdmin):
        list_display = ['title', 'author', 'category', 'difficulty',            
        'created_at']
        list_filter = ['category', 'difficulty', 'is_vegetarian', 'is_vegan']   
        search_fields = ['title', 'description']
        prepopulated_fields = {'slug': ('title',)}
        inlines = [IngredientInline, StepInline]
  ──────
  ### 8. recipes/tests.py
  
    from django.test import TestCase                                            
  
    # Create your tests here.
  ──────
  ### 9. accounts/models.py
  
    from django.db import models
  
    # Create your models here.
  ──────
  ### 10. accounts/views.py
  
    from django.shortcuts import render, redirect
    from django.contrib.auth import login, logout, authenticate
    from django.contrib.auth.decorators import login_required                   
    from .forms import RegisterForm
  

    def register_view(request):
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)                                            
                return redirect('home')                                         
        else:                                                                   
            form = RegisterForm()                                               
        return render(request, 'accounts/register.html', {'form': form})        
  

    def login_view(request):
        if request.method == 'POST':                                            
            username = request.POST['username']
            password = request.POST['password']                                 
            user = authenticate(request, username=username, password=password)  
            if user:                                                            
                login(request, user)                                            
                return redirect(request.GET.get('next', 'home'))                
            else:                                                               
                return render(request, 'accounts/login.html', {'error': 'Invalid
                credentials'})
        return render(request, 'accounts/login.html')                           
                                                                                
                                                                                
    @login_required
    def logout_view(request):
        logout(request)
        return redirect('home')
  

    @login_required
    def profile_view(request):
        recipes = request.user.recipes.all()                                    
        favorites = request.user.favorites.all()
        return render(request, 'accounts/profile.html', {
            'recipes': recipes,
            'favorites': favorites,
        })
  ──────
  ### 11. accounts/urls.py
  
    from django.urls import path                                                
    from . import views                                                         
  
    urlpatterns = [
        path('register/', views.register_view, name='register'),
        path('login/', views.login_view, name='login'),                         
        path('logout/', views.logout_view, name='logout'),                      
        path('profile/', views.profile_view, name='profile'),                   
    ]
  ──────
  ### 12. accounts/forms.py
  
    from django import forms
    from django.contrib.auth.forms import UserCreationForm                      
    from django.contrib.auth.models import User                                 
                                                                                
  
    class RegisterForm(UserCreationForm):                                       
        email = forms.EmailField(required=True,                                 
        widget=forms.EmailInput(attrs={'class': 'form-control'}))               
  
        class Meta:                                                             
            model = User                                                        
            fields = ['username', 'email', 'password1', 'password2']            
  
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in self.fields:
                self.fields[field].widget.attrs.update({'class':                
                'form-control'})
  ──────
  ### 13. accounts/tests.py
  
    from django.test import TestCase
  
    # Create your tests here.
  ──────
  ### 14. reviews/models.py
  
    from django.db import models                                                
    from django.contrib.auth.models import User                                 
    from recipes.models import Recipe
  

    class Review(models.Model):                                                 
        recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE,            
        related_name='reviews')                                                 
        user = models.ForeignKey(User, on_delete=models.CASCADE,
        related_name='reviews')
        rating = models.PositiveIntegerField(choices=[(i, i) for i in range(1,  
        6)])
        comment = models.TextField()
        created_at = models.DateTimeField(auto_now_add=True)                    
  
        class Meta:
            unique_together = ('recipe', 'user')
            ordering = ['-created_at']
  
        def __str__(self):
            return f"{self.user.username} - {self.recipe.title}: {self.rating}★"
  ──────
  ### 15. reviews/views.py
  
    from django.shortcuts import get_object_or_404, redirect                    
    from django.contrib.auth.decorators import login_required
    from .models import Review
  

    @login_required
    def delete_review(request, pk):                                             
        review = get_object_or_404(Review, pk=pk, user=request.user)            
        slug = review.recipe.slug                                               
        if request.method == 'POST':                                            
            review.delete()                                                     
        return redirect('recipe_detail', slug=slug)
  ──────
  ### 16. reviews/urls.py
  
    from django.urls import path
    from . import views
  
    urlpatterns = [                                                             
        path('delete/<int:pk>/', views.delete_review, name='delete_review'),    
    ]
  ──────
  ### 17. reviews/forms.py
  
    from django import forms                                                    
    from .models import Review
  

    class ReviewForm(forms.ModelForm):
        class Meta:
            model = Review
            fields = ['rating', 'comment']
            widgets = {                                                         
                'rating': forms.Select(attrs={'class': 'form-select'}),         
                'comment': forms.Textarea(attrs={'class': 'form-control',       
                'rows': 3, 'placeholder': 'Write your review...'}),
            }
  ──────
  ### 18. reviews/tests.py
  
    from django.test import TestCase
  
    # Create your tests here.
  ──────
  ### 19. favorites/models.py
  
    from django.db import models
    from django.contrib.auth.models import User                                 
    from recipes.models import Recipe                                           
  

    class Favorite(models.Model):                                               
        user = models.ForeignKey(User, on_delete=models.CASCADE,                
        related_name='favorites')                                               
        recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE,
        related_name='favorited_by')
        created_at = models.DateTimeField(auto_now_add=True)                    
                                                                                
        class Meta:
            unique_together = ('user', 'recipe')
                                                                                
        def __str__(self):                                                      
            return f"{self.user.username} ♥ {self.recipe.title}"                
  ──────
  ### 20. favorites/views.py
  
    from django.shortcuts import get_object_or_404, redirect
    from django.contrib.auth.decorators import login_required
    from django.http import JsonResponse
    from recipes.models import Recipe                                           
    from .models import Favorite                                                
  

    @login_required
    def toggle_favorite(request, recipe_id):                                    
        recipe = get_object_or_404(Recipe, id=recipe_id)                        
        favorite, created = Favorite.objects.get_or_create(user=request.user,   
        recipe=recipe)                                                          
        if not created:                                                         
            favorite.delete()
            is_favorited = False                                                
        else:                                                                   
            is_favorited = True                                                 
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':         
            return JsonResponse({'is_favorited': is_favorited})                 
        return redirect('recipe_detail', slug=recipe.slug)                      
  

    @login_required
    def favorite_list(request):                                                 
        favorites =                                                             
        Favorite.objects.filter(user=request.user).select_related('recipe')     
        return render(request, 'favorites/favorite_list.html', {'favorites':    
        favorites})
  ──────
  ### 21. favorites/urls.py
                                                                                
    from django.urls import path                                                
    from . import views                                                         
  
    urlpatterns = [
        path('toggle/<int:recipe_id>/', views.toggle_favorite,
        name='toggle_favorite'),                                                
        path('', views.favorite_list, name='favorite_list'),
    ]
  ──────
  ### 22. favorites/tests.py
                                                                                
    from django.test import TestCase                                            
  
    # Create your tests here.
  ──────
  ### 23. planner/models.py
                                                                                
    from django.db import models                                                
    from django.contrib.auth.models import User                                 
    from recipes.models import Recipe                                           
  
                                                                                
    class MealPlan(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE,
        related_name='meal_plans')
        week_start = models.DateField()                                         
        created_at = models.DateTimeField(auto_now_add=True)                    
  
        class Meta:
            unique_together = ('user', 'week_start')
            ordering = ['-week_start']
  
        def __str__(self):                                                      
            return f"{self.user.username}'s plan - Week of {self.week_start}"   
                                                                                
                                                                                
    class MealSlot(models.Model):                                               
        MEAL_TYPES = [
            ('breakfast', 'Breakfast'),
            ('lunch', 'Lunch'),
            ('dinner', 'Dinner'),
            ('snack', 'Snack'),
        ]
        DAY_CHOICES = [(i, d) for i, d in enumerate(['Monday', 'Tuesday',       
        'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])]
                                                                                
        meal_plan = models.ForeignKey(MealPlan, on_delete=models.CASCADE,       
        related_name='slots')                                                   
        day = models.IntegerField(choices=DAY_CHOICES)
        meal_type = models.CharField(max_length=10, choices=MEAL_TYPES)         
        recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
  
        class Meta:                                                             
            unique_together = ('meal_plan', 'day', 'meal_type')                 
            ordering = ['day', 'meal_type']
  
        def __str__(self):
            return f"{self.get_day_display()} {self.get_meal_type_display()}:   
            {self.recipe.title}"
  ──────
  ### 24. planner/views.py
  
    from django.shortcuts import render, redirect, get_object_or_404            
    from django.contrib.auth.decorators import login_required
    from django.http import JsonResponse
    from datetime import date, timedelta
    from .models import MealPlan, MealSlot
    from recipes.models import Recipe
  

    @login_required
    def meal_planner(request):
        today = date.today()
        week_start = today - timedelta(days=today.weekday())
        week_offset = int(request.GET.get('week', 0))
        week_start += timedelta(weeks=week_offset)                              
  
        meal_plan, created = MealPlan.objects.get_or_create(user=request.user,  
        week_start=week_start)
        slots = meal_plan.slots.select_related('recipe')
  
        schedule = {}
        for day_num, day_name in MealSlot.DAY_CHOICES:
            schedule[day_name] = {}
            for meal_type, meal_label in MealSlot.MEAL_TYPES:                   
                slot = slots.filter(day=day_num, meal_type=meal_type).first()   
                schedule[day_name][meal_label] = slot                           
                                                                                
        recipes = Recipe.objects.all().order_by('title')                        
  
        context = {                                                             
            'meal_plan': meal_plan,                                             
            'schedule': schedule,
            'recipes': recipes,
            'week_start': week_start,                                           
            'week_end': week_start + timedelta(days=6),                         
            'week_offset': week_offset,                                         
        }
        return render(request, 'planner/meal_planner.html', context)            
  

    @login_required
    def add_meal(request):                                                      
        if request.method == 'POST':                                            
            week_start = request.POST.get('week_start')                         
            day = request.POST.get('day')                                       
            meal_type = request.POST.get('meal_type')                           
            recipe_id = request.POST.get('recipe_id')
  
            meal_plan, _ = MealPlan.objects.get_or_create(user=request.user,    
            week_start=week_start)                                              
            recipe = get_object_or_404(Recipe, id=recipe_id)                    
  
            MealSlot.objects.update_or_create(
                meal_plan=meal_plan, day=day, meal_type=meal_type,
                defaults={'recipe': recipe}                                     
            )
            return redirect(f'/planner/?week={request.POST.get("week_offset",   
            0)}')
        return redirect('meal_planner')                                         
  

    @login_required
    def remove_meal(request, slot_id):
        slot = get_object_or_404(MealSlot, id=slot_id,
        meal_plan__user=request.user)                                           
        week_offset = request.GET.get('week', 0)
        slot.delete()
        return redirect(f'/planner/?week={week_offset}')                        
  

    @login_required
    def shopping_list(request):
        today = date.today()
        week_start = today - timedelta(days=today.weekday())
        week_offset = int(request.GET.get('week', 0))                           
        week_start += timedelta(weeks=week_offset)                              
  
        try:
            meal_plan = MealPlan.objects.get(user=request.user,
            week_start=week_start)
            slots = meal_plan.slots.select_related('recipe')
            ingredients = {}
            for slot in slots:
                for ing in slot.recipe.ingredients.all():
                    key = f"{ing.name}|{ing.unit}"                              
                    if key in ingredients:
                        ingredients[key]['quantity'] += float(ing.quantity)     
                    else:
                        ingredients[key] = {                                    
                            'name': ing.name,                                   
                            'quantity': float(ing.quantity),                    
                            'unit': ing.unit,                                   
                        }
            ingredient_list = sorted(ingredients.values(), key=lambda x:        
            x['name'])                                                          
        except MealPlan.DoesNotExist:                                           
            ingredient_list = []
  
        return render(request, 'planner/shopping_list.html', {
            'ingredients': ingredient_list,
            'week_start': week_start,
            'week_end': week_start + timedelta(days=6),
            'week_offset': week_offset,
        })
  ──────
  ### 25. planner/urls.py
  
    from django.urls import path
    from . import views
  
    urlpatterns = [                                                             
        path('', views.meal_planner, name='meal_planner'),
        path('add/', views.add_meal, name='add_meal'),
        path('remove/<int:slot_id>/', views.remove_meal, name='remove_meal'),   
        path('shopping-list/', views.shopping_list, name='shopping_list'),      
    ]
  ──────
  ### 26. planner/tests.py
  
    from django.test import TestCase
  
    # Create your tests here.
  ──────
  ### 27. planner/admin.py
  
    from django.contrib import admin
  
    # Register your models here.
  ──────
  ### 28. templates/base.html
  
    {% load static %}
    <!DOCTYPE html>
    <html lang="en" data-bs-theme="light">                                      
    <head>                                                                      
        <meta charset="UTF-8">                                                  
        <meta name="viewport" content="width=device-width, initial-scale=1.0">  
        <title>{% block title %}Khaana Khazana{% endblock %} | Khaana Khazana   
        🍛</title>                                                              
        <link                                                                   
        href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.mi
        n.css" rel="stylesheet">                                                
        <link 
        href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.0/font/bootstrap
        -icons.css" rel="stylesheet">                                           
        <link
        href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400
        ;600;700&family=Poppins:wght@300;400;500;600&display=swap"              
        rel="stylesheet">
        <link href="{% static 'css/style.css' %}" rel="stylesheet">             
    </head>                                                                     
    <body>
        <!-- Navbar -->
        <nav class="navbar navbar-expand-lg sticky-top glass-nav">              
            <div class="container">                                             
                <a class="navbar-brand fw-bold" href="{% url 'home' %}">        
                    <span class="brand-icon">🍛</span> Khaana Khazana           
                </a>                                                            
                <button class="navbar-toggler" type="button"
                data-bs-toggle="collapse" data-bs-target="#navbarNav">          
                    <span class="navbar-toggler-icon"></span>                   
                </button>                                                       
                <div class="collapse navbar-collapse" id="navbarNav">           
                    <ul class="navbar-nav me-auto">                             
                        <li class="nav-item">                                   
                            <a class="nav-link" href="{% url 'recipe_list'      
                            %}"><i class="bi bi-book"></i> Recipes</a>          
                        </li>                                                   
                        <li class="nav-item">                                   
                            <a class="nav-link" href="{% url 'meal_planner'     
                            %}"><i class="bi bi-calendar-week"></i> Meal        
                            Planner</a>                                         
                        </li>
                        {% if user.is_authenticated %}
                        <li class="nav-item">
                            <a class="nav-link" href="{% url 'favorite_list'    
                            %}"><i class="bi bi-heart"></i> Favorites</a>       
                        </li>                                                   
                        <li class="nav-item">                                   
                            <a class="nav-link" href="{% url 'recipe_create'    
                            %}"><i class="bi bi-plus-circle"></i> Add Recipe</a>
                        </li>
                        {% endif %}
                    </ul>                                                       
                    <ul class="navbar-nav">                                     
                        <li class="nav-item">                                   
                            <button class="btn btn-link nav-link"               
                            id="theme-toggle" title="Toggle Dark Mode">         
                                <i class="bi bi-moon-fill"></i>
                            </button>
                        </li>                                                   
                        {% if user.is_authenticated %}
                        <li class="nav-item dropdown">
                            <a class="nav-link dropdown-toggle" href="#"        
                            data-bs-toggle="dropdown">                          
                                <i class="bi bi-person-circle"></i> {{          
                                user.username }}
                            </a>                                                
                            <ul class="dropdown-menu dropdown-menu-end">        
                                <li><a class="dropdown-item" href="{% url       
                                'profile' %}"><i class="bi bi-person"></i>      
                                Profile</a></li>
                                <li><hr class="dropdown-divider"></li>          
                                <li><a class="dropdown-item" href="{% url       
                                'logout' %}"><i class="bi                       
                                bi-box-arrow-right"></i> Logout</a></li>        
                            </ul>
                        </li>
                        {% else %}
                        <li class="nav-item">
                            <a class="nav-link" href="{% url 'login' %}"><i     
                            class="bi bi-box-arrow-in-right"></i> Login</a>     
                        </li>
                        <li class="nav-item">                                   
                            <a class="nav-link btn btn-primary btn-sm text-white
                            ms-2 px-3" href="{% url 'register' %}">Sign Up</a>  
                        </li>
                        {% endif %}
                    </ul>                                                       
                </div>
            </div>                                                              
        </nav>
  
        <!-- Messages -->
        {% if messages %}
        <div class="container mt-3">                                            
            {% for message in messages %}
            <div class="alert alert-{{ message.tags }} alert-dismissible fade   
            show" role="alert">
                {{ message }}
                <button type="button" class="btn-close"                         
                data-bs-dismiss="alert"></button>                               
            </div>                                                              
            {% endfor %}
        </div>                                                                  
        {% endif %}
  
        <!-- Main Content -->
        <main>
            {% block content %}{% endblock %}
        </main>
                                                                                
        <!-- Footer -->
        <footer class="glass-footer mt-5">                                      
            <div class="container py-4">                                        
                <div class="row">                                               
                    <div class="col-md-4">                                      
                        <h5><span class="brand-icon">🍛</span> Khaana           
                        Khazana</h5>
                        <p class="text-muted">Discover, cook, and share amazing 
                        recipes from around the world.</p>                      
                    </div>
                    <div class="col-md-4">                                      
                        <h5>Quick Links</h5>
                        <ul class="list-unstyled">
                            <li><a href="{% url 'recipe_list' %}">All           
                            Recipes</a></li>
                            <li><a href="{% url 'meal_planner' %}">Meal         
                            Planner</a></li>
                            <li><a href="{% url 'recipe_create' %}">Add         
                            Recipe</a></li>
                        </ul>
                    </div>                                                      
                    <div class="col-md-4">                                      
                        <h5>Made with ❤️</h5>                                   
                        <p class="text-muted">A Django project by Shwetank</p>  
                    </div>                                                      
                </div>
                <hr>
                <p class="text-center text-muted mb-0">&copy; 2026 Khaana       
                Khazana. All rights reserved.</p>                               
            </div>
        </footer>                                                               
                                                                                
        <script                                                                 
        src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bund
        le.min.js"></script>                                                    
        <script>
            // Dark Mode Toggle
            const themeToggle = document.getElementById('theme-toggle');        
            const html = document.documentElement;                              
            const savedTheme = localStorage.getItem('theme') || 'light';        
            html.setAttribute('data-bs-theme', savedTheme);
            updateThemeIcon(savedTheme);
  
            themeToggle.addEventListener('click', () => {
                const current = html.getAttribute('data-bs-theme');
                const next = current === 'light' ? 'dark' : 'light';            
                html.setAttribute('data-bs-theme', next);
                localStorage.setItem('theme', next);
                updateThemeIcon(next);
            });
  
            function updateThemeIcon(theme) {
                const icon = themeToggle.querySelector('i');                    
                icon.className = theme === 'light' ? 'bi bi-moon-fill' : 'bi    
                bi-sun-fill';                                                   
            }
        </script>
        {% block extra_js %}{% endblock %}
    </body>
    </html>                                                                     
  ──────
  ### 29. templates/recipes/home.html
  
    {% extends 'base.html' %}
    {% load static %}
  
    {% block title %}Home{% endblock %}
  
    {% block content %}
    <!-- Hero Section -->
    <section class="hero-section">                                              
        <div class="hero-overlay"></div>                                        
        <div class="container hero-content text-center">                        
            <h1 class="display-3 fw-bold text-white mb-3 animate-fade-in">      
                🍛 Khaana Khazana                                               
            </h1>                                                               
            <p class="lead text-white-50 mb-4 animate-fade-in-delay">           
                Discover delicious recipes, plan your meals, and cook with      
                confidence
            </p>                                                                
            <div class="d-flex justify-content-center gap-3                     
            animate-fade-in-delay-2">
                <a href="{% url 'recipe_list' %}" class="btn btn-primary btn-lg 
                px-4">                                                          
                    <i class="bi bi-search"></i> Explore Recipes                
                </a>
                {% if not user.is_authenticated %}
                <a href="{% url 'register' %}" class="btn btn-outline-light     
                btn-lg px-4">
                    <i class="bi bi-person-plus"></i> Join Free                 
                </a>                                                            
                {% endif %}
            </div>
        </div>
    </section>
  
    <!-- Categories Section -->
    {% if categories %}
    <section class="py-5">                                                      
        <div class="container">
            <h2 class="section-title text-center mb-4">🏷️ Browse by             
            Category</h2>
            <div class="row g-3 justify-content-center">                        
                {% for cat in categories %}
                <div class="col-6 col-md-3 col-lg-2">                           
                    <a href="{% url 'recipe_list' %}?category={{ cat.slug }}"   
                    class="category-card text-decoration-none">                 
                        <div class="card glass-card text-center p-3">           
                            <span class="category-icon">{{ cat.icon }}</span>   
                            <span class="category-name">{{ cat.name }}</span>   
                        </div>
                    </a>
                </div>
                {% endfor %}
            </div>                                                              
        </div>                                                                  
    </section>
    {% endif %}
  
    <!-- Featured Recipes -->
    {% if featured_recipes %}
    <section class="py-5 bg-pattern">                                           
        <div class="container">                                                 
            <h2 class="section-title text-center mb-4">⭐ Top Rated Recipes</h2>
            <div class="row g-4">                                               
                {% for recipe in featured_recipes %}
                <div class="col-md-6 col-lg-4">                                 
                    <div class="card recipe-card glass-card h-100">
                        {% if recipe.image %}
                        <div class="recipe-img-wrapper">                        
                            <img src="{{ recipe.image.url }}"                   
                            class="card-img-top recipe-img" alt="{{ recipe.title
                            }}">
                            <div class="recipe-badges">                         
                                {% if recipe.is_vegetarian %}<span class="badge 
                                bg-success">🌿 Veg</span>{% endif %}            
                                {% if recipe.is_vegan %}<span class="badge      
                                bg-info">🌱 Vegan</span>{% endif %}             
                            </div>                                              
                        </div>
                        {% endif %}
                        <div class="card-body">                                 
                            <div class="d-flex justify-content-between          
                            align-items-start mb-2">
                                <h5 class="card-title mb-0">{{ recipe.title     
                                }}</h5>
                                <span class="badge bg-warning text-dark">       
                                    <i class="bi bi-star-fill"></i> {{          
                                    recipe.average_rating }}
                                </span>                                         
                            </div>                                              
                            <p class="card-text text-muted small">{{            
                            recipe.description|truncatewords:20 }}</p>          
                            <div class="recipe-meta">
                                <span><i class="bi bi-clock"></i> {{            
                                recipe.total_time }}m</span>
                                <span><i class="bi bi-speedometer2"></i> {{     
                                recipe.get_difficulty_display }}</span>         
                                <span><i class="bi bi-people"></i> {{           
                                recipe.servings }}</span>                       
                            </div>
                        </div>                                                  
                        <div class="card-footer bg-transparent border-0">       
                            <a href="{% url 'recipe_detail' recipe.slug %}"     
                            class="btn btn-primary w-100">                      
                                View Recipe <i class="bi bi-arrow-right"></i>   
                            </a>
                        </div>                                                  
                    </div>
                </div>
                {% endfor %}
            </div>                                                              
        </div>
    </section>
    {% endif %}
  
    <!-- Latest Recipes -->
    {% if latest_recipes %}
    <section class="py-5">                                                      
        <div class="container">                                                 
            <h2 class="section-title text-center mb-4">🆕 Latest Recipes</h2>   
            <div class="row g-4">                                               
                {% for recipe in latest_recipes %}
                <div class="col-md-6 col-lg-4">                                 
                    <div class="card recipe-card glass-card h-100">             
                        {% if recipe.image %}
                        <div class="recipe-img-wrapper">                        
                            <img src="{{ recipe.image.url }}"                   
                            class="card-img-top recipe-img" alt="{{ recipe.title
                            }}">
                        </div>                                                  
                        {% endif %}                                             
                        <div class="card-body">                                 
                            <h5 class="card-title">{{ recipe.title }}</h5>      
                            <p class="card-text text-muted small">{{            
                            recipe.description|truncatewords:15 }}</p>          
                            <div class="recipe-meta">                           
                                <span><i class="bi bi-clock"></i> {{            
                                recipe.total_time }}m</span>
                                <span><i class="bi bi-speedometer2"></i> {{     
                                recipe.get_difficulty_display }}</span>         
                            </div>
                        </div>
                        <div class="card-footer bg-transparent border-0">       
                            <a href="{% url 'recipe_detail' recipe.slug %}"     
                            class="btn btn-outline-primary w-100">
                                View Recipe <i class="bi bi-arrow-right"></i>   
                            </a>
                        </div>
                    </div>
                </div>
                {% endfor %}
            </div>
            <div class="text-center mt-4">                                      
                <a href="{% url 'recipe_list' %}" class="btn btn-primary        
                btn-lg">
                    See All Recipes <i class="bi bi-arrow-right"></i>           
                </a>
            </div>
        </div>                                                                  
    </section>
    {% endif %}
    {% endblock %}
  ──────
  ### 30. templates/recipes/recipe_list.html
  
    {% extends 'base.html' %}
    {% load static %}
  
    {% block title %}All Recipes{% endblock %}
  
    {% block content %}
    <section class="py-5">
        <div class="container">                                                 
            <h1 class="section-title text-center mb-4">📖 All Recipes</h1>      
  
            <!-- Filters -->
            <div class="card glass-card mb-4 p-3">                              
                <form method="get" class="row g-3 align-items-end">             
                    <div class="col-md-3">
                        <label class="form-label"><i class="bi bi-search"></i>  
                        Search</label>
                        <input type="text" name="q" class="form-control"        
                        placeholder="Search recipes..." value="{{ current_query 
                        }}">                                                    
                    </div>                                                      
                    <div class="col-md-2">                                      
                        <label class="form-label"><i class="bi bi-tag"></i>     
                        Category</label>
                        <select name="category" class="form-select">            
                            <option value="">All</option>
                            {% for cat in categories %}
                            <option value="{{ cat.slug }}" {% if                
                            current_category == cat.slug %}selected{% endif     
                            %}>{{ cat.name }}</option>                          
                            {% endfor %}                                        
                        </select>                                               
                    </div>                                                      
                    <div class="col-md-2">                                      
                        <label class="form-label"><i class="bi                  
                        bi-speedometer2"></i> Difficulty</label>                
                        <select name="difficulty" class="form-select">          
                            <option value="">All</option>                       
                            <option value="easy" {% if current_difficulty ==    
                            'easy' %}selected{% endif %}>Easy</option>          
                            <option value="medium" {% if current_difficulty ==  
                            'medium' %}selected{% endif %}>Medium</option>      
                            <option value="hard" {% if current_difficulty ==    
                            'hard' %}selected{% endif %}>Hard</option>          
                        </select>                                               
                    </div>                                                      
                    <div class="col-md-2">                                      
                        <label class="form-label"><i class="bi bi-leaf"></i>    
                        Diet</label>                                            
                        <select name="diet" class="form-select">                
                            <option value="">All</option>                       
                            <option value="vegetarian" {% if current_diet ==    
                            'vegetarian' %}selected{% endif                     
                            %}>Vegetarian</option>                              
                            <option value="vegan" {% if current_diet == 'vegan' 
                            %}selected{% endif %}>Vegan</option>                
                        </select>                                               
                    </div>                                                      
                    <div class="col-md-2">                                      
                        <label class="form-label"><i class="bi                  
                        bi-sort-down"></i> Sort</label>                         
                        <select name="sort" class="form-select">                
                            <option value="-created_at" {% if current_sort ==   
                            '-created_at' %}selected{% endif %}>Newest</option> 
                            <option value="created_at" {% if current_sort ==    
                            'created_at' %}selected{% endif %}>Oldest</option>  
                            <option value="title" {% if current_sort == 'title' 
                            %}selected{% endif %}>A-Z</option>                  
                            <option value="prep_time" {% if current_sort ==     
                            'prep_time' %}selected{% endif %}>Quickest</option> 
                        </select>                                               
                    </div>                                                      
                    <div class="col-md-1">                                      
                        <button type="submit" class="btn btn-primary w-100"><i  
                        class="bi bi-funnel"></i></button>                      
                    </div>                                                      
                </form>                                                         
            </div>                                                              
                                                                                
            <!-- Recipe Grid -->                                                
            <div class="row g-4">                                               
                {% for recipe in recipes %}                                     
                <div class="col-md-6 col-lg-4">                                 
                    <div class="card recipe-card glass-card h-100">             
                        {% if recipe.image %}                                   
                        <div class="recipe-img-wrapper">                        
                            <img src="{{ recipe.image.url }}"                   
                            class="card-img-top recipe-img" alt="{{ recipe.title
                            }}">                                                
                            <div class="recipe-badges">                         
                                {% if recipe.is_vegetarian %}<span class="badge 
                                bg-success">🌿 Veg</span>{% endif %}            
                                {% if recipe.is_vegan %}<span class="badge      
                                bg-info">🌱 Vegan</span>{% endif %}             
                                <span class="badge bg-{{ recipe.difficulty      
                                }}">{{ recipe.get_difficulty_display }}</span>  
                            </div>                                              
                        </div>                                                  
                        {% endif %}                                             
                        <div class="card-body">                                 
                            <div class="d-flex justify-content-between          
                            align-items-start mb-2">                            
                                <h5 class="card-title mb-0">{{ recipe.title     
                                }}</h5>                                         
                                {% if recipe.average_rating %}                  
                                <span class="badge bg-warning text-dark"><i     
                                class="bi bi-star-fill"></i> {{                 
                                recipe.average_rating }}</span>                 
                                {% endif %}                                     
                            </div>                                              
                            <p class="card-text text-muted small">{{            
                            recipe.description|truncatewords:20 }}</p>          
                            <div class="recipe-meta">                           
                                <span><i class="bi bi-clock"></i> {{            
                                recipe.total_time }}m</span>                    
                                <span><i class="bi bi-people"></i> {{           
                                recipe.servings }} servings</span>              
                                {% if recipe.calories_per_serving %}            
                                <span><i class="bi bi-fire"></i> {{             
                                recipe.calories_per_serving }} cal</span>       
                                {% endif %}                                     
                            </div>                                              
                        </div>                                                  
                        <div class="card-footer bg-transparent border-0">       
                            <a href="{% url 'recipe_detail' recipe.slug %}"     
                            class="btn btn-primary w-100">                      
                                View Recipe <i class="bi bi-arrow-right"></i>   
                            </a>                                                
                        </div>                                                  
                    </div>                                                      
                </div>                                                          
                {% empty %}                                                     
                <div class="col-12 text-center py-5">                           
                    <i class="bi bi-emoji-frown display-1 text-muted"></i>      
                    <h3 class="text-muted mt-3">No recipes found</h3>           
                    <p class="text-muted">Try adjusting your filters or <a      
                    href="{% url 'recipe_create' %}">add a new recipe</a></p>   
                </div>                                                          
                {% endfor %}                                                    
            </div>                                                              
        </div>                                                                  
    </section>                                                                  
    {% endblock %}                                                              
  ──────                                                                        
  ### 31. templates/recipes/recipe_detail.html                                  
                                                                                
    {% extends 'base.html' %}                                                   
    {% load static %}                                                           
                                                                                
    {% block title %}{{ recipe.title }}{% endblock %}                           
                                                                                
    {% block content %}                                                         
    <article class="py-5">                                                      
        <div class="container">                                                 
            <!-- Recipe Header -->                                              
            <div class="row mb-4">                                              
                <div class="col-lg-6">                                          
                    {% if recipe.image %}                                       
                    <div class="recipe-detail-img-wrapper">                     
                        <img src="{{ recipe.image.url }}" class="img-fluid      
                        rounded-4 shadow" alt="{{ recipe.title }}">             
                    </div>                                                      
                    {% endif %}                                                 
                </div>                                                          
                <div class="col-lg-6">                                          
                    <div class="d-flex align-items-center gap-2 mb-2">          
                        {% if recipe.category %}                                
                        <span class="badge bg-primary">{{ recipe.category.icon  
                        }} {{ recipe.category.name }}</span>                    
                        {% endif %}                                             
                        <span class="badge bg-{{ recipe.difficulty }}">{{       
                        recipe.get_difficulty_display }}</span>                 
                        {% if recipe.is_vegetarian %}<span class="badge         
                        bg-success">🌿 Vegetarian</span>{% endif %}             
                        {% if recipe.is_vegan %}<span class="badge bg-info">🌱  
                        Vegan</span>{% endif %}                                 
                    </div>                                                      
                    <h1 class="display-5 fw-bold">{{ recipe.title }}</h1>       
                    <p class="lead text-muted">{{ recipe.description }}</p>     
                                                                                
                    <div class="recipe-info-grid mb-3">                         
                        <div class="info-item">                                 
                            <i class="bi bi-clock"></i>                         
                            <span class="info-label">Prep</span>                
                            <span class="info-value">{{ recipe.prep_time        
                            }}m</span>                                          
                        </div>                                                  
                        <div class="info-item">                                 
                            <i class="bi bi-fire"></i>                          
                            <span class="info-label">Cook</span>                
                            <span class="info-value">{{ recipe.cook_time        
                            }}m</span>                                          
                        </div>                                                  
                        <div class="info-item">                                 
                            <i class="bi bi-hourglass-split"></i>               
                            <span class="info-label">Total</span>               
                            <span class="info-value">{{ recipe.total_time       
                            }}m</span>                                          
                        </div>                                                  
                        <div class="info-item">                                 
                            <i class="bi bi-people"></i>                        
                            <span class="info-label">Servings</span>            
                            <span class="info-value">{{ recipe.servings         
                            }}</span>                                           
                        </div>                                                  
                    </div>                                                      
                                                                                
                    <!-- Rating -->                                             
                    <div class="mb-3">                                          
                        <span class="h4 text-warning">                          
                            {% for i in "12345" %}                              
                                {% if forloop.counter <= recipe.average_rating  
                                %}                                              
                                    <i class="bi bi-star-fill"></i>             
                                {% else %}                                      
                                    <i class="bi bi-star"></i>                  
                                {% endif %}                                     
                            {% endfor %}                                        
                        </span>                                                 
                        <span class="text-muted">({{ reviews.count }}           
                        reviews)</span>                                         
                    </div>                                                      
                                                                                
                    <!-- Actions -->                                            
                    <div class="d-flex gap-2 flex-wrap">                        
                        {% if user.is_authenticated %}                          
                        <a href="{% url 'toggle_favorite' recipe.id %}"         
                        class="btn {% if is_favorited %}btn-danger{% else       
                        %}btn-outline-danger{% endif %}">                       
                            <i class="bi {% if is_favorited %}bi-heart-fill{%   
                            else %}bi-heart{% endif %}"></i>                    
                            {% if is_favorited %}Saved{% else %}Save{% endif %} 
                        </a>                                                    
                        {% endif %}                                             
                        <button class="btn btn-outline-secondary"               
                        onclick="window.print()">                               
                            <i class="bi bi-printer"></i> Print                 
                        </button>                                               
                        {% if user == recipe.author %}                          
                        <a href="{% url 'recipe_edit' recipe.slug %}" class="btn
                        btn-outline-primary">                                   
                            <i class="bi bi-pencil"></i> Edit                   
                        </a>                                                    
                        <a href="{% url 'recipe_delete' recipe.slug %}"         
                        class="btn btn-outline-danger">                         
                            <i class="bi bi-trash"></i> Delete                  
                        </a>                                                    
                        {% endif %}                                             
                    </div>                                                      
                </div>                                                          
            </div>                                                              
                                                                                
            <!-- Nutrition Info -->                                             
            {% if recipe.calories_per_serving %}                                
            <div class="card glass-card mb-4 p-4">                              
                <h3 class="mb-3"><i class="bi bi-clipboard2-pulse"></i>         
                Nutrition per Serving</h3>                                      
                <div class="row text-center">                                   
                    <div class="col-3">                                         
                        <div class="nutrition-circle calories">                 
                            <span class="nutrition-value">{{                    
                            recipe.calories_per_serving }}</span>               
                            <span class="nutrition-label">Calories</span>       
                        </div>                                                  
                    </div>                                                      
                    {% if recipe.protein %}                                     
                    <div class="col-3">                                         
                        <div class="nutrition-circle protein">                  
                            <span class="nutrition-value">{{ recipe.protein     
                            }}g</span>                                          
                            <span class="nutrition-label">Protein</span>        
                        </div>                                                  
                    </div>                                                      
                    {% endif %}                                                 
                    {% if recipe.carbs %}                                       
                    <div class="col-3">                                         
                        <div class="nutrition-circle carbs">                    
                            <span class="nutrition-value">{{ recipe.carbs       
                            }}g</span>                                          
                            <span class="nutrition-label">Carbs</span>          
                        </div>                                                  
                    </div>                                                      
                    {% endif %}                                                 
                    {% if recipe.fat %}                                         
                    <div class="col-3">                                         
                        <div class="nutrition-circle fat">                      
                            <span class="nutrition-value">{{ recipe.fat         
                            }}g</span>                                          
                            <span class="nutrition-label">Fat</span>            
                        </div>                                                  
                    </div>                                                      
                    {% endif %}                                                 
                </div>                                                          
            </div>                                                              
            {% endif %}                                                         
                                                                                
            <!-- Servings Scaler + Ingredients -->                              
            <div class="row">                                                   
                <div class="col-lg-4">                                          
                    <div class="card glass-card p-4 mb-4 sticky-lg-top"         
                    style="top: 80px;">                                         
                        <h3 class="mb-3"><i class="bi bi-basket"></i>           
                        Ingredients</h3>                                        
                                                                                
                        <!-- Serving Scaler -->                                 
                        <div class="serving-scaler mb-3">                       
                            <label class="form-label fw-bold">Servings:</label> 
                            <div class="input-group">                           
                                <button class="btn btn-outline-primary"         
                                onclick="scaleServings(-1)">−</button>          
                                <input type="number" id="servings-input"        
                                class="form-control text-center" value="{{      
                                recipe.servings }}" min="1" data-original="{{   
                                recipe.servings }}"                             
                                onchange="updateIngredients()">                 
                                <button class="btn btn-outline-primary"         
                                onclick="scaleServings(1)">+</button>           
                            </div>                                              
                        </div>                                                  
                                                                                
                        <ul class="ingredient-list list-unstyled">              
                            {% for ing in recipe.ingredients.all %}             
                            <li class="ingredient-item">                        
                                <input type="checkbox" class="form-check-input  
                                ingredient-check" id="ing-{{ ing.id }}">        
                                <label for="ing-{{ ing.id }}">                  
                                    <span class="ingredient-qty"                
                                    data-original="{{ ing.quantity }}">{{       
                                    ing.quantity }}</span>                      
                                    {{ ing.unit }} {{ ing.name }}               
                                </label>                                        
                            </li>                                               
                            {% endfor %}                                        
                        </ul>                                                   
                    </div>                                                      
                </div>                                                          
                                                                                
                <!-- Steps -->                                                  
                <div class="col-lg-8">                                          
                    <div class="card glass-card p-4 mb-4">                      
                        <div class="d-flex justify-content-between              
                        align-items-center mb-3">                               
                            <h3 class="mb-0"><i class="bi bi-list-ol"></i>      
                            Instructions</h3>                                   
                            <button class="btn btn-primary"                     
                            id="cooking-mode-btn" onclick="toggleCookingMode()">
                                <i class="bi bi-fire"></i> Cooking Mode         
                            </button>                                           
                        </div>                                                  
                        <div class="steps-list">                                
                            {% for step in recipe.steps.all %}                  
                            <div class="step-item" data-step="{{ step.order }}">
                                <div class="step-number">{{ step.order }}</div> 
                                <div class="step-content">                      
                                    <p class="step-instruction">{{              
                                    step.instruction }}</p>                     
                                    {% if step.duration_minutes %}              
                                    <div class="step-timer">                    
                                        <button class="btn btn-sm               
                                        btn-outline-warning timer-btn"          
                                        onclick="startTimer(this, {{            
                                        step.duration_minutes }})">             
                                            <i class="bi bi-stopwatch"></i> {{  
    step.duration_minutes }} min                                                
                                        </button>                               
                                        <span class="timer-display              
                                        d-none"></span>                         
                                    </div>                                      
                                    {% endif %}                                 
                                </div>                                          
                            </div>                                              
                            {% endfor %}                                        
                        </div>                                                  
                    </div>                                                      
                </div>                                                          
            </div>                                                              
                                                                                
            <!-- Reviews Section -->                                            
            <div class="card glass-card p-4 mt-4">                              
                <h3 class="mb-4"><i class="bi bi-chat-dots"></i> Reviews ({{    
                reviews.count }})</h3>                                          
                                                                                
                {% if user.is_authenticated %}                                  
                <form method="post" class="mb-4">                               
                    {% csrf_token %}                                            
                    <div class="mb-3">                                          
                        <label class="form-label">Your Rating</label>           
                        {{ review_form.rating }}                                
                    </div>                                                      
                    <div class="mb-3">                                          
                        {{ review_form.comment }}                               
                    </div>                                                      
                    <button type="submit" class="btn btn-primary">              
                        <i class="bi bi-send"></i> Submit Review                
                    </button>                                                   
                </form>                                                         
                {% endif %}                                                     
                                                                                
                {% for review in reviews %}                                     
                <div class="review-card mb-3 p-3">                              
                    <div class="d-flex justify-content-between">                
                        <div>                                                   
                            <strong>{{ review.user.username }}</strong>         
                            <span class="text-warning ms-2">                    
                                {% for i in "12345" %}                          
                                    {% if forloop.counter <= review.rating %}★{%
                                    else %}☆{% endif %}                         
                                {% endfor %}                                    
                            </span>                                             
                        </div>                                                  
                        <small class="text-muted">{{ review.created_at|timesince
                        }} ago</small>                                          
                    </div>                                                      
                    <p class="mt-2 mb-1">{{ review.comment }}</p>               
                    {% if review.user == user %}                                
                    <form method="post" action="{% url 'delete_review' review.pk
                    %}" class="d-inline">                                       
                        {% csrf_token %}                                        
                        <button type="submit" class="btn btn-sm                 
                        btn-outline-danger">                                    
                            <i class="bi bi-trash"></i> Delete                  
                        </button>                                               
                    </form>                                                     
                    {% endif %}                                                 
                </div>                                                          
                {% empty %}                                                     
                <p class="text-muted">No reviews yet. Be the first to           
                review!</p>                                                     
                {% endfor %}                                                    
            </div>                                                              
        </div>                                                                  
    </article>                                                                  
    {% endblock %}                                                              
                                                                                
    {% block extra_js %}                                                        
    <script>                                                                    
    // Serving Scaler                                                           
    function scaleServings(delta) {                                             
        const input = document.getElementById('servings-input');                
        let val = parseInt(input.value) + delta;                                
        if (val < 1) val = 1;                                                   
        input.value = val;                                                      
        updateIngredients();                                                    
    }                                                                           
                                                                                
    function updateIngredients() {                                              
        const input = document.getElementById('servings-input');                
        const newServings = parseInt(input.value);                              
        const original = parseInt(input.dataset.original);                      
        const ratio = newServings / original;                                   
                                                                                
        document.querySelectorAll('.ingredient-qty').forEach(el => {            
            const origQty = parseFloat(el.dataset.original);                    
            const newQty = (origQty * ratio).toFixed(2).replace(/\.?0+$/, '');  
            el.textContent = newQty;                                            
        });                                                                     
    }                                                                           
                                                                                
    // Cooking Mode                                                             
    function toggleCookingMode() {                                              
        document.body.classList.toggle('cooking-mode');                         
        const btn = document.getElementById('cooking-mode-btn');                
        if (document.body.classList.contains('cooking-mode')) {                 
            btn.innerHTML = '<i class="bi bi-x-circle"></i> Exit Cooking Mode'; 
            btn.classList.replace('btn-primary', 'btn-danger');                 
        } else {                                                                
            btn.innerHTML = '<i class="bi bi-fire"></i> Cooking Mode';          
            btn.classList.replace('btn-danger', 'btn-primary');                 
        }                                                                       
    }                                                                           
                                                                                
    // Step Timers                                                              
    function startTimer(btn, minutes) {                                         
        const display = btn.nextElementSibling;                                 
        btn.classList.add('d-none');                                            
        display.classList.remove('d-none');                                     
        let seconds = minutes * 60;                                             
                                                                                
        const interval = setInterval(() => {                                    
            const m = Math.floor(seconds / 60);                                 
            const s = seconds % 60;                                             
            display.textContent = `${m}:${s.toString().padStart(2, '0')}`;      
            if (seconds <= 0) {                                                 
                clearInterval(interval);                                        
                display.textContent = '✅ Done!';                               
                display.classList.add('text-success', 'fw-bold');               
                // Audio alert                                                  
                try {                                                           
                    const ctx = new AudioContext();                             
                    const osc = ctx.createOscillator();                         
                    osc.connect(ctx.destination);                               
                    osc.frequency.value = 800;                                  
                    osc.start();                                                
                    setTimeout(() => osc.stop(), 500);                          
                } catch(e) {}                                                   
            }                                                                   
            seconds--;                                                          
        }, 1000);                                                               
    }                                                                           
    </script>                                                                   
    {% endblock %}                                                              
  ──────                                                                        
  ### 32. templates/recipes/recipe_form.html                                    
                                                                                
    {% extends 'base.html' %}                                                   
                                                                                
    {% block title %}{% if editing %}Edit{% else %}New{% endif %} Recipe{%      
    endblock %}                                                                 
                                                                                
    {% block content %}                                                         
    <div class="container py-5">                                                
        <div class="row justify-content-center">                                
            <div class="col-lg-8">                                              
                <div class="card glass-card p-4">                               
                    <h2 class="mb-4">                                           
                        {% if editing %}<i class="bi bi-pencil"></i> Edit       
                        Recipe{% else %}<i class="bi bi-plus-circle"></i> New   
                        Recipe{% endif %}                                       
                    </h2>                                                       
                    <form method="post" enctype="multipart/form-data">          
                        {% csrf_token %}                                        
                                                                                
                        <div class="row g-3">                                   
                            <div class="col-md-8">{{ form.title }}</div>        
                            <div class="col-md-4">{{ form.slug }}</div>         
                            <div class="col-12">{{ form.description }}</div>    
                            <div class="col-md-6">{{ form.category }}</div>     
                            <div class="col-md-6">{{ form.difficulty }}</div>   
                            <div class="col-md-4">{{ form.prep_time }}</div>    
                            <div class="col-md-4">{{ form.cook_time }}</div>    
                            <div class="col-md-4">{{ form.servings }}</div>     
                            <div class="col-md-3">{{ form.calories_per_serving  
                            }}</div>                                            
                            <div class="col-md-3">{{ form.protein }}</div>      
                            <div class="col-md-3">{{ form.carbs }}</div>        
                            <div class="col-md-3">{{ form.fat }}</div>          
                            <div class="col-md-6">                              
                                <div class="form-check">{{ form.is_vegetarian }}
                                <label>Vegetarian</label></div>                 
                            </div>                                              
                            <div class="col-md-6">                              
                                <div class="form-check">{{ form.is_vegan }}     
                                <label>Vegan</label></div>                      
                            </div>                                              
                            <div class="col-12">                                
                                <label class="form-label">Recipe Image</label>  
                                {{ form.image }}                                
                            </div>                                              
                        </div>                                                  
                                                                                
                        <!-- Dynamic Ingredients -->                            
                        <h4 class="mt-4 mb-3"><i class="bi bi-basket"></i>      
                        Ingredients</h4>                                        
                        <div id="ingredients-container">                        
                            {% if editing %}                                    
                                {% for ing in recipe.ingredients.all %}         
                                <div class="row g-2 mb-2 ingredient-row">       
                                    <div class="col-2"><input type="number"     
                                    name="ingredient_qty[]" class="form-control"
                                    step="0.01" value="{{ ing.quantity }}"      
                                    placeholder="Qty"></div>                    
                                    <div class="col-3"><input type="text"       
                                    name="ingredient_unit[]"                    
                                    class="form-control" value="{{ ing.unit }}" 
                                    placeholder="Unit"></div>                   
                                    <div class="col-5"><input type="text"       
                                    name="ingredient_name[]"                    
                                    class="form-control" value="{{ ing.name }}" 
                                    placeholder="Ingredient"></div>             
                                    <div class="col-2"><button type="button"    
                                    class="btn btn-outline-danger w-100"        
                                    onclick="this.closest('.ingredient-row').rem
                                    ove()"><i class="bi                         
                                    bi-trash"></i></button></div>               
                                </div>                                          
                                {% endfor %}                                    
                            {% endif %}                                         
                            <div class="row g-2 mb-2 ingredient-row">           
                                <div class="col-2"><input type="number"         
                                name="ingredient_qty[]" class="form-control"    
                                step="0.01" placeholder="Qty"></div>            
                                <div class="col-3"><input type="text"           
                                name="ingredient_unit[]" class="form-control"   
                                placeholder="Unit"></div>                       
                                <div class="col-5"><input type="text"           
                                name="ingredient_name[]" class="form-control"   
                                placeholder="Ingredient"></div>                 
                                <div class="col-2"><button type="button"        
                                class="btn btn-outline-danger w-100"            
                                onclick="this.closest('.ingredient-row').remove(
                                )"><i class="bi bi-trash"></i></button></div>   
                            </div>                                              
                        </div>                                                  
                        <button type="button" class="btn btn-outline-success    
                        btn-sm mb-3" onclick="addIngredient()">                 
                            <i class="bi bi-plus"></i> Add Ingredient           
                        </button>                                               
                                                                                
                        <!-- Dynamic Steps -->                                  
                        <h4 class="mt-3 mb-3"><i class="bi bi-list-ol"></i>     
                        Steps</h4>                                              
                        <div id="steps-container">                              
                            {% if editing %}                                    
                                {% for step in recipe.steps.all %}              
                                <div class="mb-3 step-row">                     
                                    <div class="d-flex gap-2">                  
                                        <textarea name="step_instruction[]"     
                                        class="form-control" rows="2"           
                                        placeholder="Step instruction">{{       
                                        step.instruction }}</textarea>          
                                        <input type="number"                    
                                        name="step_duration[]"                  
                                        class="form-control" style="width:100px"
                                        value="{{ step.duration_minutes }}"     
                                        placeholder="Min">                      
                                        <button type="button" class="btn        
                                        btn-outline-danger"                     
                                        onclick="this.closest('.step-row').remov
                                        e()"><i class="bi                       
                                        bi-trash"></i></button>                 
                                    </div>                                      
                                </div>                                          
                                {% endfor %}                                    
                            {% endif %}                                         
                            <div class="mb-3 step-row">                         
                                <div class="d-flex gap-2">                      
                                    <textarea name="step_instruction[]"         
                                    class="form-control" rows="2"               
                                    placeholder="Step instruction"></textarea>  
                                    <input type="number" name="step_duration[]" 
                                    class="form-control" style="width:100px"    
                                    placeholder="Min">                          
                                    <button type="button" class="btn            
                                    btn-outline-danger"                         
                                    onclick="this.closest('.step-row').remove()"
                                    ><i class="bi bi-trash"></i></button>       
                                </div>                                          
                            </div>                                              
                        </div>                                                  
                        <button type="button" class="btn btn-outline-success    
                        btn-sm mb-4" onclick="addStep()">                       
                            <i class="bi bi-plus"></i> Add Step                 
                        </button>                                               
                                                                                
                        <div class="d-grid">                                    
                            <button type="submit" class="btn btn-primary        
                            btn-lg">                                            
                                {% if editing %}💾 Update Recipe{% else %}🍳    
                                Create Recipe{% endif %}                        
                            </button>                                           
                        </div>                                                  
                    </form>                                                     
                </div>                                                          
            </div>                                                              
        </div>                                                                  
    </div>                                                                      
    {% endblock %}                                                              
                                                                                
    {% block extra_js %}                                                        
    <script>                                                                    
    function addIngredient() {                                                  
        const container = document.getElementById('ingredients-container');     
        const html = `<div class="row g-2 mb-2 ingredient-row">                 
            <div class="col-2"><input type="number" name="ingredient_qty[]"     
            class="form-control" step="0.01" placeholder="Qty"></div>           
            <div class="col-3"><input type="text" name="ingredient_unit[]"      
            class="form-control" placeholder="Unit"></div>                      
            <div class="col-5"><input type="text" name="ingredient_name[]"      
            class="form-control" placeholder="Ingredient"></div>                
            <div class="col-2"><button type="button" class="btn                 
            btn-outline-danger w-100"                                           
            onclick="this.closest('.ingredient-row').remove()"><i class="bi     
            bi-trash"></i></button></div>                                       
        </div>`;                                                                
        container.insertAdjacentHTML('beforeend', html);                        
    }                                                                           
                                                                                
    function addStep() {                                                        
        const container = document.getElementById('steps-container');           
        const html = `<div class="mb-3 step-row">                               
            <div class="d-flex gap-2">                                          
                <textarea name="step_instruction[]" class="form-control"        
                rows="2" placeholder="Step instruction"></textarea>             
                <input type="number" name="step_duration[]" class="form-control"
                style="width:100px" placeholder="Min">                          
                <button type="button" class="btn btn-outline-danger"            
                onclick="this.closest('.step-row').remove()"><i class="bi       
                bi-trash"></i></button>                                         
            </div>                                                              
        </div>`;                                                                
        container.insertAdjacentHTML('beforeend', html);                        
    }                                                                           
    </script>                                                                   
    {% endblock %}                                                              
  ──────                                                                        
  ### 33. templates/recipes/recipe_confirm_delete.html                          
                                                                                
    {% extends 'base.html' %}                                                   
                                                                                
    {% block title %}Delete {{ recipe.title }}{% endblock %}                    
                                                                                
    {% block content %}                                                         
    <div class="container py-5">                                                
        <div class="row justify-content-center">                                
            <div class="col-md-6">                                              
                <div class="card glass-card p-4 text-center">                   
                    <h2 class="text-danger mb-3"><i class="bi                   
                    bi-exclamation-triangle"></i></h2>                          
                    <h3>Delete "{{ recipe.title }}"?</h3>                       
                    <p class="text-muted">This action cannot be undone.</p>     
                    <form method="post">                                        
                        {% csrf_token %}                                        
                        <div class="d-flex justify-content-center gap-3">       
                            <a href="{% url 'recipe_detail' recipe.slug %}"     
                            class="btn btn-secondary">Cancel</a>                
                            <button type="submit" class="btn                    
                            btn-danger">Delete</button>                         
                        </div>                                                  
                    </form>                                                     
                </div>                                                          
            </div>                                                              
        </div>                                                                  
    </div>                                                                      
    {% endblock %}                                                              
  ──────                                                                        
  ### 34. templates/accounts/login.html                                         
                                                                                
    {% extends 'base.html' %}                                                   
                                                                                
    {% block title %}Login{% endblock %}                                        
                                                                                
    {% block content %}                                                         
    <div class="container py-5">                                                
        <div class="row justify-content-center">                                
            <div class="col-md-5">                                              
                <div class="card glass-card p-4">                               
                    <h2 class="text-center mb-4"><i class="bi                   
                    bi-box-arrow-in-right"></i> Login</h2>                      
                    {% if error %}                                              
                    <div class="alert alert-danger">{{ error }}</div>           
                    {% endif %}                                                 
                    <form method="post">                                        
                        {% csrf_token %}                                        
                        <div class="mb-3">                                      
                            <label class="form-label">Username</label>          
                            <input type="text" name="username"                  
                            class="form-control" required>                      
                        </div>                                                  
                        <div class="mb-3">                                      
                            <label class="form-label">Password</label>          
                            <input type="password" name="password"              
                            class="form-control" required>                      
                        </div>                                                  
                        <button type="submit" class="btn btn-primary w-100      
                        mb-3">Login</button>                                    
                    </form>                                                     
                    <p class="text-center text-muted">Don't have an account? <a 
                    href="{% url 'register' %}">Sign up</a></p>                 
                </div>                                                          
            </div>                                                              
        </div>                                                                  
    </div>                                                                      
    {% endblock %}                                                              
  ──────                                                                        
  ### 35. templates/accounts/register.html                                      
                                                                                
    {% extends 'base.html' %}                                                   
                                                                                
    {% block title %}Sign Up{% endblock %}                                      
                                                                                
    {% block content %}                                                         
    <div class="container py-5">                                                
        <div class="row justify-content-center">                                
            <div class="col-md-5">                                              
                <div class="card glass-card p-4">                               
                    <h2 class="text-center mb-4"><i class="bi                   
                    bi-person-plus"></i> Create Account</h2>                    
                    <form method="post">                                        
                        {% csrf_token %}                                        
                        {% for field in form %}                                 
                        <div class="mb-3">                                      
                            <label class="form-label">{{ field.label }}</label> 
                            {{ field }}                                         
                            {% if field.errors %}                               
                            <div class="text-danger small">{{ field.errors      
                            }}</div>                                            
                            {% endif %}                                         
                        </div>                                                  
                        {% endfor %}                                            
                        <button type="submit" class="btn btn-primary w-100      
                        mb-3">Create Account</button>                           
                    </form>                                                     
                    <p class="text-center text-muted">Already have an account?  
                    <a href="{% url 'login' %}">Login</a></p>                   
                </div>                                                          
            </div>                                                              
        </div>                                                                  
    </div>                                                                      
    {% endblock %}                                                              
  ──────                                                                        
  ### 36. static/css/style.css                                                  
                                                                                
    /* ============================================                             
       KHAANA KHAZANA - Premium Recipe Website                                  
       ============================================ */                          
                                                                                
    :root {                                                                     
        --primary: #e65100;                                                     
        --primary-light: #ff833a;                                               
        --primary-dark: #ac1900;                                                
        --secondary: #2e7d32;                                                   
        --accent: #f9a825;                                                      
        --bg-light: #fefefe;                                                    
        --bg-dark: #1a1a2e;                                                     
        --glass-bg: rgba(255, 255, 255, 0.85);                                  
        --glass-border: rgba(255, 255, 255, 0.3);                               
        --text-primary: #2d3436;                                                
        --text-secondary: #636e72;                                              
        --font-heading: 'Playfair Display', serif;                              
        --font-body: 'Poppins', sans-serif;                                     
    }                                                                           
                                                                                
    * {                                                                         
        margin: 0;                                                              
        padding: 0;                                                             
        box-sizing: border-box;                                                 
    }                                                                           
                                                                                
    body {                                                                      
        font-family: var(--font-body);                                          
        background: var(--bg-light);                                            
        color: var(--text-primary);                                             
        overflow-x: hidden;                                                     
    }                                                                           
                                                                                
    h1, h2, h3, h4, h5, h6 {                                                    
        font-family: var(--font-heading);                                       
    }                                                                           
                                                                                
    /* Glass Morphism */                                                        
    .glass-card {                                                               
        background: var(--glass-bg);                                            
        backdrop-filter: blur(20px);                                            
        -webkit-backdrop-filter: blur(20px);                                    
        border: 1px solid var(--glass-border);                                  
        border-radius: 16px;                                                    
        transition: transform 0.3s ease, box-shadow 0.3s ease;                  
    }                                                                           
                                                                                
    .glass-card:hover {                                                         
        transform: translateY(-4px);                                            
        box-shadow: 0 12px 40px rgba(0, 0, 0, 0.15);                            
    }                                                                           
                                                                                
    .glass-nav {                                                                
        background: var(--glass-bg);                                            
        backdrop-filter: blur(20px);                                            
        -webkit-backdrop-filter: blur(20px);                                    
        border-bottom: 1px solid var(--glass-border);                           
        box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);                              
    }                                                                           
                                                                                
    .glass-footer {                                                             
        background: var(--glass-bg);                                            
        backdrop-filter: blur(20px);                                            
        -webkit-backdrop-filter: blur(20px);                                    
        border-top: 1px solid var(--glass-border);                              
    }                                                                           
                                                                                
    /* Brand */                                                                 
    .brand-icon {                                                               
        font-size: 1.5rem;                                                      
    }                                                                           
                                                                                
    .navbar-brand {                                                             
        font-family: var(--font-heading);                                       
        font-size: 1.4rem;                                                      
        color: var(--primary) !important;                                       
    }                                                                           
                                                                                
    /* Hero Section */                                                          
    .hero-section {                                                             
        position: relative;                                                     
        min-height: 70vh;                                                       
        display: flex;                                                          
        align-items: center;                                                    
        background: linear-gradient(135deg, #e65100 0%, #ff833a 50%, #f9a825    
        100%);                                                                  
        overflow: hidden;                                                       
    }                                                                           
                                                                                
    .hero-section::before {                                                     
        content: '';                                                            
        position: absolute;                                                     
        top: -50%;                                                              
        left: -50%;                                                             
        width: 200%;                                                            
        height: 200%;                                                           
        background: radial-gradient(circle, rgba(255,255,255,0.1) 0%,           
        transparent 70%);                                                       
        animation: float 6s ease-in-out infinite;                               
    }                                                                           
                                                                                
    @keyframes float {                                                          
        0%, 100% { transform: translate(0, 0); }                                
        50% { transform: translate(30px, -30px); }                              
    }                                                                           
                                                                                
    .hero-overlay {                                                             
        position: absolute;                                                     
        inset: 0;                                                               
        background: rgba(0, 0, 0, 0.2);                                         
    }                                                                           
                                                                                
    .hero-content {                                                             
        position: relative;                                                     
        z-index: 1;                                                             
    }                                                                           
                                                                                
    /* Animations */                                                            
    .animate-fade-in {                                                          
        animation: fadeIn 0.8s ease-out;                                        
    }                                                                           
                                                                                
    .animate-fade-in-delay {                                                    
        animation: fadeIn 0.8s ease-out 0.3s both;                              
    }                                                                           
                                                                                
    .animate-fade-in-delay-2 {                                                  
        animation: fadeIn 0.8s ease-out 0.6s both;                              
    }                                                                           
                                                                                
    @keyframes fadeIn {                                                         
        from { opacity: 0; transform: translateY(20px); }                       
        to { opacity: 1; transform: translateY(0); }                            
    }                                                                           
                                                                                
    /* Section Titles */                                                        
    .section-title {                                                            
        font-family: var(--font-heading);                                       
        font-weight: 700;                                                       
        position: relative;                                                     
        padding-bottom: 10px;                                                   
    }                                                                           
                                                                                
    .section-title::after {                                                     
        content: '';                                                            
        position: absolute;                                                     
        bottom: 0;                                                              
        left: 50%;                                                              
        transform: translateX(-50%);                                            
        width: 60px;                                                            
        height: 3px;                                                            
        background: var(--primary);                                             
        border-radius: 3px;                                                     
    }                                                                           
                                                                                
    /* Category Cards */                                                        
    .category-card .card {                                                      
        transition: all 0.3s ease;                                              
    }                                                                           
                                                                                
    .category-card:hover .card {                                                
        transform: scale(1.05);                                                 
        border-color: var(--primary);                                           
    }                                                                           
                                                                                
    .category-icon {                                                            
        font-size: 2rem;                                                        
        display: block;                                                         
        margin-bottom: 0.5rem;                                                  
    }                                                                           
                                                                                
    .category-name {                                                            
        font-weight: 500;                                                       
        font-size: 0.85rem;                                                     
        color: var(--text-primary);                                             
    }                                                                           
                                                                                
    /* Recipe Cards */                                                          
    .recipe-card {                                                              
        overflow: hidden;                                                       
    }                                                                           
                                                                                
    .recipe-img-wrapper {                                                       
        position: relative;                                                     
        overflow: hidden;                                                       
        height: 220px;                                                          
    }                                                                           
                                                                                
    .recipe-img {                                                               
        width: 100%;                                                            
        height: 100%;                                                           
        object-fit: cover;                                                      
        transition: transform 0.5s ease;                                        
    }                                                                           
                                                                                
    .recipe-card:hover .recipe-img {                                            
        transform: scale(1.1);                                                  
    }                                                                           
                                                                                
    .recipe-badges {                                                            
        position: absolute;                                                     
        top: 10px;                                                              
        left: 10px;                                                             
        display: flex;                                                          
        gap: 5px;                                                               
    }                                                                           
                                                                                
    .recipe-meta {                                                              
        display: flex;                                                          
        gap: 15px;                                                              
        font-size: 0.85rem;                                                     
        color: var(--text-secondary);                                           
    }                                                                           
                                                                                
    .recipe-meta i {                                                            
        color: var(--primary);                                                  
    }                                                                           
                                                                                
    /* Recipe Detail */                                                         
    .recipe-detail-img-wrapper {                                                
        border-radius: 20px;                                                    
        overflow: hidden;                                                       
    }                                                                           
                                                                                
    .recipe-info-grid {                                                         
        display: grid;                                                          
        grid-template-columns: repeat(4, 1fr);                                  
        gap: 10px;                                                              
    }                                                                           
                                                                                
    .info-item {                                                                
        text-align: center;                                                     
        padding: 10px;                                                          
        border-radius: 12px;                                                    
        background: rgba(230, 81, 0, 0.1);                                      
    }                                                                           
                                                                                
    .info-item i {                                                              
        font-size: 1.3rem;                                                      
        color: var(--primary);                                                  
        display: block;                                                         
    }                                                                           
                                                                                
    .info-label {                                                               
        font-size: 0.75rem;                                                     
        color: var(--text-secondary);                                           
        display: block;                                                         
    }                                                                           
                                                                                
    .info-value {                                                               
        font-weight: 600;                                                       
        font-size: 1.1rem;                                                      
        display: block;                                                         
    }                                                                           
                                                                                
    /* Nutrition Circles */                                                     
    .nutrition-circle {                                                         
        width: 100px;                                                           
        height: 100px;                                                          
        border-radius: 50%;                                                     
        display: inline-flex;                                                   
        flex-direction: column;                                                 
        align-items: center;                                                    
        justify-content: center;                                                
        margin: 0 auto;                                                         
    }                                                                           
                                                                                
    .nutrition-circle.calories { background: rgba(230, 81, 0, 0.15); border: 3px
    solid var(--primary); }                                                     
    .nutrition-circle.protein { background: rgba(46, 125, 50, 0.15); border: 3px
    solid var(--secondary); }                                                   
    .nutrition-circle.carbs { background: rgba(249, 168, 37, 0.15); border: 3px 
    solid var(--accent); }                                                      
    .nutrition-circle.fat { background: rgba(156, 39, 176, 0.15); border: 3px   
    solid #9c27b0; }                                                            
                                                                                
    .nutrition-value {                                                          
        font-weight: 700;                                                       
        font-size: 1rem;                                                        
    }                                                                           
                                                                                
    .nutrition-label {                                                          
        font-size: 0.7rem;                                                      
        color: var(--text-secondary);                                           
    }                                                                           
                                                                                
    /* Ingredients */                                                           
    .ingredient-list {                                                          
        max-height: 400px;                                                      
        overflow-y: auto;                                                       
    }                                                                           
                                                                                
    .ingredient-item {                                                          
        padding: 8px 0;                                                         
        border-bottom: 1px dashed rgba(0,0,0,0.1);                              
        display: flex;                                                          
        align-items: center;                                                    
        gap: 10px;                                                              
    }                                                                           
                                                                                
    .ingredient-item label {                                                    
        cursor: pointer;                                                        
    }                                                                           
                                                                                
    .ingredient-check:checked + label {                                         
        text-decoration: line-through;                                          
        opacity: 0.5;                                                           
    }                                                                           
                                                                                
    .serving-scaler .input-group {                                              
        max-width: 200px;                                                       
    }                                                                           
                                                                                
    /* Steps */                                                                 
    .step-item {                                                                
        display: flex;                                                          
        gap: 15px;                                                              
        padding: 15px 0;                                                        
        border-bottom: 1px solid rgba(0,0,0,0.05);                              
    }                                                                           
                                                                                
    .step-number {                                                              
        width: 36px;                                                            
        height: 36px;                                                           
        min-width: 36px;                                                        
        border-radius: 50%;                                                     
        background: var(--primary);                                             
        color: white;                                                           
        display: flex;                                                          
        align-items: center;                                                    
        justify-content: center;                                                
        font-weight: 700;                                                       
    }                                                                           
                                                                                
    .step-content {                                                             
        flex: 1;                                                                
    }                                                                           
                                                                                
    .step-instruction {                                                         
        margin-bottom: 5px;                                                     
    }                                                                           
                                                                                
    /* Reviews */                                                               
    .review-card {                                                              
        background: rgba(0, 0, 0, 0.03);                                        
        border-radius: 12px;                                                    
    }                                                                           
                                                                                
    /* Cooking Mode */                                                          
    .cooking-mode {                                                             
        background: #1a1a1a !important;                                         
        color: #fff !important;                                                 
    }                                                                           
                                                                                
    .cooking-mode .glass-card {                                                 
        background: rgba(255,255,255,0.1) !important;                           
        color: #fff !important;                                                 
    }                                                                           
                                                                                
    .cooking-mode .glass-nav,                                                   
    .cooking-mode .glass-footer {                                               
        display: none !important;                                               
    }                                                                           
                                                                                
    .cooking-mode .step-item {                                                  
        font-size: 1.3rem;                                                      
        padding: 20px 0;                                                        
    }                                                                           
                                                                                
    /* Difficulty Badges */                                                     
    .bg-easy { background-color: #4caf50 !important; }                          
    .bg-medium { background-color: #ff9800 !important; }                        
    .bg-hard { background-color: #f44336 !important; }                          
                                                                                
    /* Background Pattern */                                                    
    .bg-pattern {                                                               
        background-image: radial-gradient(circle at 1px 1px, rgba(0,0,0,0.05)   
        1px, transparent 0);                                                    
        background-size: 40px 40px;                                             
    }                                                                           
                                                                                
    /* Dark Mode Overrides */                                                   
    [data-bs-theme="dark"] {                                                    
        --glass-bg: rgba(26, 26, 46, 0.85);                                     
        --glass-border: rgba(255, 255, 255, 0.1);                               
        --text-primary: #ecf0f1;                                                
        --text-secondary: #b2bec3;                                              
        --bg-light: #0f0f23;                                                    
    }                                                                           
                                                                                
    [data-bs-theme="dark"] .glass-card:hover {                                  
        box-shadow: 0 12px 40px rgba(0, 0, 0, 0.4);                             
    }                                                                           
                                                                                
    [data-bs-theme="dark"] .review-card {                                       
        background: rgba(255, 255, 255, 0.05);                                  
    }                                                                           
                                                                                
    [data-bs-theme="dark"] .ingredient-item {                                   
        border-bottom-color: rgba(255,255,255,0.1);                             
    }                                                                           
                                                                                
    [data-bs-theme="dark"] .step-item {                                         
        border-bottom-color: rgba(255,255,255,0.1);                             
    }                                                                           
                                                                                
    /* Print Styles */                                                          
    @media print {                                                              
        .glass-nav, .glass-footer, .btn, .form-check-input, .serving-scaler,    
        #cooking-mode-btn, .review-card form, .recipe-badges { display: none    
        !important; }                                                           
                                                                                
        .glass-card { background: white !important; border: 1px solid #ddd      
        !important; box-shadow: none !important; }                              
                                                                                
        .recipe-detail-img-wrapper img { max-height: 300px; }                   
                                                                                
        body { font-size: 12pt; color: #000; }                                  
                                                                                
        .ingredient-check:checked + label { text-decoration: none; opacity: 1; }
    }                                                                           
                                                                                
    /* Responsive */                                                            
    @media (max-width: 768px) {                                                 
        .hero-section { min-height: 50vh; }                                     
        .recipe-info-grid { grid-template-columns: repeat(2, 1fr); }            
        .nutrition-circle { width: 80px; height: 80px; }                        
        .nutrition-value { font-size: 0.85rem; }                                
    }                                                                           
  ──────                                                                        
  ### 37. favorites/admin.py                                                    
                                                                                
    from django.contrib import admin                                            
                                                                                
    # Register your models here.                                                
  ──────                                                                        
  ### 38. reviews/admin.py                                                      
                                                                                
    from django.contrib import admin                                            
  
    # Register your models here.
  
  Now I have a complete picture. Let me analyze what's done vs still needed     
  based on the readme plan:                                                     
                                                                                
  ✅ Already Done:                                                              
  
  • Models (Recipe with nutrition, Ingredient, Step, Category, Review, Favorite,
  MealPlan, MealSlot)                                                           
  • Views for all apps (recipes, accounts, reviews, favorites, planner)         
  • URLs for all apps                                                           
  • Forms (RecipeForm, RegisterForm, ReviewForm)
  • Templates: base.html, home.html, recipe_list.html, recipe_detail.html,      
  recipe_form.html, recipe_confirm_delete.html, login.html, register.html       
  • CSS with glassmorphism, dark mode, animations, print styles
  • Serving scaler with ingredient updates
  • Cooking mode with timers
  • Dark mode toggle
                                                                                
  ❌ Still Missing:                                                             
                                                                                
  1. Templates: accounts/profile.html, favorites/favorite_list.html,
  planner/meal_planner.html, planner/shopping_list.html                         
  2. Tests: ALL test files are empty (recipes, accounts, reviews, favorites,    
  planner)                                                                      
  3. Admin registrations: favorites/admin.py, reviews/admin.py, planner/admin.py
  are empty                                                                     
  4. Missing import in favorites/views.py: render is not imported in            
  favorite_list                                                                 
  5. No forms.py for favorites or planner                                       
                                                                                
  Let me now build everything that's missing using a workflow to parallelize the
  work.                                                                         
● Explored 1 file (SKILL.md) (ctrl+o to expand)

  Now I have the full picture. Let me build everything that's missing. I'll use 
  a workflow to create all the missing pieces in parallel.
● Running Complete all missing templates, tests, and admin re... (ctrl+o to
expand)

  I've launched 3 parallel agents to complete all the missing work:
                                                                                
  1. Template Creator — Building the 4 missing templates (profile, favorites    
  list, meal planner, shopping list)                                            
  2. Test Writer — Writing 50+ comprehensive tests across all 5 apps            
  3. Admin & Bug Fixer — Fixing the missing render import and registering all   
  models in admin                                                               
                                                                                
  I'll let you know once everything is done and verified. ⏳                    
                                                                                
  [Workflow a1feb588-9c22-4f29-9d5a-6043227b38bb/task-19]
  
  Here are the results:
  
  • Phase: Create missing templates and fix code
  • Task 1 result: All 4 missing templates have been created successfully:      
  
  1. accounts/profile.html - User profile page with glassmorphism cards         
  2. favorites/favorite_list.html - Favorites grid with empty state
  3. planner/meal_planner.html - Weekly meal planner with modal
  4. planner/shopping_list.html - Shopping list with checkboxes
  
  • Task 2 result: All 5 test files have been written successfully with         
  comprehensive tests...
  • Task 3 result: All fixes and improvements have been completed...            
  
  All 3 tasks completed. Let me verify everything works.

● Ran (cd /home/shwetank/khaana_khazana && source venv/bin/activate && python...)
● Ran (cd /home/shwetank/khaana_khazana && source...) failed (ctrl+o to expand)

⚠ Individual quota reached. Please upgrade your subscription to increase your
limits. Resets in 167h53m53s.
Error ID: f3a86f9b-5ed7-4f6d-b0a7-df8db3d30a0c-24

 ┃ Complete all missing templates, tests, and admin registrations for Khaana
 ┃ Kha... › Test Writer needs approval for Bash
 ┃ ─────────────────────────────────────────────────────────────────────────────
 ┃
 ┃ ● Bash(cat /home/shwetank/khaana_khazana/recipes/models.py
 ┃ /home/shwetank/khaana_khazana/recipes/views.py
 ┃ /home/shwetank/khaana_khazana/recipes/urls.py)
 ┃
 ┃ ctrl+k approve · alt+j manage
───────────────────────────────────────────────────────────────────────────────────
>
───────────────────────────────────────────────────────────────────────────────────
  ● Complete all missing templates, tests, and admin registrations for Khaana Kh...
  ● Complete all missing templates, tests, and admin registrations for Khaana Kh...
  ● Complete all missing templates, tests, and admin registrations for Khaana Kh...
  ● [16:32:15] Complete all missing templates, tests, and admin registra... running
  ↓ 1 more
───────────────────────────────────────────────────────────────────────────────────
? for shortcuts     Claude Opus 4.6 (Thinking) · 1 subagent(s) · 1 task(s) · /tasks

