# -*- coding:utf-8 -*-
# Author :            Qi Wang, Tongji Univ. <wangqi14@tongji.edu.cn>
# Established at :    2022/4/17 16:22
# Modified at :       2022/4/17 23:11
# Project:

import gmsh
from gmsh import model as gm

# Before using any functions in the Python API, Gmsh must be initialized:
gmsh.initialize()
gm.add("double_circular")

# geometry parameters
radius = 4.0
height = 70.0
width = 150.0
buried_depth = 15
separation = 5.
seed_coef = 1.
# todo 增加第二种情况，即隧道距离较远的时候，需要在中间增加一列surface，相关的程序简图已经在OneNote中绘出
# constants(no modifications unless necessary)
sqrt2 = 1.414213562373095
bias_coef = 0.8
if buried_depth < bias_coef * radius * 2:
    bias_coef = 0.8 / (1.6 * radius) * buried_depth
mesh_coef_horizontal = 1.035
mesh_coef_vertical = 1.02

# some useful constants
w0 = 0.
w1 = separation / 2
w2 = separation / 2 + radius - radius / sqrt2
w3 = separation / 2 + radius
w4 = separation / 2 + radius + radius / sqrt2
w5 = separation / 2 + 2 * radius
w6 = separation / 2 + 2 * radius + bias_coef * radius
w7 = width / 2
h0 = 0.
h1 = height - buried_depth - 2 * radius - bias_coef * radius
h2 = height - buried_depth - 2 * radius
h3 = height - buried_depth - radius - radius / sqrt2
h4 = height - buried_depth - radius
h5 = height - buried_depth - radius + radius / sqrt2
h6 = height - buried_depth
h7 = height - buried_depth + bias_coef * radius
h8 = height

# Points 0~100:left 100~200:right 200~300:axis
gm.geo.addPoint(-w3, h4, 0, tag=0)
gm.geo.addPoint(w3, h4, 0, tag=100)
#
gm.geo.addPoint(w0, h4, 0, tag=201)
gm.geo.addPoint(w0, h7, 0, tag=202)
gm.geo.addPoint(w0, h8, 0, tag=203)
gm.geo.addPoint(w0, h0, 0, tag=204)
gm.geo.addPoint(w0, h1, 0, tag=208)
#
gm.geo.addPoint(-w1, h4, 0, tag=1)
gm.geo.addPoint(-w2, h5, 0, tag=2)
gm.geo.addPoint(-w3, h6, 0, tag=3)
gm.geo.addPoint(-w4, h5, 0, tag=4)
gm.geo.addPoint(-w5, h4, 0, tag=5)
gm.geo.addPoint(-w4, h3, 0, tag=6)
gm.geo.addPoint(-w3, h2, 0, tag=7)
gm.geo.addPoint(-w2, h3, 0, tag=8)
gm.geo.addPoint(w1, h4, 0, tag=101)
gm.geo.addPoint(w2, h5, 0, tag=102)
gm.geo.addPoint(w3, h6, 0, tag=103)
gm.geo.addPoint(w4, h5, 0, tag=104)
gm.geo.addPoint(w5, h4, 0, tag=105)
gm.geo.addPoint(w4, h3, 0, tag=106)
gm.geo.addPoint(w3, h2, 0, tag=107)
gm.geo.addPoint(w2, h3, 0, tag=108)
#
gm.geo.addPoint(-w3, h7, 0, tag=13)
gm.geo.addPoint(-w6, h7, 0, tag=14)
gm.geo.addPoint(-w6, h4, 0, tag=15)
gm.geo.addPoint(-w6, h1, 0, tag=16)
gm.geo.addPoint(-w3, h1, 0, tag=17)
gm.geo.addPoint(w3, h7, 0, tag=113)
gm.geo.addPoint(w6, h7, 0, tag=114)
gm.geo.addPoint(w6, h4, 0, tag=115)
gm.geo.addPoint(w6, h1, 0, tag=116)
gm.geo.addPoint(w3, h1, 0, tag=117)
#
gm.geo.addPoint(-w3, h8, 0, tag=21)
gm.geo.addPoint(-w6, h8, 0, tag=22)
gm.geo.addPoint(w3, h8, 0, tag=121)
gm.geo.addPoint(w6, h8, 0, tag=122)
#
gm.geo.addPoint(-w7, h8, 0, tag=31)
gm.geo.addPoint(-w7, h7, 0, tag=32)
gm.geo.addPoint(-w7, h4, 0, tag=33)
gm.geo.addPoint(-w7, h1, 0, tag=34)
gm.geo.addPoint(-w7, h0, 0, tag=35)
gm.geo.addPoint(w7, h8, 0, tag=131)
gm.geo.addPoint(w7, h7, 0, tag=132)
gm.geo.addPoint(w7, h4, 0, tag=133)
gm.geo.addPoint(w7, h1, 0, tag=134)
gm.geo.addPoint(w7, h0, 0, tag=135)
#
gm.geo.addPoint(-w3, h0, 0, tag=41)
gm.geo.addPoint(-w6, h0, 0, tag=42)
gm.geo.addPoint(w3, h0, 0, tag=141)
gm.geo.addPoint(w6, h0, 0, tag=142)

