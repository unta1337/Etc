# %%
# 필요 라이브러리 불러오기.
import cv2
import numpy as np
import matplotlib.pyplot as plt

from PIL import Image
import requests
from io import BytesIO

# %%
# 이미지 읽기.
url = 'https://cdn.pixabay.com/photo/2018/10/01/09/21/pets-3715733_960_720.jpg'
response = requests.get(url)
img = Image.open(BytesIO(response.content))

# %%
# 이미지 출력.
img

# %%
# img의 타입 확인.
type(img)

# %%
# PIL 이미지를 array 형태로 변환.
img_arr = np.asarray(img)

# %%
# img_arr의 타입 확인.
type(img_arr)

# %%
img_arr.shape

# %%
# 색상 값을 저장하기 위해 [[R, G, B], [...], ...]의 형태로 저장됨.
img_arr

# %%
# 배열 형태의 이미지 출력.
plt.imshow(img_arr)
plt.show()

# %%
# img를 복사하여 각 색상별 채널 분리. (파이썬 자체 배열 사용)
img_copy = img_arr.copy()

# 각 색상별 채널 분리.
red_channel = [[[img[0] for _ in range(3)] for img in img_] for img_ in img_copy]
green_channel = [[[img[1] for _ in range(3)] for img in img_] for img_ in img_copy]
blue_channel = [[[img[2] for _ in range(3)] for img in img_] for img_ in img_copy]

# %%
# 분리된 색상별 채널 출력.
plt.imshow(red_channel)
plt.show()

plt.imshow(green_channel)
plt.show()

plt.imshow(blue_channel)
plt.show()

# %%
# 각 색상별 채널 분리. (numpy 사용)
# 참고: [:, :, i] -> 배열은 삼차원 배열이며 일차원 배열의 i번 원소만 취할 것.
red_channel = img_copy[:, :, 0]
green_channel = img_copy[:, :, 1]
blue_channel = img_copy[:, :, 2]

# %%
# 분리된 색상별 채널 출력.
plt.imshow(red_channel, cmap='gray')        # 그래이 스케일 적용.
plt.show()

plt.imshow(green_channel, cmap='gray')
plt.show()

plt.imshow(blue_channel, cmap='gray')
plt.show()

# %%
# 각 채널 성분 추출.
red_channel = img_arr.copy()
red_channel[:, :, 1] = 0
red_channel[:, :, 2] = 0

green_channel = img_arr.copy()
green_channel[:, :, 0] = 0
green_channel[:, :, 2] = 0

blue_channel = img_arr.copy()
blue_channel[:, :, 0] = 0
blue_channel[:, :, 1] = 0

# %%
# 추출한 색상 채널 출력.
plt.imshow(red_channel)
plt.show()

plt.imshow(green_channel)
plt.show()

plt.imshow(blue_channel)
plt.show()

# %%
# OpenCV를 통한 이미지 출력.
# from google.colab.patches import cv2_imshow
# 로컬 환경에선 위의 함수 사용 불가.
# 참고: matplotlib의 색상 (R, G, B)
#       OpcnCV의 색상 (B, G, R)
# cv2.cvtColor() 필요.
# 플래그: COLOR_RGB2BGR 등등.

# %%
# OpenCV 이미지 읽기.
img = cv2.imread('images/lion.jpg', cv2.IMREAD_UNCHANGED)   # OpenCV는 BGR, numpy 형식으로 이미지 로드.
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)                  # cvtColor를 이용해 색상 형식 변환.

plt.imshow(img)
plt.show()

# %%
# 그래이 스케일로 읽기.
img = cv2.imread('images/lion.jpg', cv2.IMREAD_GRAYSCALE)   # OpenCV는 BGR, numpy 형식으로 이미지 로드.
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)                  # cvtColor를 이용해 색상 형식 변환.

plt.imshow(img)
plt.show()

# %%
# 이미지 쓰기.
# 무작위 이미지 생성.
img_rand = np.random.randint(0, 256, size=(200, 200, 3))
print(img_rand.shape)

# 이미지 저장.
cv2.imwrite('images/img_rand.png', img_rand)

img_rand_read = cv2.imread('images/img_rand.png')
img_rand_read = cv2.cvtColor(img_rand_read, cv2.COLOR_BGR2RGB)

print(type(img_rand_read))
print(img_rand_read.shape)

plt.imshow(img_rand_read)
plt.show()

# %%
# 도형 그리기.
# 빈 이미지 생성.
img = np.zeros((512, 512, 3), np.uint8)

plt.imshow(img)
plt.show()

# %%
# 선 그리기.
cv2.line(img, (0, 0), (511, 511), (0, 0, 255), 5)

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img)
plt.show()
img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

# %%
# 사각형 그리기.
img = cv2.rectangle(img, (400, 0), (510, 128), (0, 255, 0), 3)

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img)
plt.show()
img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

# %%
# 원 그리기.
img = cv2.circle(img, (450, 50), 50, (255, 0, 0), -1)
img = cv2.circle(img, (50, 450), 50, (255, 255, 0), 2)

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img)
plt.show()
img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

# %%
# 타원 그리기.
img = cv2.ellipse(img, (256, 256), (150, 30), 0,0, 180, (0, 255, 0), -1)
img = cv2.ellipse(img, (256, 256), (150, 50), 45, 0, 360, (255, 255, 255), 2)
img = cv2.ellipse(img, (256, 256), (150, 10), 135, 0, 270, (0, 255, 255), 2)

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img)
plt.show()
img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

# %%
# 다각형 그리기.
# 다각형을 그리기 위한 점 정의.
polygons = [
    np.array(
        [
            [10, 5],
            [20, 30],
            [70, 20],
            [50, 10]
        ],
        np.int32
    ),
    np.array(
        [
            [150, 5],
            [200, 30],
            [100, 70],
            [50, 20]
        ],
        np.int32
    ),
]
polygons = [polygon.reshape((-1, 2, 1)) for polygon in polygons]    # 출력 가능하도록 행렬 형태 변환.

img = cv2.polylines(img, [polygons[0]], True, (250, 150, 0), 4)
img = cv2.polylines(img, [polygons[1]], True, (255, 200, 255), 4)

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img)
plt.show()
img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

# %%
# 텍스트 그리기.
img = cv2.putText(img, 'OpenCV', (10, 500), cv2.FONT_HERSHEY_SIMPLEX, 4, (255, 255, 255), 3)

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img)
plt.show()
img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

# %%
# 색 공간.
# RGB 또는 BGR
img_orig = cv2.imread('images/dog.jpg')

img = cv2.cvtColor(img_orig, cv2.COLOR_BGR2RGB)
plt.imshow(img)
plt.show()

# %%
# HSV (Hue, Saturation, Value)
# a.k.a. HSB or Hue, Saturation, Brightness

img = cv2.cvtColor(img_orig, cv2.COLOR_BGR2HSV)
plt.imshow(img)
plt.show()

# %%
# HSL (Hue, Saturation, Lightness)

img = cv2.cvtColor(img_orig, cv2.COLOR_BGR2HLS)
plt.imshow(img)
plt.show()

# %%
# YCrCb (Y: Luminance, Cr/Cb: Chrominance Red/Blue)

img = cv2.cvtColor(img_orig, cv2.COLOR_BGR2YCrCb)
plt.imshow(img)
plt.show()

# %%
# Gray Scale

img = cv2.cvtColor(img_orig, cv2.COLOR_BGR2GRAY)
plt.imshow(img, cmap='gray')
plt.show()
