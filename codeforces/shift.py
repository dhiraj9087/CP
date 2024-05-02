import math
import sys
input=sys.stdin.readline
from collections import *
def main():
    # n=int(input())
    A = [ 1266, 1568, 1066, 1686, 1180, 245, 610, 853, 948, 825, 755, 743, 1160, 330, 1732, 724, 659, 1407, 1471, 621, 97, 1436, 1011, 1106, 1753, 1105, 242, 839, 284, 1427, 298, 735, 1050, 1001, 848, 2173, 624, 507, 216, 968, 515, 1105, 1390, 1627, 592, 1679, 703, 711, 667, 879, 438, 770, 902, 689, 1316, 1652, 1846, 811, 2006, 1711, 1336, 774, 1467, 1239, 1097, 1249, 1806, 976, 1160, 2029, 393, 1483, 2041, 1560, 1221, 1920, 1403, 621, 1262, 453, 1000, 956, 1193, 1560, 839, 1341, 1893, 712, 1281, 816, 1294, 405, 992, 1569, 1338, 758, 1342, 1187, 982, 1310, 1309, 1311, 1277, 1032, 509, 1915, 989, 396, 1210, 675, 958, 1092, 1090, 1044, 1796, 1271, 971, 997, 1581, 1084, 729, 1543, 1068, 1021, 1904, 1265, 145, 585, 151, 373, 842, 1525, 801, 1726, 1314, 871, 1573, 906, 1379, 375, 1248, 1261, 1659, 2253, 2144, 883, 1011, 1208, 1381, 1040, 1490, 668, 2166, 660, 891, 1971, 1574, 769, 861, 764, 822, 1665, 619, 1621, 878, 1702, 647, 1791, 1379, 1083, 343, 1048, 1090, 1571, 1745, 1641, 1098, 1669, 961, 902, 871, 294, 307, 969, 1488, 729, 1765, 1052, 1583, 1219, 615, 556, 573, 641, 290, 786, 1149, 1332, 1392, 917, 1423, 1049, 1943, 715, 292, 947, 527, 1123, 462, 878, 1519, 1768, 847, 1877, 688, 1285, 1183, 1285, 1199, 2157, 923, 996, 894, 174, 475, 772, 618, 1404, 592, 1191, 1148, 383, 423, 281, 970, 1797, 1276, 1310, 1406, 1204, 1021, 669, 881, 1415, 1713, 775, 1185, 1757, 1162, 1044, 709, 756, 271, 2059, 1328, 1137, 1359, 1787, 1019, 718, 639, 1740, 1008, 1520, 1394, 770, 1633, 1332, 682, 949, 1097, 1301, 1342, 1469, 1252, 1458, 1249, 1203, 479, 390, 1311, 1041, 1820, 1333, 1166, 1808, 1906, 1547, 899, 1652, 177, 1281, 591, 1965, 1064, 993, 907, 660, 1394, 1855, 550, 1074, 1237, 1059, 1546, 1312, 248, 1586, 606, 1530, 1651, 1055, 870, 1270, 405, 1149, 1971, 719, 1556, 1454, 908, 1174, 514, 955, 1443, 333, 980, 660, 230, 1795, 776, 1258, 686, 931, 1148, 342, 928, 1150, 1195, 1059, 1287, 1312, 1114, 1579, 1641, 954, 659, 742, 1374, 1694, 1798, 1409, 1205, 1722, 854, 1613, 1001, 1338, 781, 1424, 726, 985, 1218, 478, 1064, 820, 1209, 1625, 1021, 1230, 1217, 1039, 921, 1040, 1628, 1324, 1973, 1091, 1876, 279, 1443, 2092, 2070, 1165, 821, 1339, 1818, 1190, 834, 1238, 1834, 1128, 1295, 1793, 1689, 1082, 1438, 627, 1887, 889, 1391, 1960, 1485, 1519, 599, 1465, 1136, 1072, 779, 1155, 888, 1862, 1692, 662, 1862, 1426, 1409, 954, 1140, 768, 357, 518, 1973, 1168, 1450, 576, 1007, 1377, 1707, 1615, 1745, 827, 1801, 425, 210, 847, 616, 1544, 1400, 464, 1025, 589, 565, 1932, 1280, 929, 1404, 770, 862, 1888, 1672, 2024, 541, 1164, 1225, 1180, 1197, 1543, 1180, 738, 1812, 1019, 965, 731, 1663, 1056, 1710, 1237, 1170, 1338, 811, 1368, 1154, 1324, 1803, 2106, 693, 445, 2004, 659, 490, 573, 784, 1334, 1405, 578, 1455, 1994, 1162, 1070, 343, 1753, 1868, 260, 1624, 976, 1604, 1512, 1077, 414, 362, 1122, 1601, 1993, 498, 912, 1517, 1654, 1442, 1117, 1736, 1370, 1579, 642, 1149, 1145, 262, 2137, 256, 1076, 1424, 600, 1899, 694, 487, 1108, 1670, 1127, 1054, 262, 1049, 2053, 793, 717, 1067, 1731, 1561, 186, 959, 694, 566, 1343, 1110, 1216, 1019, 528, 1812, 1415, 1316, 1089, 1448, 1516, 1879, 1334, 926, 1568, 1599, 1435, 1510, 659, 1653, 332, 1412, 806, 1551, 786, 1044, 1063, 1302, 1170, 941, 657, 978, 1476, 1392, 1098, 1475, 839, 1813, 1090, 575, 1247, 1268, 1088, 1340, 897, 1310, 1168, 989, 364, 815, 1982, 1532, 1323, 1079, 1210, 846, 1474, 1244, 99, 1034, 316, 299, 1335, 1273, 925, 2053, 1165, 327, 1336, 694, 779, 1227, 927, 1312, 569, 1599, 515, 1036, 928, 1065, 1284, 831, 189, 1387, 459, 1868, 740, 2071, 1196, 944, 288, 1206, 453, 1482, 2122, 1310, 1622, 1385, 1944, 1408, 1676, 1015, 1958, 1678, 907, 1111, 320, 696, 1018, 1260, 685, 882, 1342, 305, 448, 1745, 121, 189, 1297, 1980, 1265, 1239, 1891, 1515, 1084, 1392, 1309, 1996, 1182, 937, 513, 1694, 785, 494, 1580, 1726, 1345, 1657, 1520, 502, 2027, 2062, 1217, 824, 944, 800, 1074, 1329, 1201, 1558, 1423, 886, 697, 1060, 480, 937, 913, 669, 771, 1410, 2121, 1390, 1528, 1292, 1505, 1005, 1134, 1222, 1947, 483, 740, 1401, 618, 1200, 1284, 669, 857, 447, 1241, 1139, 1054, 842, 493, 911, 1351, 1320, 1882, 1359, 1325, 899, 851, 1933, 1435, 430, 484, 636, 1001, 1013, 1096, 1438, 481, 737, 1871, 837, 1223, 1049, 723, 1493, 837, 1141, 1722, 1945, 1123, 1279, 1226, 1339, 1103, 655, 904, 1748, 1783, 1017, 1187, 1466, 908, 1603, 1437, 1829, 749, 1072, 380, 972, 695, 225, 1106, 1417, 1489, 1608, 766, 1270, 1184, 1333, 1678, 1203, 1590, 1336, 832, 1468, 1364, 1977, 1185, 865, 1802, 1549, 1151, 310, 1531, 1645, 1138, 1574, 648, 400, 2092, 1280, 993, 1308, 1559, 1820, 842, 1473, 968, 913, 1178, 1082, 1039, 1523, 1771, 1106, 556, 1229, 1832, 1570, 709, 498, 1801, 1041, 1063, 499, 1540, 329, 416, 1245, 1114, 834, 1032, 1041, 2213, 1528, 1109, 1172, 1409, 902, 1769, 924, 298, 1351, 1692, 1477, 532, 1247, 1595, 801, 1162, 2033, 1475, 1018, 141, 243, 1281, 987, 510, 391, 636, 1846, 1088, 1068, 1369, 1032, 806, 1137, 1068, 676, 1488, 379, 1481, 647, 1917, 1158, 877, 943, 1001, 584, 1557, 1073, 1369, 1552, 1544, 981, 1252, 1438, 1884, 1669, 1957, 1798, 2013, 1220, 1182, 535, 1849, 1486, 1215, 1564, 1078, 718, 477, 314, 574, 942, 693, 1133, 977, 619, 1404, 1698, 713, 568, 1009, 1139, 317, 1168, 2178, 1064, 1802, 1192, 1300, 1602, 730, 429, 301, 1592, 1089, 1804, 829, 1589, 1017, 1884, 1129, 1022, 1291, 914, 755, 591, 1242, 1812, 1309, 2046, 1271, 665, 1097, 1770, 1226, 796, 1451, 1851, 625, 438, 1050, 1787, 452, 800, 612, 2033, 333, 1449, 1129, 1909, 1562, 786, 909, 339, 1390, 1126, 1524, 1516, 665, 933, 866, 1772, 1266, 1152, 1433, 1354, 1405, 602, 1079, 1327, 775, 1799, 989, 712, 982, 703, 619, 737, 911, 144, 808, 917, 922, 881, 1113, 714, 801, 1373, 604, 825, 1686, 1273, 1866, 1273, 269, 794, 1081, 1935, 2142, 633, 1277, 545, 1257, 367, 474, 1677, 946, 496, 1634, 1606, 1675, 280, 932, 605, 1794, 1173, 1467, 1333, 191, 1182, 578, 607, 1367, 988, 1167, 916, 2182, 629, 589, 1796, 1618, 1546, 1276, 839, 1257, 1876, 340, 506, 1136, 1286, 1423, 1186, 1238, 922, 1232, 1156, 196, 1539, 756, 1231, 1531, 1799, 1361, 1132, 751, 914, 1680, 1310, 1628, 688, 986, 1868, 1740, 1310, 1075, 795, 1355, 1474, 1648, 905, 1800, 1035, 1158, 690, 1712, 494, 932, 485, 1240, 824, 1893, 1884, 1589, 1536, 633, 720, 778, 514, 1618, 1216, 965, 1450, 1175, 1140, 1112, 1594, 1743, 550, 1030, 560, 666, 662, 1096, 1668, 235, 1853, 442, 1127, 1676, 272, 1446, 1219, 601, 477, 253, 1270, 1127, 860, 170, 595, 870, 1397, 1195, 1024, 1022, 1147, 1282, 1306, 1838, 1398, 1194, 1507, 1682, 1084, 846, 1586, 1603, 1271, 1632, 671, 1810, 639, 1889, 2120, 725, 1244, 1483, 1093, 411, 1589, 704, 1554, 1627, 1167, 1285, 2087, 1235, 1888, 1337, 1070, 1736, 325, 918, 965, 668, 2207, 1034, 624, 485, 1370, 1675, 2215, 514, 1666, 1917, 1066, 601, 1602, 456, 786, 1465, 1648, 428, 794, 1201, 1094, 751, 1431, 1842, 1341, 429, 1567, 1095, 1812, 402, 1795, 772, 1683, 1930, 1976, 943, 702, 746, 1290, 1381, 1547, 468, 1258, 1967, 1614, 845, 824, 1311, 1032, 1336, 1669, 961, 2133, 423, 1539, 1029, 1425, 1941, 1041, 1577, 928, 798, 1991, 1387, 1256, 274, 2025, 1196, 1249, 766, 297, 980, 1117, 1346, 513, 990, 448, 633, 875, 208, 1511, 775, 1237, 491, 1426, 1060, 357, 1019, 1225, 1003, 742, 1060, 1208, 986, 1037, 716, 1186, 430, 311, 1162, 819, 999, 806, 485, 295, 1017, 1647, 1931, 1228, 1674, 1010, 1747, 2172, 1304, 1561, 1536, 1193, 583, 1359, 1164, 966, 1521, 388, 1437, 1512, 1874, 1195, 694, 1500, 1125, 1308, 1278, 1568, 1916, 294, 1114, 690, 966, 1346, 1117, 143, 1066, 1564, 768, 1354, 556, 1228, 860, 896, 1012, 860, 1628, 1765, 969, 830, 989, 1149, 1113, 766, 1124 ]
    B = 1828

    d=defaultdict(int)
    d[0]=1
    ans=0
    x=0
    for i in range(len(A)):
        x=x^A[i]
        xr=x^B
        ans+=d[xr]
        d[xr]+=1
    print(ans)
# for _ in range(int(input())):
main()