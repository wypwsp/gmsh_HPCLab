import numpy as np
import gmsh
gmsh.initialize()
gmsh.model.add("rectangular1")

# 地层高度 地层宽度 结构埋深
height_ground = 90.0
width_ground = 150.0
buried_depth = 20.0
# 跨度 高度
spans = np.array([30, 5, 10, 5])
floors = np.array([10, 5, 10])
# 土体网格密度（推荐0.2-1.5）
mesh_seed_soil = 1.2
# 结构网格密度
mesh_seed_structure = 1.


# default parameters
w = np.sum(spans)
h = np.sum(floors)
span_num = (np.shape(spans)[0])
floor_num = (np.shape(floors)[0])
mesh_coef = 0.0053 * mesh_seed_soil ** 3 + 0.012 * mesh_seed_soil ** 2 + 0.0067 * mesh_seed_soil + 1.006
mesh_coef_vertical = mesh_coef
mesh_coef_horizontal = mesh_coef

# gmsh code
gmsh.model.geo.addPoint(0, 0, 0,                                                       tag=1)
gmsh.model.geo.addPoint(width_ground, 0, 0,                                            tag=2)
gmsh.model.geo.addPoint(width_ground, height_ground, 0,                                tag=3)
gmsh.model.geo.addPoint(0, height_ground, 0,                                           tag=4)
gmsh.model.geo.addPoint(0, height_ground - buried_depth, 0,                            tag=5)
gmsh.model.geo.addPoint(0, height_ground - buried_depth - h, 0,                        tag=6)
gmsh.model.geo.addPoint(width_ground / 2 - w / 2, 0, 0,                                tag=7)
gmsh.model.geo.addPoint(width_ground / 2 + w / 2, 0, 0,                                tag=8)
gmsh.model.geo.addPoint(width_ground, height_ground - buried_depth - h, 0,             tag=9)
gmsh.model.geo.addPoint(width_ground, height_ground - buried_depth, 0,                 tag=10)
gmsh.model.geo.addPoint(width_ground / 2 + w / 2, height_ground, 0,                    tag=11)
gmsh.model.geo.addPoint(width_ground / 2 - w / 2, height_ground, 0,                    tag=12)
gmsh.model.geo.addPoint(width_ground / 2 - w / 2, height_ground - buried_depth, 0,     tag=101)
gmsh.model.geo.addPoint(width_ground / 2 - w / 2, height_ground - buried_depth - h, 0, tag=102)
gmsh.model.geo.addPoint(width_ground / 2 + w / 2, height_ground - buried_depth - h, 0, tag=103)
gmsh.model.geo.addPoint(width_ground / 2 + w / 2, height_ground - buried_depth,     0, tag=104)
for i in range(span_num - 1):
    # span_num为跨数, 跨数-1即为需要补充的点数
    gmsh.model.geo.addPoint(width_ground / 2 - w / 2 + np.sum(spans[0: i + 1]), height_ground, 0,                     tag=201 + i)
    gmsh.model.geo.addPoint(width_ground / 2 - w / 2 + np.sum(spans[0: i + 1]), height_ground - buried_depth, 0,      tag=301 + i)
    gmsh.model.geo.addPoint(width_ground / 2 - w / 2 + np.sum(spans[0: i + 1]), height_ground - buried_depth - h, 0,  tag=401 + i)
    gmsh.model.geo.addPoint(width_ground / 2 - w / 2 + np.sum(spans[0: i + 1]), 0, 0,                                 tag=501 + i)
for i in range(floor_num - 1):
    # span_num为层数, 层数-1即为需要补充的点数
    gmsh.model.geo.addPoint(0, height_ground - buried_depth - h + np.sum(floors[0: i + 1]), 0,                        tag=601 + i)
    gmsh.model.geo.addPoint(width_ground / 2 - w / 2, height_ground - buried_depth - h + np.sum(floors[0: i + 1]), 0, tag=701 + i)
    gmsh.model.geo.addPoint(width_ground / 2 + w / 2, height_ground - buried_depth - h + np.sum(floors[0: i + 1]), 0, tag=801 + i)
    gmsh.model.geo.addPoint(width_ground, height_ground - buried_depth - h + np.sum(floors[0: i + 1]), 0,             tag=901 + i)
# inner structural points
for i in range(floor_num - 1):
    for j in range(span_num - 1):
        tag = 1000 + 10 * i + j + 1
        gmsh.model.geo.addPoint(width_ground / 2 - w / 2 + np.sum(spans[0: j + 1]), height_ground - buried_depth - h + np.sum(floors[0: i + 1]), 0, tag=tag)


