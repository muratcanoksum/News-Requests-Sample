from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import  time

title = []
score = []
times = []
commit = []
link = []

url = "https://news.ycombinator.com/newest"
driver = webdriver.Chrome()
driver.get(url)

for i in range(5):
    title_r = driver.find_element(By.ID, "hnmain").find_elements(By.CLASS_NAME, "titleline")
    score_r = driver.find_element(By.ID, "hnmain").find_elements(By.CLASS_NAME, "score")
    time_r = driver.find_element(By.ID, "hnmain").find_elements(By.CLASS_NAME, "age")
    subline_r = driver.find_element(By.ID, "hnmain").find_elements(By.CLASS_NAME, "subline")
    for j in range(len(title_r)):
        title.append(title_r[j].text)
        score.append(score_r[j].text)
        times.append(time_r[j].text)
        commit.append(subline_r[j].find_elements(By.TAG_NAME,"a")[-1].text)
        link.append(title_r[j].find_element(By.TAG_NAME,"a").get_attribute("href"))
    driver.find_element(By.CLASS_NAME, "morelink").click()
    time.sleep(1)


df = pd.DataFrame()
df["Başlık"] = title
df["Score"] = score
df["Time"] = times
df["Commit Count"] = commit
df["Link"] = link

df.to_excel("HackerNews.xlsx")



