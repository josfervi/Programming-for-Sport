class BinTree(object):
    
    def __init__(self, serialized = None):
        if serialized:
            self.serialized = serialized
        else:
            sefl.serialized = []
    
    def __str__(self):
        return str(self.serialized)

bt = BinTree([1,2,3,4,5,6,7,8])


# ....... 111111111111111........
# ......./////.......\\\\\.......
# ......22222.........33333......
# ...../....|.........|....\.....
# ....4.....5.........6.....7....
# .../|.....|\......./|.....|\...
# ..8.9.....a.b.....c.d.....e.f..
# ./|.|\.../|.|\.../|.|\.../|.|\.
# g.h.i.j.k.l.m.n.o.p.q.r.s.t.u.v


#     1
#   / \
#   2   3
#  /|   |\
# 4 5   6 7


five_level_bt = '''
.......................1.......................
....................../.\......................
...................../...\.....................
..................../.....\....................
.................../.......\...................
................../.........\..................
................./...........\.................
................/.............\................
.............../...............\...............
............../.................\..............
............./...................\.............
............/.....................\............
...........2.......................3...........
........../.\...................../.\..........
........./...\.................../...\.........
......../.....\................./.....\........
......./.......\.............../.......\.......
....../.........\............./.........\......
.....4...........5...........6...........7.....
..../.\........./.\........./.\........./.\....
.../...\......./...\......./...\......./...\...
..8.....9.....a.....b.....c.....d.....e.....f..
./.\.../.\.../.\.../.\.../.\.../.\.../.\.../.\.
g...h.i...j.k...l.m...n.o...p.q...r.s...t.u...v
'''

five_level_bt_levels = five_level_bt.strip().split('\n')

def double_each_line(lst):
    for i, line in enumerate(lst):
        lst[i] += '  ' + line

six_level_bt_levels_without_root = five_level_bt_levels
double_each_line(six_level_bt_levels_without_root)
six_level_bt_without_root = '\n'.join(six_level_bt_levels_without_root)

print six_level_bt_without_root