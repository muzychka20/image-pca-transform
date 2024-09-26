from PIL import Image
import numpy as np
import sys

def get_rgb_arrays(image):
    width, height = image.size
    r_arr = []
    g_arr = []
    b_arr = []
    for j in range(height):
        for i in range(width):
            r, g, b = image.getpixel((i, j))
            r_arr.append(r)
            g_arr.append(g)
            b_arr.append(b)
    return np.array(r_arr), np.array(g_arr), np.array(b_arr)


def restore_image(image, Xnew, v, m):    
    width, height = image.size
    pixel_map = image.load()    
    index_fin = 0
    for y in range(height):
        for x in range(width):            
            Xrestored = np.dot(Xnew[index_fin], v) + m
            pixel_map[x, y] = (int(Xrestored[0]), int(Xrestored[1]), int(Xrestored[2]))
            index_fin += 1
    return image


def main():
    image_name = sys.argv[1]
    output_image_name = sys.argv[2]
    
    image = Image.open(image_name, 'r').convert('RGB')
    r_arr, g_arr, b_arr = get_rgb_arrays(image)
    
    X = np.vstack((r_arr, g_arr, b_arr))  # Объединяем в одну матрицу
    print("X:\n", X)

    Xcentered = X - X.mean(axis=1, keepdims=True)  # Центрируем данные
    print("\nXcentered:\n", Xcentered)
    
    m = X.mean(axis=1)  # Средние значения по каналам
    print("\nMean vector:\n", m)

    covmat = np.cov(Xcentered)
    print("\nCovariance matrix:", covmat, end="\n")
          
    # Вычисляем собственные значения и собственные векторы
    eigvals, eigvecs = np.linalg.eig(covmat)
    print("\nEigenvectors (e1, e2, e3):\n", eigvecs)
    print("\nEigenvalues (lamda1, lamda2, lambda3):\n", eigvals)

    # Берем вектор (один из собственныч векторов)
    v = eigvecs[:, 0]    # Первый вектор
    # v = eigvecs[:, 1]  # Второй вектор
    # v = eigvecs[:, 2]  # Третий вектор
    
    # Матричное умножение транспонированной матрицы v на матрицу центрированных данных Xcentered
    Xnew = np.dot(v.T, Xcentered)

    # Восстанавливаем изображение
    restored_image = restore_image(image, Xnew, v, m)

    # Сохраняем
    restored_image.save(output_image_name, format='png')


if "__main__" == __name__:
    main()
