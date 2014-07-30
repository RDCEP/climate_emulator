#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd


CO2 = np.array([
    [375.11, 377.78, 380.58, 383.52, 386.7, 390.12, 393.8, 397.55, 401.15,
     404.61, 407.97, 411.24, 414.42, 417.5, 420.55, 423.46, 426.14, 428.59,
     430.91, 433.15, 435.33, 437.46, 439.52, 441.51, 443.42, 445.15, 446.62,
     447.94, 449.21, 450.4, 451.52, 452.58, 453.57, 454.49, 455.33, 455.98,
     456.34, 456.52, 456.61, 456.62, 456.56, 456.44, 456.28, 456.07, 455.82,
     455.44, 454.85, 454.15, 453.42, 452.66, 451.86, 451.05, 450.24, 449.42,
     448.6, 447.83, 447.18, 446.56, 445.92, 445.28, 444.62, 443.94, 443.27,
     442.6, 441.95, 441.34, 440.8, 440.3, 439.81, 439.33, 438.85, 438.37,
     437.88, 437.4, 436.94, 436.48, 435.97, 435.47, 435., 434.52, 434.03,
     433.54, 433.03, 432.5, 431.98, 431.47, 431., 430.55, 430.11, 429.68,
     429.25, 428.82, 428.39, 427.95, 427.5, 426.96],
    [375.15, 377.95, 380.86, 383.83, 386.98, 390.16, 393.31, 396.5, 399.75,
     403.01, 406.3, 409.63, 412.99, 416.38, 419.83, 423.27, 426.57, 429.85,
     433.18, 436.55, 439.95, 443.39, 446.87, 450.37, 453.89, 457.46, 461.1,
     464.73, 468.29, 471.84, 475.38, 478.92, 482.46, 485.99, 489.49, 493.,
     496.53, 500.02, 503.42, 506.75, 510.05, 513.34, 516.62, 519.91, 523.2,
     526.38, 529.35, 532.18, 534.91, 537.54, 540.07, 542.54, 544.95, 547.32,
     549.65, 551.91, 554.07, 556.12, 558.08, 559.93, 561.68, 563.32, 564.88,
     566.38, 567.82, 569.18, 570.43, 571.56, 572.58, 573.48, 574.27, 574.93,
     575.46, 575.9, 576.26, 576.43, 576.26, 576.04, 575.97, 575.97, 576.01,
     576.1, 576.22, 576.36, 576.53, 576.77, 577.05, 577.4, 577.79, 578.2,
     578.64, 579.09, 579.55, 580.01, 580.47, 580.91],
    [375.01, 377.41, 379.79, 382.26, 384.88, 387.61, 390.46, 393.4, 396.32,
     399.17, 401.99, 404.79, 407.54, 410.26, 413., 415.77, 418.58, 421.43,
     424.32, 427.27, 430.26, 433.3, 436.38, 439.5, 442.64, 445.56, 448.02,
     450.3, 452.64, 455.04, 457.51, 460.03, 462.61, 465.23, 467.89, 470.72,
     473.89, 477.21, 480.51, 483.84, 487.22, 490.68, 494.2, 497.81, 501.5,
     505.13, 508.61, 512.05, 515.56, 519.12, 522.73, 526.42, 530.21, 534.08,
     538.06, 542.45, 547.57, 553.05, 558.56, 564.15, 569.81, 575.54, 581.37,
     587.32, 593.39, 599.43, 605.24, 610.95, 616.68, 622.42, 628.17, 633.92,
     639.67, 645.45, 651.27, 656.94, 662.25, 667.29, 672.09, 676.62, 680.89,
     684.91, 688.67, 692.18, 695.46, 698.57, 701.51, 704.42, 707.37, 710.34,
     713.32, 716.31, 719.29, 722.26, 725.23, 728.12],
    [375.2, 378.16, 381.36, 384.74, 388.43, 392.06, 395.27, 398.44, 401.79,
     405.28, 408.9, 412.66, 416.55, 420.55, 424.72, 429.09, 433.67, 438.36,
     443.07, 447.89, 452.82, 457.86, 463., 468.23, 473.55, 479.09, 485.,
     491.12, 497.34, 503.73, 510.3, 517.07, 524.01, 531.13, 538.41, 545.79,
     553.25, 560.85, 568.62, 576.55, 584.67, 593.01, 601.56, 610.34, 619.35,
     628.43, 637.46, 646.55, 655.82, 665.23, 674.76, 684.47, 694.36, 704.45,
     714.76, 725.23, 735.8, 746.47, 757.22, 768.05, 778.94, 789.89, 800.93,
     812.1, 823.41, 834.84, 846.36, 857.96, 869.65, 881.43, 893.3, 905.23,
     917.24, 929.33, 941.53, 954.05, 967.06, 980.38, 993.81, 1007.4, 1021.1,
     1034.9, 1048.8, 1062.8, 1077., 1091.1, 1105., 1118.9, 1132.9, 1146.9,
     1161., 1175.1, 1189.2, 1203.4, 1217.5, 1231.4 ],
    [375.00, 380.77, 386.63, 392.58, 398.62, 404.76, 410.99, 417.31, 423.73,
     430.25, 436.87, 443.60, 450.42, 457.36, 464.39, 471.54, 478.80, 486.17,
     493.65, 501.24, 508.96, 516.79, 524.74, 532.82, 541.02, 549.34, 557.80,
     566.38, 575.10, 583.95, 592.93, 602.06, 611.32, 620.73, 630.28, 639.98,
     649.83, 659.83, 669.99, 680.30, 690.77, 701.40, 712.19, 723.15, 734.28,
     745.58, 757.05, 768.70, 780.53, 792.55, 804.74, 817.13, 829.70, 842.47,
     855.43, 868.60, 881.97, 895.54, 909.32, 923.31, 937.52, 951.95, 966.60,
     981.48, 996.58, 1011.92, 1027.49, 1043.30, 1059.36, 1075.66, 1092.21,
     1109.02, 1126.09, 1143.42, 1161.01, 1178.88, 1197.02, 1215.44, 1234.15,
     1253.14, 1272.43, 1292.01, 1311.89, 1332.08, 1352.58, 1373.39, 1394.53,
     1415.99, 1437.78, 1459.91, 1482.37, 1505.19, 1528.35, 1551.87, 1575.75,
     1600.00],
]).transpose()

co2 = pd.DataFrame(
    CO2,
    index=np.linspace(2005, 2100, 96),
    columns=['RCP26', 'RCP45', 'RCP60', 'RCP85', 'EXP1600'],
)