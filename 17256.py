# 달달함이 넘쳐흘러
a_x, a_y, a_z = map(int, input().split())
c_x, c_y, c_z = map(int, input().split())

print(c_x - a_z, c_y // a_y, c_z - a_x)