# Lines 0~100:left 100~200:right 200~300:axis
gm.geo.addLine(201, 202, tag=221)
gm.geo.addLine(201, 208, tag=228)
gm.geo.addLine(202, 203, tag=230)
gm.geo.addLine(208, 204, tag=238)
#
gm.geo.addCircleArc(1, 0, 2, tag=1)
gm.geo.addCircleArc(2, 0, 3, tag=2)
gm.geo.addCircleArc(3, 0, 4, tag=3)
gm.geo.addCircleArc(4, 0, 5, tag=4)
gm.geo.addCircleArc(5, 0, 6, tag=5)
gm.geo.addCircleArc(6, 0, 7, tag=6)
gm.geo.addCircleArc(7, 0, 8, tag=7)
gm.geo.addCircleArc(8, 0, 1, tag=8)
gm.geo.addCircleArc(101, 100, 102, tag=101)
gm.geo.addCircleArc(102, 100, 103, tag=102)
gm.geo.addCircleArc(103, 100, 104, tag=103)
gm.geo.addCircleArc(104, 100, 105, tag=104)
gm.geo.addCircleArc(105, 100, 106, tag=105)
gm.geo.addCircleArc(106, 100, 107, tag=106)
gm.geo.addCircleArc(107, 100, 108, tag=107)
gm.geo.addCircleArc(108, 100, 101, tag=108)
#
gm.geo.addLine(1, 201, tag=11)
gm.geo.addLine(2, 202, tag=12)
gm.geo.addLine(3, 13, tag=13)
gm.geo.addLine(4, 14, tag=14)
gm.geo.addLine(5, 15, tag=15)
gm.geo.addLine(6, 16, tag=16)
gm.geo.addLine(7, 17, tag=17)
gm.geo.addLine(8, 208, tag=18)
gm.geo.addLine(101, 201, tag=111)
gm.geo.addLine(102, 202, tag=112)
gm.geo.addLine(103, 113, tag=113)
gm.geo.addLine(104, 114, tag=114)
gm.geo.addLine(105, 115, tag=115)
gm.geo.addLine(106, 116, tag=116)
gm.geo.addLine(107, 117, tag=117)
gm.geo.addLine(108, 208, tag=118)
#
gm.geo.addLine(202, 13, tag=22)
gm.geo.addLine(13, 14, tag=23)
gm.geo.addLine(14, 15, tag=24)
gm.geo.addLine(15, 16, tag=25)
gm.geo.addLine(16, 17, tag=26)
gm.geo.addLine(17, 208, tag=27)
gm.geo.addLine(202, 113, tag=122)
gm.geo.addLine(113, 114, tag=123)
gm.geo.addLine(114, 115, tag=124)
gm.geo.addLine(115, 116, tag=125)
gm.geo.addLine(116, 117, tag=126)
gm.geo.addLine(117, 208, tag=127)
#
gm.geo.addLine(13, 21, tag=31)
gm.geo.addLine(14, 22, tag=32)
gm.geo.addLine(14, 32, tag=33)
gm.geo.addLine(15, 33, tag=34)
gm.geo.addLine(16, 34, tag=35)
gm.geo.addLine(16, 42, tag=36)
gm.geo.addLine(17, 41, tag=37)
gm.geo.addLine(113, 121, tag=131)
gm.geo.addLine(114, 122, tag=132)
gm.geo.addLine(114, 132, tag=133)
gm.geo.addLine(115, 133, tag=134)
gm.geo.addLine(116, 134, tag=135)
gm.geo.addLine(116, 142, tag=136)
gm.geo.addLine(117, 141, tag=137)
#
gm.geo.addLine(203, 21, tag=41)
gm.geo.addLine(21, 22, tag=42)
gm.geo.addLine(22, 31, tag=43)
gm.geo.addLine(31, 32, tag=44)
gm.geo.addLine(32, 33, tag=45)
gm.geo.addLine(33, 34, tag=46)
gm.geo.addLine(34, 35, tag=47)
gm.geo.addLine(35, 42, tag=48)
gm.geo.addLine(42, 41, tag=49)
gm.geo.addLine(41, 204, tag=50)
gm.geo.addLine(203, 121, tag=141)
gm.geo.addLine(121, 122, tag=142)
gm.geo.addLine(122, 131, tag=143)
gm.geo.addLine(131, 132, tag=144)
gm.geo.addLine(132, 133, tag=145)
gm.geo.addLine(133, 134, tag=146)
gm.geo.addLine(134, 135, tag=147)
gm.geo.addLine(135, 142, tag=148)
gm.geo.addLine(142, 141, tag=149)
gm.geo.addLine(141, 204, tag=150)

