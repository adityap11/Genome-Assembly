# python3

#incomplete as of now

import sys
from math import *
from itertools import permutations



class PuzzleAssembly:
    # up: 0
    # left: 1
    # down: 2
    # right: 3
    def __init__(self):
        n, blocks = self._input()
        ans = self.solve(n, blocks)
        self.printResult(ans, blocks)

    def _input(self):
        data = sys.stdin.read().strip().split('\n')
        n = int(sqrt(len(data)))
        blocks = []
        for d in data:
            blocks.append(d[1:-1].split(','))
        return n, blocks

    def solve(self, n, blocks):
        ans = [[None for _ in range(n)] for __ in range(n)]
        border = [[] for _ in range(4)]
        edge = [[0 for _ in range(2)] for __ in range(4)]
        for i in range(len(blocks)):
            if 'black' == blocks[i][0]:
                if 'black' == blocks[i][1]:
                    ans[0][0] = i
                    edge[0][0] = i
                    edge[1][0] = i
                elif 'black' == blocks[i][3]:
                    ans[0][n-1] = i
                    edge[0][1] = i
                    edge[3][0] = i
                else:
                    border[0].append(i)
            elif 'black' == blocks[i][2]:
                if 'black' == blocks[i][1]:
                    ans[n-1][0] = i
                    edge[1][1] = i
                    edge[2][0] = i
                elif 'black' == blocks[i][3]:
                    ans[n-1][n-1] = i
                    edge[2][1] = i
                    edge[3][1] = i
                else:
                    border[2].append(i)
            elif 'black' == blocks[i][1]:
                border[1].append(i)
            elif 'black' == blocks[i][3]:
                border[3].append(i)
        idx = [(1, 3), (0, 2), (1, 3), (0, 2)]
        idx2 = [list(zip([0]*n, range(n))), list(zip(range(n), [0]*n)), list(zip([n-1]*n, range(n))), list(zip(range(n), [n-1]*n))]
        correctBorder = []
        for i in range(4):
            for p in permutations(border[i]):
                p = [edge[i][0]] + list(p) + [edge[i][1]]
                isCorrect = True
                for j in range(len(p)-1):
                    if blocks[p[j]][idx[i][1]] != blocks[p[j+1]][idx[i][0]]:
                        isCorrect = False
                        break
                if isCorrect:
                    #print(p)
                    for j in range(len(p)):
                        ans[idx2[i][j][0]][idx2[i][j][1]] = p[j]
        solved = set()
        for a in ans:
            for i in a:
                if None != i:
                    solved.add(i)
        unsolved = [i for i in range(len(blocks)) if not i in solved]
    
    def printResult(self, ans, block):
        for i, a in enumerate(ans):
            print(';'.join(['('+','.join(block[ans[i][j]])+')' for j in range(len(ans))]))

if __name__ == "__main__":
    PuzzleAssembly()