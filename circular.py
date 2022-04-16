import gmsh
import sys

# Before using any functions in the Python API, Gmsh must be initialized:
gmsh.initialize()
gmsh.model.add("circular2")

# geological parameters
radius = 6.0
height = 70.0
width = 150.0
buried_depth = 16.0

# mesh parameters
mesh_coef_horizontal = 1.035
mesh_coef_vertical = 1.06

# constants(no modifications unless necessary)
bias_coef = 0.8
sqrt2 = 1.414213562373095
bias = radius * (1. + bias_coef)

gmsh.model.geo.addPoint(0, 0, 0, tag=1)
gmsh.model.geo.addPoint(width, 0, 0, tag=2)
gmsh.model.geo.addPoint(width, height, 0, tag=3)
gmsh.model.geo.addPoint(0, height, 0, tag=4)
gmsh.model.geo.addPoint(width / 2, 0, 0, tag=5)
gmsh.model.geo.addPoint(width / 2, height, 0, tag=6)
gmsh.model.geo.addPoint(0, 70 - buried_depth - radius, 0, tag=7)
gmsh.model.geo.addPoint(width, 70 - buried_depth - radius, 0, tag=8)

gmsh.model.geo.addPoint(width / 2 - bias, 70 - buried_depth - radius - bias, 0, tag=11)
gmsh.model.geo.addPoint(width / 2 + bias, 70 - buried_depth - radius - bias, 0, tag=12)
gmsh.model.geo.addPoint(width / 2 + bias, 70 - buried_depth - radius + bias, 0, tag=13)
gmsh.model.geo.addPoint(width / 2 - bias, 70 - buried_depth - radius + bias, 0, tag=14)
gmsh.model.geo.addPoint(width / 2, 70 - buried_depth - radius - bias, 0, tag=15)
gmsh.model.geo.addPoint(width / 2 + bias, 70 - buried_depth - radius, 0, tag=16)
gmsh.model.geo.addPoint(width / 2, 70 - buried_depth - radius + bias, 0, tag=17)
gmsh.model.geo.addPoint(width / 2 - bias, 70 - buried_depth - radius, 0, tag=18)

gmsh.model.geo.addPoint(0, 70 - buried_depth - radius - bias, 0, tag=21)
gmsh.model.geo.addPoint(0, 70 - buried_depth - radius + bias, 0, tag=22)
gmsh.model.geo.addPoint(width, 70 - buried_depth - radius - bias, 0, tag=23)
gmsh.model.geo.addPoint(width, 70 - buried_depth - radius + bias, 0, tag=24)
gmsh.model.geo.addPoint(width / 2 - bias, 0, 0, tag=25)
gmsh.model.geo.addPoint(width / 2 + bias, 0, 0, tag=26)
gmsh.model.geo.addPoint(width / 2 - bias, height, 0, tag=27)
gmsh.model.geo.addPoint(width / 2 + bias, height, 0, tag=28)

gmsh.model.geo.addPoint(width / 2 + radius, 70 - buried_depth - radius, 0, tag=31)
gmsh.model.geo.addPoint(width / 2 + 0.5 * sqrt2 * radius, 70 - buried_depth - radius + 0.5 * sqrt2 * radius, 0, tag=32)
gmsh.model.geo.addPoint(width / 2, 70 - buried_depth, 0, tag=33)
gmsh.model.geo.addPoint(width / 2 - 0.5 * sqrt2 * radius, 70 - buried_depth - radius + 0.5 * sqrt2 * radius, 0, tag=34)
gmsh.model.geo.addPoint(width / 2 - radius, 70 - buried_depth - radius, 0, tag=35)
gmsh.model.geo.addPoint(width / 2 - 0.5 * sqrt2 * radius, 70 - buried_depth - radius - 0.5 * sqrt2 * radius, 0, tag=36)
gmsh.model.geo.addPoint(width / 2, 70 - buried_depth - radius * 2, 0, tag=37)
gmsh.model.geo.addPoint(width / 2 + 0.5 * sqrt2 * radius, 70 - buried_depth - radius - 0.5 * sqrt2 * radius, 0, tag=38)
gmsh.model.geo.addPoint(width / 2, 70 - buried_depth - radius, 0, tag=40)

