grid1 = [[3,6,15,1,5,10,6],
	[9,19,7,5,11,8,6],
	[6,8,9,9,2,9,5],
	[7,2,12,8,4,8,7],
	[2,8,7,7,1,2,7]]

grid=[[8,8,9,7,9,9,9],
	[8,8,7,7,8,8,9],
	[6,6,7,9,7,6,9],
	[8,7,7,8,7,8,9],
	[8,7,7,9,8,6,9]]

goals=[(-1,1),(-1,2),(-1,3),(-2,1),(-2,2),(-2,3)]

inp = input().split()
horse = inp[0]
horse_sum = int(inp[1])
pos=(7,int(inp[2]))

peg_movemap=[(3,1),(-3, 1),(3,-1),(-3,-1),(1,3),(-1,3),(1,-3),(-1,-3)]
hor_movemap=[(2,1),(-2, 1),(2,-1),(-2,-1),(1,2),(-1,2),(1,-2),(-1,-2)]

if horse == "p":
    movemap = peg_movemap
else:
    movemap = hor_movemap

def findAllPossibilities(current):
    new_poses=[]
    for move in movemap:
        new_pos = (current[0]+move[0], current[1]+move[1])
        new_poses.append(new_pos)
    return new_poses

def findPossibilities(current, illegals):
    new_poses=[]
    for move in movemap:
        new_pos = (current[0]+move[0], current[1]+move[1])
        if new_pos[0] >= 0 and new_pos[0] < len(grid[0]) and  new_pos[1] >= 0 and new_pos[1] < len(grid) and new_pos not in illegals:
            new_poses.append(new_pos)
    return new_poses

solution = []

def solve(pos_chain, current_sum, illegals):
    print("solving... x= " + str(pos_chain[-1][0]) + ", y= " + str(pos_chain[-1][1]))
    for move in findPossibilities(pos_chain[-1], illegals):
        if len(pos_chain) == 1:
            print("\n")
        if current_sum + grid[move[1]][move[0]] == horse_sum and len(set(goals) & set(findAllPossibilities(move))) > 0:
            solution.append(pos_chain + [move])
        elif current_sum + grid[move[1]][move[0]] < horse_sum:
            solve(pos_chain+[(move)], current_sum + grid[move[1]][move[0]], illegals + [move])

solve([pos], 0, [])

for s in solution:
    for o in s:
        print(str(o) + ", ")
    print("\n")


