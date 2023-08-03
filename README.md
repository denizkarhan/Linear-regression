# Linear-regression

Summary: In this project, you will implement your first machine learning algorithm

The aim of this project is to introduce you to the basic concept behind machine learning.
For this project, you will have to create a program that predicts the price of a car by
using a [linear function](https://en.wikipedia.org/wiki/Linear_function) train with a [gradient descent](https://en.wikipedia.org/wiki/Gradient_descent) algorithm.
We will work on a precise example for the project, but once you’re done you will be
able to use the algorithm with any other dataset.

In this project you are free to use whatever language you want.
You are also free to use any libraries you want as long as they do not do all the work
for you. For example, the use of python’s numpy.polyfit is considered cheating.
* You should use a language that allows you to easily visualize your
  data : it will be very helpful for debugging.

The first program will be used to predict the price of a car for a given mileage.
When you launch the program, it should prompt you for a mileage, and then give
you back the estimated price for that mileage. The program will use the following
hypothesis to predict the price :

![Ekran görüntüsü 2023-08-04 010827](https://github.com/denizkarhan/Linear-regression/assets/81527587/788f1b28-5a2c-49e8-8cb8-83f05f262e23)


The second program will be used to train your model. It will read your dataset file
and perform a linear regression on the data.
Once the linear regression has completed, you will save the variables theta0 and
theta1 for use in the first program.
You will be using the following formulas :

![Ekran görüntüsü 2023-08-04 011218](https://github.com/denizkarhan/Linear-regression/assets/81527587/91be0182-094e-4677-a55a-2e8e5c134fbd)


I let you guess what m is :)
Note that the estimatePrice is the same as in our first program, but here it uses
your temporary, lastly computed theta0 and theta1.
Also, don’t forget to simultaneously update theta0 and theta1.

* Plotting the data into a graph to see their repartition.
* Plotting the line resulting from your linear regression into the same graph, to see the result of your hard work !
* A program that calculates the precision of your algorithm.


https://github.com/denizkarhan/Linear-regression/assets/81527587/2efb7eb6-c027-4bf1-9d16-72243351bb7a