gmsh.model.geo.addLine(27, 4  , tag=1)
gmsh.model.geo.addLine(14, 22 , tag=2)
gmsh.model.geo.addLine(18, 7  , tag=3)
gmsh.model.geo.addLine(11, 21 , tag=4)
gmsh.model.geo.addLine(25, 1  , tag=5)
gmsh.model.geo.addLine(28, 3  , tag=6)
gmsh.model.geo.addLine(13, 24 , tag=7)
gmsh.model.geo.addLine(16, 8  , tag=8)
gmsh.model.geo.addLine(12, 23 , tag=9)
gmsh.model.geo.addLine(26, 2  , tag=10)
gmsh.model.geo.addLine(4 , 22 , tag=11)
gmsh.model.geo.addLine(22, 7  , tag=12)
gmsh.model.geo.addLine(7 , 21 , tag=13)
gmsh.model.geo.addLine(21, 1  , tag=14)
gmsh.model.geo.addLine(3 , 24 , tag=15)
gmsh.model.geo.addLine(24, 8  , tag=16)
gmsh.model.geo.addLine(8 , 23 , tag=17)
gmsh.model.geo.addLine(23, 2  , tag=18)

gmsh.model.geo.addCircleArc(31, 40, 32, tag=21)
gmsh.model.geo.addCircleArc(32, 40, 33, tag=22)
gmsh.model.geo.addCircleArc(33, 40, 34, tag=23)
gmsh.model.geo.addCircleArc(34, 40, 35, tag=24)
gmsh.model.geo.addCircleArc(35, 40, 36, tag=25)
gmsh.model.geo.addCircleArc(36, 40, 37, tag=26)
gmsh.model.geo.addCircleArc(37, 40, 38, tag=27)
gmsh.model.geo.addCircleArc(38, 40, 31, tag=28)

gmsh.model.geo.addLine(6, 27,  tag=29)
gmsh.model.geo.addLine(17, 14, tag=30)
gmsh.model.geo.addLine(15, 11, tag=31)
gmsh.model.geo.addLine(5, 25,  tag=32)
gmsh.model.geo.addLine(6, 28,  tag=33)
gmsh.model.geo.addLine(17, 13, tag=34)
gmsh.model.geo.addLine(15, 12, tag=35)
gmsh.model.geo.addLine(5, 26,  tag=36)
gmsh.model.geo.addLine(31, 16, tag=37)
gmsh.model.geo.addLine(32, 13, tag=38)
gmsh.model.geo.addLine(33, 17, tag=39)
gmsh.model.geo.addLine(34, 14, tag=40)
gmsh.model.geo.addLine(35, 18, tag=41)
gmsh.model.geo.addLine(36, 11, tag=42)
gmsh.model.geo.addLine(37, 15, tag=43)
gmsh.model.geo.addLine(38, 12, tag=44)
gmsh.model.geo.addLine(16, 12, tag=45)
gmsh.model.geo.addLine(16, 13, tag=46)
gmsh.model.geo.addLine(18, 14, tag=47)
gmsh.model.geo.addLine(18, 11, tag=48)
gmsh.model.geo.addLine(14, 27, tag=49)
gmsh.model.geo.addLine(17, 6,  tag=50)
gmsh.model.geo.addLine(13, 28, tag=51)
gmsh.model.geo.addLine(11, 25, tag=52)
gmsh.model.geo.addLine(15, 5,  tag=53)
gmsh.model.geo.addLine(12, 26, tag=54)

gmsh.model.geo.addCurveLoop([1, 11, -2, 49], 1)
gmsh.model.geo.addCurveLoop([2, 12, -3, 47], 2)
gmsh.model.geo.addCurveLoop([3, 13, -4, -48], 3)
gmsh.model.geo.addCurveLoop([4, 14, -5, -52], 4)
gmsh.model.geo.addCurveLoop([29, -49, -30, 50], 5)
gmsh.model.geo.addCurveLoop([30, -40, -23, 39], 6)
gmsh.model.geo.addCurveLoop([40, -47, -41, -24], 7)
gmsh.model.geo.addCurveLoop([41, 48, -42, -25], 8)
gmsh.model.geo.addCurveLoop([26, 43, 31, -42], 9)
gmsh.model.geo.addCurveLoop([31, 52, -32, -53], 10)
gmsh.model.geo.addCurveLoop([33, -51, -34, 50], 11)
gmsh.model.geo.addCurveLoop([34, -38, 22, 39], 12)
gmsh.model.geo.addCurveLoop([38, -46, -37, 21], 13)
gmsh.model.geo.addCurveLoop([37, 45, -44, 28], 14)
gmsh.model.geo.addCurveLoop([27, 44, -35, -43], 15)
gmsh.model.geo.addCurveLoop([35, 54, -36, -53], 16)
gmsh.model.geo.addCurveLoop([6, 15, -7, 51], 17)
gmsh.model.geo.addCurveLoop([7, 16, -8, 46], 18)
gmsh.model.geo.addCurveLoop([8, 17, -9, -45], 19)
gmsh.model.geo.addCurveLoop([9, 18, -10, -54], 20)

