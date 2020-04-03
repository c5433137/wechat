import itchat


@itchat.msg_register(itchat.content.TEXT, isGroupChat=True)
def text_reply(msg):
    print(msg.Content)
    print(msg)

    msg.user.send(u'@%s\u2005I received: %s' % (
        msg.actualNickName, msg.text))
    return msg.Content


itchat.auto_login(hotReload=True)
itchat.run()
