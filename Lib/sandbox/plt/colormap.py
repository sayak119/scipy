from Numeric import array, Float64

colormap_map = {}

colormap_map[ 'bone' ] = array(
   [ [ 0.0, 0.0, 0.005208333333333333 ],
     [ 0.013888888888888888, 0.013888888888888888, 0.024305555555555552 ],
     [ 0.027777777777777776, 0.027777777777777776, 0.043402777777777776 ],
     [ 0.041666666666666664, 0.041666666666666664, 0.0625 ],
     [ 0.055555555555555552, 0.055555555555555552, 0.081597222222222224 ],
     [ 0.069444444444444448, 0.069444444444444448, 0.10069444444444445 ],
     [ 0.083333333333333329, 0.083333333333333329, 0.11979166666666666 ],
     [ 0.09722222222222221, 0.09722222222222221, 0.13888888888888887 ],
     [ 0.1111111111111111, 0.1111111111111111, 0.1579861111111111 ],
     [ 0.125, 0.125, 0.17708333333333334 ],
     [ 0.1388888888888889, 0.1388888888888889, 0.19618055555555555 ],
     [ 0.15277777777777776, 0.15277777777777776, 0.21527777777777776 ],
     [ 0.16666666666666666, 0.16666666666666666, 0.234375 ],
     [ 0.18055555555555555, 0.18055555555555555, 0.25347222222222221 ],
     [ 0.19444444444444442, 0.19444444444444442, 0.27256944444444442 ],
     [ 0.20833333333333331, 0.20833333333333331, 0.29166666666666663 ],
     [ 0.22222222222222221, 0.22222222222222221, 0.3107638888888889 ],
     [ 0.2361111111111111, 0.2361111111111111, 0.3298611111111111 ],
     [ 0.25, 0.25, 0.34895833333333331 ],
     [ 0.2638888888888889, 0.2638888888888889, 0.36805555555555558 ],
     [ 0.27777777777777779, 0.27777777777777779, 0.38715277777777779 ],
     [ 0.29166666666666663, 0.29166666666666663, 0.40624999999999994 ],
     [ 0.30555555555555552, 0.30555555555555552, 0.42534722222222221 ],
     [ 0.31944444444444442, 0.31944444444444442, 0.44444444444444442 ],
     [ 0.33333333333333331, 0.33854166666666663, 0.45833333333333331 ],
     [ 0.34722222222222221, 0.3576388888888889, 0.47222222222222221 ],
     [ 0.3611111111111111, 0.3767361111111111, 0.4861111111111111 ],
     [ 0.375, 0.39583333333333331, 0.5 ],
     [ 0.38888888888888884, 0.41493055555555552, 0.51388888888888884 ],
     [ 0.40277777777777773, 0.43402777777777773, 0.52777777777777768 ],
     [ 0.41666666666666663, 0.45312499999999994, 0.54166666666666663 ],
     [ 0.43055555555555552, 0.47222222222222221, 0.55555555555555558 ],
     [ 0.44444444444444442, 0.49131944444444442, 0.56944444444444442 ],
     [ 0.45833333333333337, 0.51041666666666674, 0.58333333333333337 ],
     [ 0.47222222222222221, 0.52951388888888884, 0.59722222222222221 ],
     [ 0.48611111111111116, 0.54861111111111116, 0.61111111111111116 ],
     [ 0.5, 0.56770833333333337, 0.625 ],
     [ 0.51388888888888895, 0.58680555555555558, 0.63888888888888895 ],
     [ 0.52777777777777779, 0.60590277777777779, 0.65277777777777779 ],
     [ 0.54166666666666674, 0.62500000000000011, 0.66666666666666674 ],
     [ 0.55555555555555558, 0.64409722222222221, 0.68055555555555558 ],
     [ 0.56944444444444442, 0.66319444444444442, 0.69444444444444442 ],
     [ 0.58333333333333326, 0.68229166666666663, 0.70833333333333326 ],
     [ 0.59722222222222221, 0.70138888888888884, 0.72222222222222221 ],
     [ 0.61111111111111105, 0.72048611111111105, 0.73611111111111105 ],
     [ 0.625, 0.73958333333333337, 0.75 ],
     [ 0.63888888888888884, 0.75868055555555547, 0.76388888888888884 ],
     [ 0.65277777777777779, 0.77777777777777779, 0.77777777777777779 ],
     [ 0.67447916666666663, 0.79166666666666663, 0.79166666666666663 ],
     [ 0.69618055555555558, 0.80555555555555558, 0.80555555555555558 ],
     [ 0.71788194444444442, 0.81944444444444442, 0.81944444444444442 ],
     [ 0.73958333333333337, 0.83333333333333337, 0.83333333333333337 ],
     [ 0.76128472222222221, 0.84722222222222221, 0.84722222222222221 ],
     [ 0.78298611111111116, 0.86111111111111116, 0.86111111111111116 ],
     [ 0.8046875, 0.875, 0.875 ],
     [ 0.82638888888888884, 0.88888888888888884, 0.88888888888888884 ],
     [ 0.84809027777777768, 0.90277777777777768, 0.90277777777777768 ],
     [ 0.86979166666666663, 0.91666666666666663, 0.91666666666666663 ],
     [ 0.89149305555555547, 0.93055555555555547, 0.93055555555555547 ],
     [ 0.91319444444444442, 0.94444444444444442, 0.94444444444444442 ],
     [ 0.93489583333333326, 0.95833333333333326, 0.95833333333333326 ],
     [ 0.95659722222222221, 0.97222222222222221, 0.97222222222222221 ],
     [ 0.97829861111111105, 0.98611111111111105, 0.98611111111111105 ],
     [ 1.0, 1.0, 1.0 ] ],
     Float64 )

