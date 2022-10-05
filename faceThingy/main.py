# %%
import dlib, cv2
import numpy as np
from matplotlib import pyplot as plt, patches, patheffects

face_detector = dlib.get_frontal_face_detector()
shape_predictor = dlib.shape_predictor('models/shape_predictor_68_face_landmarks.dat')
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
    # Compute saved face descriptions
    for name, image_path in image_paths.items():
        image = cv2.cvtColor(cv2.imread(image_path), cv2.COLOR_BGR2RGB)

        _, image_shapes, _ = find_faces(image)
        descriptors[name] = encode_faces(image, image_shapes)[0]

    np.save('images/descriptors.npy', descriptors)

    print(descriptors)

    # Compte input.
    image = cv2.cvtColor(cv2.imread('images/matrix1.jpg'), cv2.COLOR_BGR2RGB)

    rects, shapes, _ = find_faces(image)
    target_descriptors = encode_faces(image, shapes)

    # Visualize output.
    _, axes = plt.subplots(1, figsize=(20, 20))
    axes.imshow(image)

    for i, descriptor in enumerate(target_descriptors):
        found = False

        for name, saved_descriptor in descriptors.items():
            distance = np.linalg.norm([descriptor] - saved_descriptor, axis=1)

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
def encode_faces(image, shapes):
    return np.array([
        face_recognizer.compute_face_descriptor(image, shape) for shape in shapes
    ])

# %%
if __name__ == '__main__':
    main()
