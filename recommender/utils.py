import cv2
import numpy as np
from matplotlib import pyplot as plt


## 引数として渡された画像を正方形にして返す##
# 引数として渡されるcloth_imagesは前処理をしており、服以外の部分は透明である必要がある,引数=画像データ(.pngなど)
# 引数imagesizeはデフォルトは500,引数=正方形として返す画像の1辺のサイズ
def make_square_of_clothes(cloth_images,image_size = 500,file_name="cloth_square_img.png"):
  # imgに画像をそのままnparray配列として格納
  img = cv2.imread(cloth_images,-1)
  # imgをimage_sizeを1辺とする正方形へリサイズしたものをimg_sqaureに格納
  # img_squareはnparray配列
  img_sqaure = cv2.resize(img,(image_size,image_size))
  # img_array_alineは透明部分を含まない画像の1行ごとの配列
  img_array_aline = np.empty(0)
  # cloth_squareは透明部分を含まない長方形
  cloth_array_rec = np.empty(0)
  #縦
  for i in range(image_size):
    # img_array_opacityは透明部分を含む画像の1行ごとの配列
    img_array_opacity = np.empty(0)
    count = 0
    #横
    for j in range(image_size):
      # アルファチャネルが0でない部分(不透明部分)について
      if(img_sqaure[i][j][img_sqaure.shape[2]] != 0):
        img_array_opacity = np.append(img_array_opacity,img_sqaure[i][j], axis = 0)
        count += 1
    #不透明部分がある場合わけ
    if(count > 0 and cloth_array_rec.size == 0):
      #appendによる平坦化を治して3次元配列に
      img_array_opacity = img_array_opacity.reshape([1,count,4])
      #最近傍を補間しながらリサイズ
      img_array_aline = cv2.resize(img_array_opacity,(image_size,1))
      #長方形にまだ何もなければそのまま代入
      cloth_array_rec = img_array_aline
    elif(count > 0 and cloth_array_rec.size > 0):
      #appendによる平坦化を治して3次元配列に
      img_array_opacity = img_array_opacity.reshape([1,count,4])
      #最近傍を補間しながらリサイズ
      img_array_aline = cv2.resize(img_array_opacity,(image_size,1))
      #配列を結合することで長方形を伸ばしていく
      cloth_array_rec = np.concatenate((cloth_array_rec,img_array_aline),axis=0)
  # cloth_sqaure_imgに長方形を正方形へとリサイズしたものを代入
  cloth_sqaure_img = cv2.resize(cloth_array_rec,(image_size,image_size))
  #filenameで画像を保存、アルファチャンネルを削除するために画像を保存している(改良の余地あり)
  cv2.imwrite(file_name,cloth_square_img)
  #アルファチャンネルを削除
  cloth_square_img = cv2.imread(file_name,cv2.IMREAD_COLOR)
  # 画像を保存
  # if(save_flag):
  cv2.imwrite("cloth_square_image.png",cloth_square_img)
  

