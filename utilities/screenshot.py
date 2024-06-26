from utilities.common_functions import get_parent_framework_path
class CaptureScreenshot:
    @staticmethod
    def capture_screenshot(driver):
        return driver.save_screenshot(get_parent_framework_path()/'screenshots'/'screenshot.png')
