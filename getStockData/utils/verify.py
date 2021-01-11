def isExist(driver, element):
    source = driver.page_source
    if element in source:
        return True
    else:
        return False