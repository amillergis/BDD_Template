@given(u'that splinter and the chrome web driver are installed correctly')
def step_impl(context):
    try:
        import splinter
        assert True
    except:
        raise ImportError(u'Splinter cannot be imported')