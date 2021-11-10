# AAE group 1
### Table of Contents
- [Background of Path Planning to Aviation Engineering](https://github.com/EnvironmentCommittee/AAE-group-1#theory-of-path-planning-algorithm)
- Theory of Path Planning Algorithm
- Introduction of the Engineering Tools
- Task 1
- Task 2
- Task 3
- Task 4
- Reference
- Group Presentation
*video pending*
### Background of Path Planning to Aviation Engineering

### Theory of Path Planning Algorithm
From the standpoint of the control engineer, path planning is among the most important research topics in robotics. Suggesting path planning solves several issues in a variety of industries. It has been used to guide the robot toward a certain goal, from basic trajectory planning through the selection of an appropriate action scene. Because worldwide environemntal information may not always be available a priori, path planning cannot always be done in advance. Path planning can be extensively used in partly and unknown structured settings if an appropriate method is proposed.

A suitable trajectory is created as a series of operations to keep the robot moving from the starting position to the goal position via numerous intermediate states. Every choice in path planning algorithms is made based on the evidence provided at the time and parameteres like the shortest distance measures to the destination point computed utilizing Euclidean distance calculation. There could be more than one route from the starting place to the destination. Nevertheless, in a number of cases, there is no way to get to the desired states. In terms of optimization, the ideal path should cover the smallest distance, be free of obstructions and collisions, and take the least amount of time to achieve the objective state. Futhermore, because a robot may have numerous movement restrictions, including the nonholonomic condition in underactuated systems, the chosen trajectory has to be smooth and free of excessive twists (Klancar et al., 2017).

As described by Savkin et al., there are two types of path planning (2015). The first one is path planning on a global scale. The environment is stable in this circumstance, and the global information is provided a priori in the control design. This strategy is both costly to deploy and well-studied in the published literature. Another method is local path planning, in which the path is produced using data collected from the robot's sensors while it is moving. As a result, when a robot encounters a new area, it might create a new course. This system is much more difficult to design, but it is more practical in reality.

In a path planning algorithm, there are four main switch factors which should be evaluated (Teleweck and Chandrasekaran, 2019). The first step is to optimize. This criteria assures that the chosen solution is the most efficient in terms of range, duration, price, and other factors. The second requirement is completion, which assures that the path planning algorithm delivers all potential path options. Accuracy and exactness come next. This criteria is critical in getting all states from the start to the finish line. The runtime is the final requirement. The goal of this criteria is to ensure the best-case scenario for dealing with the given challenge. Machine learning is among the most effective ways to meet the aforesaid criteria. Otte provides a investigate of machine learning appliance for path planning (2015).

### Introduction of the Engineering Tools
#### Python
Python is a widely used general-purpose, high level programming language. It was created by Guido van Rossum in 1991 and further developed by the Python Software Foundation. It was designed with an emphasis on code readability, and its syntax allows programmers to express their concepts in fewer lines of code.Python is a programming language that lets you work quickly and integrate systems more efficiently.Python also used for web development (server-side),software development, mathematics and system scripting.Python can works on different platforms (Windows, Mac, Linux, Raspberry Pi, etc),has a simple syntax similar to the English language,has syntax that allows developers to write programs with fewer lines than some other programming languages and runs on an interpreter system, meaning that code can be executed as soon as it is written.This means that prototyping can be very quick so Python can be treated in a procedural way, an object-oriented way or a functional way.
#### GitHub
GitHub is a code hosting platform for version control and collaboration. It lets you and others work together on projects from anywhere.GitHub is a web-based interface that uses Git, the open source version control software that lets multiple people make separate changes to web pages at the same time. As Carpenter notes, because it allows for real-time collaboration, GitHub encourages teams to work together to build and edit their site content.GitHub allows multiple developers to work on a single project at the same time, reduces the risk of duplicative or conflicting work, and can help decrease production time. With GitHub, developers can build code, track changes, and innovate solutions to problems that might arise during the site development process simultaneously. Non-developers can also use it to create, edit, and update website content, which Carpenter demonstrates in her tutorial.
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

Fu, Chenlei 

In this project, I did part of the tasks of the python tutorial, and part of the task 2 of the final project. I have studied java in high school, but I have never used python as a programming language before. Through the tutorial questions in the course and other online tutorial materials, I have a preliminary understanding of Python, and I can write simple codes in python. By using the Github platform, I feel the convenience of integrating work content. Each person in the group is assigned a different job, so when the work results are integrated, it will cause inconvenience. Github completes this very well. It can not only create a branch for each group member, let the group members upload their work in their own branch, and then merge it into the main repository, but also record and highlight each group member’s  changes. In general, Github can make team cooperation smoother. Through the study of the path planning algorithm, I understand how to control the flight path of the aircraft in the air. By using Python code, the location of obstacles and the setting of some special areas will be set to simulate the real world. By changing different values, we can plan the flight path. For example, if we need to reach the destination in the fastest time, then we can change the time-related variables; if we want the minimum fuel consumption, we can change the fuel-related variables. In this way, the computer will find the most suitable flight path through the pre-set code. I think such a program is very useful. In real life, all the factors can be transferred to variables in the code to realize that the aircraft can cruise automatically according to the planned route. At the same time, we can also use such a program to predict the flight time, flight fuel consumption, etc. to determine the future flight route. I believe that such a program has already been applied to our actual aircraft. To a certain extent, it guarantees the safety of passengers and can also reduce the cost of airlines.

[Reflective Essay - Fu, Chenlei.pdf](https://github.com/EnvironmentCommittee/AAE-group-1/files/7492204/Reflective.Essay.-.Fu.Chenlei.pdf)

### References
