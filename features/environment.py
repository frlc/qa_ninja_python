from selenium import webdriver
from ipdb import spost_mortem

def before_all(context):
    context.driver = webdriver.Chrome("/home/ret4o/Downloads/qaninja-liveclass-master/drivers/chromedriver")

def before_feature(context, feature):
    print(feature.name)

def before_scenario(context, scenario):
    print(scenario.name)

def before_step(context, step):
    print(step.name)

def before_tag(context, tag):
    print(tag)

def after_all(context):
    context.driver.quit()

def after_feature(context, feature):
    print(feature.name)

def after_scenario(context, scenario):
    print(scenario.name)

def after_step(context, step):
    print(step.status)
    # if step.status == 'failed' and context.config.userdata['debug']:
    #     spost_mortem(step.exc_traceback)



def after_tag(context, tag):
    print(tag)

