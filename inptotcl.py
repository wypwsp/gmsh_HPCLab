from openseespy.postprocessing.Get_Rendering import *
import openseespy.opensees as ops
import re
'''
需要建立地层单元和结构单元，自由度不同，分步骤进行建模
首先建立地层
地层节点需要减去纯节点部分节点，即全部节点 -（结构节点-接触节点）= 地层节点
单元类型为CPS4

结构节点需要导入结构节点，在inp导出的文件中将接触节点号+1000000
单元类型为T3D2
'''
node_ar = []
element_ar = []
structure_element_ar = []
SSI_structure_node_ar = []
path = r'rectangular3.inp'
structure_node_no_ar = []
SSI_soil_node_ar = []
ground_node_ar = []
structure_node_ar = []

# 全部结点和地层网格
with open(path, 'r') as f:
    li = f.readline()
    while li:
        li = f.readline()
        if r'*NODE' not in li:
            continue
        break
    li = f.readline()
    while li:
        if '*' not in li:
            node_line = li.split(",")
            node_data = [float(node_line[i]) for i in range(len(node_line))]
            node_ar.append(node_data)
            li = f.readline()
            continue
        else:
            break
    # elements
    while li:
        li = f.readline()
        if r'*ELEMENT, type=CPS4' not in li:
            continue
        break
    li = f.readline()
    while li:
        if '*ELSET' not in li:
            if '*' not in li:
                element_line = li.split(",")
                element_data = [float(element_line[i]) for i in range(len(element_line))]
                element_ar.append(element_data)
                li = f.readline()
                continue
            else:
                li = f.readline()
        else:
            break

# 结构节点号
with open(path, 'r') as f:
    li = f.readline()
    while li:
        li = f.readline()
        if r'*NSET,NSET=PhysicalLine100' not in li:
            continue
        break
    li = f.readline()
    while li:
        if '*' not in li:
            line = li.split(",")
            # print(line)
            for i in line:
                try:
                    structure_node_no_ar.append(int(i))
                except:
                    pass
            li = f.readline()
            continue
        else:
            break
# print(structure_node_ar)

# 接触(土)节点号
with open(path, 'r') as f:
    li = f.readline()
    while li:
        li = f.readline()
        if r'*NSET,NSET=PhysicalLine5' not in li:
            continue
        break
    li = f.readline()
    while li:
        if '*' not in li:
            line = li.split(",")
            # print(line)
            for i in line:
                try:
                    SSI_soil_node_ar.append(int(i))
                except:
                    pass
            li = f.readline()
            continue
        else:
            break
# print(SSI_soil_node_ar)

# 地层节点：全部节点 -（结构节点-接触节点）= 地层节点
inner_node_no_ar = [val for val in structure_node_no_ar if val not in SSI_soil_node_ar]
for node in node_ar:
    if int(node[0]) not in inner_node_no_ar:
        ground_node_ar.append(node)

# 接触(结构)节点号和坐标
node_ar = np.array(node_ar)
element_ar = np.array(element_ar)
with open(path, 'r') as f:
    li = f.readline()
    while li:
        li = f.readline()
        if r'*NSET' not in li:
            continue
        break
    li = f.readline()
    while li:
        if '*NSET,NSET=PhysicalLine' not in li:
            if '*' not in li:
                SSI_line = li.split(",")
                SSI_number = int(SSI_line[0])
                node_data = node_ar[np.argwhere(node_ar[:, 0] == SSI_number)[0]][0]
                SSI_data = [int(SSI_line[0]), node_data[1], node_data[2], node_data[3]]
                SSI_structure_node_ar.append(SSI_data)
                li = f.readline()
                continue
            else:
                li = f.readline()
        else:
            break
# 结构节点号和坐标
for node in node_ar:
    if int(node[0]) in structure_node_no_ar:
        structure_node_ar.append(node)
# 结构单元
with open(path, 'r') as f:
    li = f.readline()
    while li:
        li = f.readline()
        if r'*ELEMENT, type=T3D2' not in li:
            continue
        break
    li = f.readline()
    title = li
    while li:
        if '*ELEMENT, type=CPS4' not in li:
            if '*' in li:
                title = li
            if '*' not in li:
                structure_line = li.split(",")
                structure_data = [float(structure_line[i]) for i in range(len(structure_line))]
                ele_no = int(re.findall(r"\d+\.?\d*", title)[-1])
                if 300 <= ele_no < 500 or 700 <= ele_no < 900 or 1000 <= ele_no < 2000:
                    structure_element_ar.append(structure_data)
                li = f.readline()
                continue
            else:
                li = f.readline()
        else:
            break

ops.wipeAnalysis()
ops.wipe()

# # 地层
ops.model('basic', '-ndm', 2, '-ndf', 2)
# nDMaterial('ElasticIsotropic', matTag, E, nu, rho=0.0)
ops.nDMaterial('ElasticIsotropic', 1, 3e9, 0.34, 2000.0)
# soil and structure nodes
for node in ground_node_ar:
    ops.node(int(node[0]), node[1], node[2])
# soil elements
for e in element_ar:
    # element('quad', eleTag, *eleNodes, thick, type, matTag, < pressure = 0.0, rho = 0.0, b1 = 0.0, b2 = 0.0 >)
    ops.element('quad', int(e[0]), int(e[1]), int(e[2]), int(e[3]), int(e[4]), 1.0, 'PlaneStrain', 1)

# 结构部分
ops.model('basic', '-ndm', 2, '-ndf', 3)
ops.geomTransf("Linear", 1)  # Linear, PDelta, Corotational
# uniaxialMaterial('Elastic', matTag, E, eta=0.0, Eneg=E)
ops.uniaxialMaterial('Elastic', 2, 3.45e10)
# structure nodes
for node in structure_node_ar:
    ops.node(10000000 + int(node[0]), node[1], node[2])
# structure elements
for e in structure_element_ar:
    # element('elasticBeamColumn', eleTag, *eleNodes, Area, E_mod, Iz, transfTag, <'-mass', mass>, <'-cMass'>, <'-release', releaseCode>)
    ops.element('elasticBeamColumn', int(e[0]), 10000000 + int(e[1]), 10000000 + int(e[2]), 0.6, 3.45e10, 0.6 ** 3 / 12, 1)
print(structure_element_ar)

fig, ax = plot_model('element')
plt.show()