colormap_map[ 'grey' ] = array(
   [ [ 0, 0, 0 ],
     [ 1, 1, 1 ],
     [ 2, 2, 2 ],
     [ 3, 3, 3 ],
     [ 4, 4, 4 ],
     [ 5, 5, 5 ],
     [ 6, 6, 6 ],
     [ 7, 7, 7 ],
     [ 8, 8, 8 ],
     [ 9, 9, 9 ],
     [ 10, 10, 10 ],
     [ 11, 11, 11 ],
     [ 12, 12, 12 ],
     [ 13, 13, 13 ],
     [ 14, 14, 14 ],
     [ 15, 15, 15 ],
     [ 16, 16, 16 ],
     [ 17, 17, 17 ],
     [ 18, 18, 18 ],
     [ 19, 19, 19 ],
     [ 20, 20, 20 ],
     [ 21, 21, 21 ],
     [ 22, 22, 22 ],
     [ 23, 23, 23 ],
     [ 24, 24, 24 ],
     [ 25, 25, 25 ],
     [ 26, 26, 26 ],
     [ 27, 27, 27 ],
     [ 28, 28, 28 ],
     [ 29, 29, 29 ],
     [ 30, 30, 30 ],
     [ 31, 31, 31 ],
     [ 32, 32, 32 ],
     [ 33, 33, 33 ],
     [ 34, 34, 34 ],
     [ 35, 35, 35 ],
     [ 36, 36, 36 ],
     [ 37, 37, 37 ],
     [ 38, 38, 38 ],
     [ 39, 39, 39 ],
     [ 40, 40, 40 ],
     [ 41, 41, 41 ],
     [ 42, 42, 42 ],
     [ 43, 43, 43 ],
     [ 44, 44, 44 ],
     [ 45, 45, 45 ],
     [ 46, 46, 46 ],
     [ 47, 47, 47 ],
     [ 48, 48, 48 ],
     [ 49, 49, 49 ],
     [ 50, 50, 50 ],
     [ 51, 51, 51 ],
     [ 52, 52, 52 ],
     [ 53, 53, 53 ],
     [ 54, 54, 54 ],
     [ 55, 55, 55 ],
     [ 56, 56, 56 ],
     [ 57, 57, 57 ],
     [ 58, 58, 58 ],
     [ 59, 59, 59 ],
     [ 60, 60, 60 ],
     [ 61, 61, 61 ],
     [ 62, 62, 62 ],
     [ 63, 63, 63 ],
     [ 64, 64, 64 ],
     [ 65, 65, 65 ],
     [ 66, 66, 66 ],
     [ 67, 67, 67 ],
     [ 68, 68, 68 ],
     [ 69, 69, 69 ],
     [ 70, 70, 70 ],
     [ 71, 71, 71 ],
     [ 72, 72, 72 ],
     [ 73, 73, 73 ],
     [ 74, 74, 74 ],
     [ 75, 75, 75 ],
     [ 76, 76, 76 ],
     [ 77, 77, 77 ],
     [ 78, 78, 78 ],
     [ 79, 79, 79 ],
     [ 80, 80, 80 ],
     [ 81, 81, 81 ],
     [ 82, 82, 82 ],
     [ 83, 83, 83 ],
     [ 84, 84, 84 ],
     [ 85, 85, 85 ],
     [ 86, 86, 86 ],
     [ 87, 87, 87 ],
     [ 88, 88, 88 ],
     [ 89, 89, 89 ],
     [ 90, 90, 90 ],
     [ 91, 91, 91 ],
     [ 92, 92, 92 ],
     [ 93, 93, 93 ],
     [ 94, 94, 94 ],
     [ 95, 95, 95 ],
     [ 96, 96, 96 ],
     [ 97, 97, 97 ],
     [ 98, 98, 98 ],
     [ 99, 99, 99 ],
     [ 100, 100, 100 ],
     [ 101, 101, 101 ],
     [ 102, 102, 102 ],
     [ 103, 103, 103 ],
     [ 104, 104, 104 ],
     [ 105, 105, 105 ],
     [ 106, 106, 106 ],
     [ 107, 107, 107 ],
     [ 108, 108, 108 ],
     [ 109, 109, 109 ],
     [ 110, 110, 110 ],
     [ 111, 111, 111 ],
     [ 112, 112, 112 ],
     [ 113, 113, 113 ],
     [ 114, 114, 114 ],
     [ 115, 115, 115 ],
     [ 116, 116, 116 ],
     [ 117, 117, 117 ],
     [ 118, 118, 118 ],
     [ 119, 119, 119 ],
     [ 120, 120, 120 ],
     [ 121, 121, 121 ],
     [ 122, 122, 122 ],
     [ 123, 123, 123 ],
     [ 124, 124, 124 ],
     [ 125, 125, 125 ],
     [ 126, 126, 126 ],
     [ 127, 127, 127 ],
     [ 128, 128, 128 ],
     [ 129, 129, 129 ],
     [ 130, 130, 130 ],
     [ 131, 131, 131 ],
     [ 132, 132, 132 ],
     [ 133, 133, 133 ],
     [ 134, 134, 134 ],
     [ 135, 135, 135 ],
     [ 136, 136, 136 ],
     [ 137, 137, 137 ],
     [ 138, 138, 138 ],
     [ 139, 139, 139 ],
     [ 140, 140, 140 ],
     [ 141, 141, 141 ],
     [ 142, 142, 142 ],
     [ 143, 143, 143 ],
     [ 144, 144, 144 ],
     [ 145, 145, 145 ],
     [ 146, 146, 146 ],
     [ 147, 147, 147 ],
     [ 148, 148, 148 ],
     [ 149, 149, 149 ],
     [ 150, 150, 150 ],
     [ 151, 151, 151 ],
     [ 152, 152, 152 ],
     [ 153, 153, 153 ],
     [ 154, 154, 154 ],
     [ 155, 155, 155 ],
     [ 156, 156, 156 ],
     [ 157, 157, 157 ],
     [ 158, 158, 158 ],
     [ 159, 159, 159 ],
     [ 160, 160, 160 ],
     [ 161, 161, 161 ],
     [ 162, 162, 162 ],
     [ 163, 163, 163 ],
     [ 164, 164, 164 ],
     [ 165, 165, 165 ],
     [ 166, 166, 166 ],
     [ 167, 167, 167 ],
     [ 168, 168, 168 ],
     [ 169, 169, 169 ],
     [ 170, 170, 170 ],
     [ 171, 171, 171 ],
     [ 172, 172, 172 ],
     [ 173, 173, 173 ],
     [ 174, 174, 174 ],
     [ 175, 175, 175 ],
     [ 176, 176, 176 ],
     [ 177, 177, 177 ],
     [ 178, 178, 178 ],
     [ 179, 179, 179 ],
     [ 180, 180, 180 ],
     [ 181, 181, 181 ],
     [ 182, 182, 182 ],
     [ 183, 183, 183 ],
     [ 184, 184, 184 ],
     [ 185, 185, 185 ],
     [ 186, 186, 186 ],
     [ 187, 187, 187 ],
     [ 188, 188, 188 ],
     [ 189, 189, 189 ],
     [ 190, 190, 190 ],
     [ 191, 191, 191 ],
     [ 192, 192, 192 ],
     [ 193, 193, 193 ],
     [ 194, 194, 194 ],
     [ 195, 195, 195 ],
     [ 196, 196, 196 ],
     [ 197, 197, 197 ],
     [ 198, 198, 198 ],
     [ 199, 199, 199 ],
     [ 200, 200, 200 ],
     [ 201, 201, 201 ],
     [ 202, 202, 202 ],
     [ 203, 203, 203 ],
     [ 204, 204, 204 ],
     [ 205, 205, 205 ],
     [ 206, 206, 206 ],
     [ 207, 207, 207 ],
     [ 208, 208, 208 ],
     [ 209, 209, 209 ],
     [ 210, 210, 210 ],
     [ 211, 211, 211 ],
     [ 212, 212, 212 ],
     [ 213, 213, 213 ],
     [ 214, 214, 214 ],
     [ 215, 215, 215 ],
     [ 216, 216, 216 ],
     [ 217, 217, 217 ],
     [ 218, 218, 218 ],
     [ 219, 219, 219 ],
     [ 220, 220, 220 ],
     [ 221, 221, 221 ],
     [ 222, 222, 222 ],
     [ 223, 223, 223 ],
     [ 224, 224, 224 ],
     [ 225, 225, 225 ],
     [ 226, 226, 226 ],
     [ 227, 227, 227 ],
     [ 228, 228, 228 ],
     [ 229, 229, 229 ],
     [ 230, 230, 230 ],
     [ 231, 231, 231 ],
     [ 232, 232, 232 ],
     [ 233, 233, 233 ],
     [ 234, 234, 234 ],
     [ 235, 235, 235 ],
     [ 236, 236, 236 ],
     [ 237, 237, 237 ],
     [ 238, 238, 238 ],
     [ 239, 239, 239 ],
     [ 240, 240, 240 ],
     [ 241, 241, 241 ],
     [ 242, 242, 242 ],
     [ 243, 243, 243 ],
     [ 244, 244, 244 ],
     [ 245, 245, 245 ],
     [ 246, 246, 246 ],
     [ 247, 247, 247 ],
     [ 248, 248, 248 ],
     [ 249, 249, 249 ],
     [ 250, 250, 250 ],
     [ 251, 251, 251 ],
     [ 252, 252, 252 ],
     [ 253, 253, 253 ],
     [ 254, 254, 254 ],
     [ 255, 255, 255 ] ],
     Float64 )

