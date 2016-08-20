#!/usr/bin/env python
# coding: utf-8
import os
import sys

path_prepend = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'lib')
sys.path.append(path_prepend)
import log
from weixin import *
import command_module
import kvstore_module
import processor_module


class MyWebWeixin(WebWeixin):
    def __str__(self):
        description = \
            "=========================\n" + \
            "[#] Web Weixin\n" + \
            "[#] Debug Mode: " + str(self.DEBUG) + "\n" + \
            "[#] Uuid: " + self.uuid + "\n" + \
            "[#] Uin: " + str(self.uin) + "\n" + \
            "[#] Sid: " + self.sid + "\n" + \
            "[#] Skey: " + self.skey + "\n" + \
            "[#] DeviceId: " + self.deviceId + "\n" + \
            "[#] PassTicket: " + self.pass_ticket + "\n" + \
            "========================="
        return description

    def __init__(self):
        self.DEBUG = False
        self.uuid = ''
        self.base_uri = ''
        self.redirect_uri = ''
        self.uin = ''
        self.sid = ''
        self.skey = ''
        self.pass_ticket = ''
        self.deviceId = 'e' + repr(random.random())[2:17]
        self.BaseRequest = {}
        self.synckey = ''
        self.SyncKey = []
        self.User = []
        self.MemberList = []
        self.ContactList = []  # 好友
        self.GroupList = []  # 群
        self.GroupMemeberList = []  # 群友
        self.PublicUsersList = []  # 公众号／服务号
        self.SpecialUsersList = []  # 特殊账号
        self.autoReplyMode = False
        self.syncHost = ''
        self.user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.109 Safari/537.36'
        self.interactive = False
        self.autoOpen = False
        self.saveFolder = os.path.join(os.getcwd(), 'saved')
        self.saveSubFolders = {'webwxgeticon': 'icons', 'webwxgetheadimg': 'headimgs', 'webwxgetmsgimg': 'msgimgs',
                               'webwxgetvideo': 'videos', 'webwxgetvoice': 'voices', '_showQRCodeImg': 'qrcodes'}
        self.appid = 'wx782c26e4c19acffb'
        self.lang = 'zh_CN'
        self.lastCheckTs = time.time()
        self.memberCount = 0
        self.SpecialUsers = ['newsapp', 'fmessage', 'filehelper', 'weibo', 'qqmail', 'fmessage', 'tmessage', 'qmessage',
                             'qqsync', 'floatbottle', 'lbsapp', 'shakeapp', 'medianote', 'qqfriend', 'readerapp',
                             'blogapp', 'facebookapp', 'masssendapp', 'meishiapp', 'feedsapp',
                             'voip', 'blogappweixin', 'weixin', 'brandsessionholder', 'weixinreminder',
                             'wxid_novlwrv3lqwv11', 'gh_22b87fa7cb3c', 'officialaccounts', 'notification_messages',
                             'wxid_novlwrv3lqwv11', 'gh_22b87fa7cb3c', 'wxitil', 'userexperience_alarm',
                             'notification_messages']
        self.TimeOut = 20  # 同步最短时间间隔（单位：秒）
        self.media_count = -1

        self.cookie = cookielib.CookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookie))
        opener.addheaders = [('User-agent', self.user_agent)]
        urllib2.install_opener(opener)

    def handleMsg(self, r):
        logger.info('reimport all the modules!')
        reload(command_module)
        reload(kvstore_module)
        reload(processor_module)

        inx = 1
        for msg in r['AddMsgList']:
            try:

                logger.info('process the %d the message' % inx)

                print '[*] 你有新的消息，请注意查收'
                logging.debug('[*] 你有新的消息，请注意查收')

                if self.DEBUG:
                    fn = 'msg' + str(int(random.random() * 1000)) + '.json'
                    with open(fn, 'w') as f:
                        f.write(json.dumps(msg))
                    print '[*] 该消息已储存到文件: ' + fn
                    logging.debug('[*] 该消息已储存到文件: %s' % (fn))

                msgType = msg['MsgType']
                name = self.getUserRemarkName(msg['FromUserName'])
                content = msg['Content'].replace('&lt;', '<').replace('&gt;', '>')
                msgid = msg['MsgId']

                # view the message from user
                processor_module.view_message(msg)

                request = command_module.getRequest(content)

                processor_module.main_process(self, name, request)

            except Exception as e:
                import traceback
                traceback.print_exc()

            inx = inx + 1

            #
            # if msgType == 1:
            #     raw_msg = {'raw_msg': msg}
            #     self._showMsg(raw_msg)
            #     if self.autoReplyMode:
            #         ans = self._xiaodoubi(content) + '\n[微信机器人自动回复]'
            #         if self.webwxsendmsg(ans, msg['FromUserName']):
            #             print '自动回复: ' + ans
            #             logging.info('自动回复: ' + ans)
            #         else:
            #             print '自动回复失败'
            #             logging.info('自动回复失败')
            # elif msgType == 3:
            #     image = self.webwxgetmsgimg(msgid)
            #     raw_msg = {'raw_msg': msg,
            #                'message': '%s 发送了一张图片: %s' % (name, image)}
            #     self._showMsg(raw_msg)
            #     self._safe_open(image)
            # elif msgType == 34:
            #     voice = self.webwxgetvoice(msgid)
            #     raw_msg = {'raw_msg': msg,
            #                'message': '%s 发了一段语音: %s' % (name, voice)}
            #     self._showMsg(raw_msg)
            #     self._safe_open(voice)
            # elif msgType == 42:
            #     info = msg['RecommendInfo']
            #     print '%s 发送了一张名片:' % name
            #     print '========================='
            #     print '= 昵称: %s' % info['NickName']
            #     print '= 微信号: %s' % info['Alias']
            #     print '= 地区: %s %s' % (info['Province'], info['City'])
            #     print '= 性别: %s' % ['未知', '男', '女'][info['Sex']]
            #     print '========================='
            #     raw_msg = {'raw_msg': msg, 'message': '%s 发送了一张名片: %s' % (
            #         name.strip(), json.dumps(info))}
            #     self._showMsg(raw_msg)
            # elif msgType == 47:
            #     url = self._searchContent('cdnurl', content)
            #     raw_msg = {'raw_msg': msg,
            #                'message': '%s 发了一个动画表情，点击下面链接查看: %s' % (name, url)}
            #     self._showMsg(raw_msg)
            #     self._safe_open(url)
            # elif msgType == 49:
            #     appMsgType = defaultdict(lambda: "")
            #     appMsgType.update({5: '链接', 3: '音乐', 7: '微博'})
            #     print '%s 分享了一个%s:' % (name, appMsgType[msg['AppMsgType']])
            #     print '========================='
            #     print '= 标题: %s' % msg['FileName']
            #     print '= 描述: %s' % self._searchContent('des', content, 'xml')
            #     print '= 链接: %s' % msg['Url']
            #     print '= 来自: %s' % self._searchContent('appname', content, 'xml')
            #     print '========================='
            #     card = {
            #         'title': msg['FileName'],
            #         'description': self._searchContent('des', content, 'xml'),
            #         'url': msg['Url'],
            #         'appname': self._searchContent('appname', content, 'xml')
            #     }
            #     raw_msg = {'raw_msg': msg, 'message': '%s 分享了一个%s: %s' % (
            #         name, appMsgType[msg['AppMsgType']], json.dumps(card))}
            #     self._showMsg(raw_msg)
            # elif msgType == 51:
            #     raw_msg = {'raw_msg': msg, 'message': '[*] 成功获取联系人信息'}
            #     self._showMsg(raw_msg)
            # elif msgType == 62:
            #     video = self.webwxgetvideo(msgid)
            #     raw_msg = {'raw_msg': msg,
            #                'message': '%s 发了一段小视频: %s' % (name, video)}
            #     self._showMsg(raw_msg)
            #     self._safe_open(video)
            # elif msgType == 10002:
            #     raw_msg = {'raw_msg': msg, 'message': '%s 撤回了一条消息' % name}
            #     self._showMsg(raw_msg)
            # else:
            #     logging.debug('[*] 该消息类型为: %d，可能是表情，图片, 链接或红包: %s' %
            #                   (msg['MsgType'], json.dumps(msg)))
            #     raw_msg = {
            #         'raw_msg': msg, 'message': '[*] 该消息类型为: %d，可能是表情，图片, 链接或红包' % msg['MsgType']}
            #     self._showMsg(raw_msg)


if __name__ == '__main__':
    # logger = logging.getLogger(__name__)
    # logger = logging.getLogger('haha_log')

    log.Logs.set_context(directory='./', namespace='test')
    logger = log.Logs().get_logger('weixinBot')

    import coloredlogs

    coloredlogs.install(level='DEBUG')

    webwx = MyWebWeixin()
    webwx.start()
