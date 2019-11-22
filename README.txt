CLASIFICADOR DE IMÁGENES DEL VOLCÁN DE COLIMA 

Licencia GPL (anexada)

La detección de imágenes se hace a través de un modelo de TensorFlow y las pesas "volcano_analysis.h5"

Este modelo fue creado con fines estrictamente vulcanológicos.

Cada parte del proceso del script principal está documentado internamente, y se pueden actualizar las pesas volviendo a correr el archivo "volcano_classifier.ipynb" con nuevas imágenes.

Las imágenes van dentro de un directorio, contenidas dentro de otro directorio que nombra su clasificación

Ejemplo:


├── train
│   ├── 0inactivo
│   │   ├── 053094_result.jpg
│   │   ├── 19113850995_74422e1180_b_result.jpg
│   │   │   ├── images (7)_result.jpeg
│   │   ├── imagesas3)_result.jpeg
│   │   ├── istock-178498781_result.jpg
│   │   ├── istockphoto-918372000-170667a_result.jpg
│   │   ├── nehd-20190818144947-01_result.jpg
│   │   ├── nehd-201908181494954-01_result.jpg
│   │   ├── nell_result.jpg
│   │   ├── volcan-colima-1_result.jpg
│   │   ├── Volcan_de_Colima_2_result.jpg
│   │   ├── Volcan_de_Colima_result.jpg
│   │   ├── Volcan_de_Fuego_result.jpg
│   │   ├── Volcán_descabezado_Reserva_Nacional_Altos_de_Lircay_Región_del_Maule_04.jpg
│   │   └── whatisthedif_result.jpg
│   └── 1activo
│       ├── 000002_result.jpg
│       ├── 00001_resulta.jpeg
│       ├── a143-300x200_result.jpg
│       ├── aaaaa.jpeg
│       ├── downloadsdf2)_result.jpeg
│       ├── download_sssresult.jpeg
│       ├── downloas_result.jpeg
│       ├── volcancolima2_result.jpg
│       ├── volcan-colima-482x220_result.jpg
│       ├── volcan-colima-64536_result.jpg
│       ├── volcan-colima-explosion_result.jpeg
│       ├── volcan_colima_result.jpg
│       ├── Volcán-Colima_result.jpg
│       ├── volcan-de-colima-3_result.jpg
│       ├── volcan-de-colima_result.jpg
│       ├── volcan-de-colimsa_result.jpg
│       ├── volcanic_eruption_indonesia_result.jpeg
│       ├── volcano-for-kids-1024x680_result.jpg
│       ├── volcano-mayon-gettyimages-909166402_result.jpg
│       ├── volcan-Tungurahua-Ecuador_TINIMA20111129_1138_18_result.jpg
│       └── x_lon_mexicovolcano_150826.nbcnews-fp-1200-630_result.jpg
└── validation
    ├── 0inactivo
    │   ├── 20.jpg
    │   ├── 3713223453_f4b6619791_c.jpg
    │   ├── 46508038141_06dab790bb_c.jpg
    │   ├── 5903452826_2bd6b46034_c.jpg
    │   ├── 6281489189_2ff3af5c35_c.jpg
    │   ├── 6282006858_69be2d74d1_c.jpg
    │   ├── 640px-Green_Izalco_Volcano.jpeg
    │   ├── 8219088696_919eb19d9b_c.jpg
    │   └── m02_00517027.jpg
    └── 1activo
        ├── 13701955364_f955a3e9d1_c.jpg
        ├── 2034808_orig.jpg
        ├── 22527131698_3b67631d9d_c.jpg
        ├── 26509961312_fc16407afc_c.jpg
        ├── 26613239216_39c00810df_c.jpg
        ├── 29167870124_7ebd02e45f_c.jpg
        ├── 31640364180_52ed8d8784_b.jpg
        ├── 33980813168_83758e3f8a_c.jpg
        ├── 42556214411_70a39fac7b_c.jpg
        ├── 4725947958_56a8096cd8_c.jpg
        ├── 8537390460_d89047ea9c_c.jpg
        ├── 8815682068_f1a182a55c_c.jpg
        ├── Colima2015__0040.jpeg
        ├── eruption-colima-volcano.jpg
        └── maxresdefault.jp












Las nuevas imágenes deben de claramente demostrar la actividad o inactividad de un volcán, y no debe de haber otro objeto predominante en la imágen.

Esta es la versión de prueba, pero aún así he trabajado con mucho empeño en ella.

Rodrigo Ascencio Flores
Noviembre 2019 
