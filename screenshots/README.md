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

<img src="screenshots/nav.png">

<img src="screenshots/about1.png">

<img src="screenshots/contactp.png">

<img src="screenshots/service1.png">

<img src="screenshots/service2.png">
    
<img src="screenshots/social.png">

  2. As a site user I can easily navigate the site so that I can find what I'm looking for.
  3. As a site user I can sign up for an account so that I can make a booking with the counsellor.
  4. As a site user I can sign into my account so that I can view and change my appointment details.
  5. As a site user I can sign out of my account so that I can keep my details safe.
  6. As a site user I can send a message to the counsellor so that I can learn more about the counsellor and the benefits of therapy.
  ### Administration User Stories
  1. As a site administrator I can create, view, change and delete bookings so that I have control over my appointment system.