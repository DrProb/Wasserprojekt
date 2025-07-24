import tkinter as tk
from PIL import Image, ImageTk
import pygame

# 🎵 Mixer initialisieren
pygame.mixer.init()

# 🎵 Song-Klasse
class Song:
    def __init__(self, title, artist, image_path, audio_path):
        self.title = title
        self.artist = artist
        self.image_path = image_path
        self.audio_path = audio_path
        self.image_small = None
        self.image_large = None

    def play(self):
        pygame.mixer.music.load(self.audio_path)
        pygame.mixer.music.play()

    def pause(self):
        pygame.mixer.music.pause()

    def resume(self):
        pygame.mixer.music.unpause()

    def stop(self):
        pygame.mixer.music.stop()


# 🖥 GUI
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("💧 Wasserklänge")
        self.root.configure(bg="#1e1e1e")

        self.songs = [
            Song("Africa", "TOTO", "assets/Africa.jpg", "assets/Africa.mp3"),
            Song("American Idiot", "Green Day", "assets/American Idiot.jpg", "assets/American Idiot.mp3"),
            Song("Another Day", "Dream Theater", "assets/Another Day.jpg", "assets/Another Day.mp3"),
            Song("Another Love", "Tom Odell", "assets/Another Love.jpg", "assets/Another Love.mp3"),
            Song("Another One Bites The Dust", "Queen", "assets/Another One Bites The Dust.jpg", "assets/Another One Bites The Dust.mp3"),
            Song("Bilbao", "Eigenkreation", "assets/Bilbao.png", "assets/Bilbao.mp3"),
            Song("Billie Jean", "Michael Jackson", "assets/Billie Jean.jpg", "assets/Billie Jean.mp3"),
            Song("Careless Whisper", "George Michael", "assets/Careless Whisper.jpg", "assets/Careless Whisper.mp3"),
            Song("Crazy Train", "Ozzy Osbourne", "assets/Crazy Train.jpg", "assets/Crazy Train.mp3"),
            Song("Despacito", "Luis Fonsi", "assets/Despacito.jpg", "assets/Despacito.mp3"),
            Song("Don't Stop Believing", "Journey", "assets/Dont Stop Believing.jpg", "assets/Dont Stop Believing.mp3"),
            Song("Eye Of The Tiger", "Survivor", "assets/Eye Of The Tiger.jpg", "assets/Eye Of The Tiger.mp3"),
            Song("Fluorescent Adolescent", "Arctic Monkeys", "assets/Fluorescent Adolescent.jpg", "assets/Fluorescent Adolescent.mp3"),
            Song("Für Elise", "Beethoven", "assets/Für Elise.png", "assets/Für Elise.mp3"),
            Song("Golden Hour", "JVKE", "assets/Golden Hour.jpg", "assets/Golden Hour.mp3"),
            Song("Happier", "Marshmello ft. Bastille", "assets/Happier.jpg", "assets/Happier.mp3"),
            Song("Hey Jude", "The Beatles", "assets/Hey Jude.png", "assets/Hey Jude.mp3"),
            Song("High Hopes", "Panic! At The Disco", "assets/High Hopes.jpg", "assets/High Hopes.mp3"),
            Song("Hotel California", "The Eagles", "assets/Hotel California.jpg", "assets/Hotel California.mp3"),
            Song("House Of The Rising Sun", "The Animals", "assets/House Of The Rising Sun.jpg", "assets/House Of The Rising Sun.mp3"),
            Song("Lateralus", "TOOL", "assets/Lateratus.jpg", "assets/Lateralus.mp3"),
            Song("Memories", "Maroon 5", "assets/Memories.jpg", "assets/Memories.mp3"),
            Song("Message in a Bottle", "The Police", "assets/Message In A Bottle.jpg", "assets/Message In A Bottle.mp3"),
            Song("Mr. Blue Sky", "Electric Light Orchestra", "assets/Mr Blue Sky.jpg", "assets/Mr Blue Sky.mp3"),
            Song("Mr. Brightside", "The Killers", "assets/Mr. Brightside.jpg", "assets/Mr. Brightside.mp3"),
            Song("No Surprises", "Radiohead", "assets/No Surprises.jpg", "assets/No Surprises.mp3"),
            Song("Piano Man", "Billy Joel", "assets/Piano Man.png", "assets/Piano Man.mp3"),
            Song("See You Again", "Tyler, The Creator", "assets/See You Again.jpg", "assets/See You Again.mp3"),
            Song("Seven Nation Army", "The White Stripes", "assets/Seven Nation Army.jpg", "assets/Seven Nation Army.mp3"),
            Song("Smells Like Teen Spirit", "Nirvana", "assets/Smells Like Teen Spirit.jpg", "assets/Smells Like Teen Spirit.mp3"),
            Song("Someone Like You", "Adele", "assets/Someone Like You.jpg", "assets/Someone Like You.mp3"),
            Song("Sweet Child O' Mine", "Guns n' Roses", "assets/Sweet Child O' Mine.jpg", "assets/Sweet Child O' Mine.mp3"),
            Song("Take Five", "Dave Brubeck", "assets/Take Five.png", "assets/Take Five.mp3"),
            Song("Take Me Home, Country Roads", "John Denver", "assets/Take Me Home, Country Roads.jpg", "assets/Take Me Home, Country Roads.mp3"),
            Song("The Entertainer", "Scott Joplin", "assets/The Entertainer.jpg", "assets/The Entertainer.mp3"),
            Song("The Final Countdown", "Europe", "assets/The Final Countdown.jpg", "assets/The Final Countdown.mp3"),
            Song("This Charming Man", "The Smiths", "assets/This Charming Man.jpg", "assets/This Charming Man.mp3"),
            Song("Türkischer Marsch", "Wolfgang Amadeus Mozart", "assets/Türkischer Marsch.jpg", "assets/Türkischer Marsch.mp3"),
            Song("vampire", "Olivia Rodrigo", "assets/Vampire.jpg", "assets/Vampire.mp3"),
            Song("Viva La Vida", "Coldplay", "assets/Viva La Vida.jpg", "assets/Viva La Vida.mp3"),
            Song("What Was I Made For", "Billie Eilish", "assets/What Was I Made For.jpg", "assets/What Was I Made For.mp3"),
            Song("You Give Love A Bad Name", "Bon Jovi", "assets/You Give Love A Bad Name.jpg", "assets/You Give Love A Bad Name.mp3"),
            

            # Weitere Songs hier einfügen
        ]

        self.current_song = None
        self.main_frame = tk.Frame(self.root, bg="#1e1e1e")
        self.main_frame.pack(fill="both", expand=True)
        self.show_home()

    def show_home(self):
        self.clear_frame()
        rows = 4
        cols = 7

        grid = tk.Frame(self.main_frame, bg="#1e1e1e")
        grid.pack(padx=20, pady=20)

        for idx, song in enumerate(self.songs):
            r = idx // cols
            c = idx % cols

            frame = tk.Frame(grid, bg="#2e2e2e", bd=2, relief="ridge")
            tk.Label(frame, text=song.artist, font=("Arial", 10, "bold"), bg="#2e2e2e", fg="white").pack()

            img = Image.open(song.image_path).resize((57, 57))
            song.image_small = ImageTk.PhotoImage(img)
            label = tk.Label(frame, image=song.image_small, bg="#2e2e2e")
            label.pack()

            tk.Label(frame, text=song.title, bg="#2e2e2e", fg="white").pack()

            frame.grid(row=r, column=c, padx=10, pady=10)
            frame.bind("<Button-1>", lambda e, s=song: self.show_player(s))
            label.bind("<Button-1>", lambda e, s=song: self.show_player(s))

    def show_player(self, song):
        self.clear_frame()
        self.current_song = song
        song.play()

        title = tk.Label(self.main_frame, text=f"🎵 {song.title} – {song.artist}",
                         font=("Arial", 18, "bold"), bg="#1e1e1e", fg="white")
        title.pack(pady=20)

        # Großes Cover anzeigen
        img = Image.open(song.image_path).resize((300, 300))
        song.image_large = ImageTk.PhotoImage(img)
        image_label = tk.Label(self.main_frame, image=song.image_large, bg="#1e1e1e")
        image_label.pack(pady=10)

        # Buttons
        button_frame = tk.Frame(self.main_frame, bg="#1e1e1e")
        button_frame.pack(pady=20)

        is_paused = tk.BooleanVar(value=False)

        def toggle_pause():
            if is_paused.get():
                song.resume()
                pause_btn.config(text="⏸ Pause")
                is_paused.set(False)
            else:
                song.pause()
                pause_btn.config(text="▶️ Fortsetzen")
                is_paused.set(True)

        pause_btn = tk.Button(button_frame, text="⏸ Pause", command=toggle_pause,
                              font=("Arial", 12), bg="#444", fg="white", activebackground="#666")
        pause_btn.grid(row=0, column=0, padx=10)

        back_btn = tk.Button(button_frame, text="⬅ Zurück", command=self.show_home,
                             font=("Arial", 12), bg="#444", fg="white", activebackground="#666")
        back_btn.grid(row=0, column=1, padx=10)

    def clear_frame(self):
        pygame.mixer.music.stop()
        for widget in self.main_frame.winfo_children():
            widget.destroy()


# 🚀 Programm starten
if __name__ == "__main__":
    root = tk.Tk()
    root.attributes("-fullscreen", True)  # 🎯 Fullscreen aktivieren

    # Optional: Escape beendet Fullscreen
    def end_fullscreen(event):
        root.attributes("-fullscreen", False)

    root.bind("<Escape>", end_fullscreen)

    app = App(root)
    root.mainloop()
