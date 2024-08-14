import tkinter as tk
import tkinter.scrolledtext as tkst
import random
import video_library as lib
import font_manager as fonts

class createvideo:
    def __init__(self, window):
        # Initializes the playlist as an empty list
        self.playlist = []

        # Configures the window size and title
        window.geometry("1000x350")
        window.title("Create Video List")

        # Creates a button to add a video to the playlist
        add_video_btn = tk.Button(
            window, text="Add Video to Playlist", command=self.add_video)
        add_video_btn.grid(row=0, column=2, padx=10, pady=10)

        # Creates a button to add a random video to the playlist
        add_random_video_btn = tk.Button(
            window, text="Add Random Video", command=self.add_random_video)
        add_random_video_btn.grid(row=0, column=3, padx=10, pady=10)

        # Creates a button to play the videos in the playlist
        play_videos_btn = tk.Button(
            window, text="Play Playlist", command=self.play_playlist)
        play_videos_btn.grid(row=0, column=4, padx=10, pady=10)

        # Creates a button to clear the playlist
        reset_playlist_btn = tk.Button(
            window, text="Reset Playlist", command=self.reset_playlist)
        reset_playlist_btn.grid(row=0, column=5, padx=10, pady=10)

        # Label prompting the user to enter a video number
        enter_lbl = tk.Label(window, text="Enter Video Number")
        enter_lbl.grid(row=0, column=0, padx=10, pady=10)

        # Entry widget for the video number input
        self.input_txt = tk.Entry(window, width=3)
        self.input_txt.grid(row=0, column=1, padx=10, pady=10)

        # ScrolledText widget to display the playlist
        self.playlist_txt = tkst.ScrolledText(
            window, width=58, height=12, wrap="none")
        self.playlist_txt.grid(row=1, column=0, columnspan=6,
                               sticky="W", padx=10, pady=10)

        # Label to display status messages
        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=2, column=0, columnspan=6,
                             sticky="W", padx=10, pady=10)

    def add_video(self):
        # Retrieves the video number entered by the user
        video_id = self.input_txt.get()
        video_name = lib.get_name(video_id)
        if video_name:
            # Adds the video to the playlist and updates the display
            self.playlist.append(video_id)
            self.update_playlist_display()
            self.status_lbl.configure(text=f"Video {video_id} added to playlist")
        else:
            # Updates the status label if the video was not found
            self.status_lbl.configure(text=f"Video {video_id} not found")

    def add_random_video(self):
        random_video_id = random.choice(list(lib.library.keys()))
        self.playlist.append(random_video_id)
        self.update_playlist_display()
        self.status_lbl.configure(text=f"Random video {random_video_id} added to playlist")

    def play_playlist(self):
        # Plays all videos in the playlist and updates play counts
        for video_id in self.playlist:
            lib.increment_play_count(video_id)
        self.status_lbl.configure(text="Playlist played. Play counts updated.")

    def reset_playlist(self):
        # Clears the playlist and updates the display
        self.playlist = []
        self.update_playlist_display()
        self.status_lbl.configure(text="Playlist reset.")

    def update_playlist_display(self):
        # Updates the playlist display with the current videos
        playlist_content = "\n".join([lib.get_name(video_id) for video_id in self.playlist])
        self.playlist_txt.delete("1.0", tk.END)
        self.playlist_txt.insert("1.0", playlist_content)

if __name__ == "__main__":
    window = tk.Tk()        # Creates the main Tkinter window
    fonts.configure()       # Applies font configurations
    createvideo(window)  # Initializes the video playlist application
    window.mainloop()       # Runs the main Tkinter event loop