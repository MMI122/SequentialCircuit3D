import tkinter as tk
from tkinter import ttk
import math


class StateMachineGUI(tk.Tk):
    def _init_(self):
        super()._init_()
        self.title("State Machine Simulation with 3 Variables (2107118 - Adit Mugdha Das)")
        self.geometry("1000x850")  # Increased height for truth table visibility
        self.configure(bg="#f5f5f5")

        # Variables for state tracking
        self.current_state = (0, 0, 0)
        self.next_state = (0, 0, 0)

        # Create a styled frame for inputs
        input_frame = tk.LabelFrame(self, text="Input Values", font=("Arial", 12, "bold"), bg="#ffffff", padx=10, pady=10)
        input_frame.pack(pady=10)

        # Input labels and dropdowns
        tk.Label(input_frame, text="A:", font=("Arial", 10), bg="#ffffff").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.comboA = ttk.Combobox(input_frame, values=["0", "1"], state="readonly", width=5)
        self.comboA.set("0")
        self.comboA.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(input_frame, text="B:", font=("Arial", 10), bg="#ffffff").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.comboB = ttk.Combobox(input_frame, values=["0", "1"], state="readonly", width=5)
        self.comboB.set("0")
        self.comboB.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(input_frame, text="C:", font=("Arial", 10), bg="#ffffff").grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.comboC = ttk.Combobox(input_frame, values=["0", "1"], state="readonly", width=5)
        self.comboC.set("0")
        self.comboC.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(input_frame, text="X:", font=("Arial", 10), bg="#ffffff").grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.comboX = ttk.Combobox(input_frame, values=["0", "1"], state="readonly", width=5)
        self.comboX.set("0")
        self.comboX.grid(row=3, column=1, padx=10, pady=5)

        # Compute button
        compute_button = tk.Button(self, text="Compute Next State & Output", font=("Arial", 12, "bold"),
                                   bg="#4caf50", fg="white", activebackground="#45a049", command=self.compute_next_state)
        compute_button.pack(pady=10)

        # Result display
        self.result_label = tk.Label(self, text="Result will appear here", font=("Arial", 12), bg="#f5f5f5", fg="#333333")
        self.result_label.pack(pady=10)

        # Canvas for state diagram
        self.diagram_canvas = tk.Canvas(self, width=750, height=400, bg="#ffffff", highlightthickness=1, highlightbackground="#cccccc")
        self.diagram_canvas.pack(pady=10)

        # Truth table
        table_frame = tk.LabelFrame(self, text="Truth Table", font=("Arial", 12, "bold"), bg="#ffffff", padx=10, pady=10)
        table_frame.pack(pady=10, fill=tk.BOTH, expand=True)

        self.truth_table = ttk.Treeview(table_frame, columns=("A", "B", "C", "X", "A(t+1)", "B(t+1)", "C(t+1)", "Y"), show="headings", height=10)
        self.truth_table.pack(pady=10, fill=tk.BOTH, expand=True)

        # Define column headings
        for col in self.truth_table["columns"]:
            self.truth_table.heading(col, text=col)
            self.truth_table.column(col, width=100, anchor="center")

        # Draw the initial state diagram and populate the truth table
        self.draw_state_diagram()
        self.populate_truth_table()

    def compute_next_state(self):
        # Get the inputs as integers
        A = int(self.comboA.get())
        B = int(self.comboB.get())
        C = int(self.comboC.get())
        X = int(self.comboX.get())

        # Convert to boolean for easier logic handling
        a = (A == 1)
        b = (B == 1)
        c = (C == 1)
        x = (X == 1)

        # Compute A(t+1), B(t+1), C(t+1) using Boolean algebra
        a_next = (a and b) or (c and not x)
        b_next = (not a and c) or (b and x)
        c_next = (a and not b) or (c and not x)

        # Y = A∧B∧C∧X (example logic)
        y = a and b and c and x

        # Convert booleans back to ints
        A_next = 1 if a_next else 0
        B_next = 1 if b_next else 0
        C_next = 1 if c_next else 0
        Y = 1 if y else 0

        # Update the current and next states
        self.current_state = (A, B, C)
        self.next_state = (A_next, B_next, C_next)

        # Update the result label
        self.result_label.config(
            text=f"A(t+1) = {A_next}, B(t+1) = {B_next}, C(t+1) = {C_next}, Y = {Y}",
            font=("Arial", 14, "bold"),
            fg="#4caf50"
        )

        # Redraw the state diagram with the updated states
        self.draw_state_diagram()

    def populate_truth_table(self):
        # Clear the table
        for item in self.truth_table.get_children():
            self.truth_table.delete(item)

        # Generate truth table rows
        for A in [0, 1]:
            for B in [0, 1]:
                for C in [0, 1]:
                    for X in [0, 1]:
                        a = (A == 1)
                        b = (B == 1)
                        c = (C == 1)
                        x = (X == 1)

                        # Compute next state and output
                        a_next = (a and b) or (c and not x)
                        b_next = (not a and c) or (b and x)
                        c_next = (a and not b) or (c and not x)
                        y = a and b and c and x

                        # Convert booleans to integers
                        A_next = 1 if a_next else 0
                        B_next = 1 if b_next else 0
                        C_next = 1 if c_next else 0
                        Y = 1 if y else 0

                        # Add row to the table
                        self.truth_table.insert("", "end", values=(A, B, C, X, A_next, B_next, C_next, Y))

    def draw_state_diagram(self):
        # Clear the canvas
        self.diagram_canvas.delete("all")

        # Define center and radius for circular layout
        canvas_center = (375, 200)
        radius = 150

        # Define the states in order
        states = [
            (0, 0, 0),
            (0, 0, 1),
            (0, 1, 0),
            (0, 1, 1),
            (1, 0, 0),
            (1, 0, 1),
            (1, 1, 0),
            (1, 1, 1),
        ]

        # Calculate positions in a circular layout
        state_positions = {}
        for i, state in enumerate(states):
            angle = 2 * math.pi * i / len(states)
            x = canvas_center[0] + radius * math.cos(angle)
            y = canvas_center[1] + radius * math.sin(angle)
            state_positions[state] = (x, y)

        # Draw the states as circles
        for state, pos in state_positions.items():
            x, y = pos
            color = "#32CD32" if state == self.current_state else "#D3D3D3"
            outline = "orange" if state == self.next_state else "black"
            self.diagram_canvas.create_oval(x - 25, y - 25, x + 25, y + 25, fill=color, outline=outline, width=2)
            self.diagram_canvas.create_text(x, y, text=f"{state}", font=("Arial", 10, "bold"))

        # Draw arrows for state transitions
        if self.current_state in state_positions and self.next_state in state_positions:
            current_pos = state_positions[self.current_state]
            next_pos = state_positions[self.next_state]
            self.diagram_canvas.create_line(
                current_pos[0], current_pos[1], next_pos[0], next_pos[1], arrow=tk.LAST, width=2, fill="blue"
            )


if _name_ == "_main_":
    app = StateMachineGUI()
    app.mainloop()