class CourseEntry:
    """
    Represents a single course entry with attributes for course name, grade, and credits.

    Attributes:
        __course_name (str): The name of the course.
        __course_grade (str): The grade for the course (default is "0").
        __course_credit (str): The credits for the course (default is "0").
    """

    def __init__(self, course_name: str):
        """
        Initializes a new CourseEntry object.

        Args:
            course_name (str): The name of the course.
        """
        self.__course_name = course_name
        self.__course_grade = "0"
        self.__course_credit = "0"

    def course_name(self) -> str:
        """
        Returns the name of the course.

        Returns:
            str: The course name.
        """
        return self.__course_name

    def course_grade(self) -> str:
        """
        Returns the grade of the course.

        Returns:
            str: The course grade.
        """
        return self.__course_grade

    def course_credit(self) -> str:
        """
        Returns the credits of the course.

        Returns:
            str: The course credits.
        """
        return self.__course_credit

    def add_course_grade(self, course_grade: str) -> None:
        """
        Updates the course grade if the new grade is higher than the current grade.

        Args:
            course_grade (str): The new grade for the course.
        """
        if int(self.__course_grade) < int(course_grade) <= 5:
            self.__course_grade = course_grade

    def add_course_credit(self, course_credit: str) -> None:
        """
        Updates the course credits.

        Args:
            course_credit (str): The new credits for the course.
        """
        self.__course_credit = course_credit

    def __str__(self) -> str:
        """
        Returns a string representation of the course entry.

        Returns:
            str: A formatted string with course name, credits, and grade.
        """
        return f"{self.__course_name} ({self.__course_credit} cr) grade {self.__course_grade}"


class CourseRecord:
    """
    Manages a collection of course entries, allowing for adding courses, retrieving course data,
    and calculating statistics such as grade distribution and mean grade.

    Attributes:
        __course_record (dict): A dictionary mapping course names to CourseEntry objects.
    """

    def __init__(self):
        """
        Initializes a new CourseRecord object.
        """
        self.__course_record = {}

    def add_course_entry(self, course_name: str, course_grade: str, course_credit: str) -> None:
        """
        Adds a new course entry or updates an existing one.

        Args:
            course_name (str): The name of the course.
            course_grade (str): The grade for the course.
            course_credit (str): The credits for the course.
        """
        if not course_name in self.__course_record:
            # Create a new course entry if it doesn't exist
            self.__course_record[course_name] = CourseEntry(course_name)
        # Update the grade and credits for the course
        current_course = self.__course_record[course_name]
        current_course.add_course_grade(course_grade)
        current_course.add_course_credit(course_credit)

    def get_course_data(self, course_name: str):
        """
        Retrieves the course data for a given course name.

        Args:
            course_name (str): The name of the course.

        Returns:
            CourseEntry or None: The CourseEntry object if the course exists, otherwise None.
        """
        if course_name not in self.__course_record:
            return None
        return self.__course_record[course_name]

    def __grade_distribution(self) -> None:
        """
        Prints the grade distribution for all courses.
        """
        print("grade distribution")
        distribution = {5: 0, 4: 0, 3: 0, 2: 0, 1: 0}
        for course in self.__course_record.values():
            grade = int(course.course_grade())
            if grade in distribution:
                distribution[grade] += 1

        for grade in sorted(distribution.keys(), reverse=True):
            print(f"{grade}: {'x' * distribution[grade]}")

    def get_course_statistics(self) -> None:
        """
        Prints statistics for all courses, including the number of completed courses,
        total credits, mean grade, and grade distribution.
        """
        try:
            number_of_courses_completed = len(self.__course_record)
            total_credits = sum(int(course.course_credit()) for course in self.__course_record.values())
            total_grades = sum(int(course.course_grade()) for course in self.__course_record.values())
            mean = total_grades / number_of_courses_completed

            print(f"{number_of_courses_completed} completed courses, a total of {total_credits} credits")
            print(f"mean {mean:.1f}")
            self.__grade_distribution()
        except ZeroDivisionError:
            print("number of courses completed cannot be less than 1")


class CourseRecordApp:
    """
    Provides the user interface for interacting with the course record system.

    Attributes:
        __course_record (CourseRecord): The CourseRecord object managing the courses.
    """

    def __init__(self):
        """
        Initializes a new CourseRecordApp object.
        """
        self.__course_record = CourseRecord()

    def help(self) -> None:
        """
        Displays the command menu for the application.
        """
        print("1 add course")
        print("2 get course data")
        print("3 statistics")
        print("0 exit")

    def run(self) -> None:
        """
        Runs the application, allowing users to interact with the system through commands.
        """
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command in ("1230"):
                if command == "1":
                    # Add a new course
                    course_name = input("course: ")
                    course_grade = input("grade: ")
                    course_credit = input("credits: ")
                    self.__course_record.add_course_entry(course_name, course_grade, course_credit)
                elif command == "2":
                    # Retrieve course data
                    course_name = input("course: ")
                    search = self.__course_record.get_course_data(course_name)
                    if search is None:
                        print("no entry for this course")
                    else:
                        print(search)
                elif command == "3":
                    # Display course statistics
                    self.__course_record.get_course_statistics()
                elif command == "0":
                    # Exit the application
                    return
            else:
                self.help()


# Entry point for the application
application = CourseRecordApp()
application.run()