from matplotlib.pyplot import title
from selenium import webdriver

url = 'https://www.youtube.com/c/JohnWatsonRooney/videos?view=0&sort=p&flow=grid'

driver = webdriver.Chrome()
driver.get(url)

#style-scope ytd-grid-video-renderer

#//*[@id="video-title"] Video title
#//*[@id="metadata-container"] views
#//*[@id="metadata-line"]/span[1] views
#//*[@id="metadata-line"]/span[2] time

videos = driver.find_element_by_class_name('style-scope ytd-grid-video-renderer')

print(videos)

for video in videos:
    title = video.find_element_by_xpath('.//*[@id="video-title"]').text
    views = video.find_element_by_xpath('.//*[@id="metadata-line"]/span[1]').text
    when = video.find_element_by_xpath('.//*[@id="metadata-line"]/span[2]').text
    print(title,views,when)