colormap_map[ 'jet' ] = array(
   [ [ 0.0, 0.0, 0.5625 ],
     [ 0.0, 0.0, 0.625 ],
     [ 0.0, 0.0, 0.6875 ],
     [ 0.0, 0.0, 0.75 ],
     [ 0.0, 0.0, 0.8125 ],
     [ 0.0, 0.0, 0.875 ],
     [ 0.0, 0.0, 0.9375 ],
     [ 0.0, 0.0, 1.0 ],
     [ 0.0, 0.0625, 1.0 ],
     [ 0.0, 0.125, 1.0 ],
     [ 0.0, 0.1875, 1.0 ],
     [ 0.0, 0.25, 1.0 ],
     [ 0.0, 0.3125, 1.0 ],
     [ 0.0, 0.375, 1.0 ],
     [ 0.0, 0.4375, 1.0 ],
     [ 0.0, 0.5, 1.0 ],
     [ 0.0, 0.5625, 1.0 ],
     [ 0.0, 0.625, 1.0 ],
     [ 0.0, 0.6875, 1.0 ],
     [ 0.0, 0.75, 1.0 ],
     [ 0.0, 0.8125, 1.0 ],
     [ 0.0, 0.875, 1.0 ],
     [ 0.0, 0.9375, 1.0 ],
     [ 0.0, 1.0, 1.0 ],
     [ 0.0625, 1.0, 1.0 ],
     [ 0.125, 1.0, 0.9375 ],
     [ 0.1875, 1.0, 0.875 ],
     [ 0.25, 1.0, 0.8125 ],
     [ 0.3125, 1.0, 0.75 ],
     [ 0.375, 1.0, 0.6875 ],
     [ 0.4375, 1.0, 0.625 ],
     [ 0.5, 1.0, 0.5625 ],
     [ 0.5625, 1.0, 0.5 ],
     [ 0.625, 1.0, 0.4375 ],
     [ 0.6875, 1.0, 0.375 ],
     [ 0.75, 1.0, 0.3125 ],
     [ 0.8125, 1.0, 0.25 ],
     [ 0.875, 1.0, 0.1875 ],
     [ 0.9375, 1.0, 0.125 ],
     [ 1.0, 1.0, 0.0625 ],
     [ 1.0, 1.0, 0.0 ],
     [ 1.0, 0.9375, 0.0 ],
     [ 1.0, 0.875, 0.0 ],
     [ 1.0, 0.8125, 0.0 ],
     [ 1.0, 0.75, 0.0 ],
     [ 1.0, 0.6875, 0.0 ],
     [ 1.0, 0.625, 0.0 ],
     [ 1.0, 0.5625, 0.0 ],
     [ 1.0, 0.5, 0.0 ],
     [ 1.0, 0.4375, 0.0 ],
     [ 1.0, 0.375, 0.0 ],
     [ 1.0, 0.3125, 0.0 ],
     [ 1.0, 0.25, 0.0 ],
     [ 1.0, 0.1875, 0.0 ],
     [ 1.0, 0.125, 0.0 ],
     [ 1.0, 0.0625, 0.0 ],
     [ 1.0, 0.0, 0.0 ],
     [ 0.9375, 0.0, 0.0 ],
     [ 0.875, 0.0, 0.0 ],
     [ 0.8125, 0.0, 0.0 ],
     [ 0.75, 0.0, 0.0 ],
     [ 0.6875, 0.0, 0.0 ],
     [ 0.625, 0.0, 0.0 ],
     [ 0.5625, 0.0, 0.0 ] ],
     Float64 )

