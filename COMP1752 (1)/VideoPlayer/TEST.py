import tkinter as tk
from tkinter import messagebox, simpledialog
import csv
import webbrowser
import os

CSV_FILE = "video_library.csv"

class VideoLibrary:
    def __init__(self):
        self.library = self.load_library()

    def load_library(self):
        library = {}
        if os.path.exists(CSV_FILE):
            with open(CSV_FILE, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    library[row['name']] = {
                        'number': row['number'],
                        'director': row['director'],
                        'rating': row['rating']
                    }
        return library

    def save_library(self):
        with open(CSV_FILE, 'w', newline='') as csvfile:
            fieldnames = ['number', 'name', 'director', 'rating']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for name, data in self.library.items():
                writer.writerow({'number': data['number'], 'name': name, 'director': data['director'], 'rating': data['rating']})

    def add_video(self, number, name, director, rating):
        if name not in self.library:
            self.library[name] = {'number': number, 'director': director, 'rating': rating}
            self.save_library()
            return True
        return False

    def delete_video(self, name):
        if name in self.library:
            del self.library[name]
            self.save_library()
            return True
        return False

class AddVideo:
    def __init__(self, window, video_library):
        self.video_library = video_library
        self.window = window
        window.geometry("400x400")
        window.title("Add New Video")

        number_lbl = tk.Label(window, text="Video Number:")
        number_lbl.pack(pady=10)
        self.number_txt = tk.Entry(window, width=10)
        self.number_txt.pack(pady=10)

        name_lbl = tk.Label(window, text="Video Name:")
        name_lbl.pack(pady=10)
        self.name_txt = tk.Entry(window, width=30)
        self.name_txt.pack(pady=10)

        director_lbl = tk.Label(window, text="Director:")
        director_lbl.pack(pady=10)
        self.director_txt = tk.Entry(window, width=30)
        self.director_txt.pack(pady=10)

        rating_lbl = tk.Label(window, text="Rating:")
        rating_lbl.pack(pady=10)
        self.rating_txt = tk.Entry(window, width=10)
        self.rating_txt.pack(pady=10)

        add_btn = tk.Button(window, text="Add Video", command=self.add_video)
        add_btn.pack(pady=10)

    def add_video(self):
        number = self.number_txt.get().strip()
        name = self.name_txt.get().strip()
        director = self.director_txt.get().strip()
        rating = self.rating_txt.get().strip()

        if number.isdigit() and name and director and rating.isdigit():
            success = self.video_library.add_video(number, name, director, rating)
            if success:
                messagebox.showinfo("Success", "Video added successfully!")
                self.window.destroy()
            else:
                messagebox.showerror("Error", "Video already exists.")
        else:
            messagebox.showerror("Error", "Please fill in all fields correctly.")


class SearchVideos:
    def __init__(self, window, video_library):
        self.video_library = video_library
        self.window = window
        window.geometry("400x400")
        window.title("Search Videos")

        search_lbl = tk.Label(window, text="Search Videos:")
        search_lbl.pack(pady=10)

        self.search_txt = tk.Entry(window, width=40)
        self.search_txt.pack(pady=5)

        search_btn = tk.Button(window, text="Search", command=self.search_videos)
        search_btn.pack(pady=10)

        self.results_listbox = tk.Listbox(window, width=50, height=10)
        self.results_listbox.pack(pady=10)

        select_btn = tk.Button(window, text="Select Video", command=self.select_video)
        select_btn.pack(side="left", padx=5, pady=10)

        play_btn = tk.Button(window, text="Play Video", command=self.play_video)
        play_btn.pack(side="left", padx=5, pady=10)

        delete_btn = tk.Button(window, text="Delete Video", command=self.delete_video)
        delete_btn.pack(side="right", padx=5, pady=10)

        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.pack(pady=10)

        self.display_all_videos()

    def search_videos(self):
        query = self.search_txt.get().strip()
        if not query:
            self.status_lbl.configure(text="Please enter a search term")
            return

        self.results_listbox.delete(0, tk.END)

        results = [(name, details) for name, details in self.video_library.library.items() if query.lower() in name.lower()]

        if results:
            for name, details in results:
                self.results_listbox.insert(tk.END, f"{details['number']}: {name}: Directed by {details['director']} (Rating: {details['rating']})")
            self.status_lbl.configure(text=f"{len(results)} results found")
        else:
            self.status_lbl.configure(text="No results found")

    def display_all_videos(self):
        self.results_listbox.delete(0, tk.END)
        for name, details in self.video_library.library.items():
            self.results_listbox.insert(tk.END, f"{details['number']}: {name}: Directed by {details['director']} (Rating: {details['rating']})")
        self.status_lbl.configure(text=f"{len(self.video_library.library)} videos in library")

    def select_video(self):
        selected = self.results_listbox.get(tk.ACTIVE)
        if selected:
            self.selected_video_number = selected.split(":")[0]
            self.status_lbl.configure(text=f"Selected video number '{self.selected_video_number}'")
        else:
            self.status_lbl.configure(text="Please select a video")

    def play_video(self):
        selected = self.results_listbox.get(tk.ACTIVE)
        if selected:
            video_name = selected.split(": ")[1].split(" (")[0]  # Extract name from the string
            search_query = video_name.replace(" ", "+")
            url = f"https://www.youtube.com/results?search_query={search_query}"
            webbrowser.open(url)
            self.status_lbl.configure(text=f"Searching for '{video_name}' on YouTube")
        else:
            self.status_lbl.configure(text="Please select a video to play")

    def delete_video(self):
        selected = self.results_listbox.get(tk.ACTIVE)
        if selected:
            video_name = selected.split(": ")[1].split(" (")[0]  # Extract name from the string
            if messagebox.askyesno("Delete Video", f"Are you sure you want to delete '{video_name}'?"):
                success = self.video_library.delete_video(video_name)
                if success:
                    self.results_listbox.delete(tk.ACTIVE)
                    self.status_lbl.configure(text=f"Video '{video_name}' deleted")
                else:
                    self.status_lbl.configure(text="Error deleting video")
            else:
                self.status_lbl.configure(text="Video deletion canceled")
        else:
            self.status_lbl.configure(text="Please select a video to delete")


if __name__ == "__main__":
    video_library = VideoLibrary()

    window = tk.Tk()
    window.geometry("400x200")
    window.title("Video Library")

    add_video_btn = tk.Button(window, text="Add New Video", command=lambda: AddVideo(tk.Toplevel(window), video_library))
    add_video_btn.pack(pady=10)

    search_videos_btn = tk.Button(window, text="Search Videos", command=lambda: SearchVideos(tk.Toplevel(window), video_library))
    search_videos_btn.pack(pady=10)

    window.mainloop()
