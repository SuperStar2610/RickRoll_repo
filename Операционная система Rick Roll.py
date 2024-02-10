from time import *

print('Загрузка...')
import pygame
import json
import tkinter as tk
from tkinter import filedialog
import cv2
import random
from tkinter import Tk, Label, Button, Canvas, PhotoImage
from PIL import Image, ImageTk
import os
import sys
print()
print('Вас приветствует ОС "Rick Roll!"')
work_desk = {}
one = 1
command = ''
svoboda = 16
computer = {'Диски: ': 'Локальный диск(C:)',  'Свободно: ': f'{svoboda} ГБ'}
command = input('Пожалуйcта, введите команду: ')
if command == 'work_desk':
    print(f'Ваш рабочий стол: {work_desk}')
elif command == 'computer':
    print(f'Информация о вашем хранилище: {computer}')
    print()
elif command == 'readfile':
    file = input('Пожалуйста, введите название файла: ')
    my_file = open(file,encoding='utf-8')
    print(f'Ваш файл: {my_file.read()}')
    work_desk[f'txt_file{one}'] = file
    svoboda -= 32
    print('Добавление выполнено!')
    print()
elif command == 'delfile':
    delete = input('Пожалуйста, введите ключ файла: ')
    del work_desk[delete]
    svoboda += 50
    print('Удаление выполнено!')
    print()
elif command == 'enter_audio':
    class AudioPlayer:
        def __init__(self, master):
            self.master = master
            self.master.title('Видеоплеер "Rick Roll Audio"')
            self.master.geometry('400x400')
            self.master.config(bg = 'light blue')
            self.play_button = tk.Button(self.master, text="Play", command=self.play_music, font = ('Times New Roman',18, 'bold'))
            self.play_button.pack(pady=10)
            self.pause_button = tk.Button(self.master, text="Pause", command=self.pause_music, font = ('Times New Roman',18, 'bold'))
            self.pause_button.pack(pady=10)
        def play_music(self):
            file_path = filedialog.askopenfilename(defaultextension=".mp3",
                                                   filetypes=[("MP3 files", "*.mp3")])
            if not file_path:
                return
            pygame.mixer.init()
            pygame.mixer.music.load(file_path)
            pygame.mixer.music.play()
        def pause_music(self):
            pygame.mixer.music.pause()
    def main():
        root = tk.Tk()
        app = AudioPlayer(root)
        root.mainloop()
    if __name__ == "__main__":
        main()
    svoboda -= 64
    work_desk['audio'] = 'audiofile'
elif command == 'enter_video':
    class VideoPlayer:
        def __init__(self, master):
            self.master = master
            self.master.title('Видеоплеер "Rick Roll Video"')
            self.master.geometry('400x400')
            self.master.config(bg = 'light blue')
            self.play_button = tk.Button(self.master, text="Play", command=self.play_video , font = ('Times New Roman',18, 'bold'))
            self.play_button.pack(pady=10)
            self.pause_button = tk.Button(self.master, text="Pause", command=self.pause_video , font = ('Times New Roman',18, 'bold'))
            self.pause_button.pack(pady=10)
            self.exit_button = tk.Button(self.master, text="Exit", command=self.master.destroy, font = ('Times New Roman',18, 'bold'))
            self.exit_button.pack(pady=10)
            self.video_path = None
            self.cap = None
        def play_video(self):
            self.video_path = filedialog.askopenfilename(defaultextension=".mp4",
                                                         filetypes=[("Video files", "*.mp4")])
            if not self.video_path:
                return
            self.cap = cv2.VideoCapture(self.video_path)
            while True:
                ret, frame = self.cap.read()
                if not ret:
                    break
                cv2.imshow("Video Player", frame)
                if cv2.waitKey(30) & 0xFF == 27:  # Press 'Esc' to exit
                    break
            self.cap.release()
            cv2.destroyAllWindows()
        def pause_video(self):
            if self.cap:
                if self.pause_button.cget("text") == "Pause":
                    self.pause_button.configure(text="Resume")
                    cv2.waitKey(0)  # Pause until any key is pressed
                else:
                    self.pause_button.configure(text="Pause")
    def main():
        root = tk.Tk()
        app = VideoPlayer(root)
        root.mainloop()
    if __name__ == "__main__":
        main()
    svoboda -= 128
    work_desk['video'] = 'videofile'
elif command == 'guess':
    print('Хотите увеличить размер места на диске?')
    print('Тгда вам сюда! Выиграйте две попытки в игре "Угадай число и ваше место на диске на диске увеличится в {попытки} раз!"')
    print('ВНИМАНИЕ! На угадывание числа даётся только 8 попыток!')
    popitka = 0
    text = 'да'
    while text == 'да':
        print('Вы будете угадывать число от 1 до 100')
        sluch = random.randint(1, 100)
        counter = 0
        while True:
            chislo = int(input('Угадай число от 1 до 100 '))  # от 1 до', n))
            if chislo > 100 or chislo < 1:
                print('ОШИБКА! Вы ввели число в неверном диапазоне! Код ошибки:', random.randint(1, 10000))
            elif chislo < sluch:
                print('Не угадал! Введи число больше!!!')
                counter += 1
            elif chislo > sluch:
                print('Не угадал! Введи число меньше!!!')
                counter += 1
            else:
                popitka += 1
                print(
                    f'Поздравляю! Вы выиграли 1 попытку! Количество попыток, которые вы уже выиграли: {popitka}')
                break
            if counter == 8:
                popitka -= 1
                print('К сожалению, вы проиграли. Вы не смогли угадать число больше, чем за 8 попыток')
                print(f'Количество попыток, за которые вы выиграли, изменилось: {popitka}')
                break
        text = input('Не хочешь ещё поиграть? ').lower()
    print('Игра завершена!')
    if popitka <= 0:
        print('Поскольку вы выиграли <= 0 попыток, ваше место остаётся прежним')
    else:
        print(f'Ваше место увеличивается в {popitka} раз!!!')
        svoboda *= popitka
        print(f'Итоговый объём вашего места: {svoboda}')