colormap_map[ 'hsv' ] = array(
   [ [ 1.0, 0.0, 0.0 ],
     [ 1.0, 0.09375, 0.0 ],
     [ 1.0, 0.1875, 0.0 ],
     [ 1.0, 0.28125, 0.0 ],
     [ 1.0, 0.375, 0.0 ],
     [ 1.0, 0.46875, 0.0 ],
     [ 1.0, 0.5625, 0.0 ],
     [ 1.0, 0.65625, 0.0 ],
     [ 1.0, 0.75, 0.0 ],
     [ 1.0, 0.84375, 0.0 ],
     [ 1.0, 0.9375, 0.0 ],
     [ 0.96875, 1.0, 0.0 ],
     [ 0.875, 1.0, 0.0 ],
     [ 0.78125, 1.0, 0.0 ],
     [ 0.6875, 1.0, 0.0 ],
     [ 0.59375, 1.0, 0.0 ],
     [ 0.5, 1.0, 0.0 ],
     [ 0.40625, 1.0, 0.0 ],
     [ 0.3125, 1.0, 0.0 ],
     [ 0.21875, 1.0, 0.0 ],
     [ 0.125, 1.0, 0.0 ],
     [ 0.03125, 1.0, 0.0 ],
     [ 0.0, 1.0, 0.0625 ],
     [ 0.0, 1.0, 0.15625 ],
     [ 0.0, 1.0, 0.25 ],
     [ 0.0, 1.0, 0.34375 ],
     [ 0.0, 1.0, 0.4375 ],
     [ 0.0, 1.0, 0.53125 ],
     [ 0.0, 1.0, 0.625 ],
     [ 0.0, 1.0, 0.71875 ],
     [ 0.0, 1.0, 0.8125 ],
     [ 0.0, 1.0, 0.90625 ],
     [ 0.0, 1.0, 1.0 ],
     [ 0.0, 0.90625, 1.0 ],
     [ 0.0, 0.8125, 1.0 ],
     [ 0.0, 0.71875, 1.0 ],
     [ 0.0, 0.625, 1.0 ],
     [ 0.0, 0.53125, 1.0 ],
     [ 0.0, 0.4375, 1.0 ],
     [ 0.0, 0.34375, 1.0 ],
     [ 0.0, 0.25, 1.0 ],
     [ 0.0, 0.15625, 1.0 ],
     [ 0.0, 0.0625, 1.0 ],
     [ 0.03125, 0.0, 1.0 ],
     [ 0.125, 0.0, 1.0 ],
     [ 0.21875, 0.0, 1.0 ],
     [ 0.3125, 0.0, 1.0 ],
     [ 0.40625, 0.0, 1.0 ],
     [ 0.5, 0.0, 1.0 ],
     [ 0.59375, 0.0, 1.0 ],
     [ 0.6875, 0.0, 1.0 ],
     [ 0.78125, 0.0, 1.0 ],
     [ 0.875, 0.0, 1.0 ],
     [ 0.96875, 0.0, 1.0 ],
     [ 1.0, 0.0, 0.9375 ],
     [ 1.0, 0.0, 0.84375 ],
     [ 1.0, 0.0, 0.75 ],
     [ 1.0, 0.0, 0.65625 ],
     [ 1.0, 0.0, 0.5625 ],
     [ 1.0, 0.0, 0.46875 ],
     [ 1.0, 0.0, 0.375 ],
     [ 1.0, 0.0, 0.28125 ],
     [ 1.0, 0.0, 0.1875 ],
     [ 1.0, 0.0, 0.09375 ] ],
     Float64 )