for i in range(span_num):
    if span_num == 1:
        gmsh.model.geo.addLine(12, 11,   tag=200)
        gmsh.model.geo.addLine(101, 104, tag=300)
        gmsh.model.geo.addLine(102, 103, tag=400)
        gmsh.model.geo.addLine(7, 8,     tag=500)
    else:
        if i == 0:
            gmsh.model.geo.addLine(12, 201, tag=200)
            gmsh.model.geo.addLine(101, 301, tag=300)
            gmsh.model.geo.addLine(102, 401, tag=400)
            gmsh.model.geo.addLine(7, 501, tag=500)
        elif i == span_num - 1:
            gmsh.model.geo.addLine(200 + i, 11, tag=200 + i)
            gmsh.model.geo.addLine(300 + i, 104, tag=300 + i)
            gmsh.model.geo.addLine(400 + i, 103, tag=400 + i)
            gmsh.model.geo.addLine(500 + i, 8, tag=500 + i)
            # 竖向
            gmsh.model.geo.addLine(300 + i, 200 + i, tag=10 * (200 + i))
            gmsh.model.geo.addLine(400 + i, 500 + i, tag=10 * (500 + i))
        else:
            gmsh.model.geo.addLine(200 + i, 201 + i, tag=200 + i)
            gmsh.model.geo.addLine(300 + i, 301 + i, tag=300 + i)
            gmsh.model.geo.addLine(400 + i, 401 + i, tag=400 + i)
            gmsh.model.geo.addLine(500 + i, 501 + i, tag=500 + i)
            # 竖向
            gmsh.model.geo.addLine(300 + i, 200 + i, tag=10 * (200 + i))
            gmsh.model.geo.addLine(400 + i, 500 + i, tag=10 * (500 + i))
for i in range(floor_num):
    if floor_num == 1:
        gmsh.model.geo.addLine(6, 5,     tag=600)
        gmsh.model.geo.addLine(102, 101, tag=700)
        gmsh.model.geo.addLine(103, 104, tag=800)
        gmsh.model.geo.addLine(9, 10,    tag=900)
    else:
        if i == 0:
            gmsh.model.geo.addLine(6, 601, tag=600)
            gmsh.model.geo.addLine(102, 701, tag=700)
            gmsh.model.geo.addLine(103, 801, tag=800)
            gmsh.model.geo.addLine(9, 901, tag=900)
        elif i == floor_num - 1:
            gmsh.model.geo.addLine(600 + i, 5, tag=600 + i)
            gmsh.model.geo.addLine(700 + i, 101, tag=700 + i)
            gmsh.model.geo.addLine(800 + i, 104, tag=800 + i)
            gmsh.model.geo.addLine(900 + i, 10, tag=900 + i)
            # 横向
            gmsh.model.geo.addLine(700 + i, 600 + i, tag=10 * (600 + i))
            gmsh.model.geo.addLine(800 + i, 900 + i, tag=10 * (900 + i))
        else:
            gmsh.model.geo.addLine(600 + i, 601 + i, tag=600 + i)
            gmsh.model.geo.addLine(700 + i, 701 + i, tag=700 + i)
            gmsh.model.geo.addLine(800 + i, 801 + i, tag=800 + i)
            gmsh.model.geo.addLine(900 + i, 901 + i, tag=900 + i)
            # 横向
            gmsh.model.geo.addLine(700 + i, 600 + i, tag=10 * (600 + i))
            gmsh.model.geo.addLine(800 + i, 900 + i, tag=10 * (900 + i))
gmsh.model.geo.addLine(12, 4,    tag=1)
gmsh.model.geo.addLine(7, 1,     tag=2)
gmsh.model.geo.addLine(11, 3,    tag=3)
gmsh.model.geo.addLine(8, 2,     tag=4)
gmsh.model.geo.addLine(5, 4,     tag=5)
gmsh.model.geo.addLine(6, 1,     tag=6)
gmsh.model.geo.addLine(10, 3,    tag=7)
gmsh.model.geo.addLine(9, 2,     tag=8)
gmsh.model.geo.addLine(101, 12,  tag=2000)
gmsh.model.geo.addLine(104, 11,  tag=2100)
gmsh.model.geo.addLine(102, 6,   tag=6000)
gmsh.model.geo.addLine(101, 5,   tag=6100)
gmsh.model.geo.addLine(102, 7,   tag=5000)
gmsh.model.geo.addLine(103, 8,   tag=5100)
gmsh.model.geo.addLine(103, 9,   tag=9000)
gmsh.model.geo.addLine(104, 10,  tag=9100)
for i in range(floor_num - 1):
    for j in range(span_num):
        if span_num != 1:
            if j == 0:
                gmsh.model.geo.addLine(701 + i, 1001 + 10 * i, tag=1000+10*i)
            elif j == span_num - 1:
                gmsh.model.geo.addLine(1000 + 10 * i + j, 801 + i, tag=1000+10*i+j)
            else:
                gmsh.model.geo.addLine(1000 + 10 * i + j, 1001 + 10 * i + j, tag=1000+10*i+j)
        else:
            gmsh.model.geo.addLine(701 + i, 801 + i, tag=1000 + 10 * i)
