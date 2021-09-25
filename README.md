# Yandex-SDC-Meetup-Solution
Solution for Yandex Self-Driving Cars Meetup 2021 Contest.

The essence of the task:

We need to write a simplified version of the system that controls delivery robots in Innopolis: determine the optimal number of robots and build routes for them.

In the given map we need to place R robots, then process T requests in total of D orders.
For every order we need to assign a robot and build a path to pick-up and drop-off location. One robot can perform 60 steps per iteration. We need to maximaze the profit. 

You can read full problem description [here](images/problem.png). (Russian only)

There are 10 tests in this problem. 

If you look at what they look like, you can see that, unlike the first five, tests 6-10 are a map of real terrain. (Specifically, the map of Innopolis). All of these tests are the same. I decided to forget about the first 5 tests and focus on the solution for the Innopolis map.

Let's see if any other inputs among these tests are fundamentally different. Let's look at the orders:

Other than quantitatively, the orders are not different in any way. And you can see the first interesting feature! All orders start and end at one of 273 possible points. This means that you can lay out the shortest paths between each pair of points in advance. 

Immediately another problem is solved: We can use no more than 100 robots in total. And after analyzing it, you can see that all the orders are distributed evenly between each of these points. This means that you can place robots randomly at each of these points.

But here the computational problems began.




The final solution, which got the top 5 on the leaderboard, is as follows:


![](images/clusters.gif)


![](images/one_center.gif)


![](image/full_path.gif)