colormap_map[ 'gray' ] = array(
   [ [ 0, 0, 0 ],
     [ 1, 1, 1 ],
     [ 2, 2, 2 ],
     [ 3, 3, 3 ],
     [ 4, 4, 4 ],
     [ 5, 5, 5 ],
     [ 6, 6, 6 ],
     [ 7, 7, 7 ],
     [ 8, 8, 8 ],
     [ 9, 9, 9 ],
     [ 10, 10, 10 ],
     [ 11, 11, 11 ],
     [ 12, 12, 12 ],
     [ 13, 13, 13 ],
     [ 14, 14, 14 ],
     [ 15, 15, 15 ],
     [ 16, 16, 16 ],
     [ 17, 17, 17 ],
     [ 18, 18, 18 ],
     [ 19, 19, 19 ],
     [ 20, 20, 20 ],
     [ 21, 21, 21 ],
     [ 22, 22, 22 ],
     [ 23, 23, 23 ],
     [ 24, 24, 24 ],
     [ 25, 25, 25 ],
     [ 26, 26, 26 ],
     [ 27, 27, 27 ],
     [ 28, 28, 28 ],
     [ 29, 29, 29 ],
     [ 30, 30, 30 ],
     [ 31, 31, 31 ],
     [ 32, 32, 32 ],
     [ 33, 33, 33 ],
     [ 34, 34, 34 ],
     [ 35, 35, 35 ],
     [ 36, 36, 36 ],
     [ 37, 37, 37 ],
     [ 38, 38, 38 ],
     [ 39, 39, 39 ],
     [ 40, 40, 40 ],
     [ 41, 41, 41 ],
     [ 42, 42, 42 ],
     [ 43, 43, 43 ],
     [ 44, 44, 44 ],
     [ 45, 45, 45 ],
     [ 46, 46, 46 ],
     [ 47, 47, 47 ],
     [ 48, 48, 48 ],
     [ 49, 49, 49 ],
     [ 50, 50, 50 ],
     [ 51, 51, 51 ],
     [ 52, 52, 52 ],
     [ 53, 53, 53 ],
     [ 54, 54, 54 ],
     [ 55, 55, 55 ],
     [ 56, 56, 56 ],
     [ 57, 57, 57 ],
     [ 58, 58, 58 ],
     [ 59, 59, 59 ],
     [ 60, 60, 60 ],
     [ 61, 61, 61 ],
     [ 62, 62, 62 ],
     [ 63, 63, 63 ],
     [ 64, 64, 64 ],
     [ 65, 65, 65 ],
     [ 66, 66, 66 ],
     [ 67, 67, 67 ],
     [ 68, 68, 68 ],
     [ 69, 69, 69 ],
     [ 70, 70, 70 ],
     [ 71, 71, 71 ],
     [ 72, 72, 72 ],
     [ 73, 73, 73 ],
     [ 74, 74, 74 ],
     [ 75, 75, 75 ],
     [ 76, 76, 76 ],
     [ 77, 77, 77 ],
     [ 78, 78, 78 ],
     [ 79, 79, 79 ],
     [ 80, 80, 80 ],
     [ 81, 81, 81 ],
     [ 82, 82, 82 ],
     [ 83, 83, 83 ],
     [ 84, 84, 84 ],
     [ 85, 85, 85 ],
     [ 86, 86, 86 ],
     [ 87, 87, 87 ],
     [ 88, 88, 88 ],
     [ 89, 89, 89 ],
     [ 90, 90, 90 ],
     [ 91, 91, 91 ],
     [ 92, 92, 92 ],
     [ 93, 93, 93 ],
     [ 94, 94, 94 ],
     [ 95, 95, 95 ],
     [ 96, 96, 96 ],
     [ 97, 97, 97 ],
     [ 98, 98, 98 ],
     [ 99, 99, 99 ],
     [ 100, 100, 100 ],
     [ 101, 101, 101 ],
     [ 102, 102, 102 ],
     [ 103, 103, 103 ],
     [ 104, 104, 104 ],
     [ 105, 105, 105 ],
     [ 106, 106, 106 ],
     [ 107, 107, 107 ],
     [ 108, 108, 108 ],
     [ 109, 109, 109 ],
     [ 110, 110, 110 ],
     [ 111, 111, 111 ],
     [ 112, 112, 112 ],
     [ 113, 113, 113 ],
     [ 114, 114, 114 ],
     [ 115, 115, 115 ],
     [ 116, 116, 116 ],
     [ 117, 117, 117 ],
     [ 118, 118, 118 ],
     [ 119, 119, 119 ],
     [ 120, 120, 120 ],
     [ 121, 121, 121 ],
     [ 122, 122, 122 ],
     [ 123, 123, 123 ],
     [ 124, 124, 124 ],
     [ 125, 125, 125 ],
     [ 126, 126, 126 ],
     [ 127, 127, 127 ],
     [ 128, 128, 128 ],
     [ 129, 129, 129 ],
     [ 130, 130, 130 ],
     [ 131, 131, 131 ],
     [ 132, 132, 132 ],
     [ 133, 133, 133 ],
     [ 134, 134, 134 ],
     [ 135, 135, 135 ],
     [ 136, 136, 136 ],
     [ 137, 137, 137 ],
     [ 138, 138, 138 ],
     [ 139, 139, 139 ],
     [ 140, 140, 140 ],
     [ 141, 141, 141 ],
     [ 142, 142, 142 ],
     [ 143, 143, 143 ],
     [ 144, 144, 144 ],
     [ 145, 145, 145 ],
     [ 146, 146, 146 ],
     [ 147, 147, 147 ],
     [ 148, 148, 148 ],
     [ 149, 149, 149 ],
     [ 150, 150, 150 ],
     [ 151, 151, 151 ],
     [ 152, 152, 152 ],
     [ 153, 153, 153 ],
     [ 154, 154, 154 ],
     [ 155, 155, 155 ],
     [ 156, 156, 156 ],
     [ 157, 157, 157 ],
     [ 158, 158, 158 ],
     [ 159, 159, 159 ],
     [ 160, 160, 160 ],
     [ 161, 161, 161 ],
     [ 162, 162, 162 ],
     [ 163, 163, 163 ],
     [ 164, 164, 164 ],
     [ 165, 165, 165 ],
     [ 166, 166, 166 ],
     [ 167, 167, 167 ],
     [ 168, 168, 168 ],
     [ 169, 169, 169 ],
     [ 170, 170, 170 ],
     [ 171, 171, 171 ],
     [ 172, 172, 172 ],
     [ 173, 173, 173 ],
     [ 174, 174, 174 ],
     [ 175, 175, 175 ],
     [ 176, 176, 176 ],
     [ 177, 177, 177 ],
     [ 178, 178, 178 ],
     [ 179, 179, 179 ],
     [ 180, 180, 180 ],
     [ 181, 181, 181 ],
     [ 182, 182, 182 ],
     [ 183, 183, 183 ],
     [ 184, 184, 184 ],
     [ 185, 185, 185 ],
     [ 186, 186, 186 ],
     [ 187, 187, 187 ],
     [ 188, 188, 188 ],
     [ 189, 189, 189 ],
     [ 190, 190, 190 ],
     [ 191, 191, 191 ],
     [ 192, 192, 192 ],
     [ 193, 193, 193 ],
     [ 194, 194, 194 ],
     [ 195, 195, 195 ],
     [ 196, 196, 196 ],
     [ 197, 197, 197 ],
     [ 198, 198, 198 ],
     [ 199, 199, 199 ],
     [ 200, 200, 200 ],
     [ 201, 201, 201 ],
     [ 202, 202, 202 ],
     [ 203, 203, 203 ],
     [ 204, 204, 204 ],
     [ 205, 205, 205 ],
     [ 206, 206, 206 ],
     [ 207, 207, 207 ],
     [ 208, 208, 208 ],
     [ 209, 209, 209 ],
     [ 210, 210, 210 ],
     [ 211, 211, 211 ],
     [ 212, 212, 212 ],
     [ 213, 213, 213 ],
     [ 214, 214, 214 ],
     [ 215, 215, 215 ],
     [ 216, 216, 216 ],
     [ 217, 217, 217 ],
     [ 218, 218, 218 ],
     [ 219, 219, 219 ],
     [ 220, 220, 220 ],
     [ 221, 221, 221 ],
     [ 222, 222, 222 ],
     [ 223, 223, 223 ],
     [ 224, 224, 224 ],
     [ 225, 225, 225 ],
     [ 226, 226, 226 ],
     [ 227, 227, 227 ],
     [ 228, 228, 228 ],
     [ 229, 229, 229 ],
     [ 230, 230, 230 ],
     [ 231, 231, 231 ],
     [ 232, 232, 232 ],
     [ 233, 233, 233 ],
     [ 234, 234, 234 ],
     [ 235, 235, 235 ],
     [ 236, 236, 236 ],
     [ 237, 237, 237 ],
     [ 238, 238, 238 ],
     [ 239, 239, 239 ],
     [ 240, 240, 240 ],
     [ 241, 241, 241 ],
     [ 242, 242, 242 ],
     [ 243, 243, 243 ],
     [ 244, 244, 244 ],
     [ 245, 245, 245 ],
     [ 246, 246, 246 ],
     [ 247, 247, 247 ],
     [ 248, 248, 248 ],
     [ 249, 249, 249 ],
     [ 250, 250, 250 ],
     [ 251, 251, 251 ],
     [ 252, 252, 252 ],
     [ 253, 253, 253 ],
     [ 254, 254, 254 ],
     [ 255, 255, 255 ] ],
     Float64 )

