from splinter import Browser

def before_tag(context,tag):
    if tag in ("preview"):
        context.browser = Browser('chrome')
    else:
        context.browser = Browser("phantomjs",service_args=['--ignore-ssl-errors=true'])

def after_tag(context,tag):
    if not context.failed:
        context.browser.quit()