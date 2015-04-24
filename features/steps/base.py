@when(u'I go to "{alias}"')
def step_impl(context,alias):
    context.browser.visit(context.table[0]['url'])

@then(u'I should be taken to "{alias}"')
def step_impl(context,alias):
    context.browser.title == context.table[0]['title']

