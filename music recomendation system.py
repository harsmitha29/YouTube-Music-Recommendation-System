import tkinter as tk
from tkinter import ttk, messagebox
import webbrowser

class YouTubeMusicRecommender:
    @staticmethod
    def search_youtube(query):
        # Generate a YouTube search URL for music videos
        base_url = "https://www.youtube.com/results?search_query="
        search_query = f"{query}+video songs"  # Refined search for music-related videos
        search_url = f"{base_url}{search_query.replace(' ', '+')}"
        return search_url

class MusicRecommendationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("YouTube Music Recommender")
        self.root.geometry("600x400")
        self.root.configure(bg='#f8f9fa')

        # Title
        tk.Label(self.root, text="YouTube Music Recommender", font=("Helvetica", 16, "bold"), bg='#f8f9fa').pack(pady=10)

        # Input frame
        self.input_frame = tk.Frame(self.root, bg='#f8f9fa')
        self.input_frame.pack(pady=20)

        tk.Label(self.input_frame, text="Enter Song or Mood:", font=("Helvetica", 12), bg='#f8f9fa').pack(side=tk.LEFT, padx=5)
        self.search_var = tk.StringVar()
        ttk.Entry(self.input_frame, textvariable=self.search_var, width=40).pack(side=tk.LEFT, padx=5)

        # Search button
        tk.Button(self.root, text="Search", command=self.show_recommendations, bg='#007bff', fg='white', font=("Helvetica", 12)).pack(pady=10)

        # Results text area
        self.results_text = tk.Text(self.root, height=10, width=70, wrap=tk.WORD)
        self.results_text.pack(pady=10)

    def show_recommendations(self):
        # Clear previous results
        self.results_text.delete(1.0, tk.END)

        # Get user input
        query = self.search_var.get().strip()
        if not query:
            messagebox.showwarning("Input Error", "Please enter a song name or mood.")
            return

        # Get YouTube search URL
        search_url = YouTubeMusicRecommender.search_youtube(query)

        # Display the search URL
        self.results_text.insert(tk.END, f"Search results for '{query}':\n")
        self.results_text.insert(tk.END, search_url + "\n\n")

        # Open the search results
        if messagebox.askyesno("Open YouTube", "Do you want to view these results on YouTube?"):
            webbrowser.open(search_url)

def main():
    root = tk.Tk()
    app = MusicRecommendationApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