elif command == 'userwrite':
    login = input('Пожалуйста, введите логин вашей учётной записи: ')
    file = open(login, 'w')
    json.dump(work_desk, file, indent=4)
    file.close()
    print('Поздравляю! Вы записали рабочий стол своей учётной записи! После выключения ОС файл с учётной записью будет сохранён!')
elif command == 'enter_photo':
    print('Окно в менеджером фото открылось!')
    class PhotoViewer:
        def __init__(self, root):
            self.root = root
            self.root.title('Фото Менеджер "Rick Roll Photo"')
            self.root.geometry('1200x800')
            self.root.config(bg = 'light blue')
            self.image_paths = []
            self.current_image_index = 0
            self.label = Label(root)
            self.label.pack()
            self.load_button = Button(root, text="Load Images", command=self.load_images, font = ('Times New Roman',18, 'bold'))
            self.load_button.pack()
            self.prev_button = Button(root, text="Previous", command=self.show_previous_image, font = ('Times New Roman',18, 'bold'))
            self.prev_button.pack(side="left")
            self.next_button = Button(root, text="Next", command=self.show_next_image, font = ('Times New Roman',18, 'bold'))
            self.next_button.pack(side="right")
        def load_images(self):
            file_paths = filedialog.askopenfilenames(title="Select Images", filetypes=[
                ("Image files", "*.png;*.jpg;*.jpeg;*.gif")])
            self.image_paths = list(file_paths)
            if self.image_paths:
                self.current_image_index = 0
                self.show_image()
        def show_image(self):
            if self.image_paths:
                image_path = self.image_paths[self.current_image_index]
                image = Image.open(image_path)
                image.thumbnail((800, 600))
                photo = ImageTk.PhotoImage(image)
                self.label.config(image=photo)
                self.label.image = photo
                self.root.title(f"Photo Viewer - {os.path.basename(image_path)}")
        def show_previous_image(self):
            if self.image_paths:
                self.current_image_index = (self.current_image_index - 1) % len(self.image_paths)
                self.show_image()
        def show_next_image(self):
            if self.image_paths:
                self.current_image_index = (self.current_image_index + 1) % len(self.image_paths)
                self.show_image()
    if __name__ == "__main__":
        root = Tk()
        app = PhotoViewer(root)
        root.mainloop()
    svoboda -= 64
    work_desk['photo'] = 'photofile'
elif command == 'read_user':
    file_name = input('Пожалуйста, введите имя файла: ')
    try:
        with open(file_name, 'r') as file:
            data = json.load(file)
        work_desk = dict(data)
        sleep(1)
        print('Поздравляю! Теперь вы можете работать с этой учётной записью!')
    except FileNotFoundError:
        print(
            f'Ошибка! Файл не найден. Уникальный код ошибки: {random.randint(1, 150)}. Программа будет закрыта!')
        sleep(0.9)
        exit()
elif command == 'secret':
    class VideoPlayer:
        def __init__(self, master):
            self.master = master
            self.master.title('Видеоплеер "Secret"')
            self.master.geometry('400x400')
            self.master.config(bg='light blue')
            self.play_button = tk.Button(self.master, text="Play", command=self.play_video,
                                         font=('Times New Roman', 18, 'bold'))
            self.play_button.pack(pady=10)
            self.pause_button = tk.Button(self.master, text="Pause", command=self.pause_video,
                                          font=('Times New Roman', 18, 'bold'))
            self.pause_button.pack(pady=10)
            self.exit_button = tk.Button(self.master, text="Exit", command=self.master.destroy,
                                         font=('Times New Roman', 18, 'bold'))
            self.exit_button.pack(pady=10)
            self.video_path = None
            self.cap = None
        def play_video(self):
            self.video_path = filedialog.askopenfilename(defaultextension=".mp4",
                                                         filetypes=[("Video files", "secret.exe.mp4")])
            if not self.video_path:
                return
            self.cap = cv2.VideoCapture(self.video_path)
            while True:
                ret, frame = self.cap.read()
                if not ret:
                    break
                cv2.imshow("Video Player", frame)
                if cv2.waitKey(30) & 0xFF == 27:  # Press 'Esc' to exit
                    break
            self.cap.release()
            cv2.destroyAllWindows()
        def pause_video(self):
            if self.cap:
                if self.pause_button.cget("text") == "Pause":
                    self.pause_button.configure(text="Resume")
                    cv2.waitKey(0)  # Pause until any key is pressed
                else:
                    self.pause_button.configure(text="Pause")
    def main():
        root = tk.Tk()
        app = VideoPlayer(root)
        root.mainloop()
    if __name__ == "__main__":
        main()
    svoboda -= 128
    work_desk['video'] = 'videofile'
else:
    print('Ошибка! Вы ввели неправильную команду!')