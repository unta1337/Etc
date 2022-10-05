# %%
import dlib, cv2
import numpy as np
from matplotlib import pyplot as plt, patches, patheffects

# 얼굴 감지 객체. (어떤 얼굴인지 상관없이 얼굴의 형태를 감지)
face_detector = dlib.get_frontal_face_detector()

# 랜드마크 인식 객체. (모션 트레킹과 비슷하게 얼굴을 점으로써 표현)
shape_predictor = dlib.shape_predictor('models/shape_predictor_68_face_landmarks.dat')

# 얼굴 인식 객체. (얼굴을 감지하고 해당 얼굴이 어떤 얼굴인지 인식)
face_recognizer = dlib.face_recognition_model_v1('models/dlib_face_recognition_resnet_model_v1.dat')

image_paths = {
    'neo': 'images/neo.jpg',
    'trinity': 'images/trinity.jpg',
    'morpheus': 'images/morpheus.jpg',
    'smith': 'images/smith.jpg'
}

descriptors = {
    'neo': None,
    'trinity': None,
    'morpheus': None,
    'smith': None
}

# %%
def main():
    # Compute saved face descriptors.
    # 사전 입력에 대한 처리.
    #   사전 입력에 주어진 얼굴에 대한 학습 수행. (추후 입력에 대한 얼굴 인식에 사용됨)
    for name, image_path in image_paths.items():
        image = cv2.cvtColor(cv2.imread(image_path), cv2.COLOR_BGR2RGB)

        _, image_shapes, _ = find_faces(image)
        descriptors[name] = encode_faces(image, image_shapes)[0]

    np.save('images/descriptors.npy', descriptors)

    print(descriptors)

    # Compte input.
    # 입력에 대해 얼굴 인식 수행.
    image = cv2.cvtColor(cv2.imread('images/matrix1.jpg'), cv2.COLOR_BGR2RGB)

    rects, shapes, _ = find_faces(image)                # 얼굴의 형태를 감지한 후 이를 얼굴의 범위(직사각형)과 랜드마크(shape)로 변환.
    target_descriptors = encode_faces(image, shapes)    # 위에서 감지한 형태를 인공신경망이 처리할 수 있는 형태로 변환.

    # Visualize output.
    # 얼굴 인식을 수행하여 이를 시각적으로 출력.
    _, axes = plt.subplots(1, figsize=(20, 20))
    axes.imshow(image)

    # 감지된 얼굴에 대해 사전 학습된 얼굴들과 대조.
    for i, descriptor in enumerate(target_descriptors):
        found = False

        for name, saved_descriptor in descriptors.items():
            distance = np.linalg.norm([descriptor] - saved_descriptor, axis=1)

            # 감지된 얼굴이 사전 학습된 얼굴과 동일 또는 유사하다고 판단되면 해당 상황에 맞는 시각적 효과 출력.
            if distance < 0.6:
                found = True

                # text thingys
                text = axes.text(
                    rects[i][0][0],
                    rects[i][0][1],
                    name,
                    color='b',
                    fontsize=40,
                    fontweight='bold'
                )
                text.set_path_effects([
                    patheffects.Stroke(linewidth=10, foreground='white'),
                    patheffects.Normal()
                ])
                axes.add_patch(
                    patches.Rectangle(
                        rects[i][0],
                        rects[i][1][1] - rects[i][0][1],
                        rects[i][1][0] - rects[i][0][0],
                        linewidth=2,
                        edgecolor='w',
                        facecolor='none'
                    )
                )

                break

        # 감지된 얼굴이 사전 학습된 얼굴과 일치하기 않다고 판단되면 해당 상황에 맞는 시각적 효과 출력.
        if not found:
            axes.text(
                rects[i][0][0],
                rects[i][0][1],
                'unknown',
                color='r',
                fontsize=20,
                fontweight='bold'
            )
            axes.add_patch(
                patches.Rectangle(
                    rects[i][0],
                    rects[i][1][1] - rects[i][0][1],
                    rects[i][1][0] - rects[i][0][0],
                    linewidth=2,
                    edgecolor='r',
                    facecolor='none'
                )
            )

    plt.axis('off')
    plt.savefig('results/output.png')
    plt.show()

# %%
# 얼굴을 감지하여 이미지에 얼굴에 해당하는 영역과 얼굴에 대한 랜드마크 반환.
def find_faces(image):
    detected = face_detector(image, 1)

    if not detected:
        return np.empty(0), np.empty(0), np.empty(0)

    rects, shapes = [], []
    shapes_np = np.zeros((len(detected), 68, 2), dtype=np.int64)

    for i, d in enumerate(detected):
        rects.append(((d.left(), d.top()), (d.right(), d.bottom())))
        shape = shape_predictor(image, d)

        for j in range(68):
            shapes_np[i][j] = (shape.part(j).x, shape.part(j).y)

        shapes.append(shape)

    return rects, shapes, shapes_np

# %%
# 얼굴에 대한 랜드마크를 인공지능이 처리할 수 있는 형태로 변환.
def encode_faces(image, shapes):
    return np.array([
        face_recognizer.compute_face_descriptor(image, shape) for shape in shapes
    ])

# %%
if __name__ == '__main__':
    main()
