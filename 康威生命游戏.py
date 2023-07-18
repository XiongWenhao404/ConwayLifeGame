# -*-coding:GBK -*-

import tkinter as tk
import random

from SPECIAL_LIST import SPECIAL_LIST  # �������������

#  �������ӣ�Ϊ0ʱ���������������Ϊ1ʱʹ���ض�����������������
SEED = 0

# �������ӣ��޸ĵ�ͼ���Ա�
PROPERTY_LIST = [20, 400, 400, 500]
if SEED == 1:
    PROPERTY_LIST = SPECIAL_LIST[SEED - 1][0]

# ���ݵ�ͼ���Ա�������ԣ�����Ϊ�������С�����ڿ����ڸߣ�ˢ��ʱ��
SIZE, WINDOW_WIDTH, WINDOW_HEIGHT, DELAY = PROPERTY_LIST
WIDTH_LEN = WINDOW_WIDTH // SIZE
HEIGHT_LEN = WINDOW_HEIGHT // SIZE


# ��ʼ�������������ڻ��������
class LiVes:
    def __init__(self, seed):
        self.cells = [[random.choice([0, 1]) for _ in range(WIDTH_LEN)] for _ in
                      range(HEIGHT_LEN)] if seed == 0 else SPECIAL_LIST[SEED - 1][1:]
        self.colorSwitch = {1: "black", 0: "white"}
        self.ifChange = False

    def cellCheck(self):
        self.ifChange = False
        for i in range(HEIGHT_LEN):
            for j in range(WIDTH_LEN):
                liveNumber = self.stateStatistics(i, j)
                if self.cells[i][j] == 0:
                    if liveNumber == 3:
                        self.cells[i][j] = 1
                        self.ifChange = True
                elif self.cells[i][j] == 1:
                    if liveNumber < 2 or liveNumber > 3:
                        self.cells[i][j] = 0
                        self.ifChange = True

    def stateStatistics(self, x, y):
        liveNumbers = 0
        direction = [[1, 0], [0, 1], [1, 1], [1, -1]]
        for dx, dy in direction:
            i, j = x + dy, y + dx
            if 0 <= i < HEIGHT_LEN and 0 <= j < WIDTH_LEN and self.cells[i][j] == 1:
                liveNumbers += 1
            i, j = x - dx, y - dy
            if 0 <= i < HEIGHT_LEN and 0 <= j < WIDTH_LEN and self.cells[i][j] == 1:
                liveNumbers += 1
        return liveNumbers

    def draw(self, canvas):
        for i in range(HEIGHT_LEN):
            for j in range(WIDTH_LEN):
                canvas.create_rectangle(j * SIZE, i * SIZE, (j + 1) * SIZE, (i + 1) * SIZE,
                                        fill=self.colorSwitch[self.cells[i][j]])


# ִ�������ݽ�����ֹͣ�ݽ������¿�ʼ�µ�һ������
class Conway:
    def __init__(self, master):
        self.master = master
        self.master.title = "ConwayLifeGame"
        self.canvas = tk.Canvas(self.master, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
        self.canvas.pack()
        self.lives = LiVes(SEED)
        self.round = 0
        self.update()
        centerWindow(self.master)

    def update(self):
        self.lives.draw(self.canvas)
        self.lives.cellCheck()
        self.canvas.delete("all")
        self.lives.draw(self.canvas)
        if self.lives.ifChange is False:
            self.round += 1
        else:
            self.round = 0
        if self.round >= 3:
            self.restart()
        self.master.after(DELAY, self.update)

    # ֹͣ�ݽ������¿�ʼ�µ�һ������
    def restart(self):
        self.master.destroy()
        newRoot = tk.Tk()
        newGame = Conway(newRoot)
        print(newGame.round)  # ��������䣬�����������档����Ϊδʹ�þֲ�����'newGame'��ֵ����newGame��������ģ����ʹ�ô�����������档
        root.mainloop()


# ������ʼ��������Ļ����
def centerWindow(window, window_width=WINDOW_WIDTH, window_height=WINDOW_HEIGHT):
    # ��ȡ��Ļ�Ŀ�Ⱥ͸߶�
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    # ���㴰�ڵĿ�Ⱥ͸߶�
    # ���㴰�����Ͻǵ�����ʹ�������Ļ�м�
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    # ���ô��ڵĴ�С��λ��
    window.geometry(f"{window_width}x{window_height}+{x}+{y}")


# ����
if __name__ == "__main__":
    root = tk.Tk()
    game = Conway(root)
    root.mainloop()
