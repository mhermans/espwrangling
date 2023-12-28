def slack_post(msg):
    ''' Send a message to a predefined slack channel.'''
    import urequests

    # enable an "incoming-webhook" URL
    # cf. https://api.slack.com/incoming-webhooks
    URL = 'https://hooks.slack.com/services/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'

    headers = {'content-type': 'application/json'}
    data = '{"text":"%s"}' % msg
    resp = urequests.post(URL, data=data, headers=headers)
    return resp
