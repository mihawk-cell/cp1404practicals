from prac_07.project import Project
FILENAME = 'projects.txt'

def main():
    MENU = "(L)oad projects \n(S)ave projects\n(D)isplay projects\n(F)ilter projects by date" +\
           "(A)dd new project\n(U)pdate project\n(Q)uit "

    projects = get_file(FILENAME)
    # print(projects)
    print(f"Welcome to Pythonic Project Management\nLoaded {len(projects)} projects from {FILENAME}")
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            projects = load_data(projects)
        elif choice == "S":
            save_data(projects)
        elif choice == "D":
            display_project(projects)
        elif choice == "F":
            projects = filter_project(projects)
        elif choice == "A":
            add_project(projects)
        elif choice == "U":
            projects = update_project(projects)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you for using custom-built project management software.")


def display_project(projects):
    """Display each project details according to incomplete"""
    complete_project, incomplete_project = check_project(projects)
    print('Incomplete projects: ')
    display_project_details(incomplete_project)
    # print("")
    print('Completed projects: ')
    display_project_details(complete_project)


def display_project_details(projects):
    """display project details"""
    for number, project in enumerate(projects):
        print(f'  {project}')


def update_project(projects):
    """Update project completion percentage and priority"""
    projects = sort_projects(projects)
    display_project_details(projects)
    projects_number = {}
    for number, project in enumerate(projects):
        projects_number[str(number + 1)] = project
        # print(projects_number)
    try:
        choice = input('Project choice: ')
        chosen_project = projects_number[choice]
        print(chosen_project)
        new_percentage = input('New Percentage: ')
        new_priority = input('New Priority: ')

        if new_percentage != '':
            chosen_project.update_percentage(int(new_percentage))

        if new_priority != '':
            chosen_project.update_priority(int(new_priority))

    except KeyError:
        print('Invalid Choice')
    return projects


def add_project(projects):
    """Add new project details."""
    print('Lets add a new project')
    try:
        name = input('Name: ')
        start_date = input('Start date (dd/mm/yy): ')
        priority = int(input('Priority: '))
        cost = input('Cost estimate: ')
        cost = cost.replace('$', '')
        cost = int(cost)
        completion = input('Percent complete: ')
        project = Project(str(name)), str(start_date), int(priority)
        projects.append(project)
    except ValueError:
        print('Invalid Input')


def filter_project(projects):
    """Display project that start after user input date."""
    is_valid = False
    while not is_valid:
        try:
            date = input('Show projects that start after date')
            filtered_projects_date = []
            for project in projects:
                if project.compared_date(date):
                    filtered_projects_date.append(project)
            # print(filtered_data_projects)
            projects = sort_projects(filtered_projects_date)
            display_project_details(projects)
            is_valid = True
        except ValueError:
            print("Incorrect data format, should be dd/mm/yyyy")
            data = input('Show projects that start after date (dd/mm/yyyy):')



def save_data(projects):
    """Save projects to user input filename."""
    filename = input('Enter filename to be save: ')
    save_file(projects, filename)


def load_data(projects):
    """Load projects from user input filename"""
    filename = input("Enter filename: ")
    if filename != '':
        try:
            projects = get_file(filename)
            print(projects)
        except FileNotFoundError:
            print('Invalid Filename')
    return projects


def sort_projects(projects):
    """sort according to the project date"""
    date_list = []
    # print(projects)
    for project in projects:
        if project.start_date not in date_list:
            date_list.append(project.start_date)
    # print(data_list)
    date_list.sort()
    # print(date_list)
    sorted_project = []
    for date in date_list:
        for project in projects:
            if project.start_date == date:
                sorted_project.append(project)
    # print(sorted_project)
    return sorted_project


def get_file(filename):
    """Load projects from default file."""
    projects = []
    # Open the file for reading
    in_file = open(filename, 'r')
    # print(in_file.read())
    # File format is like: Guitar, name, year, price
    # 'Consume' the first line (header) - we don't need its '
    in_file.readline()
    # All other lines are language data
    for line in in_file:
        # print(repr(line)) #debugging
        # Strip newline from end and split it into parts by
        parts = line.strip().replace("\t", ",")
        parts = parts.split(",")
        # print(parts)  #debugging
        # Construct a project object using the elements
        project = Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4]))
        # Add the project we've just constructed to the list
        projects.append(project)
    # Close the file as soon as we've finished reading it
    in_file.close()
    return projects


def save_file(projects, filename):
    """save the data to the file as csv mode"""
    with open(filename, "w") as out_file:
        for project in projects:
            # print(project, file=out_file)
            print(f"{project.name}\t{project.start_date}\t{project}"
                  "file=out_file")


def check_project(projects):
    """split the project into completed and incomplete project"""
    complete_project = []
    incomplete_project = []
    for project in projects:
        if project.is_complete():
            complete_project.append(project)
            complete_project.sort()
        else:
            incomplete_project.append(project)
            incomplete_project.sort()
    return complete_project, incomplete_project

if __name__ == "__main__":
    main()


