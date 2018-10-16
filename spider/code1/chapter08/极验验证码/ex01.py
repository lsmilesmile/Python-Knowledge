import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image
from io import BytesIO


# 登录账号和密码
EMAIL = '1126476321@qq.com'
PASSWORD = 'Lsmile8705210'


class GrackGeetest(object):
    # 初始化
    def __init__(self):
        self.url = 'https://account.geetest.com/login'
        self.browser = webdriver.Chrome()
        self.wait = WebDriverWait(self.browser, 20)
        self.email = EMAIL
        self.password = PASSWORD

    # 模拟点击
    def get_geetest_button(self):
        """
        获得初始验证按钮
        """
        button = self.wait.until(EC.element_to_be_clickable(
            (By.CLASS_NAME, 'geetest_ring')))
        return button

    # 识别缺口
    def get_screenshot(self):
        """
        获取网页截图
        """
        screenshot = self.browser.get_screenshot_as_png()
        screenshot = Image.open(BytesIO(screenshot))  # 读取二进制文件
        return screenshot

    def get_position(self):
        """
        获取验证码位置
        """
        # 等待验证码的图片加载出来
        img = self.wait.until(EC.presence_of_element_located(
            (By.CLASS_NAME, 'geetest_canvas_img')))
        time.sleep(2)
        # 获取验证码图片位置
        location = img.location
        # 大小
        size = img.size
        top, buttom, left, right = location['y'], location['y'] + \
            size['height'], location['x'], location['x'] + size['width']
        # 返回验证码图片的上下左右的坐标
        return (top, buttom, left, right)  

    def get_geetest_image(self, name='captcha.png'):
        """
        获取验证码图片
        """
        top, buttom, left, right = self.get_position()
        print('验证码位置：', top, buttom, left, right)
        # 整个浏览器页面截图
        sceenshot = self.get_screenshot()
        # 把获得的验证码图片的位置那块剪裁下来就得到验证码图片
        captcha = screenshot.crop((left, top, right, buttom))
        return captcha

    # 以上先将整个网页截图，然后等待验证码图片加载出来，获取该图片的位置，返回其上下左右的坐标，然后将该图片剪裁下来

    # 获取有缺口的图片 - 点击滑块
    def get_silder(self):
        """
        获取滑块
        """
        slider = self.wait.until(EC.element_to_be_clickable(
            (By.CLASS_NAME, 'geetest_slider_button')))
        return slider

    # 对比图片获取缺口
    def is_pixel_equal(self, image1, image2, x, y):
        """
        判断两个像素是否相同
        """
        pixel1 = image1.load()[x, y]
        pixel2 = image2.load()[x, y]
        threshold = 60
        if abs(pixel1[0] - pixel2[0]) < threshold and abs(pixel1[1] - pixel2[1]) < threshold and abs(
                pixel1[2] - pixel2[2]) < thredhold:
            return True
        else:
            return False

    def get_gap(self, image1, image2):
        """
        image1: 不带缺口的图片；
        image2: 带缺口的图片
        """
        left = 60
        for i in range(left, image1.size[0]):
            for j in range(image1.size[1]):
                if not self.is_pixel_equal(image1, image2, i, j):
                    left = i
                    return left
        return left

    # 模拟拖动
    def get_track(self, distance):
        """
        根据偏移量获取移动轨迹
        distance: 偏移量 - 移动的总距离
        """
        # 移动轨迹 - 放每次移动多少距离，一次是0.2秒运动的距离
        track = []
        # 当前位置
        current = 0
        # 减速阈值 - 加速到什么地步开始 减速
        mid = distance * 4 / 5
        # 计算间隔
        t = 0.2
        # 初速度
        v = 0

        while current < distance:
            if current < mid:
                # 加速度为正2
                a = 2
            else:
                a = -3
            # 初速度v0
            v0 = v
            # 当前速度v = v0 + at
            v = v0 + a * t
            # 移动距离x = v0t + 1/2 * a * t^2
            move = v0 * t + 1 / 2 * a * t * t
            # 当前位移
            current += move
            # 加入轨迹
            track.append(round(move))
        return track

    # 按照移动轨迹拖动滑块
    def move_to_gap(self, slider, tracks):
        """
        slider: 滑块
        tracks: 轨迹
        """
        # click() - 点击
        #click_and_hold() - 按住不动
        ActionChains(self.browser).click_and_hold(slider).perform()
        for x in tracks:
            ActionChains(self.browser).move_by_offset(
                xoffset=x, yoffset=0).perform()  # 移动每一小段轨迹
            time.sleep(0.5)
            ActionChains(self.browser).release().perform()  # 松开
