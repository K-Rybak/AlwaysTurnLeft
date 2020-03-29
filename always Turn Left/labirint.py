from collections import defaultdict

fileRead = open('large-test.in.txt', 'r')
fileWrite = open('large-test.out.txt', 'w')

NORTH, SOUTH, WEST, EAST = [2 ** i for i in range(4)] # обозначаем стороны света (1,2,4,8)
# Смещения координат при движении
OFFSETS = {
	NORTH: ( 0, -1),
	SOUTH: ( 0,  1),
	WEST:  (-1,  0),
	EAST:  ( 1,  0),
}
# Противоположные направления
OPPOSITES = {
	NORTH: SOUTH,
	SOUTH: NORTH,
	WEST:  EAST,
	EAST:  WEST,
}
# Смена направлений при повороте на лево
LEFTS = {
	NORTH: WEST,
	WEST:  SOUTH,
	SOUTH: EAST,
	EAST:  NORTH,
}
# Смена направлений при повороте на право
RIGHTS = {
	NORTH: EAST,
	EAST:  SOUTH,
	SOUTH: WEST,
	WEST:  NORTH,
}


def maze(entrance_to_exit, exit_to_entrance):
	maze = defaultdict(int) # Создаем словарь
	x, y = 0, -1
	direction = SOUTH # Начальное направление 
	for path in [entrance_to_exit, exit_to_entrance]: # Проходим по каждому лабириниту
		for c in path: # Проходим по каждому значению
      # Двигаемся впред
			if c == "W":
				dx, dy = OFFSETS[direction]
				x += dx
				y += dy
				maze[x, y] |= OPPOSITES[direction] # Записываем направлений для каждой комнаты и каждого лабиринта(прямого, обратного)
			elif c == "L":
				direction = LEFTS[direction]
			elif c == "R":
				direction = RIGHTS[direction]
    # До ходим до конца лабиринта, меняем направление на противоположное
		direction = OPPOSITES[direction]
		del maze[(x, y)] # Удаляем не нужную комнату (Выход)
	xs = sorted(set(x for x, _ in iter(maze.keys())))
	ys = sorted(set(y for _, y in iter(maze.keys())))
	# Возращаем значения в выходной файл
	return "\n".join("".join("%x" % maze[x, y] for x in xs) for y in ys)

N = int(fileRead.readline())
for X in range(N):
	fileWrite.write("Case #%s:" % (X+1)+'\n')
	fileWrite.write(maze(*fileRead.readline().split(' '))+'\n') 

