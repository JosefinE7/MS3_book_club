# Conservative Book Club

For my third project I decided to create a virtual book club. In the current Coronavirus pandemic we are more separated than ever, and we are forced to change the way we interact with one another. A lot of the time we are unable to physically spend time together, thankfully we now live in a time where we can interact with each other from a safe distance, better than any humans before us in history. The Conservative Book Club aims to provide a interactive community around books written from a conservative point of view and unite people around the love of reading and sharing great books!

## UX

This website was created specifically with the many restrictions of the Coronavirus in mind. Before the Coronavirus a lot of people already relied heavily on technology to stay connected, now however technology is absolutely essential for staying in touch with our loved ones. Simply staying in touch is good, but it is not enough and a lot of people are also struggling with constructing a stimulating day to day schedule. To that I say: what better way to use this time of isolation to stimulate the mind with a great and educational book?

The Conservative Book Club allows people to gather around great books within genres ranging from economics to memoirs. Really providing the members with an opportunity to connect with people with similar interest from a safe distance. Today the website allows the users to add books, as well as to see books other people have recommended. It also allows the user to edit or delete books, but only the books that the user in question has added. On this website there is also an opportunity for the admin of the website to add, edit and delete book genres currently available. This is so the amount of genres can grow over time as the site itself grows, to this way be able to include even broader subjects to suit even more potential users.

#### User Stories:

- As a person part of the Coronavirus risk group I spend almost all of my time at home, I am looking to stay mentally active during this time quarantine. What I need is some book recommendations from real people and no copy pasted description from the publishing company of the book.
- As a person who is really new to the conservative point of view, I would like some book recommendations to get me started and really understand the core values from within all aspects of the point of view, ranging from economic to cultural.
- As the admin of this site I love reading, in today's age I am able to take my passion for books and make a profit through affiliate links if the people who visit my site are interested in purchasing the books that get recommended on my site. What a great way to combine work and my favorite hobby!

#### Mockups

![mockup 1](static/img/mockup_1.jpg)
![mockup 2](static/img/mockup_2.jpg)
![mockup 3](static/img/mockup_3.jpg)

The mockups I have created for this project are somewhat lacking in creativity, in the beginning of this project I had originally created a mockup that ended up being irrelevant to this project due to the fact that I misunderstood what this project was supposed to focus on. Due to english not being my first language I later realized I had misunderstood the task instructions and I had to create something completely new. I decided to use the book club example provided to me by Code Institute as inspiration, as well as the Start Bootstrap Theme of “Clean Blog” as the base for my website design and decided to make up for lost time and just get to coding.

## Features

**Navbar**

- At the top of the page there is a navigation bar that gives you different options depending on your logged in status. When not logged in to the page the user is presented with the navigation items of: Home, Log In and Register which all bring you to the connected template when clicked. Logged in to the website however, the user will see the same Home navigation item as well as the additional items of Profile, Add Book and Log Out. The admin of the website, currently under the username admin, will have the navigation item of: Manage Genres as well as the Home, Profile, Add Book and Log Out option.

**Home page**

- The Home page contains a couple of main elements, starting with a hero image displaying books at the top of the page, as well as a two headers and a paragraph introducing the website to the user. Just below this is a search bar where the user can search books already added to the website, by searching through either book name or book author. Underneath the search bar, all books added to the website are displayed. The books are displayed in card form and contains: a sample book image, book genre, book name, book author, amount of book pages, link where the user can find more information as well as a personalized description of the book by the person recommending the book which expands when the “description” button is clicked. If the user is logged in to the website there will be two additional buttons displaying next to the description button reading edit and delete to the books they themselves have added.

**Log In page**

- The Log In page is a very simple page with a header at the top of the page displaying the name of the page, just underneath is a form element that requires a username and password of the user as well as a Log In button to log the user into the website, below the button is a link to the Register page for new users.

**Register page**

- The Register page has an almost identical design to the Log In page with a header displaying the name of the page and just underneath a form element. The button under the form reads Register, the link provided below the Register button is instead intended for revisiting users redirecting them to the Log In page.

