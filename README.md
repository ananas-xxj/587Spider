交接文档
=========
* 买量包
  * 主要类文件
      * ScrollGameActivity.class
      * GameIdList.class
  * 接口协议
      * getBuyPackageGameList(int gameId, IBaseRequestCallback<BuyPackageGameList> callback);
      * getGameListById(int gameId, IBaseRequestCallback<IdGetGameInfo> callback);
      * requestGameList(IBaseRequestCallback<List<GameList>> callback);
  * 注意事项
      * 每个游戏都是Rv 的一个item,每个Item都有一个弹幕、开始游戏、下载游戏等布局，在activity中拿到对应ViewHolder进行ui操作。
      * 第一次进未登录后台开始下载买量游戏，点击开始游戏游客登录，登录成功绑定IM以及开始游戏。
      * 打不同的买量游戏需要更改GameIdList中的GameId、替换买量游戏背景mai_bg.png。
* 首页心跳房翻转动画
  * 主要类文件
    * HeartBreakViewHolder.class
    * Rotate3dAnimation.class
  * 接口协议
    * 无
  * 注意事项
    * 前面4个ImageView,翻转动画播放完后显示后面4个ImageView。
* 房间底部输入相关
  * 主要类文件
    * RoomEditView.class
    * mobi.soulgame.littlegamecenter.util.wechatkeyboardutil.KeyboardUtil.class
  * 接口协议
    * 无
  * 注意事项
    * 初始化的时候KeyboardUtil可能部分手机部分时候获取不到键盘高度，在键盘弹出回调里重新获取。
* 消息列表ui
  * 主要类文件
    * VoiceRoomChatAdapter.class
    * SpanUtils.class
  * 接口协议
    * 无
  * 注意事项
    * 麦位表情消息、爱心消息、礼物消息、系统的加入房间、离开房间都是由SpanUtils 拼接成的。
* 麦位动画
  * 主要类文件
    * RoomEmojiManager.class
    * SendRoomEmojiDialog.class
  * 接口协议
    * 无
  * 注意事项
    * 表情Id是表情图片名字id_1.png的数字
    * id_1、id_id_1、emoji_1,分别对应发送对话框静态图、消息列表静态图、表情lottie
* 赠送爱心
  * 主要类文件
    * SendLoveDialog.class
    * ReceiveLoveView.class
    * LoveGroupView.class
  * 接口协议
    * 无
  * 注意事项
    * SendLoveDialog 发送爱心对话框，ReceiveLoveView 接收爱心连击动画View, LoveGroupView 爱心弹射坠落动画。
* 口令分享
  * 主要类文件
    * ShareCipherTextDialog.class
    * CipherTextManager.class
  * 接口协议
    * requestCipherText(int type,IBaseRequestCallback<CipherTextModel> callback);
  * 注意事项
    * 用6组表情，每组4个不同表情来代表数字0123，用这组表情的01234个数字作为4进制去显示10进制的uid。
* 探探玩法
  * 主要类文件
    * tantan整个目录
  * 接口协议
    * 协议未定
  * 注意事项
    * 整个相关代码都在tantan文件目录下，只实现了ui界面。