ps1 = gmsh.model.geo.addPlaneSurface([1])
ps2 = gmsh.model.geo.addPlaneSurface([2])
ps3 = gmsh.model.geo.addPlaneSurface([3])
ps4 = gmsh.model.geo.addPlaneSurface([4])
ps5 = gmsh.model.geo.addPlaneSurface([5])
ps6 = gmsh.model.geo.addPlaneSurface([6])
ps7 = gmsh.model.geo.addPlaneSurface([7])
ps8 = gmsh.model.geo.addPlaneSurface([8])
ps9 = gmsh.model.geo.addPlaneSurface([9])
ps10 = gmsh.model.geo.addPlaneSurface([10])
ps11 = gmsh.model.geo.addPlaneSurface([11])
ps12 = gmsh.model.geo.addPlaneSurface([12])
ps13 = gmsh.model.geo.addPlaneSurface([13])
ps14 = gmsh.model.geo.addPlaneSurface([14])
ps15 = gmsh.model.geo.addPlaneSurface([15])
ps16 = gmsh.model.geo.addPlaneSurface([16])
ps17 = gmsh.model.geo.addPlaneSurface([17])
ps18 = gmsh.model.geo.addPlaneSurface([18])
ps19 = gmsh.model.geo.addPlaneSurface([19])
ps20 = gmsh.model.geo.addPlaneSurface([20])


gmsh.model.geo.synchronize()
# basic settings
gmsh.model.mesh.setRecombine(2, ps1)
gmsh.model.mesh.setRecombine(2, ps2)
gmsh.model.mesh.setRecombine(2, ps3)
gmsh.model.mesh.setRecombine(2, ps4)
gmsh.model.mesh.setRecombine(2, ps5)
gmsh.model.mesh.setRecombine(2, ps6)
gmsh.model.mesh.setRecombine(2, ps7)
gmsh.model.mesh.setRecombine(2, ps8)
gmsh.model.mesh.setRecombine(2, ps9)
gmsh.model.mesh.setRecombine(2, ps10)
gmsh.model.mesh.setRecombine(2, ps11)
gmsh.model.mesh.setRecombine(2, ps12)
gmsh.model.mesh.setRecombine(2, ps13)
gmsh.model.mesh.setRecombine(2, ps14)
gmsh.model.mesh.setRecombine(2, ps15)
gmsh.model.mesh.setRecombine(2, ps16)
gmsh.model.mesh.setRecombine(2, ps17)
gmsh.model.mesh.setRecombine(2, ps18)
gmsh.model.mesh.setRecombine(2, ps19)
gmsh.model.mesh.setRecombine(2, ps20)

gmsh.model.mesh.setAlgorithm(2, ps1, 9)
gmsh.model.mesh.setAlgorithm(2, ps2, 9)
gmsh.model.mesh.setAlgorithm(2, ps3, 9)
gmsh.model.mesh.setAlgorithm(2, ps4, 9)
gmsh.model.mesh.setAlgorithm(2, ps5, 9)
gmsh.model.mesh.setAlgorithm(2, ps6, 9)
gmsh.model.mesh.setAlgorithm(2, ps7, 9)
gmsh.model.mesh.setAlgorithm(2, ps8, 9)
gmsh.model.mesh.setAlgorithm(2, ps9, 9)
gmsh.model.mesh.setAlgorithm(2, ps10, 9)
gmsh.model.mesh.setAlgorithm(2, ps11, 9)
gmsh.model.mesh.setAlgorithm(2, ps12, 9)
gmsh.model.mesh.setAlgorithm(2, ps13, 9)
gmsh.model.mesh.setAlgorithm(2, ps14, 9)
gmsh.model.mesh.setAlgorithm(2, ps15, 9)
gmsh.model.mesh.setAlgorithm(2, ps16, 9)
gmsh.model.mesh.setAlgorithm(2, ps17, 9)
gmsh.model.mesh.setAlgorithm(2, ps18, 9)
gmsh.model.mesh.setAlgorithm(2, ps19, 9)
gmsh.model.mesh.setAlgorithm(2, ps20, 9)

