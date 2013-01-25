import pandas as pd
import numpy as np

class EmulatorParams(object):
    pass


class EmulatorData(object):
    start_year = 2005
    end_year = 2100
    T = end_year - start_year + 1
    indexes0 = np.arange(T)
    indexes1 = indexes0 + 1
    rho = np.array([
        0.98758,0.98758,0.98758,0.98758,0.98758,
        0.98758,0.98758,0.98758,0.98758,0.98758,0.98758,0.98758,0.98758,0.98758,
        0.98758,0.98758,0.98758,0.98758,0.98758,0.98758,0.98758,0.98758,0.98758,
        0.98954,0.98954,0.98954,0.98954,0.98954,0.98954,0.98954,0.98954,0.98954,
        0.98954,0.98954,0.98954,0.98954,0.98954,0.98954,0.98954,0.98954,0.98954,
        0.98954,0.98954,0.98954,0.98954,0.98954,0.98758,])
    phi = np.array([
        0.16191,0.16191,0.16191,0.16191,0.16191,
        0.16191,0.16191,0.16191,0.16191,0.16191,0.16191,0.16191,0.16191,0.16191,
        0.16191,0.16191,0.16191,0.16191,0.16191,0.16191,0.16191,0.16191,0.16191,
        0.31032,0.31032,0.31032,0.31032,0.31032,0.31032,0.31032,0.31032,0.31032,
        0.31032,0.31032,0.31032,0.31032,0.31032,0.31032,0.31032,0.31032,0.31032,
        0.31032,0.31032,0.31032,0.31032,0.31032,0.16191,])
    beta0 = np.array([
        335.13,338.41,325.11,324.41,316.57,319.42,
        318.11,332.81,322.43,317.98,326,327.43,330.99,327.6,329.6,328.21,324.45,
        310.45,320.46,327.99,327.91,328.12,321.32,317.76,319.12,325.24,323.16,
        317.71,323.23,325.52,324.84,321.95,320.77,323.09,322.46,321.46,320.63,
        322.37,328.97,327.81,336.73,329.81,315.51,374.94,307.86,319.73,295.49,])
    beta1 = np.array([
        5.3543,4.5247,3.1872,2.3206,0.1997,1.1359,
        -0.2778,1.6262,1.3042,2.2663,1.7297,0.14051,1.5177,1.3649,1.6642,2.679,
        1.1709,0.18981,1.566,1.3294,1.6493,1.2299,1.268,0.69932,0.56896,1.4162,
        1.6678,1.5508,0.72015,1.4595,1.3915,1.1078,1.8791,2.2337,0.78247,2.7308,
        1.9861,2.0629,1.5993,1.9972,4.1823,2.2427,4.0889,10.094,2.0357,3.467,4.2379,])
    beta2 = np.array([
        4.3358,4.2687,3.9558,3.1697,3.6751,3.4694,
        3.3089,2.8612,2.8583,2.3787,2.9734,3.7073,2.6101,2.5399,2.6739,4.5903,
        3.5248,4.3901,3.3082,2.8257,2.1688,2.7236,2.7307,2.2859,2.0627,1.9314,
        1.9122,1.5758,2.0868,1.9321,1.8156,1.8649,1.4193,1.6754,2.0342,1.8142,
        2.3424,2.7697,1.9374,1.7362,4.7701,1.5439,0.53892,4.2871,2.7202,2.8963,2.8621,])
    boundaries = pd.DataFrame({
        'ARL': np.array([67.5,90,0,360]),
        'ALA': np.array([57.5,67.5,190,255]),
        'CGI': np.array([50,67.5,255,350]),
        'WNA': np.array([30,57.5,225,255]),
        'CNA': np.array([30,50,255,275]),
        'ENA': np.array([30,50,275,310]),
        'CAM': np.array([10,30,245,290]),
        'AMZ': np.array([-20,10,277.5,325]),
        'SSA': np.array([-55,-20,285,320]),
        'NEU': np.array([47.5,67.5,350,40]),
        'SEU': np.array([30,47.5,350,40]),
        'SAH': np.array([17.5,30,340,40]),
        'WAF': np.array([-10,17.5,340,25]),
        'EAF': np.array([-10,17.5,25,55]),
        'SAF': np.array([-35,10,10,50]),
        'NAS': np.array([50,67.5,40,190]),
        'CAS': np.array([30,50,40,75]),
        'TIB': np.array([30,50,75,100]),
        'EAS': np.array([20,50,100,150]),
        'SAS': np.array([5,30,65,100]),
        'SEA': np.array([-10,20,100,150]),
        'NAU': np.array([-30,-10,110,155]),
        'SAU': np.array([-47.5,-30,110,180]),
        'MED': np.array([30,50,265,295]),
        'CAR': np.array([5,50,265,295]), # Caribbean
        'IND': np.array([-35,30,25,100]),
        'SPW': np.array([-50,-5,145,220]),
        'SPE': np.array([-50,-5,220,295]), # Tiny thing on left side
        'EPW': np.array([-5,5,137.5,220]),
        'EPE': np.array([-5,5,220,290]), # Java
        'NPW': np.array([5,30,120,195]),
        'NPE': np.array([5,30,195,265]), # Hawaii
        'NAT': np.array([5,50,295,2.5]),
        'SAT': np.array([-50,-5,295,25]),
        'EAT': np.array([-5,5,295,25]),
        'SIO': np.array([-50,-35,25,145]),
        'NNE': np.array([30,67.5,195,255]),
        'NNW': np.array([30,67.5,100,195]),
        'WPE': np.array([-5,5,100,137.5]), # Indonesia
        'WPS': np.array([-35,-5,100,145]),
        'HBO': np.array([50,67.5,265,290]),
        'WPN': np.array([5,30,100,120]),
        'NNA': np.array([50,67.5,290,30]),
        'ARO': np.array([67.5,90,0,360]),
        'AOP': np.array([-90,-50,120,250]),
        'AOI': np.array([-90,-50,250,120]),
        'ANL': np.array([-90,-55,0,360]),
    })
    co2raw = [
#        [370.52,370.52,370.52,370.52],
#        [372.79,372.79,372.79,372.79],
        [375.11,375.15,375.01,375.2],
        [377.78,377.95,377.41,378.16],
        [380.58,380.86,379.79,381.36],
        [383.52,383.83,382.26,384.74],
        [386.7,386.98,384.88,388.43],
        [390.12,390.16,387.61,392.06],
        [393.8,393.31,390.46,395.27],
        [397.55,396.5,393.4,398.44],
        [401.15,399.75,396.32,401.79],
        [404.61,403.01,399.17,405.28],
        [407.97,406.3,401.99,408.9],
        [411.24,409.63,404.79,412.66],
        [414.42,412.99,407.54,416.55],
        [417.5,416.38,410.26,420.55],
        [420.55,419.83,413,424.72],
        [423.46,423.27,415.77,429.09],
        [426.14,426.57,418.58,433.67],
        [428.59,429.85,421.43,438.36],
        [430.91,433.18,424.32,443.07],
        [433.15,436.55,427.27,447.89],
        [435.33,439.95,430.26,452.82],
        [437.46,443.39,433.3,457.86],
        [439.52,446.87,436.38,463],
        [441.51,450.37,439.5,468.23],
        [443.42,453.89,442.64,473.55],
        [445.15,457.46,445.56,479.09],
        [446.62,461.1,448.02,485],
        [447.94,464.73,450.3,491.12],
        [449.21,468.29,452.64,497.34],
        [450.4,471.84,455.04,503.73],
        [451.52,475.38,457.51,510.3],
        [452.58,478.92,460.03,517.07],
        [453.57,482.46,462.61,524.01],
        [454.49,485.99,465.23,531.13],
        [455.33,489.49,467.89,538.41],
        [455.98,493,470.72,545.79],
        [456.34,496.53,473.89,553.25],
        [456.52,500.02,477.21,560.85],
        [456.61,503.42,480.51,568.62],
        [456.62,506.75,483.84,576.55],
        [456.56,510.05,487.22,584.67],
        [456.44,513.34,490.68,593.01],
        [456.28,516.62,494.2,601.56],
        [456.07,519.91,497.81,610.34],
        [455.82,523.2,501.5,619.35],
        [455.44,526.38,505.13,628.43],
        [454.85,529.35,508.61,637.46],
        [454.15,532.18,512.05,646.55],
        [453.42,534.91,515.56,655.82],
        [452.66,537.54,519.12,665.23],
        [451.86,540.07,522.73,674.76],
        [451.05,542.54,526.42,684.47],
        [450.24,544.95,530.21,694.36],
        [449.42,547.32,534.08,704.45],
        [448.6,549.65,538.06,714.76],
        [447.83,551.91,542.45,725.23],
        [447.18,554.07,547.57,735.8],
        [446.56,556.12,553.05,746.47],
        [445.92,558.08,558.56,757.22],
        [445.28,559.93,564.15,768.05],
        [444.62,561.68,569.81,778.94],
        [443.94,563.32,575.54,789.89],
        [443.27,564.88,581.37,800.93],
        [442.6,566.38,587.32,812.1],
        [441.95,567.82,593.39,823.41],
        [441.34,569.18,599.43,834.84],
        [440.8,570.43,605.24,846.36],
        [440.3,571.56,610.95,857.96],
        [439.81,572.58,616.68,869.65],
        [439.33,573.48,622.42,881.43],
        [438.85,574.27,628.17,893.3],
        [438.37,574.93,633.92,905.23],
        [437.88,575.46,639.67,917.24],
        [437.4,575.9,645.45,929.33],
        [436.94,576.26,651.27,941.53],
        [436.48,576.43,656.94,954.05],
        [435.97,576.26,662.25,967.06],
        [435.47,576.04,667.29,980.38],
        [435,575.97,672.09,993.81],
        [434.52,575.97,676.62,1007.4],
        [434.03,576.01,680.89,1021.1],
        [433.54,576.1,684.91,1034.9],
        [433.03,576.22,688.67,1048.8],
        [432.5,576.36,692.18,1062.8],
        [431.98,576.53,695.46,1077],
        [431.47,576.77,698.57,1091.1],
        [431,577.05,701.51,1105],
        [430.55,577.4,704.42,1118.9],
        [430.11,577.79,707.37,1132.9],
        [429.68,578.2,710.34,1146.9],
        [429.25,578.64,713.32,1161],
        [428.82,579.09,716.31,1175.1],
        [428.39,579.55,719.29,1189.2],
        [427.95,580.01,722.26,1203.4],
        [427.5,580.47,725.23,1217.5],
        [426.96,580.91,728.12,1231.4],
    ]
    co2 = pd.DataFrame(
        co2raw, index=np.linspace(2005, 2100, 96),
        columns=['RCP26', 'RCP45', 'RCP60', 'RCP85']
    )

#REGIONS = [
#    'ARL', 'ANL', 'ALA', 'CGI', 'WNA', 'CNA', 'ENA', 'CAM', 'AMZ', 'SSA', 'NEU',
#    'SEU', 'SAH', 'WAF', 'EAF', 'SAF', 'NAS', 'CAS', 'TIB', 'EAS', 'SAS', 'SEA',
#    'SAU', 'NAU', 'CAR', 'IND', 'SPW', 'SPE', 'EPW', 'EPE', 'NPW', 'NPE', 'NAT',
#    'SAT', 'EAT', 'SIO', 'NNE', 'NNW', 'WPE', 'WPS', 'HBO', 'WPN', 'NNA', 'ARO',
#    'AOP', 'AOI', 'MED', 'ANL',
#]
