from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from classes.solve import solve
from cv2 import cv2


def launchBrowser():
    chrome_options = Options()
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--start-maximized")

    driver = webdriver.Chrome(executable_path=r'./chromedriver.exe', options=chrome_options)
    driver.get('https://sudoku.com/easy/')
    return driver


##Get a screen shot of the board, solve locally, then input the values
def main():
    #
    #
    # driver = launchBrowser()
    # t=True
    #
    # board = driver.find_element(By.CSS_SELECTOR, "div.game")
    # board.click()
    #Test for the solving algorithm
    grid = [[0, 7, 0, 0, 0, 4, 0, 0, 0],
            [3, 0, 0, 7, 0, 0, 0, 9, 5],
            [0, 0, 0, 0, 0, 0, 0, 0, 2],
            [0, 0, 0, 9, 0, 0, 2, 0, 0],
            [1, 0, 0, 0, 0, 0, 4, 0, 0],
            [0, 0, 5, 0, 0, 6, 0, 1, 9],
            [0, 0, 6, 0, 8, 0, 0, 0, 0],
            [5, 0, 0, 4, 0, 0, 0, 3, 7],
            [0, 0, 0, 0, 0, 0, 1, 0, 0]]
    print(solve(grid))
    # ss = board.screenshot("BoardImage.png")
    img = cv2.imread("BoardImage.png")
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    (thresh, blackAndWhiteImg) = cv2.threshold(imgGray, 127, 255, cv2.THRESH_BINARY)

    imH = blackAndWhiteImg.shape[0]
    imW = blackAndWhiteImg.shape[1]

    y1 = 0
    M = imH//9
    N = imW//9

    for y in range(0, imH, M):
        for x in range(0, imW, N):
            y1 = y + M
            x1 = x + N
            squares = blackAndWhiteImg[y:y+M,x:x+N]
            cv2.rectangle(blackAndWhiteImg, (x,y), (x1,y1), (255, 255, 255))
            cv2.imwrite(str(y) + str(x)+".png", squares)

    cv2.imshow("Output", blackAndWhiteImg)
    cv2.waitKey(0)
    # while t:
    #     solve(board)
    #     x=input("Enter Y:")
    #     if x=="Y":
    #         t=False
    # driver.quit()


if __name__ == "__main__":
    main()
