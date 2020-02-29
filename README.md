# Milestone Project 4: FullStack Web Development

## Pick A Book
### Introduction
This project focuses on the development of a web application that allows user to view through the different genres of books carried by the bookstore, add their favourite books to the shopping cart, make amendments to their shopping cart items and also to make a purchase once they are ready to checkout their shopping cart items.

## Demo
* Heroku Link: [Click Here](https://kjy-pick-a-book.herokuapp.com/)
* Screencast Link: [Click Here]()

## Personal Touch
- Added password reset function to the web application
- Added update user profile function to the web application
- Incorporate Goodreads API to the web application to retrieve and display ratings for all the books available in the web application
- Used AJAX JQuery and Django Digg-style endless pagination to display the filtered books result
- Added in Stripe to handle payment made by users
- Mailgun was configured with a domain name from NameCheap to send out order confirmation email to users to notify them that their payment was successful.

## Project Strategy and Scope
### User Stories
1. User would like to browse through bestsellers, new & trending as well as books that are under $5.00
    - Feature to implement: To include a carousel slider to display the bestsellers, new & trending as well as books that are under $5.00 to the user.

2. User would like to view through the details of a particular book
    - Feature to implement: To include a book details page that display book information that includes the book's title, the book's author, the book's cover, the book's base price, the book's available quantity, the book's ratings, the book's edition overview as well as the book's description to the user.

3. User would like to add a particular book to their shopping cart
    - Feature to implement: To include an add to cart button that allows user to click on to add book of their choices to the cart once they have selected the quantity of that book they would like to purchase.

4. User would like to view items in their shopping cart
    - Feature to implement: To include a view shopping cart page that allows user to browse through the items that are currently in their shopping cart. 

5. User would like to update items in their shopping cart
    - Feature to implement: To make use of jQuery to allow user to update the shopping cart items.

6. User would like to delete a particular item in the shopping cart
    - Feature to implement: To include a X button in the view shopping cart page that allows user to click on in order for them to delete the items of their choices.

7. User would like to have a summary shown to them before proceed to the actual payment page
    - Feature to implement: To include a summary table in the confirm checkout page to show the items ordered by the user together with the subtotal that they would have to pay for.

8. User would like to make payment for their orders
    - Feature to implement: To include a checkout page that prompt the user for their personal details as well as their credit card details before they could proceed to make any payment.

9. User would like to view through their purchase history
    - Feature to implement: To include a view purchase page to show the user the history and status of their order.

10. User would like to update their user profile 
    - Feature to implement: To include a user update profile page that allows user to update their name, email address, firstname as well as their lastname.

11. Superuser would like to view through and update the orders status on purchases made by their customers
    - Feature to implement: To include feature that allows only superuser to view customer's order and also to change a particular order status, i.e. from processing to either dispatched or delivered.

## Project Structure    
### a. Overview
This web application is structured into 8 main parts, i.e. user signing up for an account, logging in/out of an account, updating their user profile, browsing through the catalogues of books offered by the bookstore, add their favourite books to the shopping cart, update / delete their shopping cart items, checkout their shopping cart items as well as browse through their previous orders history.

At the landing page, users will find a navbar at the uppermost part of the web application. This navbar will show links to different pages of the web application depending on whether a user is currently logged in or not. The 2 scenarios will be as follow:
1. User not logged in: the navbar will display link to Explore More Books, Register and also Login. 
2. User logged in: the navbar will display link to Explore More Books, Profile, View Purchase, View Cart and also Logout.

At the main section of the landing page, users (both logged in as well as without logging in) will find a banner that display a short message informing the user that free shipping is applied for orders above $100 dollars and a Shop Now button below it. Further down, users will find three carousel sliders each displaying bestsellers book, new & trending book as well as books under $5.00. Clicking on the books displayed on the carousel sliders will redirect the user to a show books detail page whereby user will be able to check out all the relevant information related to the particular book and also to add the item to the cart if they are currently logged in. At the very bottom of the page, user will be able to find a footer section that contains information about the bookstore itself, the customer services it provides, the get in touch with us, the find us on links as well as a form that allows user to subscribe to the bookstore's newsletter. 

Clicking on the Explore More Books tab on the navbar will redirect users to a page whereby they will be able to browse through all the books that are currently available in the bookstore. On the left side of the same page, users will be able to use the filter by function that allows user to filter out books by a particular genre, author or price range. The query to fetch the results based on the filter option selected by the user will be done via AJAX and the results returned will be displayed using Django Digg-style pagination. To check out more on the books itself, the user will just have to click on the books of their choices and they will be redirected to the show books detail page.

Clicking on the Profile tab will redirect the users to the update user profile page. At this page, user will be able to see their firstname, lastname, username as well as email address. To update their user profile, they would just have to fill out the update user profile form and click on the update button.

Clicking on the View Purchase tab will redirect the users to a page whereby they will be able to view their previous purchases and also to check on the status of their orders. If the user logged in is a superuser, they will then be able to change the order status of a particular order.

Clicking on the View Cart tab will redirect the users to their shopping cart page whereby they will be able to see a breakdown of the items that are currently in their shopping cart. On the same page, users will be able delete a shopping cart item and also to update the quantity of books that they would like to order via jQuery event handler. To checkout the items in the shopping cart, users will just need to click on the proceed to checkout button on the bottom right which then will redirect the user to a confirm checkout page that shows user a summary of their orders and the amount that they would have to pay for. Clicking on the Place Order button will then route the user to the checkout page whereby the user will need to provide their personal details as well as their credit card details in order to make the purchase.

Clicking on the Logout button will log the user out from the web application. 

Clicking on the Register button will redirect user to the user registration page whereby user will be able to sign up for an account.

Clicking on the Login button will redirect user to the login page whereby they will need to sign in to their account using the username and email address that they have  registered for during the account registration process.

### a. Wireframes
https://drive.google.com/file/d/1r3PcmpphwMDEQxn6VMfh8b1Sz8pESkH6/view?usp=sharing

## Project Skeleton
### a. Existing Features
    i. The web application was designed with Bootstrap grid design and mobile responsiveness in mind.<br>  
    ii. New users are able to sign up for a new account.<br>  
    iii. Users are able to login and logout of the web application.<br>  
    iv. Users are able to browse through bestsellers, new & trending as well as books under $5.00 that are displayed on the carousel slider. Upon clicking on any of the books,users will be redirected to the show book details page whereby they will be able to check out information related to that particular book and also to add that particular book to their shopping cart.<br>  
    v. User are able to use the filter by genre, author or price range option to retrieve book information via AJAX. Results returned will be displayed via Django Endless Digg style pagination.<br>  
    vi. User are able to view their shopping cart items.<br>  
    vii. User are able to update the quantity of books to be ordered in the shopping cart page via jQuery event handler.<br>  
    viii. User are able to delete a particular item from their shopping cart.<br>  
    viiii. User are able to view the order summary of their order at the confirm checkout page.<br>  
    x. User are able to make payment at the check out page.<br>  
    xi. Users are able to view and update their user profile.<br>  
    xii. Users are able to browse through their order history and also to check the status of each orders that has been made.<br>  
    xiii. Superuser are able to view orders made by customer and also to change the order status of a particular order, i.e. from processing to either dispatched or delivered.<br>  
    xiiii. User will receive an order confirmation email if their payment is sucessful.<br>  

### b. Features to be implemented in the future
For the future development of this bookstore web application, I would like to include the following features:
   * Allow user to upload their profile picture when signing up for an account.
   * Allow user to receive newsletter if they have subscribed to the bookstore's newsletter.
   * Allow user to receive email reply from the bookstore once the enquiry form that they have submitted has been answered by an administrator.
   * Allow user to sign up for different category of membership which would be entitled to different discount price upon checkout for each purchases.

## Project Surface
Design Choices:
1. Carousel sliders are used to display books on the landing page to improve user experience when browsing through books collection.
2. AJAX jQuery was used to retrieve books collection based on the filter option selected by the user. It was used as it improves user experience by not reloading the current page the user is on just to populate that page with new information retrieved back from the database.
3. Tables were used to summarized the orders summary and purchase made so that information can be displayed in an organized format.
4. Unkempt, a funky and stylish fonts was used to display texts used in this web application.

## Technologies used
1. HTML5 was the markup language used for structuring the content of the web application
2. CSS3 was a style sheet language used to format the outlook of the web application
3. JavaScript was the programming language to add front end interactivity to the web application
4. jQuery is a JavaScript library. It was used to manipulate the HTML DOM element, event handling and AJAX - https://jquery.com/
5. Bootstrap 4 was the framework used to make the application responsive - https://getbootstrap.com/  
6. Slick.js was used to display books on the carousel slider - https://kenwheeler.github.io/slick/
7. Ion.RangeSlider was used to display the price range slider under the filter by option - http://ionden.com/a/plugins/ion.rangeSlider/index.html
8. Datatables.net was used as an advanced interaction controls for HTML tables - https://datatables.net/
9. Bootstrap input spinner was used to display number input element - https://shaack.com/projekte/bootstrap-input-spinner/ 
10. PostgresQL was used as the database to store all the datatables and datasets
11. Django EL(Endless) Diggstyle pagination was used to display the return filtered book result - https://github.com/shtalinberg/django-el-pagination  
12. Python was used as the backend to write up the different routes to handle the different request method
13. Stripe.JS was used to charge the user for each order - https://stripe.com/en-sg
14. UploadCare was used to store the books images - https://uploadcare.com/
15. W3C Markup was used to check the markup validity of HTML code - https://validator.w3.org/
16. JSHint was used to check check on the JS code - https://jshint.com/
17. Heroku was used to deploy the web application 

## Testing (Manual)
### Responsiveness
The web application was tested across multiple device screen sizes (small: iPhone 5, Galaxy S5, Pixel 2, medium: iPad, large: iPad Pro). Website scale responsively according to the device screen when tested in the Developer tools.

### Browser compatibility
The web application was tested and is compatible on Chrome, Opera and Firefox.

### Test Cases
| Test Case     | Description                   | Outcome  |
| ------------- |-----------------------------  | -------- |
|1              | New users can only register with a username that does not exist in the NewUser table in the database. If a record is found, a field error message will be displayed in the user registration form to inform the user that the username is already exist in the database. | Pass     |
|2              | New users can only register with a unique email address that does not currently exist in the NewUser table in the database. If a record is found, a field error message will be displayed in the user registration form to inform the user that the email address is already exist in the database. | Pass     |
|3              | New users must provide a strong enough password during account registration. If the password chosen does not meet the django password requirement, a field error message will be displayed to the user to choose a stronger password in order to proceed with the registration process. | Pass     |
|4              | New users must provide similar password in the both the password and password confirmation field during account registration. If the user did not key in a matching password, a field error message will be displayed letting the user know that the password field is mismatched. | Pass     |
|5              | Once the new user has successfully signed up for an account, they will be logged in to their account, redirected to the landing page and also be prompted with the registration successful message. | Pass     |
|6              | Existing user will be able to login to their account using their username and password. A message will be prompted to notify the user that they have successfully logged in to their account. | Pass     |
|7              | Existing user will be able to logout only if they are currently logged in to their account. | Pass     |
|8              | At the landing page, user will be able to navigate the books displayed on the carousel slider through the left and right arrow button. | Pass     |
|9              | At the landing page, user will be able to click on any books on the carousel sliders and be redirected to the show book details page . | Pass     |
|10              | At the landing page, user will be able to click on the Shop Now button and be redirected to the show all books page that will display all books that are currently in store. | Pass     |
|11              | At the footer section, user will be able to click on the About Us link that will bring the user to the about us page . | Pass     |
|12              | At the footer section, user will be able to click on the Customer Services link that will bring the user to the Customer Services page . | Pass     |
|13              | At the footer section, user will be able to click on the Contact Us link that will bring the user to the Contact Us page whereby user will be able to fill out an enquiry form . | Pass     |
|14              | At the footer section, user will be able to click on the Facebook, Instagram and Twitter media icons and be brought to the Facebook, Instagram and Twitter page respectively. | Pass     |
|15              | Upon clicking on the Explore More Books tab, user will be brought to a page whereby they will be able to view all the books that are currently in store. On this same page, user will be able to filter books through the filter by genre, author or price range option. The query will be done via AJAX and the result returned will be displayed in Django Digg style pagination. Clicking on any books returned from the query will bring the user to the show book details page whereby user will be able to view all the relevant information related to that particular book. | Pass     |
|16              | At the show book details page, user will be able to add the particular book item to their shopping cart. | Pass     |
|17              | Clicking on the View Cart tab will redirect the user to the shopping cart page. At this page, user will be able to update the quantity of books they would like to order via AJAX. Also, user would be able to delete a particular shopping cart item by clicking on the X button. An update in the quantity of books ordered will update the number of items in the shopping cart in the navbar, the stock available under the books details column and also the total amount column. | Pass     |
|18              | At the shopping cart page, user will be redirected to the home page of the website if they clicked on the continue shopping button. If they were to clicked on the proceed to checkout button, they will be redirected to the confirm checkout page. At the confirm checkout page, an order summary will be displayed showing users the details of their order and the amount that they would have to pay for. Clicking on the place order button will then redirect user to the checkout page whereby user will need to provide their personal and credit card details before being able to make a purchase. The credit card number and CVV that were used for this test was 4242424242424242 and 122 respectively. The expiry month and year of the credit provided in the form must be of at least the current month and the current year. | Pass     |
|19              | User will only be able to submit payment on the checkout page if they provide their personal and credit card details. Once the user submitted their payment, they will be redirected back to the homepage and be prompted with a payment successful or failure message. | Pass     |
|20              | Clicking on the view purchase tab will redirect the user to the page whereby they will be able to view the orders that they have made and also to check the status of their orders. | Pass     |
|21             | Clicking on the view purchase tab will redirect the superuser to the page whereby they will be able to update the status of a particular order. | Pass     |
|22              | Clicking on the profile tab will redirect the user to a page whereby they will be able to update their personal details. | Pass     |

## Apps and Files Description
The main apps and files used in this web application are briefly described as below:<br>
a. Apps
    i. BookProject - This is the main project folder. The important files in this folder is the settings.py file and the urls.py file. Settings.py files typically contains all the configured settings that is required to run the application. Urls.py file is the file that points to the different apps depending on the url that the user visited.
    ii. Acounts - This is the app that handles the process of user registration, profile updating as well as user logging in and out of the web application. The important files in this folder are the models.py file, admin.py file, forms.py file, urls.py file, views.py file and also the html templates files. In the models.py file, a NewUser class was created by inheriting from the AbstractUser class. In forms.py file, three forms were created, namely the UserLoginForm, UserRegistrationForm and also the UserUpdateForm. The UserRegistrationForm and the UserUpdateForm both inherits from the NewUser class created in models.py file. The views.py file contains the route to handle user registration, user logging in/out and also the updating of user profile. Urls.py file contains the urls to link to the different route in views.py that is responsible to be executed depending on the url the user has visited. In admin.py file, newly created models that was created in models.py file were registered so that it can be viewed in the Django admin UI. The templates folder in this app contains the login, register and user profile update html template files.
    iii. Catalog - This is the app that shows books related information. The important files in this folder are models.py file, admin.py file, urls.py file, views.py file and also the html template files. In models.py file, three classes were created, namely the Book class, Genre class and the Author class. The views.py file contains the route to show books currently available in store, display books result returned via AJAX and also a route to show the relevant information of a particular selected book. Urls.py file contains the urls to link to the different route in the views.py file. Admin.py file, the Book class, Genre class and Author class that was creted in the models.py file was registered so that it can be viewed in the Django admin UI. The templates folder in this app contains 4 files, books_list.template.html file is the file that shows all the books that is currently in store, show_book_details.template.html file will display the relevant information of a particular book, entry_list.html file is the main template file to render when the request to retrieve the book is not done through AJAX request while entry_list_page.html file contains the part to be updated if the request to obtain the filtered book result is done through AJAX request.
    iv. Carts - This is the app that shows the shopping cart items to the user. The important files in this folder are the urls.py file, views.py file, contexts.py file and also the html template files. The views.py file contains the route to handle the add to cart, update cart, remove from cart and view cart request. The urls.py file contain the urls to link to the different route in the views.py file. The contexts.py file, which is the context processor, was created so that the total cart price could be available on each page of the web application. The templates folder contains the view cart html file that will displayed a summary of the cart items when rendered.
    v. Home -  This is the app that shows information on the landing page. The important files in this folder are the urls.py file, views.py file and also the html template files. The views.py file contains route to show bestsellers, new & trending as well as books that are under $5.00. The urls.py file contain the urls to link to the different route in the views.py file. The templates folder contains 4 files, the index.template.html file will display the landing page of the website when rendered. The about us, contact us and also the our services html files will each display about us, contact us and our services information when rendered.
    vi. Order - This is the app that is in charge of handling the checking out process of an order. The important files in this folder are admin.py, forms.py, models.py, urls.py and also views.py file. Models.py files contains the Charge class, Order class and also the OrderItem class. In the forms.py file, two forms were created, namely the OrderForm and also the PaymentForm. The views.py file contains the route to handle checkout,  confirm checkout, view purchase list, view puchase orders and also update order. The urls.py file contain the urls to link to the different route in the views.py file. The classes created in the models.py file were registered in the admin.py file so that it could be viewed in the Django admin UI. The templates folder contains the html files for checkout, confirm checkout, view puchase list and also view purchase details.

b. Folders
    i. static folder contains 3 sub folders, namely static, images and js. Static folder contains the external CSS file while images and js folder contains the images and external JavaScript files used in this web application respectively.
    ii. templates contains 3 subfolders within it and a base.template.html file. The base.template.html files contains common html codes that is extended by all the html files. The other 3 subfolders are namely the admin folder, the includes folder and also the registration folder. The admin folder contain the html file to style the Django admin login UI page. In this web application, I have set the Django admin login display to the name of my bookstore, i.e. Pick-A-Book. The includes folder contains the common navbar display html files which is included in the base.template.html fiSSSle. The registration folder contains html files to reset the user's password. The method on setting up the password reset files was accomplished by following [Vitor Freitas](https://simpleisbetterthancomplex.com/tutorial/2016/09/19/how-to-create-password-reset-view.html) create a password reset view tutorial.

c. requirements.txt - the text files that contains all the packages needed to be installed in order to run this web application.

## Bugs and Limitations Discovered
jQuery was used to update the total amount and the stock available of a particular book when the order quantity is changed in the shopping cart page. 
The total amount and stock available of a particular book update accordingly when the order quantity is changed on a large screen device.
However, when this was tested out on a mobile device, the total amount and stock available does not seem to update accordingly.
Snapshot of limitations discovered:
- Laptop have the correct total amount and stock available updated (left picture)
- Mobile device does not have the correct total amount and stock available updated (right picture)

Laptop / Desktop                                        |  Mobile Device
:------------------------------------------------------:|:-----------------------------------------------------:
![display on laptop](https://i.imgur.com/e0wdE5S.png)   | ![display on mobile](https://i.imgur.com/Ef0lf1W.png)

## Deployment
### a. To run this web application on your local PC
Instructions
Note: This web application was run on a Windows PC. The following command might be slightly different if run on a Mac PC.

1. Go to [Pick A Book Github repository](https://github.com/KJY93/Project-4-Django-FullStack-Web-Development)
2. Click on the 'Clone or Download' button and then click 'Download ZIP' and extract the files to a location of on your desktop / laptop. Else, you can clone the project by running the following command on your terminal:
```git clone https://github.com/<username>/<repository>```
3. Install all the packages needed using the following command:
```pip3 install -r requirements.txt```
4. Set the enviroment variables needed to run this web application. First you would need to right click on ```My Computer```. Then right click on ```Properties```. On the left hand side of the menu bar, click on ```Advanced system settings```. Under the ```System Variables``` section, click on the ```New``` button. In the pop up dialog box, key in the ```Variable Name``` and ```Variable Value``` field. The environment variables needed to be setup would be the database url, the default from email,GoodReads API key, Mailgun access key, Mailgun domain, Stripe publishable key, Stripe secret key, UploadCare Public Key and UploadCare Secret Key.

Note: For the variable name, you are free to choose a variable name of your choice:

```
    An example of the environment variables key values pair would be as follow:
    a. DATABASE_URL(variable name) will be: postgres://xxxxxxxxxxxxxxxx (variable value)
    
    b. DEFAULT_FROM_EMAIL (variable name) will be: <xyz>@<YOUR_DOMAIN_NAME> (variable value). 
    Replace YOUR_DOMAIN_NAME to a domain name you are using, if you are using gmail, then replace it with gmail.com, if you are using yahoo, 
    then replace it with yahoo.com, if you are using a domain bought from NameCheap, GoDaddy or any other domain, 
    then replace it with the domain name that you have purchased. Also, replace xyz with the name of your mailbox.
    
    c. GOODREADS_API_KEY (variable name) will be: the key you obtained when you register for an account with GOODREADS (variable value)
    
    d. MAILGUN_ACCESS_KEY (variable name) will be: the key you obtained when you register for an account with Mailgun (variable value)
    
    e. MAILGUN_DOMAIN (variable name) will be: the domain name that you have signed up for and would like it to be associated to Mailgun (e.g. mailer.xxx.com)
    
    f. STRIPE PUBLISHABLE KEY (variable name) will be: the publishable key you obtained when you register for an account with STRIPE (variable value)
    
    g. STRIPE STRIPE_SECRET_KEY (variable name) will be: the secret key you obtained when you register for an account with STRIPE (variable value)
    
    h. UPLOADCARE_PUBLIC_KEY (variable name) will be: the publishable key you obtained when you register for an account with UPLODADCARE (variable value)
    
    i. UPLOADCARE_SECRET_KEY (variable name) will be: the secret key you obtained when you register for an account with UPLODADCARE (variable value)
```

5. To run the web application, run the following command in your terminal:
```python3 manage.py runserver 8080```
6. To open up the webpage, go to ```http://127.0.0.1:8080```.
   
### b. Heroku Deployment
The deployment to Heroku was accomplished with the guidance of the deployment walkthrough file shared to us by our instructor, Mr Paul.
The steps for the deployment are as follow:
1. Sign up for an account at [Heroku](https://www.heroku.com/)
2. Install Heroku on your terminal by running this command: ```sudo snap install heroku --classic```
3. Install the following dependencies that is needed to make the project to work on Heroku
   ```
       sudo apt install libpq-dev python3-dev
       sudo pip3 install gunicorn
       sudo pip3 install psycopg2
       sudo pip3 install Pillow
       sudo pip3 install whitenoise 
       sudo pip3 install dj_database_url
   ```
4. In the settings.py file, add WhiteNoise to the middleware:
    ```
        MIDDLEWARE = [
        .....
        'whitenoise.middleware.WhiteNoiseMiddleware'
        ]
   ```

5. Create a repository for the project. To initialize a new repository, run the following command in your terminal:
    a. git init
    b. git add .
    c. git commit -m "First Commit"
6. Create a .gitignore file and add the files that are to be ignored that is taken from [here](http://gitignore.io/api/django). Also, add the .c9 file to the end of the .gitignore file
7. Create a repository in Github
8. To link your git repository with the remote repository in Github, run the following command:
   ```git remote add origin https://github.com/<username>/<repository>```
9.  Login to Heroku by running this command: ```heroku login -i```
10. Create a new app in Heroku by running this command: ```heroku create <APP NAME> ```. Replace the <APP NAME> with a name of your choice and note that the Heroku app name chosen needs to be unique 
11. Double check the Heroku app was successfully created by running this command: ```git remote -v```
12. In Heroku, go to the settings tab and click on the 'Reveal Config Vars' button. Copy the environment variables from the .bashrc file in AWS Cloud 9 over
    ![Environment variables settings](https://i.imgur.com/SC4ckZb.png)
13. At the root folder, create a filename called Procfile. Add this line ```web: gunicorn <PROJECT_FOLDER>.wsgi:application``` inside the Procfile and replace the <PROJECT_FOLDER> with your project's name
14. Inside the settings.py file, add the domain name of the heroku app under the ALLOWED_HOST section
15. Generate a requirements.txt file with ```pip3 freeze --local > requirements.txt```
16. Add STATIC_ROOT in settings.py file in order for WhiteNoise to work properly. The line of code to be added would be ```STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')```
17. Commit all files to the git repository before deploying to Heroku. To deploy, run the following command:
    a. git add.
    b. git commit -m "deploy to Heroku"
    c. git push heroku master
18. To open the Heroku app, go to the very top of the page and click on "Open App".

### c. Setting up PostgreSQL Database
PostgreSQL will be used as the database to store all the datatables and datasets for this project. To setup the Postgres Database, the following steps that was shared to us by our instructor, Mr Paul, was followed:
1. Create a Postgres database in Heroku by running this command: ```heroku addons:create heroku-postgresql```
2. Run this command ```heroku config``` to check the URL of the database that has just been created at Step 1
3. In the .bashrc file, add this line of code ```export DATABASE_URL="database_url"```. The database_url is obtained from Step 2. Restart the bash terminal once the .bashrc file has been saved.
4. In the settings.py file, import dj_database_url package
5. In the settings.py file, go to the DATABASES section. Comment out the lines of code that uses sqlite3 as the database and add in this line of code ```DATABASES = {'default': dj_database_url.parse(os.environ["DATABASE_URL"])}```
6. Save the settings.py file and restart the terminal. After that, do a migration by running this command: ```python3 manage.py migrate```
7. Commit all files and do a git push to Heroku by running this few lines of code:
    ```
        git add .
        git commit -m "Updated settings.py"
        git push heroku master
    ```
8. Create a superuser with this command ```python3 manage.py createsuperuser```. Once the superuser account is created, the superuser will be able to access Django admin and add in models.

### Credits and Acknowledgements:
1. Django EL (Endless) Pagination: 
   Source code to implement the Digg style pagination was adapted from https://github.com/shtalinberg/django-el-pagination

2. Bootstrap-Input-Spinner:
   Source code to create the input spinner elements for number input was adapted from https://github.com/shaack/bootstrap-input-spinner

3. Bootstrap-Select:
   This jQuery plugin was used to for Bootstrap select option element - https://github.com/snapappointments/bootstrap-select

4. Star ratings display:
   Source code to display the book ratings was adapted from https://codereview.stackexchange.com/questions/177945/convert-rating-value-to-visible-stars-using-fontawesome-icons

5. Font Awesome:
   Icons from Font Awesome were used to style the view and edit button in the view purchase history tab - https://fontawesome.com/

6. Fonts: 
   Font used is from https://fonts.google.com/

7. Icons8:
   Logo from favicon is used as the logo for the tab browser of this web application - https://icons8.com/

8. Password reset:
   The password reset for this web application is accomplished by following [Vitor Freitas](https://simpleisbetterthancomplex.com/tutorial/2016/09/19/how-to-create-password-reset-view.html) create a password reset view tutorial.

Note: This is for educational purpose only and not for commercial use.