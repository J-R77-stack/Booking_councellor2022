# Councelling Appointment Booking System for Mike Wilkins Councellor

<img src="screenshots/responsive.png">

This project is a fictional Website for a councellor named Mike Wilkins. People looking for a councellor can view the site on all types of devises, where they can learn more and also book, edit and cancel appointments with Mike. The site is fully responsive and accessible.

[Here is the live version link to my project]()

## Menu

* [About](#About)

* [UX](#ux)

  * User Stories
  * Design
  * Wireframes

* [Features](#features)

* [Tecnologies Used](#tecnologies_used)

* [Testing](#testing)

* [Deployment](#deployment)

* [Credits](#credits)

# About

Mike Wilkins Councelling is a fictional website for a Councellor. The site can be viewed on mobile, desktop, laptop and tablets. Users can view the site in the usual way by navigating through the pages to learn more about the business. Users can view the Home, About, Services, Contact and Blog pages. The blog has not been set up yet so the users can sign up for an email for when it will be live. As well as this the User is able to create an account and then book, edit or delete appointments with the councellor. The User cannot use this service unless they have signed up for an account. Once signed in the User can view all their appointments using the My appointments link that appears in the nav bar. Site Admin Users can also create, edit and delete bookings in the Admin panel.

# UX
  ## User stories
  ### Site User Stories
  1. As a site user I can understand the purpose of the site so that I can learn more about the business with ease.
  2. As a site user I can easily navigate the site so that I can find what I'm looking for.
  3. As a site user I can sign up for an accountso that I can make a booking with the counsellor.
  4. As a site user I can sign into my account so that I can view and change my appointment details.
  5. As a site user I can sign out of my account so that I can keep my details safe.
  6. As a site user I can send a message to the counsellor so that I can learn more about the counsellor and the benefits of therapy.
  ### Administration User Stories
  1. As a site administrator I can create, view, change and delete bookings so that I have control over my appointment system.

  ## Design
  The site is designed with five pages - Home, About, Contact, Book, Services and Blog. There are links  and a Nav bar provided  to connect to other parts of the site. Each page is fully responsive.
  
  I used the greyscale bootstrap theme from [Startbootstrap](http://startbootstrap.com/) and modified it to suit my ideas
  
  The main fonts used are Nunito, and Varela Round and the main colours are grey, green, black and white.

  ## Wireframes
  Below are the wireframes that I created using [Balsamiq](https://balsamiq.com/)

  ### Home Page
  <img src="screenshots/home.png">

  ### About Page
  <img src="screenshots/About.png">

  ### Services Page
  <img src="screenshots/services.png">

  ### Book Page
  <img src="screenshots/book.png">

  ### Contact Page
  <img src="screenshots/contact.png">

  ### Blog Page
  <img src="screenshots/blog.png">

  # Features

  The site is fully responsive by using the Bootstrap Greyscale Theme. All features get resized correctly except for the appointment table in view_appointment.html when viewed on a mobile. However one is able to slide across to view and also tilt the device to look in landcape mode.

  The site is easy to navigate by using the navbar.

  ## Future Features
   1. Email sent to user when booked, edited or deleted appointment.
   2. Email sent to user when asked councellor a question in the contact form to say he'll be in touch.
   3. Set up interactive blog app with information about mental health issues.

  # Tecnologies Used
    
  ### Languages

  1. [HTML5](https://en.wikipedia.org/wiki/HTML5)
  2. [CSS](https://en.wikipedia.org/wiki/CSS)
  3. [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

  ### Libaries Frameworks and Programs

  1. [Bootstrap 5.1.3](https://getbootstrap.com/docs/5.1/getting-started/introduction/)
      * Used to provide the framework and responsiveness.

  2. [Django](https://www.djangoproject.com/)
      * Used for fuctionality, the data model and database.

  3. [JQuery](https://jquery.com/)
      * Came with the Bootstrap theme and also used for the installed bootstrap Tempus Dominus Datetimepicker.

  4. [Javascript](https://en.wikipedia.org/wiki/JavaScript) 
      * Used for message pop ups and countdown.

  5. [Google Fonts](https://fonts.google.com/)
      * Main fonts being Nunito and Varela Round

  6. [Font Awesome](https://fontawesome.com/)
      * Used for Interactive social icons in footer and also for About page.

  7. [Git](https://git-scm.com/)
      * Used for version control.

  8. [GitHub](https://github.com/)
      * Used to store the code once pushed from Git.

  9. [Balsamiq](https://balsamiq.com/)
      * A wireframe program used to create the mock-ups.

  10. [Microsoft Word](https://en.wikipedia.org/wiki/Microsoft_Word)
      * Used for drawing up the data model.
      <img src="screenshots/datamodel.png">

  11. [Cloudinary](https://cloudinary.com/)
      * Insalled but ended up not using as I found the images of the bootstrap greyscale theme very appropriate for the   design I was looking for for the project.

  12. [SQLite3](https://en.wikipedia.org/wiki/SQLite)
      * Used as this is the default database for Django.

  13. [Heroku](https://www.heroku.com/)
      * Used for Deployment and storage of app.

# Testing

I used the W3C Validators to check for errors in the HTML and CSS Files of the project and PEP8 online checker for the python code.

  * [W3C URI Validator](https://validator.w3.org/#validate_by_uri)
  * [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input)
  * [PEP8](http://pep8online.com/)

  ### HTML Validation

  The About page had two errors that I couldnt find a solution for.
  1. Bad value for attribute width 100% on element img.
  2. Section lacks heading. Consider using h2-h6 elements.
  <img src="screenshots/aboutcheck.png">
  
  The other pages also had the same error.
  1. Section lacks heading. Consider using h2-h6 elements. I persume its bcause the bootstrap theme i used is for a one page landing page that one can scroll up and down so the h1-h6 elements are further up the page. So by breaking up the page as I did the the validator would be confused as its expecting the dom tree order.
  <img src="screenshots/addappointment.png">
  <img src="screenshots/blogcheck.png">
  <img src="screenshots/contactcheck.png">
  <img src="screenshots/deletecheck.png">
  <img src="screenshots/editcheck.png">
  <img src="screenshots/logincheck.png">
  <img src="screenshots/logoutcheck.png">
  <img src="screenshots/servicespage.png">
  <img src="screenshots/signupcheck.png">
  <img src="screenshots/viewappointmentcheck.png">

### CSS Validation

<img src="screenshots/csscheck.png">

### PEP8 Validation

1. admin.py
<img src="screenshots/admin.png">

2. forms.py
<img src="screenshots/forms.png">

3. models.py
<img src="screenshots/models.png">

4. urls.py
<img src="screenshots/urls.png">

4. views.py
<img src="screenshots/views.png">
    
## User Stories Evaluation
To ensure that the project fulfils the goals set out in the user stories:
  ### Site User Stories
  1. As a site user I can understand the purpose of the site so that I can learn more about the business with ease.
    * Once in the site the user is welcomed with an attractive and easy to navigate landing page with a fuctional Nav bar which takes them to the other pages of the site. The Hero Image holds an inspirational quote and a call to action button to book an appoointment straight away. The name of the councellor is easy to see in the top left hand corner. The user is also able to navigate from all pages to the councellors social media sites.  The user can click on the about services or contact tab in the nav bar to learn more about the business.

<img src="screenshots/home1.png">

<img src="screenshots/about1.png">

<img src="screenshots/contactp.png">

<img src="screenshots/service1.png">

<img src="screenshots/service2.png">
    
<img src="screenshots/social.png">

  2. As a site user I can easily navigate the site so that I can find what I'm looking for.
     * By using the Nav bar the site user can easily navigate the site
    <img src="screenshots/nav.png">

  3. As a site user I can sign up for an account so that I can make an appointment with the counsellor.
     * The User can easily book an appointment with the councellor by clicking on the book tab in the nav bar or the call to action button on the Home or About pages. This will take them to the sign in page where they either can sign in using existing details or sign up for an account using the link (sign up) above the sign in form. They can only book an appointment if they're a registered user. The register link in the nav bar takes them to the sign up form and the log in link in the nav bar takes them to the sign in form as well. Once signed up or signed in the user is redirected back to the Home page where the Login and Register Links are replaced with Logout and Logged in as (username) There's also an new link called My appointments.
    <img src="screenshots/signinapp.png">
    <img src="screenshots/signupapp.png">

  4. As a site user I can sign into my account so that I can view and change my appointment details.
     * Once logged in using the steps above the user can click on My appointments in the Nav bar which will take them to the view appointments page where they an view edit or delete appointments.
    <img src="screenshots/table.png">
    <img src="screenshots/deleteapp.png">
    <img src="screenshots/editapp.png">
  5. As a site user I can sign out of my account so that I can keep my details safe.
     * The user can sign out at anytime to keep details safe.
     <img src="screenshots/signoutapp.png">
  6. As a site user I can send a message to the counsellor so that I can learn more about the counsellor and the benefits of therapy.
     * The user can send a message to the councellor on the contact page to find out more information. (This feature is not yet functional)
    <img src="screenshots/contactp.png">
  ### Administration User Stories
  1. As a site administrator I can create, view, change and delete bookings so that I have control over my appointment system.
     * Once a site admin has been set up the user can log in to look at and change appointments.
    <img src="screenshots/adminshot.png">

# Deployment
 1. In the Gitpod Terminal install django, gunicorn, supporting libraries, requirements file and created Project and App.
 2. Create Heroku App
 3. In Resources tab in Heroku search for Heroku Postgres in the add ons and attached to project.
 4. In Heroku under settings click on Reaveal Config Vars and copy the DATABASE_URL text.
 5. In Gitpod create new env.py file on top level directory and import the os.
 6. In env.py set environment variables by adding the database url from Heroku.
 7. Add secret key to env.py and config vars in Heroku.
 8. In settings.py import os and set if statement to say that outside the development environment the environment variables must be used from env.py.
 9. In settings.py comment out DATABASES section and repleace with django database URL in env.py and Heroku config vars.
 10. Migrate changes using python3 manage.py migrate.
 11. Set static and media files to be stored on Cloundinary by copying API environment variable from cloundinary dashboard and adding to env.py and Heroku config vars.
 12. Add DISABLE_COLLECTSTATIC = 1 to Heroku config vars.
 13. Add Cloudinary libraries to installed apps.
 14. In settings.py set up static file storage, directory and root, media_url and default storage. Also set up templates directory.
 15. Add Heroku host name to ALLOWED_HOSTS and also localhost.
 16. Create 3 new folders on top level directory - media, static and templates.
 17. Create Procfile in top directory and add code with project name.
 18. Add, deployment commit and push to github.
 19. Deploy project in Heroku in Deployment tab add github to deployment method. Looked for my github repository and connect heroku app, clicked on deploy branch twards the bottom of the page. waited for it to build.
 20. oppened app at top of page to see successful deployment
 21. After completing the project I turn debug to False in setting.py and removed DISABLE_COLLECTSTATIC in Heroku config vars.

 # Credits 

 * Code Institutes two walk through projects were used as a base to build my own project. The 'Hello Django walkthrough' helped me to understand and build the CRUD fuctionalities and 'I think therefore I blog' helped me to understand and build the authentication and message fuctionality.

 * The Greyscale Bootstrap theme was used from [Startbootstrap](http://startbootstrap.com/) as the structure and style of the project and to also make it responsive.

 * I looked at and used images from [Pixabay](https://pixabay.com/)

 * I researched datetimepickers for the booking form and settled on [Tempus Dominus](https://pypi.org/project/django-tempus-dominus/) which I found the easiest to impliment.

 * I used [w3schools](https://www.w3schools.com/default.asp) and [Stack Overflow](https://stackoverflow.com/) for Problems with code syntax and functionality. I found alot of good answers there.

 ## Acknowledgements

 * My Mentor for support and feedback
 * Code institute tutors for help with problems with my code
 * Friends and family for checking the fuctionality of the website.


