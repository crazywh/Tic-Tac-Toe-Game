import pygame, sys, os
from pygame.locals import *

# 设置窗口打开位置
os.environ['SDL_VIDEO_WINDOW_POS'] = "400, 100"
# 初始化
pygame.init()
pygame.mixer.init()
size = w, h = 600, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption("井字游戏")
font = pygame.font.SysFont('arial', 26)

# 定义颜色
BULE = (0, 0, 60)
WHITE = (200, 200, 200)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

#加载音乐
pygame.mixer.music.load('sound/bg.mp3')
pygame.mixer.music.set_volume(0.5)

# 绘制文字
def print_text(font, x, y, text, color = WHITE):
	ti = font.render(text, True, color)
	screen.blit(ti, (x, y))

# 绘制图形
def draw_circle(x, y, r, w, color):
	pygame.draw.circle(screen, color, (x, y), r, w)

def draw_x(x, y, w1, w2, color):
	pygame.draw.line(screen, color, (x, y), (x + w1, y + w1), w2)
	pygame.draw.line(screen, color, (x + w1, y), (x, y + w1), w2)

def draw_play(i, flag, coor):
	if flag:
		draw_circle(coor[i % 3], coor[i // 3], 70, 2, RED)
	else:
		draw_x(coor[i % 3], coor[i // 3], 140, 2, GREEN)

def main():
	pygame.mixer.music.play()
	# 当前玩家标志
	play = True
	flag = [0] * 9
	# 辅助绘制图形
	coor1 = [130, 300, 470]
	coor2 = [60, 230, 400]
	# 声音开关标志
	sound = True
	# 胜负标志
	win = 0
	while True:		
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == MOUSEBUTTONDOWN:				
				if event.button == 1:
					pos = event.pos
					if 440 < pos[0] < 546 and 0 < pos[1] < 31:
						sound = not sound
					elif 50 < pos[0] < 210 and 50 < pos[1] < 210:
						if flag[0] == 0 and not win:
							if play:
								flag[0] = 1
							else:
								flag[0] = 2
							play = not play
					elif 220 < pos[0] < 380 and 50 < pos[1] < 210:
						if flag[1] == 0 and not win:
							if play:
								flag[1] = 1
							else:
								flag[1] = 2
							play = not play
					elif 390 < pos[0] < 550 and 50 < pos[1] < 210:
						if flag[2] == 0 and not win:
							if play:
								flag[2] = 1
							else:
								flag[2] = 2
							play = not play
					elif 50 < pos[0] < 210 and 220 < pos[1] < 380:
						if flag[3] == 0 and not win:
							if play:
								flag[3] = 1
							else:
								flag[3] = 2
							play = not play
					elif 220 < pos[0] < 380 and 220 < pos[1] < 380:
						if flag[4] == 0 and not win:
							if play:
								flag[4] = 1
							else:
								flag[4] = 2
							play = not play
					elif 390 < pos[0] < 550 and 220 < pos[1] < 380:
						if flag[5] == 0 and not win:
							if play:
								flag[5] = 1
							else:
								flag[5] = 2
							play = not play
					elif 50 < pos[0] < 210 and 390 < pos[1] < 550:
						if flag[6] == 0 and not win:
							if play:
								flag[6] = 1
							else:
								flag[6] = 2
							play = not play
					elif 220 < pos[0] < 380 and 390 < pos[1] < 550:
						if flag[7] == 0 and not win:
							if play:
								flag[7] = 1
							else:
								flag[7] = 2
							play = not play
					elif 390 < pos[0] < 550 and 390 < pos[1] < 550:
						if flag[8] == 0 and not win:
							if play:
								flag[8] = 1
							else:
								flag[8] = 2
							play = not play
				# print(flag)

		screen.fill(BULE)
		# 绘制正方形
		for i in range(3):
			for j in range(3):
				pygame.draw.rect(screen, WHITE, (50 + 170 * j, 50 + 170 * i, 160, 160), 5)
		# 音乐控制
		if sound:
			print_text(font, 440, 0, "Sound: ON")
			pygame.mixer.music.unpause()
		else:
			print_text(font, 440, 0, "Sound: OFF")
			pygame.mixer.music.pause()
		# 玩家标志绘制
		if play:
			# 绘制圆形  (x, y, r, line_width, color)
			draw_circle(70, 20, 15, 2, RED)
		else:
			# 绘制叉 (x, y, 距离差值, line_width, color)
			draw_x(55, 5, 30, 2, GREEN)		
		for i in range(9):
			if flag[i] == 1:
				draw_play(i, True, coor1)
			elif flag[i] == 2:
				draw_play(i, False, coor2)

		# 判断胜负
		if not win:
			for i in [0, 3, 6]:
				if flag[i] == flag[i + 1] == flag[i + 2]:
					if flag[i] == 1:
						win = 1
					elif flag[i] == 2:
						win = 2

		if not win:
			for i in [0, 1, 2]:
				if flag[i] == flag[i + 3] == flag[i + 6]:
					if flag[i] == 1:
						win = 1
					elif flag[i] == 2:
						win = 2

		if not win:
			if flag[0] == flag[4] == flag[8]:
				if flag[0] == 1:
					win = 1
				elif flag[0] == 2:
					win = 2
		if not win:
			if flag[2] == flag[4] == flag[6]:
				if flag[2] == 1:
					win = 1
				elif flag[2] == 2:
					win = 2
		if not win and all(flag):
			win = 3

		if win:
			if win == 1:
				print_text(font, 250, 10, "O WIN!!")
				print_text(font, 240, 560, "PLAY AGAIN!!")
			elif win == 2:
				print_text(font, 250, 10, "X WIN!!")
				print_text(font, 240, 560, "PLAY AGAIN!!")
			elif win == 3:
				print_text(font, 250, 10, "IS DRAW!!")
				print_text(font, 240, 560, "PLAY AGAIN!!")
			pygame.mixer.music.stop()

			if pygame.mouse.get_pressed()[0]:
				pos = pygame.mouse.get_pos()
				if 240 < pos[0] < 350 and  560 < pos[1] < 590:
					main() 

		pygame.display.update()

if __name__ == "__main__":
	main()