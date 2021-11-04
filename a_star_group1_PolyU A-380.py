"""

A380 grid planning

"""

import math
import matplotlib.pyplot as plt

show_animation = True

class AStarPlanner:

    def __init__(self, ox, oy, resolution, rr, fc_x, fc_y, tc_x, tc_y, lc_x, lc_y):
        """
        Initialize grid map for a star planning

        ox: x position list of Obstacles [m]
        oy: y position list of Obstacles [m]
        resolution: grid resolution [m]
        rr: robot radius[m]
        """

        self.resolution = resolution 
        self.rr = rr 
        self.min_x, self.min_y = 0, 0
        self.max_x, self.max_y = 0, 0
        self.obstacle_map = None
        self.x_width, self.y_width = 0, 0
        self.motion = self.get_motion_model() 
        self.calc_obstacle_map(ox, oy)

        self.fc_x = fc_x
        self.fc_y = fc_y
        self.tc_x = tc_x
        self.tc_y = tc_y
        self.lc_x = lc_x
        self.lc_y = lc_y

        self.C_F = 1
        self.Delta_F = 1
        self.C_T = 2
        self.Delta_T = 5
        self.C_C = 10
        self.C_L = 0.5
        self.Delta_L = 1
        
        self.Delta_F_A = 0.2 
        self.Delta_T_A = 0.2 
        self.Delta_L_A = -0.2
        
        self.costPerGrid = self.C_F * self.Delta_F + self.C_T * self.Delta_T + self.C_C

        print("PolyU-A380 cost part1-> ", self.C_F * (self.Delta_F + self.Delta_F_A) )
        print("PolyU-A380 cost part2-> ", self.C_T * (self.Delta_T + self.Delta_T_A) )
        print("PolyU-A380 cost part3-> ", self.C_C )
        print("Polyu-A380 cost part4-> ", self.C_L * self.Delta_L_A)

    class Node: 
        def __init__(self, x, y, cost, parent_index):
            self.x = x 
            self.y = y  
            self.cost = cost
            self.parent_index = parent_index

        def __str__(self):
            return str(self.x) + "," + str(self.y) + "," + str(self.cost) + "," + str(self.parent_index)

        def planning(self, sx, sy, gx, gy):
        """
        A star path search

        input:
            s_x: start x position [m]
            s_y: start y position [m]
            gx: goal x position [m]
            gy: goal y position [m]

        output:
            rx: x position list of the final path
            ry: y position list of the final path
        """

        start_node = self.Node(self.calc_xy_index(sx, self.min_x), self.calc_xy_index(sy, self.min_y), 0.0, -1)
        goal_node = self.Node(self.calc_xy_index(gx, self.min_x), self.calc_xy_index(gy, self.min_y), 0.0, -1)
        open_set, closed_set = dict(), dict() 
        open_set[self.calc_grid_index(start_node)] = start_node 

        while 1:
            if len(open_set) == 0:
                print("Open set is empty..")
                break

            c_id = min(open_set,key=lambda o: open_set[o].cost + self.calc_heuristic(self, goal_node,open_set[o])) 
            current = open_set[c_id]

            if show_animation:  
                plt.plot(self.calc_grid_position(current.x, self.min_x),self.calc_grid_position(current.y, self.min_y), "xc")
                plt.gcf().canvas.mpl_connect('key_release_event',lambda event: [exit(0) if event.key == 'escape' else None])
                
                if len(closed_set.keys()) % 10 == 0:
                    plt.pause(0.001)

                if current.x == goal_node.x and current.y == goal_node.y:
                print("Find goal with cost of -> ",current.cost )
                goal_node.parent_index = current.parent_index
                goal_node.cost = current.cost
                break

            del open_set[c_id]

            closed_set[c_id] = current

            for i, _ in enumerate(self.motion): # tranverse the motion matrix
                node = self.Node(current.x + self.motion[i][0],current.y + self.motion[i][1],current.cost + self.motion[i][2] * self.costPerGrid, c_id)
                
                if self.calc_grid_position(node.x, self.min_x) in self.tc_x:
                    if self.calc_grid_position(node.y, self.min_y) in self.tc_y:
                        node.cost = node.cost + self.Delta_T_A * self.motion[i][2]
                
                    if self.calc_grid_position(node.x, self.min_x) in self.fc_x:
                    if self.calc_grid_position(node.y, self.min_y) in self.fc_y:
                        node.cost = node.cost + self.Delta_F_A * self.motion[i][2]
              
                if self.calc_grid_position(node.x, self.min_x) in self.lc_x:
                    if self.calc_grid_position(node.y, self.min_y) in self.lc_y:
                       node.cost = node.cost + self.Delta_L_A * self.motion[i][2]
                        
                n_id = self.calc_grid_index(node)

                if not self.verify_node(node):
                    continue

                if n_id in closed_set:
                    continue

                if n_id not in open_set:
                    open_set[n_id] = node  
                else:
                    if open_set[n_id].cost > node.cost:
                       open_set[n_id] = node

        rx, ry = self.calc_final_path(goal_node, closed_set)
        
        return rx, ry

    def calc_final_path(self, goal_node, closed_set):
       rx, ry = [self.calc_grid_position(goal_node.x, self.min_x)], [self.calc_grid_position(goal_node.y, self.min_y)] 
        parent_index = goal_node.parent_index
        while parent_index != -1:
            n = closed_set[parent_index]
            rx.append(self.calc_grid_position(n.x, self.min_x))
            ry.append(self.calc_grid_position(n.y, self.min_y))
            parent_index = n.parent_index

        return rx, ry

    def calc_heuristic(self, n1, n2):
        w = 1.0  
        d = w * math.hypot(n1.x - n2.x, n1.y - n2.y)
        d = d * self.costPerGrid
        return d
    
    def calc_heuristic_maldis(n1, n2):
        w = 1.0  
        dx = w * math.abs(n1.x - n2.x)
        dy = w *math.abs(n1.y - n2.y)
        return dx + dy

    def calc_grid_position(self, index, min_position):
        """
        calc grid position

        :param index:
        :param min_position:
        :return:
        """
        pos = index * self.resolution + min_position
        return pos

    def calc_xy_index(self, position, min_pos):
        return round((position - min_pos) / self.resolution)

    def calc_grid_index(self, node):
        return (node.y - self.min_y) * self.x_width + (node.x - self.min_x) 

    def verify_node(self, node):
        px = self.calc_grid_position(node.x, self.min_x)
        py = self.calc_grid_position(node.y, self.min_y)

        if px < self.min_x:
            return False
        elif py < self.min_y:
            return False
        elif px >= self.max_x:
            return False
        elif py >= self.max_y:
            return False

       if self.obstacle_map[node.x][node.y]:
            return False

        return True

    def calc_obstacle_map(self, ox, oy):

        self.min_x = round(min(ox))
        self.min_y = round(min(oy))
        self.max_x = round(max(ox))
        self.max_y = round(max(oy))
        print("min_x:", self.min_x)
        print("min_y:", self.min_y)
        print("max_x:", self.max_x)
        print("max_y:", self.max_y)

        self.x_width = round((self.max_x - self.min_x) / self.resolution)
        self.y_width = round((self.max_y - self.min_y) / self.resolution)
        print("x_width:", self.x_width)
        print("y_width:", self.y_width)

        self.obstacle_map = [[False for _ in range(self.y_width)]
                             for _ in range(self.x_width)] 
        for ix in range(self.x_width):
            x = self.calc_grid_position(ix, self.min_x) 
            for iy in range(self.y_width):
                y = self.calc_grid_position(iy, self.min_y)
                for iox, ioy in zip(ox, oy):  
                    d = math.hypot(iox - x, ioy - y)
                    if d <= self.rr:
                        self.obstacle_map[ix][iy] = True 
                        break

     def get_motion_model(): 
        motion = [[1, 0, 1],[0, 1, 1],[-1, 0, 1],[0, -1, 1],[-1, -1, math.sqrt(2)],[-1, 1, math.sqrt(2)],[1, -1, math.sqrt(2)],[1, 1, math.sqrt(2)]]
        return motion

