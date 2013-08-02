import numpy as np
import pandas as pd


all_boundaries = {
    'BCC_CSM': pd.DataFrame({
        'ARL': np.array([0.860447, 287.458429, 3.599405, 3.599405, 0.16191]),
        'ARO': np.array([0.831043, 281.495731, 4.688243, 4.688243, 0.31032]),
        'ANL': np.array([0.876582, 289.887679, 3.162522, 3.162522, 0.16191]),
        'AOP': np.array([0.832341, 257.031747, 7.760533, 7.760533, 0.31032]),
        'AOI': np.array([0.813758, 258.029818, 9.335264, 9.335264, 0.31032]),
        'ALA': np.array([0.87807, 241.448298, 5.024315, 5.024315, 0.16191]),
        'CGI': np.array([0.961066, 271.407783, 4.02533, 4.02533, 0.16191]),
        'WNA': np.array([0.997297, 271.015023, 21.541199, 21.541199, 0.16191]),
        'CNA': np.array([0.725699, 266.932909, 6.264987, 6.264987, 0.16191]),
        'ENA': np.array([0.818798, 265.660085, 6.68826, 6.68826, 0.16191]),
        'CAM': np.array([0.816191, 278.685591, 4.7705, 4.7705, 0.16191]),
        'AMZ': np.array([0.858908, 283.220686, 4.694124, 4.694124, 0.16191]),
        'SSA': np.array([0.84311, 280.027009, 4.95365, 4.95365, 0.16191]),
        'NEU': np.array([0.82976, 293.694662, 3.322811, 3.322811, 0.16191]),
        'SEU': np.array([0.803594, 297.233072, 4.070454, 4.070454, 0.16191]),
        'SAH': np.array([0.843762, 288.641357, 3.572087, 3.572087, 0.16191]),
        'WAF': np.array([0.898777, 277.217016, 4.885832, 4.885832, 0.16191]),
        'EAF': np.array([0.793921, 287.10752, 4.230751, 4.230751, 0.16191]),
        'SAF': np.array([0.832659, 296.341725, 4.601015, 4.601015, 0.16191]),
        'NAS': np.array([0.861096, 297.93678, 4.078982, 4.078982, 0.16191]),
        'CAS': np.array([0.867843, 295.896494, 4.012736, 4.012736, 0.16191]),
        'TIB': np.array([0.81071, 294.906099, 3.986572, 3.986572, 0.16191]),
        'EAS': np.array([0.676392, 268.280488, 5.885335, 5.885335, 0.16191]),
        'SAS': np.array([0.826515, 284.023188, 4.722482, 4.722482, 0.16191]),
        'SEA': np.array([0.799178, 272.605379, 4.644939, 4.644939, 0.16191]),
        'NAU': np.array([0.880085, 280.018845, 4.332006, 4.332006, 0.16191]),
        'SAU': np.array([0.894253, 294.51581, 4.02465, 4.02465, 0.16191]),
        'MED': np.array([0.816828, 298.574095, 3.108875, 3.108875, 0.31032]),
        'CAR': np.array([0.822337, 295.964855, 3.867855, 3.867855, 0.31032]),
        'IND': np.array([0.850456, 289.461232, 3.272985, 3.272985, 0.31032]),
        'SPW': np.array([0.873495, 291.664203, 3.218868, 3.218868, 0.31032]),
        'SPE': np.array([0.880759, 297.220157, 2.699889, 2.699889, 0.31032]),
        'EPW': np.array([0.82782, 298.663887, 2.723588, 2.723588, 0.31032]),
        'EPE': np.array([0.789429, 294.57762, 2.383051, 2.383051, 0.31032]),
        'NPW': np.array([0.889034, 293.162337, 2.399789, 2.399789, 0.31032]),
        'NPE': np.array([0.821932, 300.557611, 2.761653, 2.761653, 0.31032]),
        'NAT': np.array([0.89622, 298.244352, 2.989733, 2.989733, 0.31032]),
        'SAT': np.array([0.816601, 298.659497, 2.61254, 2.61254, 0.31032]),
        'EAT': np.array([0.790974, 298.090213, 2.584726, 2.584726, 0.31032]),
        'SIO': np.array([0.880966, 293.783521, 2.817875, 2.817875, 0.31032]),
        'NNE': np.array([0.871737, 291.179194, 2.65455, 2.65455, 0.31032]),
        'NNW': np.array([0.834625, 299.89762, 2.802704, 2.802704, 0.31032]),
        'WPE': np.array([0.85582, 285.221885, 2.735712, 2.735712, 0.31032]),
        'WPS': np.array([0.923718, 284.362084, 4.081354, 4.081354, 0.31032]),
        'HBO': np.array([0.912747, 282.250259, 4.555291, 4.555291, 0.31032]),
        'WPN': np.array([0.81673, 301.113225, 2.691748, 2.691748, 0.31032]),
        'NNA': np.array([0.793073, 298.547957, 2.527858, 2.527858, 0.31032]),
    }, index=['rho', 'beta0', 'beta1', 'beta2', 'phi']),
    'CanESM': pd.DataFrame({
        'ARL': np.array([0.992731, 287.496364, 7.715974, 7.715974, 0.16191]),
        'ARO': np.array([0.987632, 282.430683, 7.180434, 7.180434, 0.31032]),
        'ANL': np.array([0.993874, 289.560162, 7.61585, 7.61585, 0.16191]),
        'AOP': np.array([0.985162, 258.720466, 9.61623, 9.61623, 0.31032]),
        'AOI': np.array([0.983958, 260.756247, 11.817963, 11.817963, 0.31032]),
        'ALA': np.array([0.997551, 238.387076, 18.440044, 18.440044, 0.16191]),
        'CGI': np.array([0.994605, 271.683906, 6.94636, 6.94636, 0.16191]),
        'WNA': np.array([0.996887, 269.137766, 15.727013, 15.727013, 0.16191]),
        'CNA': np.array([0.984043, 269.576001, 7.648617, 7.648617, 0.16191]),
        'ENA': np.array([0.987363, 269.80145, 9.081453, 9.081453, 0.16191]),
        'CAM': np.array([0.985068, 281.70307, 5.964253, 5.964253, 0.16191]),
        'AMZ': np.array([0.979371, 287.851121, 4.883777, 4.883777, 0.16191]),
        'SSA': np.array([0.975054, 284.5404, 4.978155, 4.978155, 0.16191]),
        'NEU': np.array([0.991038, 294.654887, 7.379552, 7.379552, 0.16191]),
        'SEU': np.array([0.993127, 298.404801, 12.565044, 12.565044, 0.16191]),
        'SAH': np.array([0.996728, 287.696497, 17.602767, 17.602767, 0.16191]),
        'WAF': np.array([0.9887, 280.158915, 6.965189, 6.965189, 0.16191]),
        'EAF': np.array([0.982613, 288.005664, 5.035428, 5.035428, 0.16191]),
        'SAF': np.array([0.981923, 297.091351, 5.775934, 5.775934, 0.16191]),
        'NAS': np.array([0.996635, 297.885542, 17.406905, 17.406905, 0.16191]),
        'CAS': np.array([0.996689, 296.249344, 15.829067, 15.829067, 0.16191]),
        'TIB': np.array([0.99671, 294.98846, 16.923385, 16.923385, 0.16191]),
        'EAS': np.array([0.97915, 271.429392, 5.709799, 5.709799, 0.16191]),
        'SAS': np.array([0.975689, 286.022933, 5.13864, 5.13864, 0.16191]),
        'SEA': np.array([0.974705, 272.693555, 4.873507, 4.873507, 0.16191]),
        'NAU': np.array([0.976654, 282.571913, 4.11365, 4.11365, 0.16191]),
        'SAU': np.array([0.994923, 294.032905, 11.884524, 11.884524, 0.16191]),
        'MED': np.array([0.997096, 297.202531, 15.998666, 15.998666, 0.31032]),
        'CAR': np.array([0.996664, 295.627365, 16.216712, 16.216712, 0.31032]),
        'IND': np.array([0.997359, 288.225623, 15.94452, 15.94452, 0.31032]),
        'SPW': np.array([0.98075, 292.894832, 4.058358, 4.058358, 0.31032]),
        'SPE': np.array([0.983108, 297.701294, 3.865309, 3.865309, 0.31032]),
        'EPW': np.array([0.995802, 298.186688, 9.662194, 9.662194, 0.31032]),
        'EPE': np.array([0.996554, 293.49033, 10.211775, 10.211775, 0.31032]),
        'NPW': np.array([0.99576, 291.712965, 7.24604, 7.24604, 0.31032]),
        'NPE': np.array([0.994906, 299.989739, 8.276351, 8.276351, 0.31032]),
        'NAT': np.array([0.992333, 298.453522, 6.55314, 6.55314, 0.31032]),
        'SAT': np.array([0.995675, 298.964489, 8.18114, 8.18114, 0.31032]),
        'EAT': np.array([0.992737, 297.204638, 5.971867, 5.971867, 0.31032]),
        'SIO': np.array([0.984506, 293.73415, 3.867709, 3.867709, 0.31032]),
        'NNE': np.array([0.997034, 289.68317, 11.821771, 11.821771, 0.31032]),
        'NNW': np.array([0.996566, 299.672104, 11.231726, 11.231726, 0.31032]),
        'WPE': np.array([0.997392, 284.356903, 12.800824, 12.800824, 0.31032]),
        'WPS': np.array([0.982354, 285.010398, 3.873596, 3.873596, 0.31032]),
        'HBO': np.array([0.978091, 284.067832, 3.827416, 3.827416, 0.31032]),
        'WPN': np.array([0.996418, 300.615826, 10.7455, 10.7455, 0.31032]),
        'NNA': np.array([0.995867, 298.336912, 8.834747, 8.834747, 0.31032]),
    }, index=['rho', 'beta0', 'beta1', 'beta2', 'phi']),
    'CCSM4': pd.DataFrame({
        'ARL': np.array([0.830972, 286.45086, 3.676889, 3.676889, 0.16191]),
        'ARO': np.array([0.822803, 280.511306, 4.554655, 4.554655, 0.31032]),
        'ANL': np.array([0.836358, 288.888906, 3.318214, 3.318214, 0.16191]),
        'AOP': np.array([0.846733, 255.974773, 7.624367, 7.624367, 0.31032]),
        'AOI': np.array([0.901805, 258.050593, 9.695085, 9.695085, 0.31032]),
        'ALA': np.array([0.852863, 237.80037, 5.055503, 5.055503, 0.16191]),
        'CGI': np.array([0.268311, 269.161123, 3.552126, 3.552126, 0.16191]),
        'WNA': np.array([0.695449, 267.76122, 4.755977, 4.755977, 0.16191]),
        'CNA': np.array([0.839561, 266.711157, 6.860294, 6.860294, 0.16191]),
        'ENA': np.array([0.737505, 266.578723, 6.018492, 6.018492, 0.16191]),
        'CAM': np.array([0.821001, 279.555714, 4.544471, 4.544471, 0.16191]),
        'AMZ': np.array([0.766238, 284.634211, 4.096124, 4.096124, 0.16191]),
        'SSA': np.array([0.831997, 281.486666, 4.573439, 4.573439, 0.16191]),
        'NEU': np.array([0.644874, 293.092768, 3.418089, 3.418089, 0.16191]),
        'SEU': np.array([0.806429, 296.081014, 3.936648, 3.936648, 0.16191]),
        'SAH': np.array([0.653345, 288.367117, 3.640267, 3.640267, 0.16191]),
        'WAF': np.array([0.896573, 279.937302, 3.981846, 3.981846, 0.16191]),
        'EAF': np.array([0.878254, 287.68687, 3.97588, 3.97588, 0.16191]),
        'SAF': np.array([0.650435, 295.56465, 4.296887, 4.296887, 0.16191]),
        'NAS': np.array([0.818253, 297.158417, 3.682635, 3.682635, 0.16191]),
        'CAS': np.array([0.818837, 295.633561, 3.465445, 3.465445, 0.16191]),
        'TIB': np.array([0.795701, 294.209965, 3.599888, 3.599888, 0.16191]),
        'EAS': np.array([0.853203, 268.703785, 6.456362, 6.456362, 0.16191]),
        'SAS': np.array([0.80816, 285.991239, 4.36554, 4.36554, 0.16191]),
        'SEA': np.array([0.785164, 272.842672, 4.765827, 4.765827, 0.16191]),
        'NAU': np.array([0.855184, 280.916216, 3.934659, 3.934659, 0.16191]),
        'SAU': np.array([0.845821, 294.000603, 3.732071, 3.732071, 0.16191]),
        'MED': np.array([0.776575, 296.734812, 3.118457, 3.118457, 0.31032]),
        'CAR': np.array([0.829018, 295.644607, 3.726077, 3.726077, 0.31032]),
        'IND': np.array([0.833184, 288.563408, 3.633851, 3.633851, 0.31032]),
        'SPW': np.array([0.859073, 293.109475, 3.098235, 3.098235, 0.31032]),
        'SPE': np.array([0.824938, 297.38514, 2.721536, 2.721536, 0.31032]),
        'EPW': np.array([0.793387, 297.821352, 2.837099, 2.837099, 0.31032]),
        'EPE': np.array([0.790734, 293.925267, 2.846727, 2.846727, 0.31032]),
        'NPW': np.array([0.780089, 292.175398, 2.43383, 2.43383, 0.31032]),
        'NPE': np.array([0.747099, 300.039601, 2.822396, 2.822396, 0.31032]),
        'NAT': np.array([0.815128, 297.670834, 2.967578, 2.967578, 0.31032]),
        'SAT': np.array([0.770769, 298.576308, 2.685371, 2.685371, 0.31032]),
        'EAT': np.array([0.795449, 297.557451, 2.642405, 2.642405, 0.31032]),
        'SIO': np.array([0.891002, 293.844893, 2.549265, 2.549265, 0.31032]),
        'NNE': np.array([0.876007, 291.215296, 2.951986, 2.951986, 0.31032]),
        'NNW': np.array([0.692865, 299.215664, 2.741494, 2.741494, 0.31032]),
        'WPE': np.array([0.89439, 284.331066, 3.520001, 3.520001, 0.31032]),
        'WPS': np.array([0.886958, 285.242158, 3.65984, 3.65984, 0.31032]),
        'HBO': np.array([0.882251, 282.764139, 4.265822, 4.265822, 0.31032]),
        'WPN': np.array([0.776999, 300.081508, 2.827846, 2.827846, 0.31032]),
        'NNA': np.array([0.825884, 297.383887, 2.797835, 2.797835, 0.31032]),
    }, index=['rho', 'beta0', 'beta1', 'beta2', 'phi']),
    'GISS_E2_H': pd.DataFrame({
        'ARL': np.array([0.419183, 288.193081, 2.996194, 2.996194, 0.16191]),
        'ARO': np.array([-0.584446, 282.411875, 3.911377, 3.911377, 0.31032]),
        'ANL': np.array([0.639009, 290.54139, 2.636117, 2.636117, 0.16191]),
        'AOP': np.array([-0.984471, 256.038016, 7.617967, 7.617967, 0.31032]),
        'AOI': np.array([-0.991194, 257.753009, 10.943906, 10.943906, 0.31032]),
        'ALA': np.array([-1.01903, 244.061625, 3.000909, 3.000909, 0.16191]),
        'CGI': np.array([-1.02073, 276.833895, 1.905794, 1.905794, 0.16191]),
        'WNA': np.array([0.880941, 275.937573, 1.766089, 1.766089, 0.16191]),
        'CNA': np.array([-1.014979, 268.328625, 5.908136, 5.908136, 0.16191]),
        'ENA': np.array([0.103739, 267.692041, 6.101226, 6.101226, 0.16191]),
        'CAM': np.array([0.748722, 279.185299, 3.503823, 3.503823, 0.16191]),
        'AMZ': np.array([0.805058, 283.930491, 3.441006, 3.441006, 0.16191]),
        'SSA': np.array([0.692293, 280.57256, 3.996011, 3.996011, 0.16191]),
        'NEU': np.array([0.626949, 293.11754, 2.863742, 2.863742, 0.16191]),
        'SEU': np.array([0.811087, 297.648721, 3.518702, 3.518702, 0.16191]),
        'SAH': np.array([0.867921, 291.658954, 1.949995, 1.949995, 0.16191]),
        'WAF': np.array([0.292183, 276.480585, 5.304403, 5.304403, 0.16191]),
        'EAF': np.array([0.470626, 287.096823, 3.494194, 3.494194, 0.16191]),
        'SAF': np.array([-0.315029, 299.435028, 4.221892, 4.221892, 0.16191]),
        'NAS': np.array([-0.828287, 300.47184, 3.436147, 3.436147, 0.16191]),
        'CAS': np.array([-0.83526, 297.862774, 3.704418, 3.704418, 0.16191]),
        'TIB': np.array([0.671085, 296.649656, 3.750187, 3.750187, 0.16191]),
        'EAS': np.array([-0.949646, 268.149696, 5.208826, 5.208826, 0.16191]),
        'SAS': np.array([-0.148952, 285.42905, 3.85781, 3.85781, 0.16191]),
        'SEA': np.array([0.842213, 272.587106, 4.470535, 4.470535, 0.16191]),
        'NAU': np.array([-0.045126, 281.490978, 3.3844, 3.3844, 0.16191]),
        'SAU': np.array([0.550207, 297.260344, 3.314479, 3.314479, 0.16191]),
        'MED': np.array([0.645283, 297.549274, 2.472343, 2.472343, 0.31032]),
        'CAR': np.array([0.853704, 298.393891, 3.457058, 3.457058, 0.31032]),
        'IND': np.array([0.81144, 290.712819, 2.685099, 2.685099, 0.31032]),
        'SPW': np.array([0.663953, 290.90237, 2.891952, 2.891952, 0.31032]),
        'SPE': np.array([0.737925, 296.828611, 2.560442, 2.560442, 0.31032]),
        'EPW': np.array([-0.581941, 298.175157, 2.429798, 2.429798, 0.31032]),
        'EPE': np.array([0.625573, 294.637987, 1.761709, 1.761709, 0.31032]),
        'NPW': np.array([0.69827, 294.051372, 2.044487, 2.044487, 0.31032]),
        'NPE': np.array([0.772053, 300.378736, 2.927115, 2.927115, 0.31032]),
        'NAT': np.array([-1.022127, 298.907838, 3.161103, 3.161103, 0.31032]),
        'SAT': np.array([0.550161, 297.965245, 2.258811, 2.258811, 0.31032]),
        'EAT': np.array([0.595364, 297.252754, 2.475285, 2.475285, 0.31032]),
        'SIO': np.array([0.807191, 293.81041, 2.339722, 2.339722, 0.31032]),
        'NNE': np.array([0.764537, 292.435489, 2.312374, 2.312374, 0.31032]),
        'NNW': np.array([0.607268, 299.976328, 2.578571, 2.578571, 0.31032]),
        'WPE': np.array([0.844365, 286.951544, 1.769847, 1.769847, 0.31032]),
        'WPS': np.array([0.905749, 285.459132, 3.072922, 3.072922, 0.31032]),
        'HBO': np.array([-1.016629, 281.981669, 3.844201, 3.844201, 0.31032]),
        'WPN': np.array([0.768447, 301.067769, 2.238196, 2.238196, 0.31032]),
        'NNA': np.array([-1.01358, 298.578885, 2.173499, 2.173499, 0.31032]),
    }, index=['rho', 'beta0', 'beta1', 'beta2', 'phi']),
    'IPSL_CM5A_LR': pd.DataFrame({
        'ARL': np.array([0.915276, 285.183372, 4.766341, 4.766341, 0.16191]),
        'ARO': np.array([0.907614, 279.96456, 6.026394, 6.026394, 0.31032]),
        'ANL': np.array([0.919618, 287.309344, 4.25648, 4.25648, 0.16191]),
        'AOP': np.array([0.932785, 257.053047, 8.437974, 8.437974, 0.31032]),
        'AOI': np.array([0.940091, 258.422017, 10.790589, 10.790589, 0.31032]),
        'ALA': np.array([0.949746, 238.659431, 4.214698, 4.214698, 0.16191]),
        'CGI': np.array([0.995318, 271.907899, 8.509882, 8.509882, 0.16191]),
        'WNA': np.array([0.957771, 270.054014, 3.07763, 3.07763, 0.16191]),
        'CNA': np.array([0.935792, 268.7202, 7.981822, 7.981822, 0.16191]),
        'ENA': np.array([0.936364, 265.883459, 7.742968, 7.742968, 0.16191]),
        'CAM': np.array([0.890935, 277.600585, 6.128192, 6.128192, 0.16191]),
        'AMZ': np.array([0.860392, 281.556062, 5.784925, 5.784925, 0.16191]),
        'SSA': np.array([0.878235, 279.27165, 5.981576, 5.981576, 0.16191]),
        'NEU': np.array([0.892257, 292.69888, 5.079768, 5.079768, 0.16191]),
        'SEU': np.array([0.909578, 296.042509, 5.623428, 5.623428, 0.16191]),
        'SAH': np.array([0.873427, 286.814354, 4.638081, 4.638081, 0.16191]),
        'WAF': np.array([0.924927, 275.741877, 7.477003, 7.477003, 0.16191]),
        'EAF': np.array([0.887627, 284.611784, 5.92377, 5.92377, 0.16191]),
        'SAF': np.array([0.901093, 292.515421, 6.189928, 6.189928, 0.16191]),
        'NAS': np.array([0.902055, 296.984764, 5.617298, 5.617298, 0.16191]),
        'CAS': np.array([0.890628, 294.683823, 5.528902, 5.528902, 0.16191]),
        'TIB': np.array([0.88797, 293.838364, 5.394709, 5.394709, 0.16191]),
        'EAS': np.array([0.914352, 267.628351, 7.749312, 7.749312, 0.16191]),
        'SAS': np.array([0.904648, 283.235793, 6.710367, 6.710367, 0.16191]),
        'SEA': np.array([0.889408, 270.341864, 6.897627, 6.897627, 0.16191]),
        'NAU': np.array([0.894901, 278.452331, 6.098187, 6.098187, 0.16191]),
        'SAU': np.array([0.897254, 293.443005, 5.835727, 5.835727, 0.16191]),
        'MED': np.array([0.903306, 296.992688, 4.565016, 4.565016, 0.31032]),
        'CAR': np.array([0.849482, 294.831771, 5.281182, 5.281182, 0.31032]),
        'IND': np.array([0.858815, 286.659144, 4.55493, 4.55493, 0.31032]),
        'SPW': np.array([0.868791, 290.221935, 4.509378, 4.509378, 0.31032]),
        'SPE': np.array([0.907056, 295.185988, 4.143833, 4.143833, 0.31032]),
        'EPW': np.array([0.894091, 295.856135, 4.28233, 4.28233, 0.31032]),
        'EPE': np.array([0.891427, 291.49711, 3.675959, 3.675959, 0.31032]),
        'NPW': np.array([0.913481, 289.642154, 3.288683, 3.288683, 0.31032]),
        'NPE': np.array([0.924744, 298.195811, 4.781813, 4.781813, 0.31032]),
        'NAT': np.array([0.935728, 296.490857, 4.768287, 4.768287, 0.31032]),
        'SAT': np.array([0.905079, 296.367939, 4.292854, 4.292854, 0.31032]),
        'EAT': np.array([0.909976, 295.878962, 4.480931, 4.480931, 0.31032]),
        'SIO': np.array([0.919239, 290.134017, 4.186701, 4.186701, 0.31032]),
        'NNE': np.array([0.901627, 287.227232, 3.985241, 3.985241, 0.31032]),
        'NNW': np.array([0.906186, 297.425425, 4.575501, 4.575501, 0.31032]),
        'WPE': np.array([0.930513, 280.522818, 3.334014, 3.334014, 0.31032]),
        'WPS': np.array([0.916296, 283.34401, 4.560233, 4.560233, 0.31032]),
        'HBO': np.array([0.909323, 280.320733, 5.170303, 5.170303, 0.31032]),
        'WPN': np.array([0.901126, 298.628873, 4.35827, 4.35827, 0.31032]),
        'NNA': np.array([0.870483, 295.190697, 4.062374, 4.062374, 0.31032]),
    }, index=['rho', 'beta0', 'beta1', 'beta2', 'phi']),
    'IPSL_CM5A_MR': pd.DataFrame({
        'ARL': np.array([0.88758, 286.153817, 4.284712, 4.284712, 0.16191]),
        'ARO': np.array([0.881473, 281.002178, 5.410455, 5.410455, 0.31032]),
        'ANL': np.array([0.891332, 288.261282, 3.826059, 3.826059, 0.16191]),
        'AOP': np.array([0.896326, 259.641709, 7.14482, 7.14482, 0.31032]),
        'AOI': np.array([0.920625, 261.410151, 9.0339, 9.0339, 0.31032]),
        'ALA': np.array([0.756018, 241.382813, 3.158887, 3.158887, 0.16191]),
        'CGI': np.array([0.915338, 273.258765, 1.784516, 1.784516, 0.16191]),
        'WNA': np.array([0.878282, 271.711518, 2.065, 2.065, 0.16191]),
        'CNA': np.array([0.894405, 269.990418, 6.78965, 6.78965, 0.16191]),
        'ENA': np.array([0.908967, 268.473084, 6.544941, 6.544941, 0.16191]),
        'CAM': np.array([0.883135, 278.993465, 5.685967, 5.685967, 0.16191]),
        'AMZ': np.array([0.908502, 283.85162, 5.770391, 5.770391, 0.16191]),
        'SSA': np.array([0.906896, 281.233736, 5.26291, 5.26291, 0.16191]),
        'NEU': np.array([0.893996, 293.119403, 5.19945, 5.19945, 0.16191]),
        'SEU': np.array([0.86909, 297.304768, 5.143309, 5.143309, 0.16191]),
        'SAH': np.array([0.86835, 287.808679, 4.651783, 4.651783, 0.16191]),
        'WAF': np.array([0.907623, 278.08749, 5.445671, 5.445671, 0.16191]),
        'EAF': np.array([0.854913, 286.441839, 5.140472, 5.140472, 0.16191]),
        'SAF': np.array([0.843582, 293.661299, 5.722015, 5.722015, 0.16191]),
        'NAS': np.array([0.875862, 297.908634, 5.379641, 5.379641, 0.16191]),
        'CAS': np.array([0.869745, 295.821035, 5.224433, 5.224433, 0.16191]),
        'TIB': np.array([0.867048, 294.86143, 5.129973, 5.129973, 0.16191]),
        'EAS': np.array([0.894841, 269.781501, 6.374491, 6.374491, 0.16191]),
        'SAS': np.array([0.903272, 285.013677, 6.041466, 6.041466, 0.16191]),
        'SEA': np.array([0.865967, 271.913005, 6.475449, 6.475449, 0.16191]),
        'NAU': np.array([0.905808, 280.292163, 5.5567, 5.5567, 0.16191]),
        'SAU': np.array([0.867946, 294.80723, 5.326463, 5.326463, 0.16191]),
        'MED': np.array([0.878038, 297.742094, 4.246625, 4.246625, 0.31032]),
        'CAR': np.array([0.818582, 296.014107, 5.032231, 5.032231, 0.31032]),
        'IND': np.array([0.832952, 287.964035, 4.566128, 4.566128, 0.31032]),
        'SPW': np.array([0.884677, 291.352616, 3.651826, 3.651826, 0.31032]),
        'SPE': np.array([0.895587, 296.179068, 3.769354, 3.769354, 0.31032]),
        'EPW': np.array([0.88313, 296.87599, 4.110287, 4.110287, 0.31032]),
        'EPE': np.array([0.869728, 292.508459, 3.696296, 3.696296, 0.31032]),
        'NPW': np.array([0.868555, 290.351844, 3.234777, 3.234777, 0.31032]),
        'NPE': np.array([0.875155, 298.910914, 4.435569, 4.435569, 0.31032]),
        'NAT': np.array([0.904361, 296.868382, 4.416728, 4.416728, 0.31032]),
        'SAT': np.array([0.887493, 297.68243, 4.0603, 4.0603, 0.31032]),
        'EAT': np.array([0.878231, 296.878378, 4.007293, 4.007293, 0.31032]),
        'SIO': np.array([0.901424, 291.559347, 3.600911, 3.600911, 0.31032]),
        'NNE': np.array([0.882471, 288.4247, 4.11149, 4.11149, 0.31032]),
        'NNW': np.array([0.896163, 298.281456, 4.305655, 4.305655, 0.31032]),
        'WPE': np.array([0.803267, 281.914848, 3.121427, 3.121427, 0.31032]),
        'WPS': np.array([0.913181, 284.015066, 4.018919, 4.018919, 0.31032]),
        'HBO': np.array([0.921945, 281.720921, 4.625936, 4.625936, 0.31032]),
        'WPN': np.array([0.878203, 299.640745, 4.026109, 4.026109, 0.31032]),
        'NNA': np.array([0.877607, 296.265926, 3.975404, 3.975404, 0.31032]),
    }, index=['rho', 'beta0', 'beta1', 'beta2', 'phi']),
    'MIROC5': pd.DataFrame({
        'ARL': np.array([0.939989, 288.034446, 3.157749, 3.157749, 0.16191]),
        'ARO': np.array([0.939505, 283.10727, 4.324218, 4.324218, 0.31032]),
        'ANL': np.array([0.940326, 290.054798, 2.679621, 2.679621, 0.16191]),
        'AOP': np.array([0.935314, 257.444026, 8.22798, 8.22798, 0.31032]),
        'AOI': np.array([0.944794, 258.734184, 10.558706, 10.558706, 0.31032]),
        'ALA': np.array([0.881903, 244.989383, 1.962362, 1.962362, 0.16191]),
        'CGI': np.array([0.984372, 277.211526, 0.106278, 0.106278, 0.16191]),
        'WNA': np.array([-0.233791, 275.433335, 0.985971, 0.985971, 0.16191]),
        'CNA': np.array([0.946005, 269.957241, 6.977428, 6.977428, 0.16191]),
        'ENA': np.array([0.912053, 268.729749, 6.755755, 6.755755, 0.16191]),
        'CAM': np.array([0.943585, 281.953322, 4.434377, 4.434377, 0.16191]),
        'AMZ': np.array([0.933993, 286.158089, 5.050935, 5.050935, 0.16191]),
        'SSA': np.array([0.932772, 282.237036, 5.149036, 5.149036, 0.16191]),
        'NEU': np.array([0.943, 295.089584, 4.027071, 4.027071, 0.16191]),
        'SEU': np.array([0.94876, 297.401028, 4.229917, 4.229917, 0.16191]),
        'SAH': np.array([0.935094, 290.876943, 2.923943, 2.923943, 0.16191]),
        'WAF': np.array([0.942243, 280.921326, 4.084255, 4.084255, 0.16191]),
        'EAF': np.array([0.943794, 289.718903, 3.953692, 3.953692, 0.16191]),
        'SAF': np.array([0.929126, 298.542118, 4.583774, 4.583774, 0.16191]),
        'NAS': np.array([0.955745, 299.088305, 4.219753, 4.219753, 0.16191]),
        'CAS': np.array([0.94496, 297.535024, 3.919978, 3.919978, 0.16191]),
        'TIB': np.array([0.949339, 295.722437, 3.985939, 3.985939, 0.16191]),
        'EAS': np.array([0.929066, 269.815312, 5.353445, 5.353445, 0.16191]),
        'SAS': np.array([0.937214, 288.861826, 4.551659, 4.551659, 0.16191]),
        'SEA': np.array([0.946902, 275.221379, 5.282512, 5.282512, 0.16191]),
        'NAU': np.array([0.958787, 283.525425, 3.901738, 3.901738, 0.16191]),
        'SAU': np.array([0.956343, 296.981138, 3.645494, 3.645494, 0.16191]),
        'MED': np.array([0.950331, 298.05819, 2.857129, 2.857129, 0.31032]),
        'CAR': np.array([0.959675, 297.034036, 4.052747, 4.052747, 0.31032]),
        'IND': np.array([0.932421, 290.413546, 3.036404, 3.036404, 0.31032]),
        'SPW': np.array([0.926359, 292.240763, 3.237052, 3.237052, 0.31032]),
        'SPE': np.array([0.945732, 297.172682, 3.270704, 3.270704, 0.31032]),
        'EPW': np.array([0.943749, 297.602102, 2.784139, 2.784139, 0.31032]),
        'EPE': np.array([0.906121, 293.66895, 2.272321, 2.272321, 0.31032]),
        'NPW': np.array([0.940928, 292.242108, 1.884584, 1.884584, 0.31032]),
        'NPE': np.array([0.974169, 299.771661, 3.067377, 3.067377, 0.31032]),
        'NAT': np.array([0.943676, 297.868742, 3.541793, 3.541793, 0.31032]),
        'SAT': np.array([0.957858, 297.49037, 3.164119, 3.164119, 0.31032]),
        'EAT': np.array([0.957538, 297.261683, 2.945282, 2.945282, 0.31032]),
        'SIO': np.array([0.920965, 293.372003, 2.496786, 2.496786, 0.31032]),
        'NNE': np.array([0.940539, 290.615945, 2.529939, 2.529939, 0.31032]),
        'NNW': np.array([0.950946, 299.207778, 3.391261, 3.391261, 0.31032]),
        'WPE': np.array([0.735244, 285.336663, 1.784371, 1.784371, 0.31032]),
        'WPS': np.array([0.967686, 286.720227, 3.172335, 3.172335, 0.31032]),
        'HBO': np.array([0.954191, 283.697136, 3.765344, 3.765344, 0.31032]),
        'WPN': np.array([0.951069, 300.239509, 2.770523, 2.770523, 0.31032]),
        'NNA': np.array([0.937011, 296.911443, 2.613973, 2.613973, 0.31032]),
    }, index=['rho', 'beta0', 'beta1', 'beta2', 'phi']),
    'MIROC_ESM': pd.DataFrame({
        'ARL': np.array([0.956401, 287.222046, 4.640659, 4.640659, 0.16191]),
        'ARO': np.array([0.956762, 283.101305, 6.100216, 6.100216, 0.31032]),
        'ANL': np.array([0.956156, 288.900868, 4.045477, 4.045477, 0.16191]),
        'AOP': np.array([0.958846, 261.219966, 10.389317, 10.389317, 0.31032]),
        'AOI': np.array([0.963545, 263.885665, 12.410994, 12.410994, 0.31032]),
        'ALA': np.array([0.948071, 242.023282, 5.437874, 5.437874, 0.16191]),
        'CGI': np.array([0.893432, 271.845433, 2.641924, 2.641924, 0.16191]),
        'WNA': np.array([0.962933, 270.180669, 4.951983, 4.951983, 0.16191]),
        'CNA': np.array([0.95947, 272.312466, 8.000664, 8.000664, 0.16191]),
        'ENA': np.array([0.942916, 271.945308, 7.797163, 7.797163, 0.16191]),
        'CAM': np.array([0.966077, 281.998328, 6.585555, 6.585555, 0.16191]),
        'AMZ': np.array([0.959563, 286.333128, 6.370447, 6.370447, 0.16191]),
        'SSA': np.array([0.954718, 283.796106, 6.990292, 6.990292, 0.16191]),
        'NEU': np.array([0.951405, 296.207011, 3.926869, 3.926869, 0.16191]),
        'SEU': np.array([0.965115, 296.879116, 6.492604, 6.492604, 0.16191]),
        'SAH': np.array([0.950194, 289.276126, 5.035632, 5.035632, 0.16191]),
        'WAF': np.array([0.956816, 281.480759, 5.504519, 5.504519, 0.16191]),
        'EAF': np.array([0.952691, 289.276504, 5.474975, 5.474975, 0.16191]),
        'SAF': np.array([0.94795, 295.542598, 5.903, 5.903, 0.16191]),
        'NAS': np.array([0.952314, 298.540995, 4.255297, 4.255297, 0.16191]),
        'CAS': np.array([0.954288, 296.480032, 3.83672, 3.83672, 0.16191]),
        'TIB': np.array([0.956341, 295.356497, 4.588098, 4.588098, 0.16191]),
        'EAS': np.array([0.962137, 271.082748, 9.002828, 9.002828, 0.16191]),
        'SAS': np.array([0.955352, 288.263319, 5.727456, 5.727456, 0.16191]),
        'SEA': np.array([0.945029, 272.833727, 6.891963, 6.891963, 0.16191]),
        'NAU': np.array([0.95412, 282.890549, 6.094377, 6.094377, 0.16191]),
        'SAU': np.array([0.944999, 294.074957, 5.244459, 5.244459, 0.16191]),
        'MED': np.array([0.947127, 297.536107, 4.107286, 4.107286, 0.31032]),
        'CAR': np.array([0.976106, 297.008879, 4.74187, 4.74187, 0.31032]),
        'IND': np.array([0.958238, 288.141191, 4.451317, 4.451317, 0.31032]),
        'SPW': np.array([0.953337, 291.767322, 5.012366, 5.012366, 0.31032]),
        'SPE': np.array([0.953536, 296.605706, 4.124581, 4.124581, 0.31032]),
        'EPW': np.array([0.949469, 296.66668, 3.57412, 3.57412, 0.31032]),
        'EPE': np.array([0.947515, 292.47367, 3.138879, 3.138879, 0.31032]),
        'NPW': np.array([0.951368, 290.62156, 3.068843, 3.068843, 0.31032]),
        'NPE': np.array([0.949965, 297.800518, 3.857416, 3.857416, 0.31032]),
        'NAT': np.array([0.957805, 296.73294, 4.392992, 4.392992, 0.31032]),
        'SAT': np.array([0.956052, 296.886567, 3.685298, 3.685298, 0.31032]),
        'EAT': np.array([0.958088, 296.383661, 3.839291, 3.839291, 0.31032]),
        'SIO': np.array([0.957659, 292.765509, 4.163693, 4.163693, 0.31032]),
        'NNE': np.array([0.951599, 289.079164, 3.606583, 3.606583, 0.31032]),
        'NNW': np.array([0.957271, 298.27561, 3.958456, 3.958456, 0.31032]),
        'WPE': np.array([0.947324, 283.238585, 3.022437, 3.022437, 0.31032]),
        'WPS': np.array([0.974724, 285.846666, 4.92217, 4.92217, 0.31032]),
        'HBO': np.array([0.966287, 284.778055, 5.253164, 5.253164, 0.31032]),
        'WPN': np.array([0.949526, 298.869948, 3.254483, 3.254483, 0.31032]),
        'NNA': np.array([0.954018, 297.070712, 3.625144, 3.625144, 0.31032]),
    }, index=['rho', 'beta0', 'beta1', 'beta2', 'phi']),
    'MRI_CGCM3': pd.DataFrame({
        'ARL': np.array([0.939937, 286.965703, 2.944952, 2.944952, 0.16191]),
        'ARO': np.array([0.928311, 281.051991, 3.780074, 3.780074, 0.31032]),
        'ANL': np.array([0.945624, 289.389547, 2.605369, 2.605369, 0.16191]),
        'AOP': np.array([0.916084, 256.871748, 6.529049, 6.529049, 0.31032]),
        'AOI': np.array([0.918323, 258.560447, 8.355975, 8.355975, 0.31032]),
        'ALA': np.array([0.952665, 243.458331, 3.424285, 3.424285, 0.16191]),
        'CGI': np.array([0.941853, 274.197497, 2.3374, 2.3374, 0.16191]),
        'WNA': np.array([0.984967, 273.154028, 3.360914, 3.360914, 0.16191]),
        'CNA': np.array([0.923042, 269.317592, 4.14598, 4.14598, 0.16191]),
        'ENA': np.array([0.938513, 265.922677, 5.344982, 5.344982, 0.16191]),
        'CAM': np.array([0.941239, 278.636198, 3.386021, 3.386021, 0.16191]),
        'AMZ': np.array([0.950744, 283.187035, 3.552332, 3.552332, 0.16191]),
        'SSA': np.array([0.955634, 279.792218, 4.304106, 4.304106, 0.16191]),
        'NEU': np.array([0.930169, 292.592252, 3.183987, 3.183987, 0.16191]),
        'SEU': np.array([0.924406, 295.669852, 3.212472, 3.212472, 0.16191]),
        'SAH': np.array([0.861858, 289.303731, 2.377837, 2.377837, 0.16191]),
        'WAF': np.array([0.954933, 277.400405, 4.263504, 4.263504, 0.16191]),
        'EAF': np.array([0.913972, 286.132718, 3.331862, 3.331862, 0.16191]),
        'SAF': np.array([0.904167, 294.92656, 4.060256, 4.060256, 0.16191]),
        'NAS': np.array([0.921076, 298.998168, 3.6702, 3.6702, 0.16191]),
        'CAS': np.array([0.929827, 297.171159, 3.198743, 3.198743, 0.16191]),
        'TIB': np.array([0.922287, 295.792108, 3.228637, 3.228637, 0.16191]),
        'EAS': np.array([0.928348, 267.715726, 5.074122, 5.074122, 0.16191]),
        'SAS': np.array([0.891224, 284.228847, 3.958023, 3.958023, 0.16191]),
        'SEA': np.array([0.89689, 271.893631, 3.838035, 3.838035, 0.16191]),
        'NAU': np.array([0.938133, 280.519629, 3.88804, 3.88804, 0.16191]),
        'SAU': np.array([0.941621, 295.408106, 2.705551, 2.705551, 0.16191]),
        'MED': np.array([0.936167, 296.940062, 2.632011, 2.632011, 0.31032]),
        'CAR': np.array([0.93704, 297.137751, 3.1335, 3.1335, 0.31032]),
        'IND': np.array([0.930733, 290.85583, 2.487086, 2.487086, 0.31032]),
        'SPW': np.array([0.954239, 290.198667, 3.163115, 3.163115, 0.31032]),
        'SPE': np.array([0.943989, 296.67527, 2.57542, 2.57542, 0.31032]),
        'EPW': np.array([0.925713, 297.651085, 2.214957, 2.214957, 0.31032]),
        'EPE': np.array([0.926181, 294.32024, 1.778039, 1.778039, 0.31032]),
        'NPW': np.array([0.91472, 293.501421, 1.681248, 1.681248, 0.31032]),
        'NPE': np.array([0.94138, 299.558238, 2.802448, 2.802448, 0.31032]),
        'NAT': np.array([0.928287, 297.193295, 2.820232, 2.820232, 0.31032]),
        'SAT': np.array([0.949344, 297.642789, 2.131576, 2.131576, 0.31032]),
        'EAT': np.array([0.941989, 297.008457, 2.425238, 2.425238, 0.31032]),
        'SIO': np.array([0.958135, 292.10346, 2.669982, 2.669982, 0.31032]),
        'NNE': np.array([0.921073, 291.73685, 2.010992, 2.010992, 0.31032]),
        'NNW': np.array([0.931977, 298.853582, 2.583344, 2.583344, 0.31032]),
        'WPE': np.array([0.953808, 285.77521, 2.254861, 2.254861, 0.31032]),
        'WPS': np.array([0.956357, 285.062922, 2.604507, 2.604507, 0.31032]),
        'HBO': np.array([0.960737, 280.812151, 4.306746, 4.306746, 0.31032]),
        'WPN': np.array([0.92819, 299.755408, 2.243889, 2.243889, 0.31032]),
        'NNA': np.array([0.917711, 297.272558, 2.114962, 2.114962, 0.31032]),
    }, index=['rho', 'beta0', 'beta1', 'beta2', 'phi']),
    'NorESM': pd.DataFrame({
        'ARL': np.array([0.913384, 286.31401, 2.998293, 2.998293, 0.16191]),
        'ARO': np.array([0.922568, 280.60661, 4.211842, 4.211842, 0.31032]),
        'ANL': np.array([0.905101, 288.644884, 2.500483, 2.500483, 0.16191]),
        'AOP': np.array([0.9398, 255.383014, 7.86144, 7.86144, 0.31032]),
        'AOI': np.array([0.935897, 259.096856, 8.692844, 8.692844, 0.31032]),
        'ALA': np.array([0.166272, 237.444837, 2.632943, 2.632943, 0.16191]),
        'CGI': np.array([-1.023863, 270.928856, 1.151397, 1.151397, 0.16191]),
        'WNA': np.array([-0.995856, 269.203332, 1.79494, 1.79494, 0.16191]),
        'CNA': np.array([0.95407, 266.114909, 6.724899, 6.724899, 0.16191]),
        'ENA': np.array([0.954474, 265.594851, 6.99633, 6.99633, 0.16191]),
        'CAM': np.array([0.943399, 279.107991, 4.75122, 4.75122, 0.16191]),
        'AMZ': np.array([0.922653, 282.732432, 4.754617, 4.754617, 0.16191]),
        'SSA': np.array([0.948046, 279.665097, 5.106604, 5.106604, 0.16191]),
        'NEU': np.array([0.912737, 293.56125, 3.353175, 3.353175, 0.16191]),
        'SEU': np.array([0.900438, 295.75437, 3.542722, 3.542722, 0.16191]),
        'SAH': np.array([0.839288, 288.460025, 2.738573, 2.738573, 0.16191]),
        'WAF': np.array([0.943255, 279.651707, 4.195911, 4.195911, 0.16191]),
        'EAF': np.array([0.933178, 287.968648, 3.917766, 3.917766, 0.16191]),
        'SAF': np.array([0.893501, 294.859591, 4.127692, 4.127692, 0.16191]),
        'NAS': np.array([0.875537, 296.979048, 3.157251, 3.157251, 0.16191]),
        'CAS': np.array([0.878963, 295.185914, 3.035152, 3.035152, 0.16191]),
        'TIB': np.array([0.902184, 293.811261, 3.063152, 3.063152, 0.16191]),
        'EAS': np.array([0.925582, 267.28254, 6.582986, 6.582986, 0.16191]),
        'SAS': np.array([0.945574, 285.378234, 4.909955, 4.909955, 0.16191]),
        'SEA': np.array([0.935799, 272.575204, 5.116683, 5.116683, 0.16191]),
        'NAU': np.array([0.943925, 278.947703, 4.462947, 4.462947, 0.16191]),
        'SAU': np.array([0.921627, 294.329385, 3.39981, 3.39981, 0.16191]),
        'MED': np.array([0.90463, 296.96778, 2.693007, 2.693007, 0.31032]),
        'CAR': np.array([0.896148, 295.252777, 2.750377, 2.750377, 0.31032]),
        'IND': np.array([0.867584, 288.759836, 2.48798, 2.48798, 0.31032]),
        'SPW': np.array([0.946812, 292.067251, 3.240853, 3.240853, 0.31032]),
        'SPE': np.array([0.933614, 296.187525, 2.727907, 2.727907, 0.31032]),
        'EPW': np.array([0.882735, 296.796245, 2.434853, 2.434853, 0.31032]),
        'EPE': np.array([0.750074, 292.996424, 1.991392, 1.991392, 0.31032]),
        'NPW': np.array([0.818359, 291.581213, 1.516779, 1.516779, 0.31032]),
        'NPE': np.array([0.87937, 299.561517, 2.18502, 2.18502, 0.31032]),
        'NAT': np.array([0.92887, 297.301645, 2.456807, 2.456807, 0.31032]),
        'SAT': np.array([0.913078, 297.341507, 2.50831, 2.50831, 0.31032]),
        'EAT': np.array([0.929827, 296.391732, 2.262281, 2.262281, 0.31032]),
        'SIO': np.array([0.94811, 292.751528, 2.65085, 2.65085, 0.31032]),
        'NNE': np.array([0.909955, 289.639312, 2.363242, 2.363242, 0.31032]),
        'NNW': np.array([0.877464, 298.522277, 2.496515, 2.496515, 0.31032]),
        'WPE': np.array([-1.009128, 284.274976, 1.860333, 1.860333, 0.31032]),
        'WPS': np.array([0.950392, 284.97547, 2.895952, 2.895952, 0.31032]),
        'HBO': np.array([0.947442, 282.193261, 4.051639, 4.051639, 0.31032]),
        'WPN': np.array([0.885707, 299.158055, 2.426446, 2.426446, 0.31032]),
        'NNA': np.array([0.869235, 296.255332, 2.377817, 2.377817, 0.31032]),
    }, index=['rho', 'beta0', 'beta1', 'beta2', 'phi']),
}