# horizontal  10
gmsh.model.mesh.setTransfiniteCurve(1, 30, coef=mesh_coef_horizontal)
gmsh.model.mesh.setTransfiniteCurve(2, 30, coef=mesh_coef_horizontal)
gmsh.model.mesh.setTransfiniteCurve(3, 30, coef=mesh_coef_horizontal)
gmsh.model.mesh.setTransfiniteCurve(4, 30, coef=mesh_coef_horizontal)
gmsh.model.mesh.setTransfiniteCurve(5, 30, coef=mesh_coef_horizontal)
gmsh.model.mesh.setTransfiniteCurve(6, 30, coef=mesh_coef_horizontal)
gmsh.model.mesh.setTransfiniteCurve(7, 30, coef=mesh_coef_horizontal)
gmsh.model.mesh.setTransfiniteCurve(8, 30, coef=mesh_coef_horizontal)
gmsh.model.mesh.setTransfiniteCurve(9, 30, coef=mesh_coef_horizontal)
gmsh.model.mesh.setTransfiniteCurve(10, 30, coef=mesh_coef_horizontal)
# vertical 隧道下方土层 5
gmsh.model.mesh.setTransfiniteCurve(14, 20, coef=mesh_coef_vertical)
gmsh.model.mesh.setTransfiniteCurve(52, 20, coef=mesh_coef_vertical)
gmsh.model.mesh.setTransfiniteCurve(53, 20, coef=mesh_coef_vertical)
gmsh.model.mesh.setTransfiniteCurve(54, 20, coef=mesh_coef_vertical)
gmsh.model.mesh.setTransfiniteCurve(18, 20, coef=mesh_coef_vertical)
# horizontal+vertical 加密网格 16
gmsh.model.mesh.setTransfiniteCurve(48, 10)
gmsh.model.mesh.setTransfiniteCurve(47, 10)
gmsh.model.mesh.setTransfiniteCurve(30, 10)
gmsh.model.mesh.setTransfiniteCurve(34, 10)
gmsh.model.mesh.setTransfiniteCurve(46, 10)
gmsh.model.mesh.setTransfiniteCurve(45, 10)
gmsh.model.mesh.setTransfiniteCurve(35, 10)
gmsh.model.mesh.setTransfiniteCurve(31, 10)
gmsh.model.mesh.setTransfiniteCurve(36, 10)
gmsh.model.mesh.setTransfiniteCurve(32, 10)
gmsh.model.mesh.setTransfiniteCurve(29, 10)
gmsh.model.mesh.setTransfiniteCurve(33, 10)
gmsh.model.mesh.setTransfiniteCurve(12, 10)
gmsh.model.mesh.setTransfiniteCurve(13, 10)
gmsh.model.mesh.setTransfiniteCurve(16, 10)
gmsh.model.mesh.setTransfiniteCurve(17, 10)
# vertical 隧道上方土层 5
gmsh.model.mesh.setTransfiniteCurve(11, 10)
gmsh.model.mesh.setTransfiniteCurve(49, 10)
gmsh.model.mesh.setTransfiniteCurve(50, 10)
gmsh.model.mesh.setTransfiniteCurve(51, 10)
gmsh.model.mesh.setTransfiniteCurve(15, 10)
# circular 隧道加密 8
gmsh.model.mesh.setTransfiniteCurve(24, 10)
gmsh.model.mesh.setTransfiniteCurve(23, 10)
gmsh.model.mesh.setTransfiniteCurve(22, 10)
gmsh.model.mesh.setTransfiniteCurve(21, 10)
gmsh.model.mesh.setTransfiniteCurve(28, 10)
gmsh.model.mesh.setTransfiniteCurve(27, 10)
gmsh.model.mesh.setTransfiniteCurve(26, 10)
gmsh.model.mesh.setTransfiniteCurve(25, 10)
# horizontal+vertical 斜向加密 8
gmsh.model.mesh.setTransfiniteCurve(40, 8)
gmsh.model.mesh.setTransfiniteCurve(41, 8)
gmsh.model.mesh.setTransfiniteCurve(42, 8)
gmsh.model.mesh.setTransfiniteCurve(43, 8)
gmsh.model.mesh.setTransfiniteCurve(44, 8)
gmsh.model.mesh.setTransfiniteCurve(37, 8)
gmsh.model.mesh.setTransfiniteCurve(38, 8)
gmsh.model.mesh.setTransfiniteCurve(39, 8)
for i in range(20):
    gmsh.model.mesh.setTransfiniteSurface(i + 1)


gmsh.model.addPhysicalGroup(1, [23, 24, 25, 26, 27, 28, 21, 22], 1)
# Physical Point("top")
gmsh.model.addPhysicalGroup(0, [33], 11)
# Physical Point("right")
gmsh.model.addPhysicalGroup(0, [31], 12)
# Physical Point("bottom")
gmsh.model.addPhysicalGroup(0, [37], 13)
# Physical Point("left")
gmsh.model.addPhysicalGroup(0, [35], 14)
# Physical Point("top_right")
gmsh.model.addPhysicalGroup(0, [32], 15)
# Physical Point("bottom_right")
gmsh.model.addPhysicalGroup(0, [38], 16)
# Physical Point("bottom_left")
gmsh.model.addPhysicalGroup(0, [36], 17)
# Physical Point("top_left")
gmsh.model.addPhysicalGroup(0, [34], 18)

gmsh.model.mesh.generate(2)
gmsh.fltk.run()
gmsh.finalize()



