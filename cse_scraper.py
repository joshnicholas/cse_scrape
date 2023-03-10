import pandas as pd 
from selenium import webdriver 
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
import datetime 
import pytz

utc_now = pytz.utc.localize(datetime.datetime.utcnow())
today = utc_now.astimezone(pytz.timezone("Asia/Colombo"))


today_stem = today.strftime('%Y%m%d')
today = today.strftime('%Y-%m-%d')


chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Firefox(options=chrome_options)
driver.implicitly_wait(10)


urlo = 'https://www.cse.lk/pages/trade-summary/trade-summary.component.html'

#%%
driver.get(urlo)


# print(driver.page_source)

# final_select = Select(driver.find_element_by_name('DataTables_Table_0_length'))
final_select = Select(driver.find_element("name", 'DataTables_Table_0_length'))
final_select.select_by_visible_text('All')

WebDriverWait(driver, 3)

df = pd.read_html(driver.page_source)[0]

df['Date'] = today

driver.close()

with open(f'daily_dumps/{today_stem}.csv', 'w') as f:
    df.to_csv(f, index=False, header=True) 

# print(df.shape)

old = pd.read_csv('cse.csv')

# print(old.shape)

new = old.append(df)
new = new.drop_duplicates(subset=['Symbol', 'Date'])

print(new)

with open("cse.csv", "w") as f:
    new.to_csv(f, header=True, index=False)

# with open("cse.json", "w") as f:
#     new.to_json(f)