**Profile page**

- The profile page is reached either through the Log In or Register page, and is the first page the user is taken to after logging in. At the top of the page is a header displaying the words: Profile of _Users Name_. Below are the books the user in question has added to the website with the same display structure as on the Home page: displaying the book: genre, name, author, amount of pages, link and personalized description as well as an edit and delete function.

**Add Book page**

- The Add Book page is the page where the users can add new books. The page has an Add Book heading, underneath there is a form element. The form first asks under what genre the book fits in, as this project is submitted there are six available genres to choose from. After this there are text inputs asking for the book: name, author, amount of pages, link and a personalized description. At the bottom there is a submit button with the text "Add Book".

**Manage Genres page**

- If the user is logged in as the admin of the website, there will be a navigation bar item titled: Manage Genres. The page follows the same header structure as the other pages, underneath the Manage Genres header there is a big button displaying the words: “Add Genre”. Through this button the admin can create new genres available to all the users of the site. Below the “Add Genre” button all current genres are displayed with a name, as well as an edit and delete button, for the admin to be able to edit and delete the current genres available.

**Footer**

- In the footer element there is a small header referring to the social media icon links provided underneath. The links are currently connected to my own social media accounts.

### Features left to implement

- I would like to add additional commenting features to make it possible for several users to provide their comments on the same book, I hope to implement that in the future.

- In the future I am looking to add a Zoom meeting extension to the website to make it possible for users to have virtual book club meetings, to this way be able to make the interaction between members even more personal.

* Right now it is up to the user to add a link to the book they are adding for other users to be able to check out more information/ purchase the book. This is only a temporary solution however and I hope to, if the website grows in popularity, to make the admin be the one to add all the links. To that way be able to make money off the site by affiliate links.

- I was originally trying to include the book cover of every book in the image element next to each book, however trying this out I realised that I did not have enough time to implement this properly and I faced the possibility of users adding images in all different sizes and messing with the layout of the site. I ultimately decided against including the book covers but I hope to implement this in the future.

## Technologies used

The technologies used when creating this website is as follows:

