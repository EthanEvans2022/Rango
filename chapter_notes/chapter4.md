# Chapter 4: Templated and Media Files

## 4.1: Using Templates
- Templates are a part of the *Model-View-Template* and work with views
- Templates makes it easier to provide structure and functionality of an app by seperating the app logic from the presentational concerns 
- Think of templates as the scaffolding for building an HTML page
    - It contains *static parts* that do not change and special syntax (*template tags*) that can be overridden and changed to display *dynamic content* 

### Configuring the Templates Directory
- You need to create two directories for working with template files
    1. `Templates`
    2. A subdirectory called `rango`
        - Good practice to split templates from apps like this
- To tell Django where templates are, you have to edit the `settings.py` file
    - Locate the `TEMPLATES` data structure and edit the `DIRS` list  
    - You can add a dynamic path to the templates folder by using the `BASE_DIR` constant at the top of the `settings.py` file which is the absolute path to the directory containing the `settings.py`, which uses `__file__` combined with built-in Python functions like `os.path.abspath()` and `os.path.dirname()`
        - Having access to `BASE_DIR` makes it easy to reference Django
    - We can use this to make a new variable `TEMPLATE_DIR` that will reference the new template directory by using `os.path.join()` function to join multiple paths with the following:
        - `TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')`
    - The `join` function concatenates the variable `BASE_DIR` and 'templates' to make the new file path `<workspace>/tango_with_django_project/templates/`
        - **ALWAYS USE `os.path.join` TO CONCATENATE SYSTEM PATHS**, this will ensure that the path is write regardless of what operating system the code is running on 
    - Now we add this new file path to the `DIRS` list like so: 
        - `'DIRS': [TEMPLATE_DIR, ]`

### Adding a Template
- We can add a new template in the new template folder and input the following Django template code:
    ```
    <!DOCTYPE html>
    <html>
        <head> 
            <title>Rango</title>
        </head>
        <body>
            <h1>Rango says...</h1>
            <div>
                hey there partner! <br />
                <strong>{{ boldmessage }}</strong><br />
            </div>
            <div>
                <a href="/rango/about/">About</a><br />
            </div> </body>
    </html>
    ```
    - This clearly makes an HTML page
    - The `{{ boldmessage}}` is an example of a *Django template variable*, which can have its value set and replaced 
- To use this template, we have to change the `index()` view from earlier to display the template, instead of some text 
- Move to `rango/views.py` and check if all of these `imports` are at the top: 
    - `from django.shortcuts import render`
- Change the `index()` view to the following:
    ```
    def index(request):
        # Consturct a dictionary to pass to the template engine as its context.
        # Note the key boldmessage matches to {{boldmessage}} in the template!
        context_dict = {'boldmessage': 'cruncy, creamy, cookie, candy, cupcake!'}
        # Return a rendered response to send to the client
        # We make use of the shortcut function to make our lives easier
        # Note the first parameter is the template we wish to use
        return render(request, 'range/index.html', context=context_dict)
    ```
    - First, make a dictionary for all the template variables as key-value pairs
    - Then call the render helper function with the user's request as the first parameter, the template's filename as the second, and the context dictionary as the third. The funciton takes the data and smashes it together with the template to produce a complete HTML page that is returned with a `HttpResponse`, which is then sent to the client
- When a template file is loaded with the Django templating system, a *template context* is created
    - This template context is a dictionary that maps template variable namex with Python variables, where the Python variable replaces the template variable throuhout the entire template
- Load the template to check if the template loaded properly

## 4.2 Serving Static Media Files
- You can reference CSS or JavaScript files in the HTML template like how you can normally
- CSS and JavaScript files are considered to be **static files** because they are sent to the client as is
- Create a new directory called `static` within the project's home directory with a subdirectory of `images`
    - Make sure the `static` and `templates` directory are at the same level
