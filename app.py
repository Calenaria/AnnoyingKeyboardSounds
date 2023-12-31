import random, keyboard, pygame, mutagen, os
from tkinter import filedialog
from gui.gui import load_gui

class SoundApp:
    def __init__(self, root):
        self.root = root
        self.sounds = []
        self.is_listening = False
        load_gui(self)

    def toggle_listening(self):
        if self.is_listening:
            keyboard.unhook_all()
            self.toggle_listener.config(text="Start")
        else:
            keyboard.on_press(self.play_random_sound)
            self.toggle_listener.config(text="Stop")
        self.is_listening = not self.is_listening

    def play_random_sound(self, event = None):
        if self.sounds:
            selected_sound = random.choice(self.sounds)
            channel = pygame.mixer.find_channel()
            if channel is not None:
                sound = pygame.mixer.Sound(selected_sound)
                sound.set_volume(self.volume_scale.get())
                channel.play(sound)

    def clear_sounds(self):
        for x in self.treeview.get_children():
            self.treeview.delete(x)
        self.sounds = []

    def add_sound(self):
        file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3 *.wav")])
        if file_path:
            self.sounds.append(file_path)
            audio_info = mutagen.File(file_path, easy=True)
            duration = audio_info.info.length
            base_name = os.path.basename(file_path)
            self.treeview.insert('', 'end', values=(base_name, f"{duration:.2f}s"))

    def remove_sound(self):
        if self.sounds:
            selected_item = self.treeview.selection()
            if selected_item:
                selected_base_name: str = self.treeview.item(selected_item, 'values')[0]
                selected_sound = next(sound for sound in self.sounds if os.path.basename(sound) == selected_base_name)
                self.treeview.delete(selected_item)
                self.sounds.remove(selected_sound)
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.stop()