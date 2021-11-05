# AAE group 1
### Table of Contents
- [Background of Path Planning to Aviation Engineering]
- Theory of Path Planning Algorithm
- Introduction of the Engineering Tools
- Task 1
- Task 2
- Task 3
- Task 4
- Reference
- Group Presentation
*video pending*
### (Background of Path Planning to Aviation Engineering)

### Theory of Path Planning Algorithm
From the standpoint of the control engineer, path planning is among the most important research topics in robotics. Suggesting path planning solves several issues in a variety of industries. It has been used to guide the robot toward a certain goal, from basic trajectory planning through the selection of an appropriate action scene. Because worldwide environemntal information may not always be available a priori, path planning cannot always be done in advance. Path planning can be extensively used in partly and unknown structured settings if an appropriate method is proposed.

A suitable trajectory is created as a series of operations to keep the robot moving from the starting position to the goal position via numerous intermediate states. Every choice in path planning algorithms is made based on the evidence provided at the time and parameteres like the shortest distance measures to the destination point computed utilizing Euclidean distance calculation. There could be more than one route from the starting place to the destination. Nevertheless, in a number of cases, there is no way to get to the desired states. In terms of optimization, the ideal path should cover the smallest distance, be free of obstructions and collisions, and take the least amount of time to achieve the objective state. Futhermore, because a robot may have numerous movement restrictions, including the nonholonomic condition in underactuated systems, the chosen trajectory has to be smooth and free of excessive twists (Klancar et al., 2017).

As described by Savkin et al., there are two types of path planning (2015). The first one is path planning on a global scale. The environment is stable in this circumstance, and the global information is provided a priori in the control design. This strategy is both costly to deploy and well-studied in the published literature. Another method is local path planning, in which the path is produced using data collected from the robot's sensors while it is moving. As a result, when a robot encounters a new area, it might create a new course. This system is much more difficult to design, but it is more practical in reality.

In a path planning algorithm, there are four main switch factors which should be evaluated (Teleweck and Chandrasekaran, 2019). The first step is to optimize. This criteria assures that the chosen solution is the most efficient in terms of range, duration, price, and other factors. The second requirement is completion, which assures that the path planning algorithm delivers all potential path options. Accuracy and exactness come next. This criteria is critical in getting all states from the start to the finish line. The runtime is the final requirement. The goal of this criteria is to ensure the best-case scenario for dealing with the given challenge. Machine learning is among the most effective ways to meet the aforesaid criteria. Otte provides a investigate of machine learning appliance for path planning (2015).

### Introduction of the Engineering Tools
#### Python

#### GitHub

### Task 1(I will edit this part and add some context)
a. Methodology

b. Results (total cost)
A380: 2909.636000524682
A381: 3675.1330778255983
A382: 4438.615941564147
A383: 5192.027737490824

c. Discussion

### Task2
a. Methodology

b. Results
 when:Ct=20,Cf=20, the cost is the lowest
 because
 <img width="520" alt="180ffa328a444610f331031ac026254" src="https://user-images.githubusercontent.com/90884384/137430450-ce876dcb-fe63-4e05-b09b-0924bd94d288.png">
and 
![image](https://user-images.githubusercontent.com/90884384/137430483-1e783886-90f8-47b2-9f47-9e34f3a86840.png)

![Task2-2-1](https://user-images.githubusercontent.com/77454664/137463653-905d0a33-9dbf-4172-8e7e-57df71a8cbdf.PNG)
![task2-2-2](https://user-images.githubusercontent.com/77454664/137463668-95074824-104c-4c56-973d-3e5c240fa03f.PNG)
[Task2-2.pdf](https://github.com/EnvironmentCommittee/AAE-group-1/files/7352361/Task2-2.pdf)

c. Discussion
 #### above is task 2

### Task 3
a. Methodology

b. Results

c. Discussion

### Task 4
a. Methodology

b. Results 

c. Discussion


### Reflective Essay

### References