for i in range(span_num - 1):
    for j in range(floor_num):
        if floor_num != 1:
            if j == 0:
                gmsh.model.geo.addLine(401 + i, 1001 + i, tag=1100+i)
            elif j == floor_num - 1:
                gmsh.model.geo.addLine(991 + 10 * j + i, 301 + i, tag=1100+10*j+i)
            else:
                gmsh.model.geo.addLine(991 + 10 * j + i, 1001 + 10 * j + i, tag=1100+10*j+i)
        else:
            gmsh.model.geo.addLine(401 + i, 301 + i, tag=1100+10*j+i)


gmsh.model.geo.addCurveLoop([1, -5, -6100, 2000], 1)
gmsh.model.geo.addCurveLoop([6000, 6, -2, -5000], 2)
gmsh.model.geo.addCurveLoop([5100, 4, -8, -9000], 3)
gmsh.model.geo.addCurveLoop([9100, 7, -3, -2100], 4)
for i in range(floor_num - 1):
    gmsh.model.geo.addCurveLoop([-6000 - 10 * i, 700 + i, 6010 + 10 * i, -600 - i], 501 + i)
    gmsh.model.geo.addCurveLoop([9000 + 10 * i, 900 + i, -9010 - 10 * i, -800 - i], 701 + i)
gmsh.model.geo.addCurveLoop([-6000 - 10 * (floor_num - 1), 700 + (floor_num - 1), 6100, -600 - (floor_num - 1)], 510)
gmsh.model.geo.addCurveLoop([9000 + 10 * (floor_num - 1), 900 + (floor_num - 1), -9100, -800 - (floor_num - 1)], 710)
for i in range(span_num - 1):
    gmsh.model.geo.addCurveLoop([-2000 - 10 * i, 300 + i, 2010 + 10 * i, -200 - i], 801 + i)
    gmsh.model.geo.addCurveLoop([5000 + 10 * i, 500 + i, -5010 - 10 * i, -400 - i], 601 + i)
gmsh.model.geo.addCurveLoop([-2000 - 10 * (span_num - 1), 300 + (span_num - 1), 2100, -200 - (span_num - 1)], 810)
gmsh.model.geo.addCurveLoop([5000 + 10 * (span_num - 1), 500 + (span_num - 1), -5100, -400 - (span_num - 1)], 610)


gmsh.model.geo.addPlaneSurface([1], 1)
gmsh.model.geo.addPlaneSurface([2], 2)
gmsh.model.geo.addPlaneSurface([3], 3)
gmsh.model.geo.addPlaneSurface([4], 4)
for i in range(floor_num - 1):
    gmsh.model.geo.addPlaneSurface([501 + i], 501 + i)
    gmsh.model.geo.addPlaneSurface([701 + i], 701 + i)
gmsh.model.geo.addPlaneSurface([510], 510)
gmsh.model.geo.addPlaneSurface([710], 710)
for i in range(span_num - 1):
    gmsh.model.geo.addPlaneSurface([601 + i], 601 + i)
    gmsh.model.geo.addPlaneSurface([801 + i], 801 + i)
gmsh.model.geo.addPlaneSurface([610], 610)
gmsh.model.geo.addPlaneSurface([810], 810)


gmsh.model.geo.synchronize()
gmsh.model.mesh.setRecombine(2, 1)
gmsh.model.mesh.setRecombine(2, 2)
gmsh.model.mesh.setRecombine(2, 3)
gmsh.model.mesh.setRecombine(2, 4)
for i in range(floor_num - 1):
    gmsh.model.mesh.setRecombine(2, 501 + i)
    gmsh.model.mesh.setRecombine(2, 701 + i)
for i in range(span_num - 1):
    gmsh.model.mesh.setRecombine(2, 601 + i)
    gmsh.model.mesh.setRecombine(2, 801 + i)