gm.geo.addPlaneSurface([gm.geo.addCurveLoop([11, 221, -12, -1])], tag=1)
gm.geo.addPlaneSurface([gm.geo.addCurveLoop([12, 22, -13, -2])], tag=2)
gm.geo.addPlaneSurface([gm.geo.addCurveLoop([13, 23, -14, -3])], tag=3)
gm.geo.addPlaneSurface([gm.geo.addCurveLoop([14, 24, -15, -4])], tag=4)
gm.geo.addPlaneSurface([gm.geo.addCurveLoop([15, 25, -16, -5])], tag=5)
gm.geo.addPlaneSurface([gm.geo.addCurveLoop([16, 26, -17, -6])], tag=6)
gm.geo.addPlaneSurface([gm.geo.addCurveLoop([17, 27, -18, -7])], tag=7)
gm.geo.addPlaneSurface([gm.geo.addCurveLoop([18, -228, -11, -8])], tag=8)
gm.geo.addPlaneSurface([gm.geo.addCurveLoop([111, 221, -112, -101])], tag=101)
gm.geo.addPlaneSurface([gm.geo.addCurveLoop([112, 122, -113, -102])], tag=102)
gm.geo.addPlaneSurface([gm.geo.addCurveLoop([113, 123, -114, -103])], tag=103)
gm.geo.addPlaneSurface([gm.geo.addCurveLoop([114, 124, -115, -104])], tag=104)
gm.geo.addPlaneSurface([gm.geo.addCurveLoop([115, 125, -116, -105])], tag=105)
gm.geo.addPlaneSurface([gm.geo.addCurveLoop([116, 126, -117, -106])], tag=106)
gm.geo.addPlaneSurface([gm.geo.addCurveLoop([117, 127, -118, -107])], tag=107)
gm.geo.addPlaneSurface([gm.geo.addCurveLoop([118, -228, -111, -108])], tag=108)

gm.geo.addPlaneSurface([gm.geo.addCurveLoop([230, 41, -31, -22])], tag=11)
gm.geo.addPlaneSurface([gm.geo.addCurveLoop([31, 42, -32, -23])], tag=12)
gm.geo.addPlaneSurface([gm.geo.addCurveLoop([32, 43, 44, -33])], tag=13)
gm.geo.addPlaneSurface([gm.geo.addCurveLoop([-24, 33, 45, -34])], tag=14)
gm.geo.addPlaneSurface([gm.geo.addCurveLoop([-25, 34, 46, -35])], tag=15)
gm.geo.addPlaneSurface([gm.geo.addCurveLoop([-36, 35, 47, 48])], tag=16)
gm.geo.addPlaneSurface([gm.geo.addCurveLoop([-37, -26, 36, 49])], tag=17)
gm.geo.addPlaneSurface([gm.geo.addCurveLoop([-238, -27, 37, 50])], tag=18)
gm.geo.addPlaneSurface([gm.geo.addCurveLoop([230, 141, -131, -122])], tag=111)
gm.geo.addPlaneSurface([gm.geo.addCurveLoop([131, 142, -132, -123])], tag=112)
gm.geo.addPlaneSurface([gm.geo.addCurveLoop([132, 143, 144, -133])], tag=113)
gm.geo.addPlaneSurface([gm.geo.addCurveLoop([-124, 133, 145, -134])], tag=114)
gm.geo.addPlaneSurface([gm.geo.addCurveLoop([-125, 134, 146, -135])], tag=115)
gm.geo.addPlaneSurface([gm.geo.addCurveLoop([-136, 135, 147, 148])], tag=116)
gm.geo.addPlaneSurface([gm.geo.addCurveLoop([-137, -126, 136, 149])], tag=117)
gm.geo.addPlaneSurface([gm.geo.addCurveLoop([-238, -127, 137, 150])], tag=118)

