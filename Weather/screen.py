import tkinter as tk

from Weather import get_data


class Screen:
    BEIGE = "#F3E9D2"
    DARK = "#3D342B"
    BROWN = "#7A5C3E"
    LIGHT_BROWN = "#A98B6F"
    WHITE = "#FFFDF8"
    ERROR = "#FF2C2C"

    def __init__(self):
        self.window = tk.Tk()

        self.setup_window()
        self.create_top_section()
        self.create_weather_section()
        self.create_bottom_section()
        self.setup_bindings()

    def setup_window(self):
        self.window.title("Weather App")
        self.window.geometry("600x800")
        self.window.resizable(False, False)
        self.window.configure(bg=self.BEIGE)

    def create_top_section(self):
        top_frame = tk.Frame(
            self.window,
            bg=self.BEIGE
        )
        top_frame.pack(side="top", pady=50)

        title_label = tk.Label(
            top_frame,
            text="Enter the city name",
            font=("Arial", 26, "bold"),
            fg=self.DARK,
            bg=self.BEIGE
        )
        title_label.pack(pady=(0, 20))

        self.city_entry = tk.Entry(
            top_frame,
            font=("Arial", 18),
            fg=self.DARK,
            bg=self.WHITE,
            insertbackground=self.DARK,
            justify="center",
            relief="flat",
            bd=0,
            width=28
        )
        self.city_entry.pack(ipady=14)

        self.city_entry.focus()

    def create_weather_section(self):
        self.weather_frame = tk.Frame(
            self.window,
            bg=self.BEIGE
        )

        self.weather_label = tk.Label(
            self.weather_frame,
            text="",
            font=("Arial", 24, "bold"),
            fg=self.DARK,
            bg=self.WHITE,
            width=25,
            height=6,
            relief="flat"
        )
        self.weather_label.pack()

        self.clear_button = tk.Button(
            self.weather_frame,
            text="Clear",
            command=self.clear_weather,
            font=("Arial", 12, "bold"),
            fg=self.WHITE,
            bg=self.BROWN,
            activebackground=self.LIGHT_BROWN,
            activeforeground=self.WHITE,
            relief="flat",
            bd=0,
            padx=30,
            pady=10,
            cursor="hand2"
        )

    def create_bottom_section(self):
        bottom_frame = tk.Frame(
            self.window,
            bg=self.BEIGE
        )
        bottom_frame.pack(side="bottom", pady=45)

        enter_label = tk.Label(
            bottom_frame,
            text="Press Enter to show the weather there",
            font=("Arial", 13),
            fg=self.BROWN,
            bg=self.BEIGE
        )
        enter_label.pack(pady=5)

        escape_label = tk.Label(
            bottom_frame,
            text="Press Escape to exit",
            font=("Arial", 12),
            fg=self.LIGHT_BROWN,
            bg=self.BEIGE
        )
        escape_label.pack(pady=5)

    def setup_bindings(self):
        self.window.bind("<Return>", self.show_weather)
        self.window.bind("<Escape>", self.exit_program)

    def show_weather(self, event=None):
        city = self.city_entry.get().strip()

        if not city:
            return

        data = get_data(city)
        print(f"\nrequesting {city} data...\n")
        print("_"*20)

        if data:
            self.display_weather(city, data)
            print(f"\nreceived the data successfully :)\n")
            print("_" * 20)

        else:
            self.show_error()
            print(f"\nSomething went wrong :(\n")
            print("_" * 20)

        self.show_weather_section()

    def display_weather(self, city, data):
        temp = data["main"]["temp"] - 273.15
        description = data["weather"][0]["description"]

        self.weather_label.config(
            text=f"Weather in {city}\n\n"
                 f"{temp:.0f}°C  •  {description}",
            fg=self.DARK
        )

    def show_error(self):
        self.weather_label.config(
            text="Please enter a valid city name",
            fg=self.ERROR
        )

    def show_weather_section(self):
        self.weather_frame.pack(expand=True)
        self.clear_button.pack(pady=(15, 0))

    def clear_weather(self):
        self.weather_frame.pack_forget()

    def exit_program(self, event=None):
        self.window.destroy()

    def run(self):
        self.window.mainloop()