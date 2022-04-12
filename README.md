[![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://www.github.com/jackrobert0220)
[![Twitter](https://img.shields.io/badge/<Twitter>-%231DA1F2.svg?style=for-the-badge&logo=Twitter&logoColor=white)](https://www.twitter.com/jackglazzzer)
[![Instagram](https://img.shields.io/badge/<Instagram>-%23E4405F.svg?style=for-the-badge&logo=Instagram&logoColor=white)](https://www.instagram.com/jackglazzzer)
[![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/jack-glazer)
<div align="center">
  <img src="main_app/static/images/logo_2.jpg" alt="logo" width="600" height="399">
</div>
 
# Django Guitars

## Description

- A web-based application where guitar enthusiasts may post their unique guitars for selling or trading!
   
Users are able to:
- 🎸 post their own guitar with details, once signed up
- 🔍 view all guitars posted by all users
- 📲 update guitar data, such as image, color, brand, etc.
- 📤 contact other users via email link (only available if signed up)

- The application serves as a one-stop-shop for super-rare guitars that you cannot find on most websites. 

- By creating Django Guitars, I was able to better understand Django's functionality and take advantage of the framework's built-in features, such as error handling and admin access. 

## Links

- [![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/jackrobert0220/Django-Guitars)[GitHub Repo](https://github.com/jackrobert0220/Django-Guitars/ "Django Guitars Repo")

- [![Heroku](https://img.shields.io/badge/heroku-%23430098.svg?style=for-the-badge&logo=heroku&logoColor=white)](https://djangoguitars.herokuapp.com/)[Live on Heroku](https://djangoguitars.herokuapp.com/ "Live View")

## Technologies Used
[![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org/)
[![Bootstrap](https://img.shields.io/badge/bootstrap-%23563D7C.svg?style=for-the-badge&logo=bootstrap&logoColor=white)](https://getbootstrap.com/)
[![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org/index.html)
[![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/HTML_basics)
[![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS)
[![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)](https://git-scm.com/)
[![Heroku](https://img.shields.io/badge/heroku-%23430098.svg?style=for-the-badge&logo=heroku&logoColor=white)](https://dashboard.heroku.com/)
 
# User-Flow:

- Create a login to begin posting your guitar/bass collection online for others to check out.

- Once logged in, user will gain the ability to post to their profile of 
   their guitar along with its attributes: 
   - Brand
   - Model
   - Year
   - Price 
   - Number of Strings 
   - Color
   - Image
   - Pickup Type
   - Owned By

- The user's guitar will be added to the master list of all user's guitars.

- When creating a guitar post, the user is first prompted to add Pickups with its own attributes:
    - Type
    - Brand
    - Active (y/n)

- After posting either Guitars and/or Hardware Options, the user will 
   have the ability to UPDATE and DELETE their POSTS.

- A link to email an offer to a Guitar's owner will be available on each Guitar page.

- User must be logged in to utilize the above-mentioned functions.

![Screen Shot 2022-04-11 at 7 48 38 PM](https://user-images.githubusercontent.com/91999893/162869461-d3f41292-babf-4d77-a5e2-a07b9cc66f47.png)


----------------------------------------------------------------------------------------------------------

# ERD(Entity-Relational-Data):

Utilzing Django's framework, there will be models for the User, Guitars and Pickups.

![Screen Shot 2022-04-11 at 7 49 52 PM](https://user-images.githubusercontent.com/91999893/162869555-2f868c95-6619-49d1-94d6-6d4ff5d18b49.png)


----------------------------------------------------------------------------------------------------------

# Wireframes:

![Screen Shot 2022-04-11 at 7 51 43 PM](https://user-images.githubusercontent.com/91999893/162869756-ab9912c3-575f-478a-8f4f-c0e8a6aa6952.png)

![Screen Shot 2022-04-11 at 7 52 22 PM](https://user-images.githubusercontent.com/91999893/162869822-353904f2-743d-48af-8999-59353c4d2ab2.png)

![Screen Shot 2022-04-11 at 7 52 39 PM](https://user-images.githubusercontent.com/91999893/162869843-3e81aef1-b015-4f7d-954c-a8ed9f434514.png)

![Screen Shot 2022-04-11 at 7 53 02 PM](https://user-images.githubusercontent.com/91999893/162869886-d080024c-889f-4bee-8b0c-916cebeb8c4f.png)

![Screen Shot 2022-04-11 at 7 53 47 PM](https://user-images.githubusercontent.com/91999893/162869970-73c958cd-a32d-45ce-9d9d-302aa97335b3.png)

![Screen Shot 2022-04-11 at 7 54 31 PM](https://user-images.githubusercontent.com/91999893/162870049-59a69da7-a358-4082-9de4-0a62bcfe8003.png)