gm.geo.synchronize()

# quad mesh
for i in range(8):
    gm.mesh.setRecombine(2, i + 1)
    gm.mesh.setRecombine(2, i + 11)
    gm.mesh.setRecombine(2, i + 101)
    gm.mesh.setRecombine(2, i + 111)
    gm.mesh.setAlgorithm(2, i + 1, 9)
    gm.mesh.setAlgorithm(2, i + 11, 9)
    gm.mesh.setAlgorithm(2, i + 101, 9)
    gm.mesh.setAlgorithm(2, i + 111, 9)
    gm.mesh.setTransfiniteSurface(i + 1)
    gm.mesh.setTransfiniteSurface(i + 11)
    gm.mesh.setTransfiniteSurface(i + 101)
    gm.mesh.setTransfiniteSurface(i + 111)

# seed
# 水平横向
gmsh.model.mesh.setTransfiniteCurve(43, int(seed_coef * 20), coef=mesh_coef_horizontal)
gmsh.model.mesh.setTransfiniteCurve(33, int(seed_coef * 20), coef=mesh_coef_horizontal)
gmsh.model.mesh.setTransfiniteCurve(34, int(seed_coef * 20), coef=mesh_coef_horizontal)
gmsh.model.mesh.setTransfiniteCurve(35, int(seed_coef * 20), coef=mesh_coef_horizontal)
gmsh.model.mesh.setTransfiniteCurve(48, int(seed_coef * 20), coef=1 / mesh_coef_horizontal)
gmsh.model.mesh.setTransfiniteCurve(143, int(seed_coef * 20), coef=mesh_coef_horizontal)
gmsh.model.mesh.setTransfiniteCurve(133, int(seed_coef * 20), coef=mesh_coef_horizontal)
gmsh.model.mesh.setTransfiniteCurve(134, int(seed_coef * 20), coef=mesh_coef_horizontal)
gmsh.model.mesh.setTransfiniteCurve(135, int(seed_coef * 20), coef=mesh_coef_horizontal)
gmsh.model.mesh.setTransfiniteCurve(148, int(seed_coef * 20), coef=1 / mesh_coef_horizontal)
# 隧道下方
gmsh.model.mesh.setTransfiniteCurve(47, int(seed_coef * 30), coef=mesh_coef_vertical)
gmsh.model.mesh.setTransfiniteCurve(36, int(seed_coef * 30), coef=mesh_coef_vertical)
gmsh.model.mesh.setTransfiniteCurve(37, int(seed_coef * 30), coef=mesh_coef_vertical)
gmsh.model.mesh.setTransfiniteCurve(238, int(seed_coef * 30), coef=mesh_coef_vertical)
gmsh.model.mesh.setTransfiniteCurve(147, int(seed_coef * 30), coef=mesh_coef_vertical)
gmsh.model.mesh.setTransfiniteCurve(136, int(seed_coef * 30), coef=mesh_coef_vertical)
gmsh.model.mesh.setTransfiniteCurve(137, int(seed_coef * 30), coef=mesh_coef_vertical)
# horizontal+vertical 加密网格 16
gmsh.model.mesh.setTransfiniteCurve(221, 10)
gmsh.model.mesh.setTransfiniteCurve(228, 10)
gmsh.model.mesh.setTransfiniteCurve(22, 10)
gmsh.model.mesh.setTransfiniteCurve(23, 10)
gmsh.model.mesh.setTransfiniteCurve(24, 10)
gmsh.model.mesh.setTransfiniteCurve(25, 10)
gmsh.model.mesh.setTransfiniteCurve(26, 10)
gmsh.model.mesh.setTransfiniteCurve(27, 10)
gmsh.model.mesh.setTransfiniteCurve(41, 10)
gmsh.model.mesh.setTransfiniteCurve(42, 10)
gmsh.model.mesh.setTransfiniteCurve(45, 10)
gmsh.model.mesh.setTransfiniteCurve(46, 10)
gmsh.model.mesh.setTransfiniteCurve(49, 10)
gmsh.model.mesh.setTransfiniteCurve(50, 10)
gmsh.model.mesh.setTransfiniteCurve(122, 10)
gmsh.model.mesh.setTransfiniteCurve(123, 10)
gmsh.model.mesh.setTransfiniteCurve(124, 10)
gmsh.model.mesh.setTransfiniteCurve(125, 10)
gmsh.model.mesh.setTransfiniteCurve(126, 10)
gmsh.model.mesh.setTransfiniteCurve(127, 10)
gmsh.model.mesh.setTransfiniteCurve(141, 10)
gmsh.model.mesh.setTransfiniteCurve(142, 10)
gmsh.model.mesh.setTransfiniteCurve(145, 10)
gmsh.model.mesh.setTransfiniteCurve(146, 10)
gmsh.model.mesh.setTransfiniteCurve(149, 10)
gmsh.model.mesh.setTransfiniteCurve(150, 10)
# vertical 隧道上方土层 5
gmsh.model.mesh.setTransfiniteCurve(44, 10)
gmsh.model.mesh.setTransfiniteCurve(32, 10)
gmsh.model.mesh.setTransfiniteCurve(31, 10)
gmsh.model.mesh.setTransfiniteCurve(230, 10)
gmsh.model.mesh.setTransfiniteCurve(131, 10)
gmsh.model.mesh.setTransfiniteCurve(132, 10)
gmsh.model.mesh.setTransfiniteCurve(144, 10)
# circular 隧道加密 10
# todo 隧道加密的方法应该再做优化，应该在surface1,8,101,108使用单侧bias的网格种子
gmsh.model.mesh.setTransfiniteCurve(1, 10)
gmsh.model.mesh.setTransfiniteCurve(2, 10)
gmsh.model.mesh.setTransfiniteCurve(3, 10)
gmsh.model.mesh.setTransfiniteCurve(4, 10)
gmsh.model.mesh.setTransfiniteCurve(5, 10)
gmsh.model.mesh.setTransfiniteCurve(6, 10)
gmsh.model.mesh.setTransfiniteCurve(7, 10)
gmsh.model.mesh.setTransfiniteCurve(8, 10)
gmsh.model.mesh.setTransfiniteCurve(101, 10)
gmsh.model.mesh.setTransfiniteCurve(102, 10)
gmsh.model.mesh.setTransfiniteCurve(103, 10)
gmsh.model.mesh.setTransfiniteCurve(104, 10)
gmsh.model.mesh.setTransfiniteCurve(105, 10)
gmsh.model.mesh.setTransfiniteCurve(106, 10)
gmsh.model.mesh.setTransfiniteCurve(107, 10)
gmsh.model.mesh.setTransfiniteCurve(108, 10)
# horizontal+vertical 斜向加密 8
gmsh.model.mesh.setTransfiniteCurve(11, 8)
gmsh.model.mesh.setTransfiniteCurve(12, 8)
gmsh.model.mesh.setTransfiniteCurve(13, 8)
gmsh.model.mesh.setTransfiniteCurve(14, 8)
gmsh.model.mesh.setTransfiniteCurve(15, 8)
gmsh.model.mesh.setTransfiniteCurve(16, 8)
gmsh.model.mesh.setTransfiniteCurve(17, 8)
gmsh.model.mesh.setTransfiniteCurve(18, 8)
gmsh.model.mesh.setTransfiniteCurve(111, 8)
gmsh.model.mesh.setTransfiniteCurve(112, 8)
gmsh.model.mesh.setTransfiniteCurve(113, 8)
gmsh.model.mesh.setTransfiniteCurve(114, 8)
gmsh.model.mesh.setTransfiniteCurve(115, 8)
gmsh.model.mesh.setTransfiniteCurve(116, 8)
gmsh.model.mesh.setTransfiniteCurve(117, 8)
gmsh.model.mesh.setTransfiniteCurve(118, 8)

gmsh.model.mesh.generate(2)
gmsh.fltk.run()
gmsh.finalize()
