# Course Record Manager

A Python-based course management system that allows users to:
- Add courses with their name, grade, and credits.
- Retrieve course data for a specific course.
- Display statistics, including the number of completed courses, total credits, mean grade, and grade distribution.

This project demonstrates object-oriented programming principles and basic command-line interaction.

---

## Features

1. **Add Courses**:
   - Add a course with its name, grade, and credits.
   - Grades can only be updated if the new grade is higher than the current grade.
   - Each course name results in a single entry in the records.

2. **Retrieve Course Data**:
   - View details of a specific course, including its name, credits, and grade.

3. **View Statistics**:
   - Display the number of completed courses, total credits, mean grade, and grade distribution.

4. **Grade Distribution**:
   - Shows the distribution of grades in the format:
     ```
     grade distribution
     5: xx
     4: x
     3:
     2: x
     1: x
     ```

---


## Installation

1. **Clone the repository**:
   ```sh
   git clone https://github.com/keedcode/course-record-manager.git
   cd course-record-manager

## Example Usage

```plaintext
1 add course
2 get course data
3 statistics
0 exit

command: 1
course: ItP
grade: 3
credits: 5

command: 2
course: ItP
ItP (5 cr) grade 3

command: 1
course: ItP
grade: 5
credits: 5

command: 2
course: ItP
ItP (5 cr) grade 5

command: 1
course: ItP
grade: 1
credits: 5

command: 2
course: ItP
ItP (5 cr) grade 5

command: 3
5 completed courses, a total of 29 credits
mean 3.4
grade distribution
5: xx
4: x
3:
2: x
1: x

command: 0



