# Advanced Software Engineering/ Musavi
This repository contains my project files and here in **README.md** you can find the description of my project software engineering metrics.<br><br>

My project is a simple RepiceBook "RezetBuch", Which consists of 6 different classes **CookInstruction**, **Database**, **Ingeredient**, **Recipe**, **RecipeManager** and **RecipeBook** which is implemented in **Main.py**.The project also contains functionality such as **Insert** , **Delete** , **Update** , **Search** , **View all Recipes**.<br><br>


For this project I used **Python** as Programming language and **Sqllite3** as my database for store and retrival. For this project I used console as showing the result.<br>


## 1. Git/Github 
I used Git and Github which is used for version control, storing and tracking code to frequently commit and push my code to GitHub. At the very first beginning I did a pull but I did everything in my IDE my local code base was always up-to-date. My git times can be seen at the [contribution chart](https://github.com/semmusavi?tab=overview&from=2024-03-01&to=2024-03-01) in my GitHub.<br><br>

[![GitHub Streak](https://github-readme-streak-stats.herokuapp.com/?user=semmusavi&theme=cobalt)](https://github.com/semmusavi/st_project)  

## 2. UML Diagrams
For this Project I created 4 different UML diagrams in the following you can find the links to diagrams <br>
  1. [Use Case Diagram](https://github.com/semmusavi/st_project/blob/main/UML/Usecase_Diagram.png) it is to present a graphical overview of the functionality provided by a system in terms of actors, their goals and any dependencies between those use cases.<br>
  2. [Sequence Diagram](https://github.com/semmusavi/st_project/blob/main/UML/Sequence_Diagram.png) here it is shown how processes operate with one another and in what order <br>
  3. [Class Diagram](https://github.com/semmusavi/st_project/blob/main/UML/Class_Diagram.png) here you can see the structure of a system by showing the system’s classes, their attributes, operations (or methods), and the relationships among objects.<br>
  4. [Activity Diagram](https://github.com/semmusavi/st_project/blob/main/UML/Activity_diagram.png) shows the flow between different activities<br>

## 3. DDD 
In this link you find **Core Domain Chart**, **Context Mapping Diagram** of my project [link](https://github.com/semmusavi/st_project/blob/main/UML/DDD.png) Event Storming Diagram is here [Link](https://github.com/semmusavi/st_project/blob/main/Event_storming.png).<br> I extended my project. For example the project is just implemented with Console output but I extended the DDD with Web, Desktop and mobile app. Moreover, User Login and ads is also considered.    

## 4. Metrics
I used SonarCloud which is Online of Sonarcube. For this I have connected my Github repository with it to analyse the source code of my project automatically. The Metrics of my project are listed below.
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
  Class names (**RecipeBook**, **RecipeManager**, **Database**) are also meaningful and reflect their responsibilities. Here is the link to [print_menu()](https://github.com/semmusavi/st_project/blob/95d258075b90e35871d0dc9a3dfd98fcd32d3037/main.py#L11)
  
* DRY Principle (Don't Repeat Yourself):
  
  I tried to avoid duplications.  For example, the menu display logic is encapsulated within the **print_menu()** method, avoiding duplication of print 
  statements. The **run()** method is responsible for the main loop of the program, which reduces duplication of code for handling user input.

  * Duplicated Lines [![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=semmusavi_st_project&metric=duplicated_lines_density)](https://sonarcloud.io/summary/new_code?id=semmusavi_st_project)<br>

* Comments and Docstring:

  I wrote comments and docstrings which perform  explanations for the purpose and functionality of methods and classes. These comments help code readability   and understanding of my project for work with the code in the future. This is the [Link](https://github.com/semmusavi/st_project/blob/95d258075b90e35871d0dc9a3dfd98fcd32d3037/main.py#L7) to source code

## 6 and 7:  Build Management and CI/CD
I have considered these two parts together and have used Github action for Build Managment and Continuous Integration, and Continuous Delivery. At first I attemped to use Jenkins but I realized it is compatiable with Java screenshot of build [Jenkins_Screenshot](https://github.com/semmusavi/st_project/blob/main/jenkins_maven_build.png) , therefore I chose Github Action which is accessible via Github and consist of three steps **Build** , **Test** and **Deploy**.

* Here is the screenshot of Github action workflow. [screenshot](https://github.com/semmusavi/st_project/blob/main/Github_Action_workflow.png)

For implementing CI/CD pipeline using Github Action I had to use yaml file. The link to my yaml file is [here](https://github.com/semmusavi/st_project/blob/main/.github/workflows/python-app.yml). 

In the yaml file three steps of CI/CD pipeline are implemented. 
* In the **Build** step the main.py will run and requirments and dependencies will install. [Link](https://github.com/semmusavi/st_project/blob/main/Build_Step.png)
* In the **Test** step I used my unittest file. [Link](https://github.com/semmusavi/st_project/blob/main/Test_Step.png)
* In the **Deploy** step after successfully completation of test step it will run and print the message "Deploy app". [Link](https://github.com/semmusavi/st_project/blob/main/Deploy_Step.png)

## 8 Unit tests

For this part, I used the Python unittest module to test various aspects of my project, including **classes**, **methods**, and the **database**.

The test consists of these parts: 
*  **TestRecipeManager** : This one tests the **add_recipe()** method of the RecipeManager class 
*  **TestRecipeBook** : This one tests the **run()** method of the RecipeBook class 
*  **TestRecipe** : This one tests the **__rep__()** method of the Recipe class 
*  **TestIngredient** : This one tests the **__repr__()** method of the Ingredient class
*  **TestCookInstruction** : This one tests the **__repr__()** method of the CookInstruction class
*  **TestDatabase** : This one tests the **insert_recipe()** method of the Database class

Here is the link to my python test file of my project. [Link](https://github.com/semmusavi/st_project/blob/main/test_recipe_book.py)
Here is the screenshot of test file result. [Link](https://github.com/semmusavi/st_project/blob/main/Test_File_Result.png)

## 9 IDE 
I have used Visual Studio Code as IDE of my project because I have already used it and I am comfortable with it here are shortcuts and code snippets which I used when I code in this IDE.

* Type a shortcut like "def" and then press Tab to insert code snippet. It will insert a function template.
* Ctrl + F5 will run the program
* Ctrl + D Duplicate a line
* Alt + Shift + . Select all intances of a word then you remove or change
* Alt + select by mouse for vertical selection which you can code in multiple line at the same time.   

## 10 DSL
For this step (Domain Specific Language) there are two file the first one which is Interpreter was implemented to read and execute the second one which is DSL. The interpreter is responsible for executing actions in RecipeBook application. The actions of interpreter will execute Add, Search, Delete, Update and View all Recipe of the project. In DSL file every line represents an action in the Recipebook Application. 
Here is the link to the [Interpreter](https://github.com/semmusavi/st_project/blob/main/interpreter.py) 
Here is the link to the [DSL file](https://github.com/semmusavi/st_project/blob/main/recipe_book_data.dsl)

## 11 Functional Programming
For the Functional programing principles I used python as my programming language and a simple python program to cover all aspects and it is not related to my recipebook project. 
In the python file there are
* list of book which represents **final data structures** and consists of collection of book with attributes like title, price and genre.
* The process_data() function which respresents a **higher-order function**. It takes a list of books and a function as arguments, applies the function to each book using map(), and returns the result of     the list.
* The get_price() function which respresents **side-effect free** function. It takes a book object as input and returns its price.
* The make_genre_filter() function returns a function genre_filter as its result which respresents **Functions as Parameters and Return Values** and is used as a parameter to the filter() function. The       process_data() function takes another function
* The make_genre_filter() function creates a **closure** with a nested function genre_filter that captures the genre variable.

Here is the link to my functional programming file. [Functional programming](https://github.com/semmusavi/st_project/blob/main/functional_programming.py) 