- Place an image in the images subdirectory
- Django also needs to know about this new directory like it did for the templates directory, so we need to edit the `settings.py` again 
- Create a variable called `STATIC_DIR` at the top of `settings.py` and use the same trick that utilitzed `os.path.join()` to point to the new `static` directory
- Then create a new data struct called `STATICFILES_DIRS`, which Django will expect to find static files, and add the new directory path. By default this list does not exist, but check just in case
- Make sure `STATIC_URL` has been defined to `'/static/'` by default at the bottom
- `STATIC_DIR` and `STATICFILES_DIRS` refer to the location on the computer where static files are stored
- `STATIC_URL` is where to specify where these static files can be found when we run the Django development server
    - The first two are like server-side locations, while the last is a client-side location

### Static Media Files and Templates
- Using **template tags** (`{% %}`), we can tell the Django template engine that this file will use static files by including `{% load static %}`
- We then use another template tag with a call to `static`, which will combine the url specified at `STATIC_URL` and whatever else follows to create a new URL to get `{% static 'images/rango.jpg' %}` 
    - This new URL can be fed as the `src` to an image tag to display the image
- Use the `{% static %}` template tag whenever you want to reference a static file within a template 
- The following example shows how JavaScript, CSS, and images can be included within a template: 
    ```
<!DOCTYPE html>
{% load staticfiles %} <html>
    <head>
        <title>Rango</title>
        <!-- CSS -->
        <link rel="stylesheet" href="{% static "css/base.css" %}" /> <!-- JavaScript -->
        <script src="{% static "js/jquery.js" %}"></script>
    </head>
    <body>
        <!-- Image -->
        <img src="{% static "images/rango.jpg" %}" alt="Picture of Rango" /> 
    </body>
</html>
    ```
- Django will show a `http 404 error` in the console if a static file is missing or if the reference to it is incorrect

### 4.3 Serving Media
- Often you want to be able to serve dynamic media content, like files that your users upload and can change
- To serve these dynamic files, the settings need to be updated (full testing of this will be done later in the tutorial)
- Open `settings.py` where we will first tell Django where these media files will be stored
    - This is done by creating an absolute path from `BASE_DIR`, like how `TEMPLATE_DIR` and `STATIC_DIR` were created
- In some open space, add two variables:
    ```
    MEDIA_ROOT = MEDIA_DIR
    MEDIA_URL = '/media/'
    ```
    - The first variable tells where Django should look for the media files are stored and the second tells where to serve them to
- Django provides a *template context processor*, which allows us to later on reference the `MEDIA_URL` path when we need to access uploaded content
- This is done by editing the `TEMPLATES` list within `settings.py` and by editing the `context_processors` sub-list and adding the following to the list of context processors:
    `'django.template.context_processors.media',`
- Last thing to do for serving media files in a development environment is to tell Django to serve content from `MEDIA_URL`
- This is done by going into the **project's** `urls.py`, **NOT** `rango/urls.py`
- Add the following imports if they are not already there
    ```
    from django.conf import settings
    from django.conf.urls.static import static
    ```
- Modify the `urlpatterns` list and append a call to the `static()` function that was just imported liked below 
    ```
    urlpatterns = [
        ...
        ...
    ] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    ```
- This change will allow media content to be served from the `media` directory to the `/media/` url

### 4.4 Basic Workflow
- This chapter showed how to set up and create templates, use templates within the views, setup Django development serve to serve static media files and how to include images within the templates
#### Steps for creating a template and integrating with a view:
    1. Create a new template file and place it within the template directory specified within the settings, where you can use template variables and template tags 
    2. Find or create a new view within an app's `views.py` file
    3. Add view specific logic to the view (i.e. getting data from a db)
    4. Make a dictionary object which you can pass to the template engine as part of the template's context
    5. Use the `render()` function to generate the rendered response
        - Make sure you reference the request, then the template file, then the context dictionary
    6. Map the view to a URL if it has not already been mapped

#### Steps for serving a static media file
    1. Put the static media file and put it in the static directory as specified by the `STATICFILES_DIRS` that is defined in the settings
    2. Add a reference to the media file in the template
        - Use the `{% load staticfiles &} and {% static "<filename>" %}` to reference a resource

#### Steps for serving media files
    1. Place a file within the project's media direcotry, which is specified in the `MEDIA_ROOT` variable in the settings
    2. Link to the media file in a template through the `{{ MEDIA_URL }}` context variable 
        - Ex: `<img src="{{ MEDIA_URL }}cat.jpg"/>`