gmsh.model.mesh.setRecombine(2, 510)
gmsh.model.mesh.setRecombine(2, 610)
gmsh.model.mesh.setRecombine(2, 710)
gmsh.model.mesh.setRecombine(2, 810)


gmsh.model.mesh.setAlgorithm(2, 1, 9)
gmsh.model.mesh.setAlgorithm(2, 2, 9)
gmsh.model.mesh.setAlgorithm(2, 3, 9)
gmsh.model.mesh.setAlgorithm(2, 4, 9)
for i in range(floor_num - 1):
    gmsh.model.mesh.setAlgorithm(2, 501 + i, 9)
    gmsh.model.mesh.setAlgorithm(2, 701 + i, 9)
for i in range(span_num - 1):
    gmsh.model.mesh.setAlgorithm(2, 601 + i, 9)
    gmsh.model.mesh.setAlgorithm(2, 801 + i, 9)
gmsh.model.mesh.setAlgorithm(2, 510, 9)
gmsh.model.mesh.setAlgorithm(2, 610, 9)
gmsh.model.mesh.setAlgorithm(2, 710, 9)
gmsh.model.mesh.setAlgorithm(2, 810, 9)


# 左右侧水平线
n0 = int(np.ceil(width_ground / 3 / mesh_seed_soil))
for i in range(floor_num):
    gmsh.model.mesh.setTransfiniteCurve(6000 + 10 * i, n0, coef=mesh_coef_horizontal)
    gmsh.model.mesh.setTransfiniteCurve(9000 + 10 * i, n0, coef=mesh_coef_horizontal)
gmsh.model.mesh.setTransfiniteCurve(6100, n0, coef=mesh_coef_horizontal)
gmsh.model.mesh.setTransfiniteCurve(9100, n0, coef=mesh_coef_horizontal)
gmsh.model.mesh.setTransfiniteCurve(1, n0, coef=mesh_coef_horizontal)
gmsh.model.mesh.setTransfiniteCurve(2, n0, coef=mesh_coef_horizontal)
gmsh.model.mesh.setTransfiniteCurve(3, n0, coef=mesh_coef_horizontal)
gmsh.model.mesh.setTransfiniteCurve(4, n0, coef=mesh_coef_horizontal)
# 上侧竖向线
n1 = int(np.ceil(buried_depth / mesh_seed_soil)) + 1
for i in range(span_num):
    gmsh.model.mesh.setTransfiniteCurve(2000 + 10 * i, n1, coef=mesh_coef_vertical)
gmsh.model.mesh.setTransfiniteCurve(2100, n1, coef=mesh_coef_vertical)
gmsh.model.mesh.setTransfiniteCurve(5, n1, coef=mesh_coef_vertical)
gmsh.model.mesh.setTransfiniteCurve(7, n1, coef=mesh_coef_vertical)
# 下侧竖向线
n2 = int(np.ceil((height_ground - buried_depth - h) / 1.5 / mesh_seed_soil)) + 1
for i in range(span_num):
    gmsh.model.mesh.setTransfiniteCurve(5000 + 10 * i, n2, coef=mesh_coef_vertical)
gmsh.model.mesh.setTransfiniteCurve(5100, n2, coef=mesh_coef_vertical)
gmsh.model.mesh.setTransfiniteCurve(6, n2, coef=mesh_coef_vertical)
gmsh.model.mesh.setTransfiniteCurve(8, n2, coef=mesh_coef_vertical)
# 水平结构线 (四组)
for i in range(span_num):
    n3 = int(np.ceil(spans[i] / mesh_seed_soil)) + 1
    gmsh.model.mesh.setTransfiniteCurve(200 + i, n3)
    gmsh.model.mesh.setTransfiniteCurve(300 + i, n3)
    gmsh.model.mesh.setTransfiniteCurve(400 + i, n3)
    gmsh.model.mesh.setTransfiniteCurve(500 + i, n3)
# 竖直结构线 (四组)
for i in range(floor_num):
    n4 = int(np.ceil(floors[i] / mesh_seed_soil)) + 1
    gmsh.model.mesh.setTransfiniteCurve(600 + i, n4)
    gmsh.model.mesh.setTransfiniteCurve(700 + i, n4)
    gmsh.model.mesh.setTransfiniteCurve(800 + i, n4)
    gmsh.model.mesh.setTransfiniteCurve(900 + i, n4)
