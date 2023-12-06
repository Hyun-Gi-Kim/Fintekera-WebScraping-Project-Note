import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
import logging 

class GlassdoorScrape:
    def __init__(self, keyword = 'United States', page_count = 40):
        self.keyword = keyword  ##str
        #Keyword for location
        self.pages = page_count  ##int
        #Number of pages to extract
        self.jobs = []
        self.salary = []
    
    def run_scraper(self):
        import selenium
        from selenium import webdriver
        from selenium.webdriver.common.keys import Keys
        import time
        from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, ElementNotInteractableException
        import pandas as pd
        
        options = webdriver.ChromeOptions()
        options.add_argument("window-size=1920,1080")
        driver = webdriver.Chrome(options = options)
        driver.get("https://www.glassdoor.co.in/Job/Home/recentActivity.htm")
        search_input = driver.find_element(by = 'id', value = "searchBar-location")
        search_input.send_keys(self.keyword)
        search_input.send_keys(Keys.ENTER)

        try:
            driver.find_element(by = 'xpath', value = ".//button[@class='e1jbctw80 ei0fd8p1 css-1n14mz9 e1q8sty40']").click()
            time.sleep(1)
        except NoSuchElementException:
            time.sleep(1)
            pass
        
        for _ in range(self.pages):
            try:
                driver.find_element(by = 'xpath', value = ".//button[@class='e1jbctw80 ei0fd8p1 css-1n14mz9 e1q8sty40']").click()
                time.sleep(1)
            except NoSuchElementException:
                time.sleep(1)
                pass
            try:
                driver.find_element("xpath","//div[@class = 'JobsList_buttonWrapper__haBp5']/button[@class='button_Button__meEg5 button-base_Button__9SPjH']").click()
                time.sleep(1)
            except NoSuchElementException:
                time.sleep(1)
                pass
            try:
                driver.find_element(by = 'xpath', value = ".//button[@class='CloseButton']").click()
                time.sleep(1)
            except NoSuchElementException:
                time.sleep(1)
                pass
        
    
        
            jobs = driver.find_elements(by = 'xpath', value = "//li[@data-test='jobListing']")
            for card in jobs:
                try:
                    driver.find_element(by = 'xpath', value = ".//button[@class='CloseButton']").click()
                    time.sleep(1)
                except NoSuchElementException:
                    time.sleep(1)
                    pass
                card.click()
                time.sleep(1)

                #Closes the signup prompt
                try:
                    driver.find_element(by = 'xpath', value = ".//button[@class='e1jbctw80 ei0fd8p1 css-1n14mz9 e1q8sty40']").click()
                    time.sleep(1)
                except NoSuchElementException:
                    time.sleep(1)
                    pass
                
                #Expands the Description section by clicking on Show More
                try:
                    driver.find_element('xpath',"//button[@class='JobDetails_showMore__j5Z_h']").click()
                    time.sleep(1)
                except NoSuchElementException:
                    card.click()
                
                #Scrape

                try:
                    self.jobs.append(driver.find_element("xpath","//div[@class='JobDetails_jobTitle__Rw_gn']").text)
                except:
                    self.jobs.append("#N/A")
                    pass

                try:
                    self.salary.append(card.find_element("css selector","[data-test='detailSalary']").text)
                    self.salary = [item.split("(")[0].strip() for item in self.salary]
                except:
                    self.salary.append("#N/A")
                    pass
        self.save_to_csv_and_excel()

    def save_to_csv_and_excel(self):
        current_date_str = pd.to_datetime('today').strftime("%Y-%m-%d_%H-%M-%S") 
        csv_filename = f'all_jobs_Glassdoor_{current_date_str}.csv'
        excel_filename = f'all_jobs_Glassdoor_{current_date_str}.xlsx'

        df = pd.DataFrame({
            'Job Title': self.jobs,
            'Salary': self.salary
            # Add more columns as needed
        })
        df['Salary'] = df['Salary'].astype('str')
        df['Salary'] = df['Salary'].str.split('(').str[0]
        df['Salary'] = df['Salary'].apply(lambda x: x.replace("$", ""))
        def determine_salary_type(row):
            if 'Per hour' in row['Salary']:
                return 'Hourly'
            else:
                return 'Annually'
        df['Salary_Type'] = df.apply(determine_salary_type, axis=1)
        df['Location'] = location
        df['Website'] = 'Glassdoor'
        current_date = datetime.now().date()
        df['Scrape Date'] = current_date
        df = df[df['Salary'] != '#N/A']

        # Save to CSV
        df.to_csv(csv_filename, index=False)

        # Save to Excel
        df.to_excel(excel_filename, index=False)

