from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException

desired_caps = {}

desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '11.0'
desired_caps['deviceName'] = 'Pixel_4a_API_30'
desired_caps['automationName'] = 'UIAutomator2'
desired_caps['app'] = 'C:\\Users\\IDN MEDIA\\Downloads\\FOLDERKU\\org.tasks_130302.apk'

driver =webdriver.Remote('http://localhost:4723/wd/hub/', desired_caps)

class Createtasks:
    def addtasks(self):
        try: 
            self.driver.find_element_by_id("org.tasks:id/fab").click()
            self.driver.find_element_by_id("org.tasks:id/title").click()
            self.driver.find_element_by_id("org.tasks:id/title").send_keys("Create Reminder Mawar")
            self.driver.findElementByXPath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout[2]/android.widget.ScrollView/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.ViewGroup[1]/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.widget.TextView").click()
            self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="15 July 2023").click()
            self.driver.find_element_by_id("org.tasks:id/ok_button").click()
            self.driver.findElementByXPath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout[2]/android.widget.ScrollView/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[1]/android.widget.TextView").click()
            self.driver.findElementByAccessibilityId("15 July 2023").click
            self.driver.find_element_by_id("org.tasks:id/ok_button").click()
            self.driver.findElementByXPath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout[2]/android.widget.ScrollView/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.ViewGroup[2]/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.widget.TextView").click()
            self.driver.findElementByXPath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout[2]/android.widget.ScrollView/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.ViewGroup[3]/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.widget.TextView").click()
            self.driver.find_element_by_id("org.tasks:id/current_location").click()
            self.driver.find_element_by_id("com.android.permissioncontroller:id/permission_allow_foreground_only_button").click()
            self.driver.find_element_by_id("org.tasks:id/google_marker").click()
            self.driver.find_element_by_id("org.tasks:id/current_location").click()
            self.driver.findElementByXPath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout/androidx.cardview.widget.CardView/android.widget.TextView").click()
            self.driver.findElementByAccessibilityId("Collapse").click()
            self.driver.findElementByXPath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout[2]/android.widget.ScrollView/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.ViewGroup[4]/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View").click()

            print("Passed, Success AddTasks")
        except NoSuchElementException as e:
            print("Error, Failed AddTasks", e)



class Edittasks:
    def editinformationtasks(self):
        try: 
            self.driver.findElementByXPath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.TextView[1]").click()
            self.driver.find_element_by_id("org.tasks:id/title").sendKeys("add Remin mawar edit 1")
            self.driver.find_element_by_id("org.tasks:id/fab").click()

            print("Passed, Success edit information tasks")
        except NoSuchElementException as b:
            print("Error, Failed edit information tasks", b)


class Deletetasks:
    def deletetasks(self):
        try: 
            self.driver.findElementByXPath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.TextView[1]").click()
            self.driver.findElementByAccessibilityId("Delete task").click()
            self.driver.find_element_by_id("android:id/button1").click()

            print("Passed, Success delete tasks")
        except NoSuchElementException as i:
            print("Error, Failed delete tasks", i)
            
        self.driver.close_app()
        self.driver.quit()