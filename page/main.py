import allure

from page.base_page import BasePage
from page.customer import Customer
from page.houselist import HouseList
from page.login import Login
from page.message import Message
from page.my import My
from page.newsdynamic import NewsDynamic
from page.search import Search


class Main(BasePage):
    """
    首页，各点击入口
    """
    def goto_adv(self):
        """
        点击横幅广告
        :return:
        """
        with allure.step("点击横幅广告"):
            self.steps("../page/main.yaml")
        self.tsleep(2)
        return self

    def goto_all_house(self):
        """
        点击“全部”类型
        :return:HouseList
        """
        with allure.step("点击全部"):
            self.steps("../page/main.yaml")
        return HouseList(self._driver)

    def goto_zz_house(self):
        """
        点击“住宅”类型
        :return:HouseList
        """
        with allure.step("点击住宅"):
            self.steps("../page/main.yaml")
        return HouseList(self._driver)

    def goto_sy_house(self):
        """
        点击“商业”类型
        :return:HouseList
        """
        with allure.step("点击商业"):
            self.steps("../page/main.yaml")
        return HouseList(self._driver)

    def goto_gy_house(self):
        """
        点击“公寓”类型
        :return:HouseList
        """
        with allure.step("点击公寓"):
            self.steps("../page/main.yaml")
        return HouseList(self._driver)

    def goto_fav_setting(self):
        """
        点击智能推荐右侧的设置
        :return: self
        """
        with allure.step("点击智能推荐右侧的设置"):
            self.steps("../page/main.yaml")
        return self

    def goto_recommend_first_house(self):
        """
        点击智能推荐第一个房源
        :return: HouseList(self._driver)
        """
        with allure.step("点击智能推荐第一个房源"):
            self.steps("../page/main.yaml")
        self.tsleep(1)
        return HouseList(self._driver)

    def goto_news_dynamic(self):
        """
        点击“项目资讯”
        :return:
        """
        with allure.step("点击“项目资讯”"):
            self.steps("../page/main.yaml")
        return NewsDynamic(self._driver)

    def goto_search(self):
        """
        点击搜索
        :return:Search
        """
        with allure.step("点击搜索框"):
            self.steps("../page/main.yaml")
        return Search(self._driver)

    def swipe_to_list(self):
        """
        将精选推荐滑动出来，原因：部分手机屏幕小，首屏会展示不出来
        :return:self
        """
        with allure.step("将精选推荐滑动出来"):
            self.steps("../page/main.yaml")
        return self

    def click_tab_new(self):
        """
        点击最新上架
        :return:self
        """
        with allure.step("点击最新上架"):
            self.steps("../page/main.yaml")
        self.tsleep(1)
        return self

    def click_tab_hot(self):
        """
        点击热门报备
        :return:self
        """
        with allure.step("点击热门报备"):
            self.steps("../page/main.yaml")
        self.tsleep(1)
        return self

    def click_tab_all(self):
        """
        点击综合排序
        :return:self
        """
        with allure.step("点击综合排序"):
            self.steps("../page/main.yaml")
        self.tsleep(1)
        return self

    def goto_my(self):
        """
        点击“我的”
        :return: My(self._driver)
        """
        with allure.step("进入“我的”页面"):
            self.steps("../page/main.yaml")
        return My(self._driver)

    def goto_custom(self):
        """
        点击“客户”
        :return: Customer(self._driver)
        """
        with allure.step("进入“客户”页面"):
            self.steps("../page/main.yaml")
        return Customer(self._driver)

    def goto_message(self):
        """
        点击“消息”
        :return: Message(self._driver)
        """
        with allure.step("进入“消息”页面"):
            self.steps("../page/main.yaml")
        return Message(self._driver)

    def goto_index(self):
        """
        点击“首页”
        :return: self
        """
        with allure.step("进入“首页”页面"):
            self.steps("../page/main.yaml")
        return self

    def goto_login(self):
        """
        去登录
        :return: Login(self._driver)
        """
        return Login(self._driver)