def main():
    print(__file__ + " start the A star algorithm demo !!") 

    sx = 5  
    sy = 10  
    gx = 45 
    gy = 50  
    grid_size = 1  
    robot_radius = 1.0  

    ox, oy = [], []
    for i in range(-10, 60): 
        ox.append(i)
        oy.append(-10)
    for i in range(-10, 60): 
        ox.append(60.0)
        oy.append(i)
    for i in range(-10, 60): 
        ox.append(i)
        oy.append(60.0)
    for i in range(-10, 60): 
        ox.append(-10.0)
        oy.append(i)

    for i in range(-10, 30): 
        ox.append(20.0)
        oy.append(i)
    for i in range(5,60): 
        ox.append(40)
        oy.append(i)
    for i in range(20,50): 
        ox.append(i)
        oy.append(40)
    for i in range(45,60): 
        ox.append(i)
        oy.append(35)
    for i in range(40,55): 
        ox.append(i)
        oy.append(10)
    for i in range(35,45): 
        ox.append(i)
        oy.append(5)
    
   fc_x, fc_y = [], []
    for i in range(25,40):
        for j in range(5,15):
            fc_x.append(i)
            fc_y.append(j)
    
    tc_x, tc_y = [], []
    for i in range(-5,20):
        for j in range(15,35):
            tc_x.append(i)
            tc_y.append(j)
                
   lc_x, lc_y = [], []

    for i in range(26,30):
        for j in range(26,30):

            lc_x.append(i)

            lc_y.append(j)

    if show_animation:  
        plt.plot(ox, oy, ".k") 
        plt.plot(sx, sy, "8b")  
        plt.plot(gx, gy, "Xb") 
        
        plt.plot(fc_x, fc_y, "oy") 
        plt.plot(tc_x, tc_y, "or") 
        plt.plot(lc_x, lc_y, "Xg")

        plt.grid(True) 
        plt.axis("equal") 

    a_star = AStarPlanner(ox, oy, grid_size, robot_radius, fc_x, fc_y, tc_x, tc_y, lc_x, lc_y)
    rx, ry = a_star.planning(sx, sy, gx, gy)

    if show_animation:  
        plt.plot(rx, ry, "-r") 
        plt.pause(0.001) 
        plt.show() 

if __name__ == '__main__':
    main()
