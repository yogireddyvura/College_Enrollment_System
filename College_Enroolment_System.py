import tkinter as tk
from tkinter import messagebox, simpledialog

class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number
        self.courses = []

    def __str__(self):
        courses_str = ', '.join(self.courses) if self.courses else "No courses assigned"
        return f"Name: {self.name}, Roll Number: {self.roll_number}, Courses: {courses_str}"

class CollegeEnrollmentSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("College Enrollment System")
        self.students = {}

        # Create UI components
        self.create_widgets()

    def create_widgets(self):
        # Labels
        tk.Label(self.root, text="Student Name:").grid(row=0, column=0)
        tk.Label(self.root, text="Roll Number:").grid(row=1, column=0)

        # Entry fields
        self.name_entry = tk.Entry(self.root)
        self.name_entry.grid(row=0, column=1)

        self.roll_number_entry = tk.Entry(self.root)
        self.roll_number_entry.grid(row=1, column=1)

        # Buttons
        self.enroll_button = tk.Button(self.root, text="Enroll Student", command=self.enroll_student)
        self.enroll_button.grid(row=2, column=0)

        self.view_button = tk.Button(self.root, text="View Student Details", command=self.view_student)
        self.view_button.grid(row=2, column=1)

        self.assign_courses_button = tk.Button(self.root, text="Assign Courses", command=self.assign_courses)
        self.assign_courses_button.grid(row=3, column=0)

        self.view_all_button = tk.Button(self.root, text="View All Students", command=self.view_all_students)
        self.view_all_button.grid(row=3, column=1)

    def enroll_student(self):
        name = self.name_entry.get()
        roll_number = self.roll_number_entry.get()

        if roll_number in self.students:
            messagebox.showerror("Error", "Roll number already exists. Please use a unique roll number.")
        else:
            self.students[roll_number] = Student(name, roll_number)
            messagebox.showinfo("Success", "Student enrolled successfully!")
            self.clear_entries()

    def view_student(self):
        roll_number = self.roll_number_entry.get()
        if roll_number in self.students:
            messagebox.showinfo("Student Details", str(self.students[roll_number]))
        else:
            messagebox.showerror("Error", "Student not found.")

    def assign_courses(self):
        roll_number = self.roll_number_entry.get()
        if roll_number in self.students:
            courses = simpledialog.askstring("Assign Courses", "Enter Courses (comma-separated):")
            if courses:
                courses_list = [course.strip() for course in courses.split(',')]
                self.students[roll_number].courses.extend(courses_list)
                messagebox.showinfo("Success", "Courses assigned successfully!")
        else:
            messagebox.showerror("Error", "Student not found.")

    def view_all_students(self):
        if not self.students:
            messagebox.showinfo("Students", "No students enrolled.")
            return
        records = "\n".join([str(student) for student in self.students.values()])
        messagebox.showinfo("All Students", records)

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.roll_number_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = CollegeEnrollmentSystem(root)
    root.mainloop()