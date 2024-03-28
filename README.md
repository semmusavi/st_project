# Advanced Software Engineering/ Musavi
This repository contains my project files and here in **README.md** you can find the description of my project software engineering metrics.<br><br>

My projct is a simple RepiceBook "RezetBuch", Which consists of 6 different classes **CookInstruction**, **Database**, **Ingeredient**, **Recipe**, **RecipeManager** and **RecipeBook** which is implemented in **Main.py**.The project also contains functionality such as **Insert** , **Delete** , **Update** , **Search** , **View all Recipes**.<br><br>


For this project I used **Python** as Programming language and **Sqllite3** as my database for store and retrival. For this project I used console as showing the result.<br>


## 1. Git/Github 
I used Git and Github which is used for version control, storing and tracking code to frequently commit and push my code to GitHub. At the very first beginning I did a pull but I did everything in my IDE my local code base was always up-to-date. My git times can be seen at the [contribution chart](https://github.com/semmusavi?tab=overview&from=2024-03-01&to=2024-03-01) in my GitHub.<br><br>

[![GitHub Streak](https://github-readme-streak-stats.herokuapp.com/?user=semmusavi&theme=cobalt)](https://github.com/semmusavi/st_project)  

## 2. UML Diagrams
For this Project I created 4 different UML diagrams in the following you can find the links to diagrams <br>
  1. [UseCase Diagram](https://github.com/semmusavi/st_project/blob/main/UML/Usecase_Diagram.png) it is to present a graphical overview of the functionality provided by a system in terms of actors, their goals and any dependencies between those use cases.<br>
  2. [Sequence Diagram](https://github.com/semmusavi/st_project/blob/main/UML/Sequence_Diagram.png) here it is shown how processes operate with one another and in what order <br>
  3. [Class Diagram](https://github.com/semmusavi/st_project/blob/main/UML/Class_Diagram.png) here you can see the structure of a system by showing the system’s classes, their attributes, operations (or methods), and the relationships among objects.<br>
  4. [Activity Diagram](https://github.com/semmusavi/st_project/blob/main/UML/Activity_diagram.png) shows the flow between different activities<br>

## 3. DDD 
here is the [link](https://github.com/semmusavi/st_project/blob/main/UML/DDD.png) to my DDD diagram.<br>

## 4. Metrics
I used SonarCloud which is Online of Sonarcube. For this I have connected my Github repository with it to analyse the source code of my project automatically. 
* Quality Gate Status  [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=semmusavi_st_project&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=semmusavi_st_project)<br>
* Bugs [![Bugs](https://sonarcloud.io/api/project_badges/measure?project=semmusavi_st_project&metric=bugs)](https://sonarcloud.io/summary/new_code?id=semmusavi_st_project)<br>
* Duplicated Lines [![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=semmusavi_st_project&metric=duplicated_lines_density)](https://sonarcloud.io/summary/new_code?id=semmusavi_st_project)<br>
* Reliability Rating [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=semmusavi_st_project&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=semmusavi_st_project)<br>
* Security Rating [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=semmusavi_st_project&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=semmusavi_st_project)<br>
* Maintainability Rating [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=semmusavi_st_project&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=semmusavi_st_project)<br>
* Vulnerabilities [![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=semmusavi_st_project&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=semmusavi_st_project)<br>
* Code Smells [![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=semmusavi_st_project&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=semmusavi_st_project)<br>

## 5. Clean Code Development

### for my project I have followed some clean code principles which are:

* I used Meaningful Names and Convention:
  
  For variable and method I chose **snake_case**. For example, **print_menu()** method clearly indicates that it displays the menu options, **add_recipe()**    method adds a recipe, and so on.
  Class names (**RecipeBook**, **RecipeManager**, **Database**) are also meaningful and reflect their responsibilities.
  
* DRY Principle (Don't Repeat Yourself):
  
  I tried to avoid duplications.  For example, the menu display logic is encapsulated within the **print_menu()** method, avoiding duplication of print 
  statements. The **run()** method is responsible for the main loop of the program, which reduces duplication of code for handling user input.

  * Duplicated Lines [![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=semmusavi_st_project&metric=duplicated_lines_density)](https://sonarcloud.io/summary/new_code?id=semmusavi_st_project)<br>

* Comments and Docstring:

  I wrote comments and docstrings which perform  explanations for the purpose and functionality of methods and classes. These comments help code readability   and understanding of my project for work with the code in the future.

## 6 and 7:  Build Management and CI/CD
I have considered these two parts together and have used Github action for Build Managment and Continuous Integration, and Continuous Delivery. At first I attemped to use Jenkins but I realized it is compatiable with Java screenshot of build [Jenkins_Screenshot](https://github.com/semmusavi/st_project/blob/main/jenkins_maven_build.png) , therefore I chose Github Action which is accessible via Github and consist of three steps **Build** , **Test** and **Deploy**.

