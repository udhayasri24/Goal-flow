
import tkinter as tk
from tkinter import messagebox, simpledialog

class CareerPatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Career Pather - Goal Oriented Planner")
        self.root.geometry("600x400")

        self.goals = {}  # Dictionary to hold goals and their tasks

        # UI Elements
        self.title_label = tk.Label(root, text="Career Pather", font=("Helvetica", 20, "bold"))
        self.title_label.pack(pady=10)

        self.goal_listbox = tk.Listbox(root, width=40, height=10)
        self.goal_listbox.pack(side=tk.LEFT, padx=10, pady=10)
        self.goal_listbox.bind('<<ListboxSelect>>', self.show_tasks)

        # Frame for tasks and buttons
        self.right_frame = tk.Frame(root)
        self.right_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.tasks_label = tk.Label(self.right_frame, text="Tasks for Selected Goal", font=("Helvetica", 14))
        self.tasks_label.pack(pady=5)

        self.task_listbox = tk.Listbox(self.right_frame, width=40, height=10)
        self.task_listbox.pack(pady=5)

        # Buttons for Goals
        self.goal_button_frame = tk.Frame(root)
        self.goal_button_frame.pack(side=tk.BOTTOM, pady=10)

        self.add_goal_btn = tk.Button(self.goal_button_frame, text="Add Goal", command=self.add_goal)
        self.add_goal_btn.pack(side=tk.LEFT, padx=5)

        self.delete_goal_btn = tk.Button(self.goal_button_frame, text="Delete Goal", command=self.delete_goal)
        self.delete_goal_btn.pack(side=tk.LEFT, padx=5)

        # Buttons for Tasks
        self.task_button_frame = tk.Frame(self.right_frame)
        self.task_button_frame.pack(pady=10)

        self.add_task_btn = tk.Button(self.task_button_frame, text="Add Task", command=self.add_task)
        self.add_task_btn.pack(side=tk.LEFT, padx=5)

        self.delete_task_btn = tk.Button(self.task_button_frame, text="Delete Task", command=self.delete_task)
        self.delete_task_btn.pack(side=tk.LEFT, padx=5)

    def add_goal(self):
        goal = simpledialog.askstring("Add Goal", "Enter your career goal:")
        if goal:
            if goal in self.goals:
                messagebox.showwarning("Duplicate Goal", "This goal already exists!")
            else:
                self.goals[goal] = []
                self.goal_listbox.insert(tk.END, goal)

    def delete_goal(self):
        selected_idx = self.goal_listbox.curselection()
        if not selected_idx:
            messagebox.showwarning("No Selection", "Please select a goal to delete.")
            return
        goal = self.goal_listbox.get(selected_idx)
        confirm = messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete the goal:\n'{goal}'?")
        if confirm:
            self.goal_listbox.delete(selected_idx)
            del self.goals[goal]
            self.task_listbox.delete(0, tk.END)

    def add_task(self):
        selected_idx = self.goal_listbox.curselection()
        if not selected_idx:
            messagebox.showwarning("No Goal Selected", "Please select a goal first.")
            return
        task = simpledialog.askstring("Add Task", "Enter a task/step for this goal:")
        if task:
            goal = self.goal_listbox.get(selected_idx)
            self.goals[goal].append(task)
            self.task_listbox.insert(tk.END, task)

    def delete_task(self):
        selected_goal_idx = self.goal_listbox.curselection()
        selected_task_idx = self.task_listbox.curselection()
        if not selected_goal_idx or not selected_task_idx:
            messagebox.showwarning("No Selection", "Please select a task to delete.")
            return
        goal = self.goal_listbox.get(selected_goal_idx)
        task = self.task_listbox.get(selected_task_idx)
        confirm = messagebox.askyesno("Confirm Delete", f"Delete task:\n'{task}'?")
        if confirm:
            self.task_listbox.delete(selected_task_idx)
            self.goals[goal].remove(task)

    def show_tasks(self, event):
        self.task_listbox.delete(0, tk.END)
        selected_idx = self.goal_listbox.curselection()
        if selected_idx:
            goal = self.goal_listbox.get(selected_idx)
            tasks = self.goals.get(goal, [])
            for task in tasks:
                self.task_listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = CareerPatherApp(root)
    root.mainloop()
