#ROBOT SQQUAD MANAGER
## Ishat Noor Mahi - STA-34
#robosust_final_project

robots = []
def deploy_robot(robot_squad):

    while True:
        name = input("Enter Robot Name: ").strip().capitalize()
        type = input("Enter Robot Type: ").strip().capitalize()
        status = 'idle'
        capabilities = []
        while True:
            new_c = input("Type Capability & Hit Enter | Type 'done' to finish: ").strip().lower()
            if new_c == "done":
                break
            else:
                capabilities.append(new_c.capitalize()) 
        
        robot = {
            'Name': name,
            'Type': type,
            'capabilities':capabilities,
            'status':status,
        }
        robots.append(robot)
        print("=====================\nRobot Registered!\n=====================")
        
        add_more = input("Do you want to add more robots? (yes/no): ").strip().lower()
        if add_more != 'yes':
            break


def view_all_robots(robot_squad):

    if len(robot_squad)==0:
        print("No robots are currently deployed")
    else:
        for robot in robot_squad:
            print(f"Name: {robot['Name']} | Type: {robot['Type']} | Status: {robot['status']}")
    print("=================================")

# view_all_robots(robots)

def view_robot_details(robot_squad):
    name = input("Robot Name: ").strip().capitalize()

    for robot in robot_squad:
        if robot["Name"]== name:
            return robot
                  
    return "Robot Not Found"


def assign_task(robot_squad):
    name = input("Robot Name: ").strip().capitalize()
    for robot in robot_squad:
        if robot["Name"]== name:
            cap = input("Add task: ")
            robot["capabilities"].append(cap)
            return robot_squad
        else:
            return "Not found"

def decommission_robot(robot_squad):
    name = input("Robot Name: ").strip().capitalize()
    
    for robot in robot_squad:
        
        if robot["Name"]== name:
            robot_squad.remove(robot)
            return f"Robot {name} Decommissioned"
        else:
            return "Robot Not found"

def initialize():

    while True:
        print("\n========== ROBOT SQUAD MANAGER ==========")
        print("1 ➡ Deploy robot\n2 ➡ View all robots\n3 ➡ View robot details\n4 ➡ assign Task to robot\n5 ➡ Decommission a robot\n0 ➡ Exit")

        user_response = int(input("Choose An Option: "))

        if user_response == 1:
            print("==========Deploying Robot...==========")
            deploy_robot(robots)
        elif user_response == 2:
            print("==========Viewing All Robots...==========")
            view_all_robots(robots)
        elif user_response == 3:
            print("==========Viewing Robot Details...==========")
            print(view_robot_details(robots))
        elif user_response == 4:
            print("==========Assigning Task to Robot...==========")
            print(assign_task(robots))
        elif user_response == 5:
            print("==========Decommissioning Robot...==========")
            print(decommission_robot(robots))
        elif user_response == 0:
            print("Exiting Program...")
            break
        else:
            print("Invalid Option")

initialize()