# 梁柱单元
for i in range(floor_num - 1):
    for j in range(span_num):
        if span_num != 1:
            if j == 0:
                gmsh.model.mesh.setTransfiniteCurve(1000+10*i, int(np.ceil(spans[j] / mesh_seed_structure)))
            elif j == span_num - 1:
                gmsh.model.mesh.setTransfiniteCurve(1000+10*i+j, int(np.ceil(spans[j] / mesh_seed_structure)))
            else:
                gmsh.model.mesh.setTransfiniteCurve(1000+10*i+j, int(np.ceil(spans[j] / mesh_seed_structure)))
        else:
            gmsh.model.mesh.setTransfiniteCurve(1000 + 10 * i, int(np.ceil(spans[j] / mesh_seed_structure)))
for i in range(span_num - 1):
    for j in range(floor_num):
        if floor_num != 1:
            if j == 0:
                gmsh.model.mesh.setTransfiniteCurve(1100+i, int(np.ceil(floors[j] / mesh_seed_structure)))
            elif j == floor_num - 1:
                gmsh.model.mesh.setTransfiniteCurve(1100+10*j+i, int(np.ceil(floors[j] / mesh_seed_structure)))
            else:
                gmsh.model.mesh.setTransfiniteCurve(1100+10*j+i, int(np.ceil(floors[j] / mesh_seed_structure)))
        else:
            gmsh.model.mesh.setTransfiniteCurve(1100+10*j+i, int(np.ceil(floors[j] / mesh_seed_structure)))


for i in range(floor_num - 1):
    gmsh.model.mesh.setTransfiniteSurface(501 + i)
    gmsh.model.mesh.setTransfiniteSurface(701 + i)
for i in range(span_num - 1):
    gmsh.model.mesh.setTransfiniteSurface(601 + i)
    gmsh.model.mesh.setTransfiniteSurface(801 + i)
gmsh.model.mesh.setTransfiniteSurface(1)
gmsh.model.mesh.setTransfiniteSurface(2)
gmsh.model.mesh.setTransfiniteSurface(3)
gmsh.model.mesh.setTransfiniteSurface(4)
gmsh.model.mesh.setTransfiniteSurface(510)
gmsh.model.mesh.setTransfiniteSurface(610)
gmsh.model.mesh.setTransfiniteSurface(710)
gmsh.model.mesh.setTransfiniteSurface(810)

# 记录所有土-结构接触土体节点
top_array = [300]
bottom_array = [400]
right_array = [800]
left_array = [700]
for i in range(span_num - 1):
    top_array.append(301 + i)
    bottom_array.append(401 + i)
for i in range(floor_num - 1):
    right_array.append(801 + i)
    left_array.append(701 + i)
gmsh.model.addPhysicalGroup(1, top_array, 1)
gmsh.model.addPhysicalGroup(1, bottom_array, 2)
gmsh.model.addPhysicalGroup(1, left_array, 3)
gmsh.model.addPhysicalGroup(1, right_array, 4)
gmsh.model.addPhysicalGroup(1, top_array + bottom_array + left_array + right_array, 5)
# 记录所有土-结构接触结构节点
for i in range(span_num - 1):
    gmsh.model.addPhysicalGroup(0, [301 + i], 301 + i)
    gmsh.model.addPhysicalGroup(0, [401 + i], 401 + i)
for i in range(floor_num - 1):
    gmsh.model.addPhysicalGroup(0, [701 + i], 701 + i)
    gmsh.model.addPhysicalGroup(0, [801 + i], 801 + i)
gmsh.model.addPhysicalGroup(0, [101], 101)
gmsh.model.addPhysicalGroup(0, [102], 102)
gmsh.model.addPhysicalGroup(0, [103], 103)
gmsh.model.addPhysicalGroup(0, [104], 104)
# 记录所有结构节点 (含接触部分)
structure_array = []
for i in range(floor_num - 1):
    for j in range(span_num):
        if span_num != 1:
            if j == 0:
                structure_array.append(1000+10*i)
            elif j == span_num - 1:
                structure_array.append(1000+10*i+j)
            else:
                structure_array.append(1000+10*i+j)
        else:
            structure_array.append(1000 + 10 * i)
for i in range(span_num - 1):
    for j in range(floor_num):
        if floor_num != 1:
            if j == 0:
                structure_array.append(1100+i)
            elif j == floor_num - 1:
                structure_array.append(1100+10*j+i)
            else:
                structure_array.append(1100+10*j+i)
        else:
            structure_array.append(1100+10*j+i)

gmsh.model.addPhysicalGroup(1, structure_array + top_array + bottom_array + left_array + right_array, 100)
gmsh.model.mesh.generate(2)


gmsh.model.geo.synchronize()
gmsh.fltk.run()
gmsh.write('test_export.inp')
gmsh.finalize()


