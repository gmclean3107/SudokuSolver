from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from classes.solve import solve


def launchBrowser():
    chrome_options = Options()
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--start-maximized")

    driver = webdriver.Chrome(executable_path=r'./chromedriver.exe', options=chrome_options)
    driver.get('https://sudoku.com/easy/')
    return driver


##Get a screen shot of the board, solve locally, then input the values
def main():
    driver = launchBrowser()
    t=True

    board = driver.find_element(By.CSS_SELECTOR, "div.game")
    board.click()
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
    ss = board.screenshot("BoardImage.png")
    while t:
        solve(board)
        x=input("Enter Y:")
        if x=="Y":
            t=False
    driver.quit()


if __name__ == "__main__":
    main()
