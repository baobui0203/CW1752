import tkinter as tk
import tkinter.scrolledtext as tkst


import video_library as lib
import font_manager as fonts


def set_text(text_area, content):
    # Deletes all text from the given text_area from the start (1.0) to the end (tk.END)
    text_area.delete("1.0", tk.END)
    # Inserts the given content into the text_area at the beginning (1.0)
    text_area.insert(1.0, content)


class CheckVideos():
    def __init__(self, window):
        # Sets the size of the window to 750x350 pixels
        window.geometry("750x350")
        # Sets the title of the window to "Check Videos"
        window.title("Check Videos")
        # Creates a button to list all videos and assigns its callback method
        list_videos_btn = tk.Button(
            window, text="List All Videos", command=self.list_videos_clicked)
        # Places the button in the grid layout at row 0, column 0 with padding
        list_videos_btn.grid(row=0, column=0, padx=10, pady=10)
        # Creates a label prompting the user to enter a video number
        enter_lbl = tk.Label(window, text="Enter Video Number")
        # Places the label in the grid layout at row 0, column 1 with padding
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)
        # Creates an entry widget in the grid layout at row 0, column 2 with padding
        self.input_txt = tk.Entry(window, width=3)
        self.input_txt.grid(row=0, column=2, padx=10, pady=10)
        # Creates a button to check the video and assigns its callback method
        check_video_btn = tk.Button(
            window, text="Check Video", command=self.check_video_clicked)
        check_video_btn.grid(row=0, column=3, padx=10, pady=10)
        # Creates a ScrolledText widget to list videos, in the grid at row 1, column 0, spanning 3 columns
        self.list_txt = tkst.ScrolledText(
            window, width=48, height=12, wrap="none")
        self.list_txt.grid(row=1, column=0, columnspan=3,
                           sticky="W", padx=10, pady=10)
        # Creates a Text widget to show video details, in the grid at row 1, column 3
        self.video_txt = tk.Text(window, width=24, height=4, wrap="none")
        self.video_txt.grid(row=1, column=3, sticky="NW", padx=10, pady=10)
        # Creates a label to show the status, in the grid at row 2, spanning 4 columns
        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=2, column=0, columnspan=4,
                             sticky="W", padx=10, pady=10)
        # Calls the method to list all videos initially
        self.list_videos_clicked()

    def check_video_clicked(self):
        # Gets the video number entered by the user
        key = self.input_txt.get()
        # Retrieves the video name from the library using the entered key
        name = lib.get_name(key)
        if name is not None:
            # Retrieves the director, rating, and play count of the video
            director = lib.get_director(key)
            rating = lib.get_rating(key)
            play_count = lib.get_play_count(key)
            # Creates a string with video details
            video_details = f"{name}\n{director}\nrating: {rating}\nplays: {play_count}"
            # Sets the video details in the video_txt Text widget
            set_text(self.video_txt, video_details)
        else:
            # Sets a not found message if the video does not exist
            set_text(self.video_txt, f"Video {key} not found")
        # Updates the status label to indicate the button was clicked
        self.status_lbl.configure(text="Check Video button was clicked!")

    def list_videos_clicked(self):
        # Retrieves a list of all videos from the library
        video_list = lib.list_all()
        # Sets the video list in the list_txt ScrolledText widget
        set_text(self.list_txt, video_list)
        # Updates the status label to indicate the button was clicked
        self.status_lbl.configure(text="List Videos button was clicked!")


if __name__ == "__main__":
    # Only runs when this file is run as a standalone script
    window = tk.Tk()        # Creates a Tkinter window
    fonts.configure()       # Configures the fonts (assuming this is a predefined function)
    CheckVideos(window)     # Creates an instance of the CheckVideos class
    window.mainloop()       # Starts the Tkinter main event loop
