import random, keyboard, pygame, mutagen, os
from tkinter import filedialog
from gui.gui import load_gui

class SoundApp:
    def __init__(self, root):
        self.root = root
        self.sounds = []
        load_gui(self)
        keyboard.on_press(self.play_random_sound) 

    def play_random_sound(self):
        if self.sounds:
            selected_sound = random.choice(self.sounds)
            channel = pygame.mixer.find_channel()
            if channel is not None:
                sound = pygame.mixer.Sound(selected_sound)
                sound.set_volume(self.volume_scale.get())
                channel.play(sound)

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