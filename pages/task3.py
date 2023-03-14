def convert(img_, rows, cols):
  img_ = cv2.imread("OIP.jpg")
  img_ = cv2.cvtColor(img_, cv2.COLOR_BGR2RGB)
  rows, cols, dims = img_.shape
  return img_

def translation(img_, rows, cols):

    img_translated = np.float32([[1, 0, 50], 
                                [0, 1, 50],
                                [0, 0, 1]])
    img_translated =  cv2.warpPerspective(img_, img_translated, (cols, rows))

    return img_translated
    
    
def rotation(img_, rows, cols):
    angle = np.radians(10)
    m_rotated = np.float32([[np.cos(angle), -(np.sin(angle)), 0],
                            [np.sin(angle), np.cos(angle), 0],
                            [0, 0, 1]])

    rotated_img = cv2.warpPerspective(img_, m_rotated, (int(cols), int(rows)))
    return rotated_img

def scaling(img_, rows, cols):
    m_scaling = np.float32([[1.5, 0, 0],
                            [0, 1.8, 0],
                            [0, 0, 1]])
    scaled_img = cv2.warpPerspective(img_, m_scaling, (cols*2, rows*2))
    return scaled_img

def reflection(img_, rows, cols):
    m_reflection = np.float32([[1, 0, 0],
                               [0, -1, rows],
                               [0, 0, 1]])
    reflected_img = cv2.warpPerspective(img_, m_reflection, (int(cols), int(rows)))
    return reflected_img
    img_flipped = reflection(img_, rows, cols)
    plt.axis("off")
    plt.imshow(img_flipped) 
      
def shear(img_, rows, cols):
    m_shearing = np.float32([[1, 0.5, 0],
                            [0, 1, 0],
                            [0, 0, 1]])
    sheared_img = cv2.warpPerspective(img_, m_shearing, (int(cols*1.5),int(rows*1.5)))
    return sheared_img      
      
def user_choices(user_choice, img):

    if user_choice == 1:
        convert(img_, rows, cols)
        manipulated_img = translation(img, rows, cols)

    elif user_choice == 2:
        convert(img_, rows, cols)
        manipulated_img  = rotation(img, rows, cols)

    elif user_choice == 3:
        convert(img_, rows, cols)
        manipulated_img  = scaling(img, rows, cols)

    elif user_choice == 4:
        convert(img_, rows, cols)
        manipulated_img  = reflection(img, rows, cols)

    elif user_choice == 5:
        convert(img_, rows, cols)
        manipulated_img  = shear(img, rows, cols)
    
    return manipulated_img 


    
          
  
