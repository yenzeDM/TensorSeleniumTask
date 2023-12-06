from selenium.webdriver.common.by import By


class BasePageLocators:
    pass


class ContactPageLocators:
    CLICK_ON_TENSOR_BANNER = (By.CSS_SELECTOR, '#contacts_clients > div.sbis_ru-container > div > div > div.s-Grid-col.s-Grid-col--4.s-Grid-col--xm12 > div > a > img')
    CORRECT_REGION_SELECTED = (By.CSS_SELECTOR, 'div.s-Grid-container.s-Grid-container--space.s-Grid-container--alignEnd.s-Grid-container--noGutter.sbisru-Contacts__underline > div:nth-child(1) > div > div:nth-child(2) > span > span')
    IS_LIST_OF_PARTNERS = (By.CSS_SELECTOR, 'div.sbisru-Contacts-List__col.ws-flex-shrink-1.ws-flex-grow-1')
    CHANGE_REGION = (By.CSS_SELECTOR, 'div.sbis_ru-Region-Panel > div > ul > li:nth-child(43)')
    PARTNERS = (By.CSS_SELECTOR, '.pb-xm-12.pr-xm-32')


class SbisRuPageLocators:
    GO_TO_CONTACT_PAGE = (By.CSS_SELECTOR, 'div.sbisru-Header__container.sbis_ru-container > ul > li.sbisru-Header__menu-item.sbisru-Header__menu-item-1.mh-8.s-Grid--hide-sm > a')
    GO_TO_DOWNLOAD_PAGE = (By.CSS_SELECTOR, 'div.sbisru-Footer__container > div:nth-child(10) > ul > li:nth-child(6) > a')


class TensorRuPageLocators:
    IS_BLOCK_POWER_IS_IN_PEOPLE = (By.CSS_SELECTOR, '#container > div.tensor_ru-content_wrapper > div > div.tensor_ru-Index__block4-bg > div > div > div:nth-child(1) > div')
    TITLE = (By.CSS_SELECTOR, '#container > div.tensor_ru-content_wrapper > div > div.tensor_ru-Index__block4-bg > div > div > div:nth-child(1) > div > p.tensor_ru-Index__card-title.tensor_ru-pb-16')
    CLICK_MORE_DETAILS_IN_BLOCK_POWER_IS_IN_PEOPLE = (By.CSS_SELECTOR, 'div.tensor_ru-Index__block4-bg > div > div > div:nth-child(1) > div > p:nth-child(4) > a')


class TensorAboutPageLocators:
    PICTURE_DEVELOPING_A_VLSI_SYSTEM = (By.CSS_SELECTOR, 'div.tensor_ru-container.tensor_ru-section.tensor_ru-About__block3 > div.s-Grid-container > div:nth-child(1) > a > div.tensor_ru-About__block3-image-wrapper > img')
    PICTURE_PROMOTE_SERVICES = (By.CSS_SELECTOR, 'div.s-Grid-container > div:nth-child(2) > a > div.tensor_ru-About__block3-image-wrapper > img')
    PICTURE_CREATE_INFRASTRUCTURE = (By.CSS_SELECTOR, 'div.s-Grid-container > div:nth-child(3) > a > div.tensor_ru-About__block3-image-wrapper > img')
    PICTURE_ACCOMPANY_CLIENTS = (By.CSS_SELECTOR, 'div.s-Grid-container > div:nth-child(4) > a > div.tensor_ru-About__block3-image-wrapper > img')


class SbisRuDownloadPageLocators:
    SELECT_VLSI_PLAGIN = (By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[1]/div/div/div/div[1]/div/div/div/div[3]/div[2]')
    SELECT_WINDOWS_OS = (By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[1]/div/div/div/div[2]/div/div[2]/div/div/div[1]/div/div[1]')
    CHECK_FILE_SIZE = (By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[1]/div/div/div/div[2]/div/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/div/a')