- [jQuery](https://jquery.com/)

  - The project uses JQuery to simplify DOM manipulation, jQuery is crucial to almost all extensions on the page.

- [Bootstrap](https://getbootstrap.com/)

  - The project uses Bootstrap to provide a grid system, as well as basic layout and styling.

- [Start Bootstrap](https://startbootstrap.com/)

  - The project uses the Start Bootstarp Clean Blog Theme as base for the website design.

- [Bootstrap Material Design](https://mdbootstrap.com/)

  - The project uses Bootstrap Material Design to further style the website through additional Bootstrap code.

- [Font Awesome](https://fontawesome.com/)

  - The project uses Font Awesome to add icons.

- [Google Fonts](https://fonts.google.com/)

  - The project uses Google Fonts to style the website text.

- [Mongodb](https://www.mongodb.com/)

  - The project uses the Mongo database to store and retrieve data from the website.

- [Flask](https://flask.palletsprojects.com/en/1.1.x/)

  - The project uses Flask for Python functionality.

- [Dnspython](https://www.dnspython.org/)

  - The project uses dnspython for Python functionality.

- [PyMongo](https://flask.palletsprojects.com/en/1.1.x/)
  - The project uses PyMongo for interacting with MongoDB database from Python.

## Testing

### Testing Navbar

1. Go to Home page
1. Hover mouse over all navbar anchor links
1. Home, Log In, Register, Profile, Add Book, Add Genre and Log Out section all react by changing color when hovered over
1. Click Home, Log In, Register, Profile, Add Book, Add Genre and Log Out navitems
1. All navbar items connects to intended page
1. Test successful

### Testing Home page

#### Testing _Sign up_ link:

1. Click on Home tab in navbar
1. Scroll down underneath header and paragraphs explaining the website
1. Hover mouse over _Sign up_ anchor
1. Anchor reacts to hovering
1. Click anchor
1. Clicking anchor brings me to _Register_ page
1. Test successful

#### Testing search bar:

1. Click on Home tab in navbar
1. Scroll down to search bar element
1. Click the search bar input
1. Search bar reacts and text is able to be put in
1. Try to search with an empty field
1. Unable to search, get a message requesting me to fill in field
1. Write _Orwell_ in search bar
1. Click _Search_ button
1. Matches to _Orwell_ show up
1. Search author test successful
1. Click _Reset_ button
1. Click brings me back to Home page
1. Reset test successful
1. Write _oRWell_ in search bar
1. Click _Search_ button
1. Matches to _Orwell_ show up
1. Search author test with capital and lowercase letters successful
1. Uses search bar for _Housing_
1. The book _The Housing Boom and Bust_ shows up
1. Books search successful
1. Click _Reset_ button
1. Click brings me back to Home page
1. Second reset test successful

#### Testing _For More Information_ link:

1. Click on Home tab in navbar
1. Scroll down to first book element
1. Hover mouse over _For More Information_ anchor in book element
1. Anchor reacts to hovering
1. Click anchor
1. Clicking anchor opens a new tab in the browser window to the books Amazon page
1. Test successful

#### Book description button:

1. Click on Home tab in navbar
1. Scroll down to book element
1. Hover mouse over _Book Description_ button
1. Button reacts to hovering
1. Click _Book Description_ button
1. Button reacts by expanding and showing _Book Description_ text
1. Click _Book Description_ button again
1. Book description text disappears
1. _Book Description_ button test successful

### Testing Log In page

#### Logging in with already existing user:

1. Click on Log In tab in navbar
1. Click _Log In_ button
1. Error message appears asking user to fill in _Username_ field
1. Fill in existing username in _Username_ field
1. Click _Log In_ button
1. Error message appears asking user to fill in _Password_ field
1. Fill in password to existing username in _Password_ field
1. Click _Log In_ button
1. Login successfully takes me to users profile page
1. Login successful

#### Logging in with wrong password/user:

1. Click on Log In tab in navbar
1. Fill in existing username in _Username_ field
1. Fill in wrong password in _Password_ field
1. Click _Log In_ button
1. Redirected back to _Log In_ page with “Incorrect Username and/or Password” message
1. Fill in false username in _Username_ field
1. Fill in propper password to another user password in _Password_ field
1. Redirected back to _Log In_ page with “Incorrect Username and/or Password” message
1. “Incorrect Username and/or Password” test successful

#### Testing _New Here?_ link:

1. Click on Log In tab in navbar
1. Scroll down underneath login form
1. Hover mouse over _Register Account_ anchor
1. Anchor reacts to hovering
1. Click anchor
1. Clicking anchor brings me to _Register_ page
1. Test successful

### Testing Register page

#### Register with already existing user:

1. Click on Register tab in navbar
1. Click _Register_ button
1. Error message appears asking user to fill in _Username_ field
1. Fill in existing username in _Username_ field
1. Click _Register_ button
1. Error message appears asking user to fill in _Password_ field
1. Fill in password to existing username in _Password_ field
1. Click _Register_ button
1. Redirected back to _Register_ page with “Username already exists!” message
1. _Username already exists!_ test successful
1. Fill in new/ not previously existing username
1. Fill in new/ not previously existing password
1. Click _Register_ button
1. Register new user successful, click takes me to new users profile page
1. Register new user successful

#### Testing _Already Registered?_ link:

1. Click on Register tab in navbar
1. Scroll down underneath register form
1. Hover mouse over _Log In_ anchor
1. Anchor reacts to hovering
1. Click anchor
1. Clicking anchor brings me to _Log In_ page
1. Test successful

### Testing Add Book page

#### Testing adding book:

1. Click on Add Book tab in navbar
1. Click _Add Book_ button
1. Error message appears asking user to select _Book Genre_ in selector
1. Pick Economics
1. Click _Add Book_ button
1. Error message appears asking user to fill in _Book Name_ field
1. Fill in _Wealth and Poverty_
1. Click _Add Book_ button
1. Error message appears asking user to fill in _Book Author_ field
1. Fill in _George Gilder_
1. Click _Add Book_ button
1. Error message appears asking user to fill in _Book amount pages_ field
1. Fill in _256_
1. Click _Add Book_ button
1. Error message appears asking user to fill in _Book link_ field
1. Fill in book Amazon link
1. Click _Add Book_ button
1. Error message appears asking user to fill in _Book description_ field
1. Fill in book description (too long to include here)
1. Click _Add Book_ button
1. Click takes me back to the Home page with the flash message of “Book Added Successfully!”
1. Scroll down to bottom of added books
1. _Wealth and Poverty_ is successfully added
1. Test successful

#### Testing Add Book cancel button:

1. Click on Add Book tab in navbar
1. Scroll down to _Cancel_ button
1. Click _Cancel_ button
1. Click takes me back to Home page
1. Test successful

### Testing Profile page

#### Testing book edit:

1. Click on Profile tab in navbar
1. Scroll down to _Wealth and Poverty_ book mentioned above
1. Click _Book Description_ button
1. Book description text appears
1. Click _Book Description_ button
1. Book description text disappears
1. Book description button test successful
1. Click _Edit_ button
1. All information previously added under the book “Wealth and Poverty” appears in all fields and select item
1. Change _Book Genre_ to _History_
1. Click _Save_ button
1. Click takes me back to a shorter version of the Home page with the flash message of “Book Edited Successfully!”
1. Scroll down to _Wealth and Poverty_
1. _Wealth and Poverty_ has successfully been changed
1. Repeat and make changes in every field in _Wealth and Poverty_ in edit form individually
1. Click _Save_ button
1. Click takes me back to a shorter version of the Home page with the flash message of “Book Edited Successfully!”
1. Scroll down to _Wealth and Poverty_
1. _Wealth and Poverty_ has successfully been changed
1. Test successful

#### Testing book delete button:

1. Click on Profile tab in navbar
1. Scroll down to _Wealth and Poverty_ book mentioned above
1. Click _Delete_ button
1. Click takes me back to the Home page with the flash message of “Book Successfully Deleted!”
1. Scroll down to where _Wealth and Poverty_ was previously
1. _Wealth and Poverty_ has successfully been deleted
1. Test successful

### Testing Log Out tab

1. Login through _Log In_ page
1. Arrive on _Profile_ page
1. Click on Log Out tab in navbar
1. Click takes me back to Log In page with the flash message: “You have been logged out”
1. Test successful

### Testing Manage Genres page

#### Testing add new genre:

1. Log in as _admin_
1. Arrive on _Profile_ page
1. Click on Manage Genres tab in navbar
1. Click _Add New Genre_ button
1. Arrive on _Add Genre_ page
1. Write _Fantasy_ on _Genre Name_ input line
1. Click takes me back to the Manage Genres page with the flash message: “New Genre Added!”
1. Scroll down to look at existing genres
1. _Fantasy_ has successfully been added
1. Test successful

#### Testing edit genre:

1. Log in as _admin_
1. Click on Manage Genres tab in navbar
1. Click _Edit_ button next to _Fantasy_ genre added in test above
1. Arrive on _Edit Genre_ page
1. Change _Fantasy_ to _Fanatsyyy_ in _Genre Name_ input line
1. Click _Save Genre_ button
1. Click takes me back to the Manage Genres page with the flash message: “Genre Successfully Updated!”
1. Scroll down to look at existing genres
1. _Fantasy_ now appears as _Fantasyyy_
1. Test successful

#### Testing delete genre:

1. Log in as _admin_
1. Click on Manage Genres tab in navbar
1. Click _Delete_ button next to _Fantasyyy_ genre added in test above
1. Click takes me back to the Manage Genres page with the flash message: “Genre Successfully Removed”
1. Scroll down to look at existing genres
1. _Fantasyyy_ is no longer there
1. Test successful

### Testing footer section

#### Testing footer links:

1. Click on Home tab in navbar
1. Scroll down to the bottom of the page website
1. Hover mouse over all three social media icons
1. Icons react to hovering
1. Click _Twitter_ icon
1. Icon open twitter profile in separate browser tab
1. Click _Facebook_ icon
1. Icon open facebook profile in separate browser tab
1. Click _Instagram_ icon
1. Icon open instagram profile in separate browser tab
1. Test successful

**Screen sizes**

- The Conservative Book Club uses the Bootstrap screen adaptation and can be seen and used on large(above 1200px in width), medium(above 768px in width) and extra small(screens below 578px in width) screen sizes.

**Bugs**

- In the add*book.html I tried to add an icon element in front of the select element for picking the book genre, for some reason the icon would not appear or would overlap the select element. I tried every way I could think of to adjust it properly to be able to keep the styling of the form consistent, however I could not figure it out. I suspect there is some kind of conflict between the \_Clean Blog* theme and _Material Design for Bootstrap_ styling, but as of the time of handing this project in I could not figure it out. The book genre selector is therefore without icon.

* The navbar does not stick to the top of the page when scrolling down only while scrolling up, I tried switching around styling in the css file as well as using Bootstrap class names but I can not seem to fix it. I am aiming to resolve this issue as soon as possible, but as of handing in this project (17/11/20) I have still not found a solution.

## Deployment

**Before Deploying**

#### [MongoDB Atlas](https://www.mongodb.com/)

1. Setting up an account and cluster:

   1. A vital part of this project is the database, on instruction from Code Institute I used MongoDB for the functionality of the website. You can create a free account with them allowing you to 521MB which is more than enough for this project. When first arriving on the website you will be presented with a _Start Free_ and _Try Free_ button, when clicking either of those buttons you will be taken to a form asking for: company name, first name, last name, email and password. The form also asks what your what you are planning to use MongoDB for, click the option that best applies to your situation. After filling in the form, check the checkbox of terms and then submit it by clicking the _Get Started Free_. You will be taken to an additional page where you are asked to give a project name as well as pick a preferred coding language, pick the Python option for now and then click the _Continue_ button. On the next page click the _Create a cluster_ in the _Free_ option.
   1. This takes you to the _Create a starter Cluster_ page. In the _Cloud Provider_ section pick the _Amazon Web Services_ and set the region to _N.Virginia(us-east-1)_. Next, if you have followed the instructions the _Cluster Tier_ should be automatically set to the _Free forever_ option keep this option as it is. Then scroll down past the _Additional Settings_, click the _Cluster Name_ section and provide your cluster a name. In a previous project I followed the Code Institute instructions and named my cluster _myFirstCluster_, but you can pick whatever name you want then click the _Create Cluster_ button.

1. Creating a user and providing access:

   1. After creating your cluster on the left and side of the screen there will be a _Database Access_ option under the header _Security_ click this tab, you will arrive in the _Database Users_ section, click the button in the middle of the page named _Add new database user_. Pick a username and a password, you will use this when connecting to the database in your project. Do not use any special characters/non-alphanumeric characters in your username or password this will create issues to your connection to Python further down the line in your project. The _Database User Privileges_ section should already be set to _Read and Write to Any Database_ leave it at this and click the _Add User_ button. Then in the sidebar underneath the _Security_ header pick the _Network Access_ option, which takes you to the _IP Access List_, click the _Add IP Address_, you do this to make sure it has access to the database. In the modal that pops up there is a _Allow Access from Anywhere_ button which automatically fills in the _Access List Entry_ field to _0.0.0.0/0_. Ideally you should put the IP’s of your hosts here as a further security feature, but since I am just following the Code Institute instructions provided to me for simplicity, click the _Confirm_ button.

1. Database Creation with MongoDB Atlas:

   1. Now that the MongoDB cluster is created, maneuver back to the _Cluster_ section of the page by clicking the _Clusters_ option on the left part of the page. You need to create a new database, so on the _Clusters_ page click the _Collection_ button in the cluster. Then click the _Create Database_ button and a form will appear asking for _Database Name_ and _Collection Name_, in this project the database is called _book_database_. There will be more than one collection name added, but for the first one I decided to add the collection name of _books_ and then click the _Create_ button. After the database is generated click select the _book_database_ and then click the _Create Collection_ button to add more collections, the second collection I created was the _genres_ collection. Add yet another collection by clicking the _Create Collection_, the final collection will be called _users_ to store the information of the users of the site. These are the three collections that will form the basis of the book club application.

1. Insert data into collections:
   1. Click the _genres_ collection and in the right corner there is a _Insert Document_ button, click this button. From here you will add key-value pairs, in this case the key will be _genre_name_ and the first value is _Economics_, then click on the green _Insert_ button. The key and value pairs does not have to be added manually through MongoDB so you will now move on to adding key and value pairs to the _books_ collection. Click the _Insert Document_ in the _books_ collection. The first key will be _genre_name_ with the value of _Economics_ which created previously, second key is _book_name_ with the value _Economic facts and Fallacies_, third key _book_author_ with the value of _Thomas Sowell_, forth key _book_pages_ with the value of _272_, fifth key _book_discription_ with the value of the description. I will not add the book description here because it is too long but you can find it [here](https://www.amazon.com/Economic-Facts-Fallacies-Thomas-Sowell/dp/0465022030). Finally we will add the key _created_by_ and I personally put the value of _Josefin_ which is my name. This is just to get us up and running initially. Click on the green _Insert_ button and this should submit the first book into the database. You can now build the Book Club Flask project upon this data.

#### Cloning the MS3_book_club project

You can gain access to my project by going to GitHub pages, below is a step by step process allowing you to download my project and make it your own. One of the things provided by the Code Institute is [gitpod-full-template](https://github.com/Code-Institute-Org/gitpod-full-template) which provided me with useful extensions, shortcuts etc.

If you would like to download and work on this project separately, make sure to:

1. Have GitPod is installed on your local system
1. Go into JosefinE7 repositories
1. Click onto the: MS3_book_club repository
1. Click the git clone or download button
1. Open the project up in your own workspace
1. Add all third party libraries, write "pip3 install -r requirements.txt" in terminal
1. Write a git add command: “git add .” in terminal
1. Write a commit message: “git commit -m ‘Initial commit’” in the terminal
1. Write: “git push” in the terminal
1. Start working on your own version of the Conservative Book Club website; add and commit as you go along

#### env.py

One file that will not be added to the project when downloading or cloning is the absolutely crucial env.py file that contains hidden information that you don’t want to publish to the internet. Write “touch env.py” in the terminal, to make sure this is not pushed to GitHub write “touch .gitignore” in the terminal. Open the .gitignore file by clicking it, write _env.py_ on the first line of the document and right underneath \_\_\_pycache\_\_\_, remember to save the file and then close it. Open the env.py and add _import os_ on the first line, skip one line and then add:

- os.environ.setdefault("IP", "the_IP_address_you_put_into_MongoDB")
- os.environ.setdefault("PORT", "5000") - The "PORT" and "5000" is the standard used for Flask applications
- os.environ.setdefault("SECRET_KEY", "your_secret_key") - the secret key is used for flash() and session() functions from Flask so pick a value safer than \_your_secret_key.
- os.environ.setdefault("MONGO_URI", "LINK") - To find your MONGO_URI file go back to MongoDB, on the _Clusters page_ click the connect button on your cluster. You will be presented with different options but pick the _Connect your Application_ option. Select Python under the _Select your driver and person_ and pick the appropriate version for your setup. Below this there will be a link, the link has your username and cluster details already, but you need to fill in the database name and password directly in the link (the username and password comes from the Database Access page, NOT with your login credentials to the MongoDB website). Paste this link as a value to your MONGO_URI key.
- os.environ.setdefault("MONGO_DBNAME", "your_database_name")

**Deploying the project**

#### [Heroku](https://id.heroku.com/login)

1. Create required files:

   1. Create a requirements.txt file to tell Heroku which applications and dependencies are needed to run our app. You can do this by writing “pip3 freeze --local > requirements.txt” in the command line of the project. Heroku looks for a file called _Procfile_, with a capital P, to know which file runs the app as well as how to run it so write: “echo web: python run.py > Procfile” in the commandline of the project. Check that both the Procfile and the requirements.txt file have been created successfully. Make sure that there is no blank line at the bottom of the Procfile, because this can create a problem when deploying to Heroku.

1. Setting up account on Heroku:

   1. Github pages only allows you post static websites so in this project I am instead using Heroku to deploy my project. To start deploying my project I went to: Heroku. I signed up to a new account, since I didn’t have one since previously, to sign up I provided my first name, last name, email, country as well as selecting Python as Primary development language. Before clicking the _Create Free Account_ button you have to pass a CAPTCHA. After clicking the submit button Heroku sends a confirmation email to the email provided in the form. In the email there is a confirmation link, when clicking the link you are able to decide your password as well as confirm it an extra time before clicking the “Set password and log in” button right underneath the password form. After setting up your password you will be taken to a page that says _Click here to proceed_, clicking the button takes you to your app dashboard.

1. Creating a Heroku app:

   1. When the account and password is created and you have successfully logged in you will be presented with the Heroku dashboard. There will be a couple of different languages presented, but below the languages there is a button that says: “Create new app”, click this button. You will be taken to a form where you give the app a name, I named my app: “flask-book-club”, the name has to be unique, in lowercase and use dashes(-) instead of spaces. Then you have to choose the region closest to you, the options provided are the United States or Europe. I live in Europe therefore I picked that, then click the “Create App” button at the bottom of the form. From there you are brought to a new dashboard where you are presented with different options to connect the app.

1. Connecting the app:

   1. After creating the app you will be taken to the Deploy section where you have a couple of different options, you can use the Heroku CLI for which there are instructions provided close to the top of the page. I personally decided to use Automatic Deployment from my GitHub repository. So in the “Deployment method” section click the Github-connect to GitHub option, in the “search for repository to connect to“ put in you GitHub username, then in the add your repository name in the “repo-name” search bar. The name of my repository is MS3_book_club. When you have written your repository name click the Search button. After clicking the button your repository should be listed below, click the “Connect to this app” button to connect.

1. Dealing with hidden files and deploying to Heroku:
   1. Before you can click the button to enable Automatic Deploys in the section below, you have to make Heroku aware of the hidden files of the project for the project to be able to deploy properly. In my project I have contained the environment variables within the project in a hidden env.py file, Heroku can not automatically read those variables. You take care of this by clicking the ‘Settings’ tab for your app, and then click on the ‘Reveal Config Variables’ in the ‘Config Vars’ of the page. By clicking the ‘Reveal Config Variables’ you can securely provide Heroku with the variables that are required. The env.py in this project contains a couple of different variables. Make sure that no quotes are included when putting in the keys and values, since this can cause issues. All the keys and values are the same as the ones listed above in the env.py section. Click the add buttons on all the keys and values you have added and then go back to the ‘Deploy’ tab. Before deploying make sure all the files in your repository are added, committed and pushed to GitHub. After this you can click the _Enable Automatic Deploys_ button in the _Automatic Deploys_ section of the page. Underneath the _Automatic Deploys_ section in the _Manual Deploy_ section click the _Deploy Branch_ button, as this project only has the main branch. After clicking the _Deploy Branch_ button Heroku will start building the app from Github, when it is done if there are not any issues you will get a _Your app was successfully deployed!_ message with a button titled _View_ to view your app. Your app is now deployed successfully and whenever you push changes to GitHub Heroku will automatically update the app.

## Credits

**Content**

- All the book description text is all taken from the Amazon reviews section of said book.

**Media**

- [Hero image](https://upload.wikimedia.org/wikipedia/commons/5/5a/Books_HD_%288314929977%29.jpg)
- [book.jpg](https://p1.pxfuel.com/preview/323/411/701/book-old-vintage-chipped.jpg)

**Acknowledgements**

- I would like to thank my mentor Sandeep A. for helping me on this project, his guidance and knowledge was crucial for the final result of this projec
