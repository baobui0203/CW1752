import tkinter as tk
import tkinter.scrolledtext as tkst
import video_library as lib
import font_manager as fonts

# Define a class for updating video information

class UpdateVideos:
    def __init__(self, window):
        # Set the window dimensions to 750x350 pixels
        window.geometry("750x350")
        # Set the window title to "Update Videos"
        window.title("Update Videos")

        # Create a button for updating the video rating, linking it to the corresponding method
        update_rating_btn = tk.Button(
            window, text="Update Rating", command=self.update_rating)
        # Position the button in the grid layout at row 0, column 0 with padding
        update_rating_btn.grid(row=0, column=0, padx=10, pady=10)

        # Label prompting the user to input a video number
        enter_lbl = tk.Label(window, text="Enter Video Number")
        # Position the label in the grid at row 0, column 1 with padding
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)

        # Entry widget for the video number
        self.video_number_txt = tk.Entry(window, width=3)
        # Position the entry widget in the grid at row 0, column 2 with padding
        self.video_number_txt.grid(row=0, column=2, padx=10, pady=10)

        # Label prompting the user to input a new rating
        rating_lbl = tk.Label(window, text="Enter New Rating")
        # Position the label in the grid at row 0, column 3 with padding
        rating_lbl.grid(row=0, column=3, padx=10, pady=10)

        # Entry widget for the new rating
        self.rating_txt = tk.Entry(window, width=3)
        # Position the entry widget in the grid at row 0, column 4 with padding
        self.rating_txt.grid(row=0, column=4, padx=10, pady=10)

        # Label to display status messages to the user
        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        # Position the status label in the grid at row 1, spanning 5 columns
        self.status_lbl.grid(row=1, column=0, columnspan=5,
                             sticky="W", padx=10, pady=10)

        # Text widget to show video details
        self.details_txt = tk.Text(window, width=48, height=12, wrap="none")
        # Position the Text widget in the grid at row 2, column 0, spanning 5 columns
        self.details_txt.grid(row=2, column=0, columnspan=5,
                              sticky="W", padx=10, pady=10)

    # Method for handling the rating update
    def update_rating(self):
        # Get the video number from the input field
        video_id = self.video_number_txt.get()
        try:
            # Convert the input rating to an integer
            new_rating = int(self.rating_txt.get())
            # Fetch the video name from the library using the video number
            video_name = lib.get_name(video_id)
            if video_name:
                # Update the rating in the library
                lib.set_rating(video_id, new_rating)
                # Fetch the play count of the video
                play_count = lib.get_play_count(video_id)
                # Generate a string with the updated video details
                details = f"{video_name}\nNew Rating: {new_rating}\nPlay Count: {play_count}"
                # Update the details text box with the new information
                self.details_txt.delete("1.0", tk.END)
                self.details_txt.insert("1.0", details)
                # Display a success message in the status label
                self.status_lbl.configure(text=f"Video {video_id} rating updated successfully")
            else:
                # Display a message if the video was not found
                self.status_lbl.configure(text=f"Video {video_id} not found")
        except ValueError:
            # Display an error message if the rating input is invalid
            self.status_lbl.configure(text="Please enter a valid rating")

# Main program execution
if __name__ == "__main__":
    # Create the main Tkinter window
    window = tk.Tk()
    # Apply font settings (assuming this is a predefined function)
    fonts.configure()
    # Instantiate the VideoUpdater class
    UpdateVideos(window)
    # Start the Tkinter event loop
    window.mainloop()