colormap_map[ 'copper' ] = array(
   [ [ 0.0, 0.0, 0.0 ],
     [ 0.01984126984126984, 0.0124, 0.0078968253968253969 ],
     [ 0.03968253968253968, 0.024799999999999999, 0.015793650793650794 ],
     [ 0.059523809523809521, 0.037199999999999997, 0.023690476190476189 ],
     [ 0.079365079365079361, 0.049599999999999998, 0.031587301587301587 ],
     [ 0.099206349206349201, 0.062, 0.039484126984126983 ],
     [ 0.11904761904761904, 0.074399999999999994, 0.047380952380952378 ],
     [ 0.1388888888888889, 0.086800000000000002, 0.055277777777777773 ],
     [ 0.15873015873015872, 0.099199999999999997, 0.063174603174603175 ],
     [ 0.17857142857142855, 0.11159999999999999, 0.071071428571428563 ],
     [ 0.1984126984126984, 0.124, 0.078968253968253965 ],
     [ 0.21825396825396826, 0.13639999999999999, 0.086865079365079353 ],
     [ 0.23809523809523808, 0.14879999999999999, 0.094761904761904756 ],
     [ 0.25793650793650791, 0.16119999999999998, 0.10265873015873016 ],
     [ 0.27777777777777779, 0.1736, 0.11055555555555555 ],
     [ 0.29761904761904762, 0.186, 0.11845238095238095 ],
     [ 0.31746031746031744, 0.19839999999999999, 0.12634920634920635 ],
     [ 0.33730158730158727, 0.21079999999999999, 0.13424603174603172 ],
     [ 0.3571428571428571, 0.22319999999999998, 0.14214285714285713 ],
     [ 0.37698412698412698, 0.23559999999999998, 0.15003968253968253 ],
     [ 0.3968253968253968, 0.248, 0.15793650793650793 ],
     [ 0.41666666666666663, 0.26039999999999996, 0.16583333333333333 ],
     [ 0.43650793650793651, 0.27279999999999999, 0.17373015873015871 ],
     [ 0.45634920634920634, 0.28520000000000001, 0.18162698412698411 ],
     [ 0.47619047619047616, 0.29759999999999998, 0.18952380952380951 ],
     [ 0.49603174603174599, 0.31, 0.19742063492063491 ],
     [ 0.51587301587301582, 0.32239999999999996, 0.20531746031746032 ],
     [ 0.5357142857142857, 0.33479999999999999, 0.21321428571428569 ],
     [ 0.55555555555555558, 0.34720000000000001, 0.22111111111111109 ],
     [ 0.57539682539682535, 0.35959999999999998, 0.22900793650793649 ],
     [ 0.59523809523809523, 0.372, 0.2369047619047619 ],
     [ 0.615079365079365, 0.38439999999999996, 0.2448015873015873 ],
     [ 0.63492063492063489, 0.39679999999999999, 0.2526984126984127 ],
     [ 0.65476190476190477, 0.40920000000000001, 0.2605952380952381 ],
     [ 0.67460317460317454, 0.42159999999999997, 0.26849206349206345 ],
     [ 0.69444444444444442, 0.434, 0.27638888888888891 ],
     [ 0.71428571428571419, 0.44639999999999996, 0.28428571428571425 ],
     [ 0.73412698412698418, 0.45880000000000004, 0.29218253968253971 ],
     [ 0.75396825396825395, 0.47119999999999995, 0.30007936507936506 ],
     [ 0.77380952380952384, 0.48360000000000003, 0.30797619047619046 ],
     [ 0.79365079365079361, 0.496, 0.31587301587301586 ],
     [ 0.81349206349206349, 0.50840000000000007, 0.32376984126984126 ],
     [ 0.83333333333333326, 0.52079999999999993, 0.33166666666666667 ],
     [ 0.85317460317460325, 0.53320000000000001, 0.33956349206349207 ],
     [ 0.87301587301587302, 0.54559999999999997, 0.34746031746031741 ],
     [ 0.8928571428571429, 0.55800000000000005, 0.35535714285714287 ],
     [ 0.91269841269841268, 0.57040000000000002, 0.36325396825396822 ],
     [ 0.93253968253968256, 0.58279999999999998, 0.37115079365079368 ],
     [ 0.95238095238095233, 0.59519999999999995, 0.37904761904761902 ],
     [ 0.97222222222222221, 0.60760000000000003, 0.38694444444444442 ],
     [ 0.99206349206349198, 0.62, 0.39484126984126983 ],
     [ 1.0, 0.63239999999999996, 0.40273809523809523 ],
     [ 1.0, 0.64479999999999993, 0.41063492063492063 ],
     [ 1.0, 0.65720000000000001, 0.41853174603174603 ],
     [ 1.0, 0.66959999999999997, 0.42642857142857138 ],
     [ 1.0, 0.68200000000000005, 0.43432539682539684 ],
     [ 1.0, 0.69440000000000002, 0.44222222222222218 ],
     [ 1.0, 0.70679999999999998, 0.45011904761904764 ],
     [ 1.0, 0.71919999999999995, 0.45801587301587299 ],
     [ 1.0, 0.73160000000000003, 0.46591269841269839 ],
     [ 1.0, 0.74399999999999999, 0.47380952380952379 ],
     [ 1.0, 0.75639999999999996, 0.48170634920634919 ],
     [ 1.0, 0.76879999999999993, 0.4896031746031746 ],
     [ 1.0, 0.78120000000000001, 0.4975 ] ],
     Float64 )
