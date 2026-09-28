"""Discord redesign icon name -> ordered candidate Iconify names. First one a set has wins.

A trailing `!` on a line's key marks a state icon (muted, locked, denied...): it maps only through
its own candidates, never falls back to the plain icon, so a muted mic never shows as a live one.
"""
import json, re, sys

B = {}  # base concepts, reused below


def c(*names):
    out = []
    for n in names:
        out += n.split()
    return out


B['bell'] = c('bell remind notification bell-ring alarm')
B['bellslash'] = c('bell-off bell-slash close-remind notification-off bell-x bell-mute')
B['bellz'] = c('bell-z bell-snooze bell-sleep snooze bell-off close-remind notification-off')
B['trash'] = c('trash delete trash-can trash-2 bin trash-alt')
B['settings'] = c('settings setting-two setting settings-2 settings-cog cog gear setting-line setting-alt-line')
B['mic'] = c('microphone mic voice microphone-one mic-alt')
B['micslash'] = c('microphone-off microphone-slash mic-off mic-slash voice-off close-voice mute')
B['user'] = c('user profile person user-alt user-one people')
B['users'] = c('users user-group peoples people friends group team user-multiple')
B['home'] = c('home home-two house')
B['search'] = c('search magnifying-glass zoom search-alt')
B['heart'] = c('heart like favorite love')
B['chat'] = c('chat message comment chat-alt message-one messages chat-bubble comments')
B['x'] = c('x close cross close-small close-round close-ring close-one')
B['pencil'] = c('pencil edit edit-alt edit-pencil pen write edit-two edit-one')
B['pin'] = c('pin pushpin push-pin pin-alt map-pin local-pin')
B['link'] = c('link link-one chain link-alt link-two')
B['copy'] = c('copy duplicate copy-one copy-alt files')
B['eye'] = c('eye view preview-open show visible')
B['eyeslash'] = c('eye-off eye-slash preview-close hide invisible eye-closed')
B['lock'] = c('lock locked padlock lock-one lock-alt')
B['unlock'] = c('unlock lock-open unlocked lock-unlocked')
B['plus'] = c('plus add plus-circle add-one')
B['minus'] = c('minus reduce remove minus-circle reduce-one')
B['check'] = c('check checkmark done check-small tick correct check-one')
B['check2'] = c('check-double checks double-check done-all check-all')
B['info'] = c('information-circle info information info-circle circle-info info-alt')
B['help'] = c('question-mark-circle help question help-circle question-circle circle-help')
B['warn'] = c('warning alert attention caution exclamation warning-circle alert-circle danger alert-triangle')
B['error'] = c('alert-circle attention exclamation-circle warning-circle info-circle-error caution alert')
B['xcircle'] = c('close-circle-1 close-circle x-circle circle-x close-one close-ring close-round delete-one')
B['okcircle'] = c('check-circle-1 check-ring-round check-circle circle-check check-one check-ring check-round success')
B['download'] = c('download download-one arrow-down-to-line download-simple down-load')
B['upload'] = c('upload upload-one arrow-up-from-line upload-simple up-load')
B['share'] = c('share share-one share-two share-alt share-android export')
B['refresh'] = c('refresh reload rotate sync refresh-one redo')
B['undo'] = c('undo return rotate-left back')
B['redo'] = c('redo go-on rotate-right forward')
B['menu'] = c('menu-burger-horizontal menu hamburger burger hamburger-button menu-alt application-menu')
B['moreh'] = c('menu-kebab-horizontal meatballs-menu more-horizontal more dots-horizontal menu-dots ellipsis more-one kebab-horizontal')
B['morev'] = c('menu-kebab-vertical more-vertical dots-vertical more-two menu-dots-vertical kebab more-vertical-alt')
B['image'] = c('image picture photo pic picture-one gallery')
B['images'] = c('images gallery pictures photos image-multiple album') + B['image']
B['camera'] = c('camera camera-one photograph')
B['video'] = c('video video-camera video-two camera-video videocamera video-one')
B['videoslash'] = c('video-off video-slash camera-off video-camera-off close-video')
B['phone'] = c('phone phone-call call telephone phone-telephone')
B['hangup'] = c('phone-off phone-x phone-hang-up hang-up phone-missed')
B['headphones'] = c('headphones headphone headset headphone-sound')
B['headslash'] = c('headphones-off headphone-off headset-off headphones-slash')
B['gift'] = c('gift present gift-box gift-one')
B['star'] = c('star star-one')
B['gif'] = c('gif gif-box file-gif')
B['sticker'] = c('sticker stickers sticker-smile')
B['smile'] = c('smile emoji face-smile smiling-face happy mood-smile emotion-happy emoji-happy grinning-face-with-open-mouth')
B['clip'] = c('paperclip attachment paper-clip clip attachment-one')
B['file'] = c('file document file-text doc file-blank page')
B['folder'] = c('folder folder-close folder-one')
B['hash'] = c('hash hashtag number pound')
B['thread'] = c('thread threads message-reply reply comments message-square')
B['forum'] = c('forum comments messages chat-bubbles message-square-dots chat-dots')
B['megaphone'] = c('megaphone announcement speaker loudspeaker volume-notice broadcast bullhorn')
B['volume'] = c('volume volume-up speaker volume-notice volume-2 sound volume-high sound-max')
B['volumex'] = c('sound-mute volume-off volume-x volume-mute mute volume-cross')
B['music'] = c('music music-note music-one note musical-note')
B['play'] = c('play play-one player-play')
B['pause'] = c('pause pause-one player-pause')
B['stop'] = c('stop stop-one player-stop square')
B['screen'] = c('monitor screen desktop computer display')
B['cast'] = c('screen-share cast airplay monitor-up') + B['screen']
B['tv'] = c('tv television tv-one') + B['screen']
B['mobile'] = c('smartphone mobile phone-mobile iphone device-mobile cellphone')
B['laptop'] = c('laptop computer')
B['keyboard'] = c('keyboard keyboard-one')
B['key'] = c('key key-one key-two password')
B['shield'] = c('shield security protect shield-alt')
B['globe'] = c('globe earth world planet internet')
B['compass'] = c('compass compass-one explore navigation')
B['location'] = c('location map-pin map-marker place local pin-alt')
B['clock'] = c('clock time clock-one alarm-clock')
B['timer'] = c('timer stopwatch alarm-clock') + B['clock']
B['hourglass'] = c('hourglass hourglass-full hourglass-null sand-clock') + B['clock']
B['calendar'] = c('calendar calendar-one date calendar-dot calendar-thirty')
B['tag'] = c('tag tag-one label price-tag')
B['tags'] = c('tags tag-multiple') + B['tag']
B['bookmark'] = c('bookmark bookmark-one')
B['flag'] = c('flag flag-one report')
B['fire'] = c('fire flame fire-one')
B['flash'] = c('lightning flash bolt zap thunderbolt')
B['bulb'] = c('lightbulb bulb idea light lamp')
B['wand'] = c('magic-wand wand magic wizard')
B['sparkles'] = c('sparkles sparkle stars magic spark') + B['wand']
B['palette'] = c('palette paint-palette color art palette-one platte')
B['brush'] = c('brush paint-brush paintbrush paint')
B['dropper'] = c('eyedropper dropper color-picker pipette straw')
B['robot'] = c('robot bot robot-one robot-two android')
B['bug'] = c('bug bug-one insect')
B['wrench'] = c('wrench tool tools spanner')
B['hammer'] = c('hammer gavel law')
B['crown'] = c('crown crown-one')
B['trophy'] = c('trophy cup award trophy-one')
B['medal'] = c('medal medal-one award badge')
B['mail'] = c('mail envelope email letter mail-one')
B['text'] = c('text text-size font type letters font-size')
B['quote'] = c('quote quotes quotation double-quotes')
B['slash'] = c('slash command terminal code slash-square')
B['code'] = c('code embed code-one code-brackets brackets')
B['list'] = c('list list-bullets list-unordered bullet-list list-one list-two ordered-list')
B['grid'] = c('grid grid-four apps category view-grid all-application dashboard grid-2')
B['game'] = c('game gamepad game-controller controller game-handle joystick game-ps')
B['puzzle'] = c('puzzle puzzle-piece extension jigsaw plugin')
B['shop'] = c('shop store shopping shopping-bag bag market shopping-cart cart')
B['card'] = c('credit-card card bank-card payment wallet')
B['piggy'] = c('piggy-bank piggy save-money savings bank')
B['ticket'] = c('ticket ticket-one coupon ticket-alt')
B['gem'] = c('diamond gem crystal diamond-one diamonds')
B['server'] = c('server database stack layers')
B['webhook'] = c('webhook api')
B['idcard'] = c('id-card id identification vcard user-card badge card')
B['qr'] = c('qr-code qrcode qr scan-code two-dimensional-code')
B['logout'] = c('logout log-out sign-out exit door-open sign-out-circle')
B['door'] = c('door door-open portal') + B['logout']
B['a11y'] = c('accessibility wheelchair universal-access handicap')
B['chart'] = c('analytics chart chart-line chart-bar graph histogram trending-up data')
B['beaker'] = c('beaker flask experiment test-tube lab chemistry science')
B['book'] = c('book book-one notebook book-open')
B['school'] = c('education school graduation graduation-cap mortarboard') + B['book']
B['car'] = c('car car-one')
B['train'] = c('train subway metro')
B['bike'] = c('bike bicycle cycling')
B['plane'] = c('plane airplane travel flight aircraft')
B['food'] = c('food fork-knife restaurant cutlery hamburger-food pizza')
B['candy'] = c('candy lollipop sweets')
B['nature'] = c('tree leaf nature plant flower tree-one')
B['cloud'] = c('cloud cloud-one')
B['clipcheck'] = c('clipboard-check clipboard checklist list-checkbox clipboard-list')
B['speed'] = c('speedometer speed gauge tachometer dashboard dashboard-one')
B['filters'] = c('filter filters sliders adjustments setting-config equalizer tune sliders-horizontal')
B['drag'] = c('drag drag-handle grip-vertical move drag-vertical')
B['lang'] = c('language translate translation') + B['globe']
B['send'] = c('send send-one paper-plane telegram send-hor')
B['unread'] = c('mail-unread message-unread unread dot')
B['maximize'] = c('maximize fullscreen expand full-screen expand-one')
B['external'] = c('external-link link-external share-one open launch arrow-up-right export')
B['browser'] = c('browser window web') + B['globe']
B['signpost'] = c('signpost sign-post guidepost direction road-sign')
B['cube'] = c('cube box object package')
B['skull'] = c('skull skull-one dead')
B['moon'] = c('moon dark-mode night moon-one')
B['sun'] = c('sun light-mode sun-one day')
B['thumbup'] = c('thumbs-up like thumb-up good-one')
B['thumbdown'] = c('thumbs-down dislike thumb-down bad-one')
B['inventory'] = c('inventory archive backpack package box')
B['radar'] = c('radar scan nearby')
B['badge'] = c('badge verified certificate star-badge') + B['medal']
B['disc'] = c('disc vinyl record-disc cd music-cd record')
B['cc'] = c('closed-captions cc subtitles caption')
B['blur'] = c('blur background image-blur')
B['wifi'] = c('wifi signal network connection antenna')
B['paper'] = c('paper page note') + B['file']
B['hand'] = c('hand raise-hand hand-raised palm hand-up')
B['poll'] = c('poll vote ballot chart-bar chart-histogram')
B['stamp'] = c('stamp seal approve')
B['boost'] = c('rocket') + B['gem']
B['swapcam'] = c('camera-rotate switch-camera flip-camera camera-switch')
B['stage'] = c('podcast broadcast stage') + B['mic']
B['wave'] = c('sound-wave waveform audio soundboard') + B['music']
B['up'] = c('arrow-up arrow-small-up up')
B['down'] = c('arrow-down arrow-small-down down')
B['left'] = c('arrow-left arrow-small-left left back')
B['right'] = c('arrow-right arrow-small-right right')
B['chup'] = c('chevron-up angle-up caret-up up expand-up up-small')
B['chdown'] = c('chevron-down angle-down caret-down down expand-down down-small')
B['chleft'] = c('chevron-left angle-left caret-left left left-small')
B['chright'] = c('chevron-right angle-right caret-right right right-small')
B['updown'] = c('arrows-up-down arrow-up-down sort switch-vertical sort-two')
B['upleft'] = c('arrow-up-left arrow-left-up')
B['upright'] = c('arrow-up-right arrow-right-up') + B['external']
B['backspace'] = c('backspace delete-left delete-key')
B['burger'] = B['menu']
B['stageicon'] = B['stage']


def plus(base, *mods):
    """`base-mod` and `mod-base` for each candidate, e.g. user-plus, add-user."""
    out = []
    for m in mods:
        for b in B[base][:6]:
            out += [f'{b}-{m}', f'{m}-{b}']
    return out


PLUS = ('plus', 'add')
MINUS = ('minus', 'remove', 'reduce')
XMOD = ('x', 'off', 'close', 'remove', 'delete', 'cross')
SLASH = ('off', 'slash', 'mute', 'close', 'disabled')
LOCK = ('lock', 'locked')
WARN = ('warning', 'alert', 'exclamation')
CHECK = ('check', 'checked', 'done')

# `!` = state icon: no fallback to the base concept.
MAP = {
    'AccessibilityIcon': B['a11y'], 'AnalyticsIcon': B['chart'], 'AnnouncementsIcon': B['megaphone'],
    'AppsIcon': B['grid'], 'ActivitiesIcon': c('rocket') + B['game'], 'ArrowLargeDownIcon': B['down'],
    'ArrowLargeLeftIcon': B['left'], 'ArrowLargeRightIcon': B['right'], 'ArrowLargeUpIcon': B['up'],
    'ArrowSmallDownIcon': B['down'], 'ArrowSmallLeftIcon': B['left'], 'ArrowSmallRightIcon': B['right'],
    'ArrowSmallUpIcon': B['up'], 'ArrowsUpDownIcon': B['updown'], 'ArrowAngleLeftUpIcon': B['upleft'],
    'ArrowAngleRightUpIcon': B['upright'], 'AtIcon': c('at at-sign mention email-at'),
    'AttachmentIcon': B['clip'], 'AuthorizedAppsIcon': c('shield-check') + B['grid'], 'BackspaceIcon': B['backspace'],
    'BadgeIcon': B['badge'], 'BeakerIcon': B['beaker'], 'BellIcon': B['bell'], 'BellSlashIcon!': B['bellslash'],
    'BellZIcon!': B['bellz'], 'BicycleIcon': B['bike'], 'BillIcon': c('bill receipt invoice'),
    'BlurBackgroundIcon': B['blur'], 'BookCheckIcon': c('book-check') + B['book'], 'BookmarkIcon': B['bookmark'],
    'BookmarkOutlineIcon': B['bookmark'], 'BoostGemIcon': B['boost'], 'BoostGemOutlineIcon': B['boost'],
    'BoostTier2Icon': B['boost'], 'BoostTier3Icon': B['boost'], 'BrowserIcon': B['browser'], 'BugIcon': B['bug'],
    'BurgerIcon': B['menu'], 'CalendarIcon': B['calendar'], 'CalendarMinusIcon!': plus('calendar', *MINUS),
    'CalendarPlusIcon!': plus('calendar', *PLUS), 'CalendarXIcon!': plus('calendar', *XMOD),
    'CameraIcon': B['camera'], 'CameraSwapIcon': B['swapcam'], 'CandyIcon': B['candy'], 'CarIcon': B['car'],
    'ChannelListIcon': B['list'], 'ChannelNotificationIcon': B['bell'], 'ChannelsFollowedIcon': B['megaphone'],
    'ChatIcon': B['chat'], 'ChatAlertIcon!': plus('chat', *WARN), 'ChatArrowRightIcon': c('message-sent forward share-one') + plus('chat', 'arrow-right', 'forward'),
    'ChatCheckIcon!': plus('chat', *CHECK), 'ChatDotsIcon': plus('chat', 'dots') + B['chat'],
    'ChatMarkUnreadIcon': B['unread'] + plus('chat', 'dot', 'unread'), 'ChatPlusIcon!': plus('chat', *PLUS),
    'ChatShieldIcon': B['shield'], 'ChatSmileIcon': plus('chat', 'smile') + B['chat'],
    'ChatWarningIcon!': plus('chat', *WARN), 'ChatXIcon!': plus('chat', *XMOD),
    'CheckmarkBoldIcon': B['check'], 'CheckmarkLargeBoldIcon': B['check'], 'CheckmarkLargeIcon': B['check'],
    'CheckmarkSmallBoldIcon': B['check'], 'CheckmarkSmallIcon': B['check'],
    'ChevronLargeDownIcon': B['chdown'], 'ChevronLargeLeftIcon': B['chleft'], 'ChevronLargeRightIcon': B['chright'],
    'ChevronLargeUpIcon': B['chup'], 'ChevronSmallDownIcon': B['chdown'], 'ChevronSmallLeftIcon': B['chleft'],
    'ChevronSmallRightIcon': B['chright'], 'ChevronSmallUpIcon': B['chup'],
    'CircleCheckIcon': B['okcircle'], 'CircleErrorIcon': B['error'], 'CircleExclamationPointIcon': B['error'],
    'CircleInformationIcon': B['info'], 'CircleMinusIcon': c('minus-circle circle-minus reduce-one') + B['minus'],
    'CirclePlayIcon': c('play-circle circle-play') + B['play'], 'CirclePlusIcon': c('plus-circle circle-plus add-one') + B['plus'],
    'CircleQuestionIcon': B['help'], 'CircleWarningIcon': B['error'], 'CircleXIcon': B['xcircle'],
    'ClipboardCheckIcon': B['clipcheck'], 'ClipboardListIcon': c('clipboard-list clipboard'), 'ClipsIcon': c('film clapperboard movie video-film') + B['video'],
    'ClockIcon': B['clock'], 'ClockWarningIcon!': plus('clock', *WARN), 'ClockXIcon!': plus('clock', *XMOD),
    'CloseLargeBoldIcon': B['x'], 'CloseLargeIcon': B['x'], 'CloseSmallBoldIcon': B['x'], 'CloseSmallIcon': B['x'],
    'ClosedCaptionsOutlineIcon': B['cc'], 'CloudIcon': B['cloud'], 'ClydeIcon': B['robot'], 'CompassIcon': B['compass'],
    'ConnectionAverageIcon': B['wifi'], 'ConnectionBadIcon': B['wifi'], 'ConnectionFineIcon': B['wifi'],
    'ConnectionUnknownIcon': B['wifi'], 'CopyIcon': B['copy'], 'CreativeIcon': B['palette'], 'CreditCardIcon': B['card'],
    'CrownIcon': B['crown'], 'DenyIcon': c('forbid block ban prohibited stop-sign circle-slash'),
    'DoorExitIcon': B['logout'], 'DoubleCheckmarkIcon': B['check2'], 'DownloadIcon': B['download'], 'DragIcon': B['drag'],
    'EducationIcon': B['school'], 'EmbedIcon': B['code'], 'EmojiSkullIcon': B['skull'], 'EnvelopeIcon': B['mail'],
    'EyeDropperIcon': B['dropper'], 'EyeIcon': B['eye'], 'EyeSlashIcon!': B['eyeslash'], 'FileIcon': B['file'],
    'FileUpIcon': c('file-upload file-up upload-file') + B['upload'], 'FileWarningIcon!': plus('file', *WARN),
    'FiltersHorizontalIcon': B['filters'], 'FireIcon': B['fire'], 'FlagIcon': B['flag'], 'FlashIcon': B['flash'],
    'FolderIcon': B['folder'], 'FolderPlusIcon!': plus('folder', *PLUS), 'FoodIcon': B['food'], 'ForumIcon': B['forum'],
    'FriendsIcon': B['users'], 'FullscreenEnterIcon': B['maximize'], 'GameControllerIcon': B['game'], 'GifIcon': B['gif'],
    'GiftIcon': B['gift'], 'GlobeEarthIcon': B['globe'], 'GridHorizontalIcon': B['grid'], 'GridSquareIcon': B['grid'],
    'GroupIcon': B['users'], 'GroupPlusIcon!': plus('users', *PLUS) + plus('user', *PLUS), 'HammerIcon': B['hammer'],
    'HandRequestSpeakIcon': B['hand'], 'HashmarkIcon': B['hash'], 'ChannelsTextIcon': B['hash'],
    'HeadphonesIcon': B['headphones'], 'HeadphonesSlashIcon!': B['headslash'], 'HeadphonesDenyIcon!': B['headslash'],
    'HeartIcon': B['heart'], 'HomeIcon': B['home'], 'HourglassIcon': B['hourglass'], 'HubIcon': B['school'],
    'IdCardIcon': B['idcard'], 'IdIcon': B['idcard'], 'ImageIcon': B['image'], 'ImageFileIcon': B['image'],
    'ImagesIcon': B['images'], 'ImagePlusIcon!': plus('image', *PLUS), 'ImageBrokenIcon!': plus('image', 'off', 'broken'),
    'ImageTextIcon': B['image'], 'InventoryIcon': B['inventory'], 'KeyIcon': B['key'], 'KeyboardIcon': B['keyboard'],
    'LanguageIcon': B['lang'], 'LaptopPhoneIcon': c('devices device') + B['laptop'], 'LettersIcon': B['text'],
    'LightbulbIcon': B['bulb'], 'LinkExternalMediumIcon': B['external'], 'LinkExternalSmallIcon': B['external'],
    'LinkIcon': B['link'], 'LinkPlusIcon!': plus('link', *PLUS), 'ListBulletsIcon': B['list'], 'ListViewIcon': B['list'],
    'LocationIcon': B['location'], 'LockIcon': B['lock'], 'LockUnlockedIcon': B['unlock'], 'MagicDoorIcon': B['door'],
    'MagicWandIcon': B['wand'], 'MagnifyingGlassIcon': B['search'], 'MarkUnreadIcon': B['unread'],
    'MaximizeIcon': B['maximize'], 'MedalIcon': B['medal'], 'MenuIcon': B['menu'], 'MicrophoneIcon': B['mic'],
    'MicrophoneSlashIcon!': B['micslash'], 'MicrophoneDenyIcon!': B['micslash'], 'MobilePhoneIcon': B['mobile'],
    'ModerationIcon': B['hammer'] + B['shield'], 'MoreHorizontalIcon': B['moreh'], 'MoreVerticalIcon': B['morev'],
    'MusicIcon': B['music'], 'MusicSlashIcon!': plus('music', *SLASH), 'NatureIcon': B['nature'], 'NearbyScanIcon': B['radar'],
    'NewUserIcon': plus('user', *PLUS), 'NewUserLargeIcon': plus('user', *PLUS), 'NitroWheelIcon': B['gem'],
    'ObjectIcon': B['cube'], 'PaintPaletteIcon': B['palette'], 'PaintbrushThinIcon': B['brush'], 'PaperIcon': B['paper'],
    'PaperPlusIcon!': plus('file', *PLUS), 'PauseIcon': B['pause'], 'PencilIcon': B['pencil'],
    'PencilSparkleIcon': B['wand'] + B['pencil'], 'PhoneCallIcon': B['phone'], 'PhoneCallThinIcon': B['phone'],
    'PhoneHangUpIcon!': B['hangup'], 'PhoneHangUpThinIcon!': B['hangup'], 'PhoneIcon': B['phone'],
    'PiggyBankIcon': B['piggy'], 'PinIcon': B['pin'], 'PlayIcon': B['play'], 'PlusLargeIcon': B['plus'],
    'PlusMediumIcon': B['plus'], 'PlusSmallIcon': B['plus'], 'PollsIcon': B['poll'], 'PrivacyAndSafetyIcon': B['shield'],
    'PuzzlePieceIcon': B['puzzle'], 'QrCodeIcon': B['qr'], 'QrCodeCameraIcon': c('scan scan-code') + B['qr'],
    'QuestsIcon': c('map treasure target quest compass'), 'QuoteIcon': B['quote'], 'ReactionIcon': B['smile'],
    'AddSuperReactionIcon': c('smile-plus emoji-add') + B['sparkles'], 'RecordPlayerIcon': B['disc'], 'RedoIcon': B['redo'],
    'RefreshIcon': B['refresh'], 'RetryIcon': B['refresh'], 'RobotIcon': B['robot'], 'ScienceIcon': B['beaker'],
    'ScienceDefaultIcon': B['beaker'], 'ScreenIcon': B['screen'], 'ScreenStreamIcon': B['cast'], 'ScreenArrowIcon': B['cast'],
    'ScreenXIcon!': plus('screen', *XMOD), 'ScreenStopWatchingIcon!': plus('screen', *XMOD),
    'SendMessageIcon': B['send'], 'ServerIcon': B['server'], 'ServerGridIcon': B['grid'], 'SettingsIcon': B['settings'],
    'ShareIcon': B['share'], 'ShieldIcon': B['shield'], 'ShieldLockIcon': c('shield-lock') + B['shield'],
    'ShieldUserIcon': c('shield-user user-shield') + B['shield'], 'ShopIcon': B['shop'], 'ShopSparkleIcon': B['shop'],
    'SignPostIcon': B['signpost'], 'SkullIcon': B['skull'], 'SlashIcon': B['slash'], 'SlashBoxIcon': B['slash'],
    'SmileIcon': B['smile'], 'SmilePlusIcon': c('smile-plus emoji-add face-plus mood-plus') + B['smile'],
    'SoundboardIcon': B['wave'], 'SoundboardSlashIcon!': plus('music', *SLASH), 'SparklesIcon': B['sparkles'],
    'SpeedometerIcon': B['speed'], 'SpoilerIcon': B['eyeslash'], 'StaffBadgeIcon': B['badge'], 'StageIcon': B['stage'],
    'StampIcon': B['stamp'], 'StarIcon': B['star'], 'StarOutlineIcon': B['star'], 'StickerIcon': B['sticker'] + B['smile'],
    'StickerPlusIcon': c('sticker-plus') + B['sticker'], 'StopIcon': B['stop'], 'SubscriptionIcon': B['gem'],
    'SuperReactionIcon': B['sparkles'], 'TagIcon': B['tag'], 'TagsIcon': B['tags'], 'TextIcon': B['text'],
    'ThemeDarkIcon': B['moon'], 'ThemeLightIcon': B['sun'], 'ThemeMidnightIcon': B['moon'], 'ThreadIcon': B['thread'],
    'ThreadPlusIcon!': plus('thread', *PLUS) + plus('chat', *PLUS), 'ThumbsDownIcon': B['thumbdown'],
    'ThumbsUpIcon': B['thumbup'], 'TicketIcon': B['ticket'], 'TicketDollarIcon': B['ticket'], 'TimerIcon': B['timer'],
    'TopicsIcon': B['hash'], 'TrainIcon': B['train'], 'TranscriptOutlineIcon': B['cc'] + B['file'], 'TrashIcon': B['trash'],
    'TravelIcon': B['plane'], 'TreehouseIcon': B['nature'], 'TriangleExclamationPointIcon': B['warn'],
    'TrophyIcon': B['trophy'], 'TvIcon': B['tv'], 'UndoIcon': B['undo'], 'UnknownGameIcon': B['game'],
    'UnsendIcon': B['undo'], 'UploadIcon': B['upload'], 'UserIcon': B['user'], 'UserCheckIcon!': plus('user', *CHECK),
    'UserCircleIcon': c('user-circle circle-user avatar profile-circle') + B['user'], 'UserCircleNewIcon': c('user-circle') + B['user'],
    'UserMinusIcon!': plus('user', *MINUS), 'UserPlusIcon!': plus('user', *PLUS), 'UserSquareIcon': c('user-square') + B['user'],
    'UserStatusIcon': B['user'], 'VideoIcon': B['video'], 'VideoSlashIcon!': B['videoslash'], 'VideoDenyIcon!': B['videoslash'],
    'VideoSelfieIcon': B['video'], 'VoiceNormalIcon': B['volume'], 'ChannelsVoiceNormalIcon': B['volume'],
    'VoiceXIcon!': B['volumex'], 'ChannelsVoiceXIcon!': B['volumex'], 'VrHeadsetIcon': c('vr virtual-reality vr-glasses'),
    'WarningIcon': B['warn'], 'WebhookIcon': B['webhook'], 'WebhookPlusIcon!': plus('webhook', *PLUS),
    'WindowLaunchIcon': B['external'], 'WrenchIcon': B['wrench'], 'XLargeBoldIcon': B['x'], 'XLargeIcon': B['x'],
    'XSmallBoldIcon': B['x'], 'XSmallIcon': B['x'], 'GroupArrowDownIcon': B['users'],
    'MobilePhoneSettingsIcon': B['mobile'], 'MobilePhoneShareIcon': B['mobile'], 'MobilePhoneDenyIcon!': plus('mobile', *XMOD),
    'OrbsIcon': c('orb coin coins planet'), 'EmojiSmilingFaceWithHeartsIcon': B['smile'],
    'HandRequestDenyIcon!': plus('hand', *XMOD), 'MicrophoneArrowRightIcon': B['mic'], 'StageLockIcon!': plus('stage', *LOCK),
    'ThreadLockIcon!': plus('thread', *LOCK), 'ForumLockIcon!': plus('forum', *LOCK), 'ImageLockIcon!': plus('image', *LOCK),
    'TextLockIcon!': plus('hash', *LOCK), 'ChannelsTextLockedIcon!': plus('hash', *LOCK), 'VoiceLockIcon!': plus('volume', *LOCK),
    'ChannelsVoiceLockedIcon!': plus('volume', *LOCK), 'AnnouncementsLockIcon!': plus('megaphone', *LOCK),
    'StampXIcon!': plus('stamp', *XMOD), 'RemixIcon': B['wand'], 'TextControllerIcon': B['game'],
    'UserPlatformIcon': B['user'], 'EmojiColdFaceIcon': [], 'ExperimentalLfgIcon': B['users'],
}

SETS = ['icon-park-outline', 'keyline-icons', 'mynaui', 'iconamoon', 'pixelarticons', 'lets-icons',
        'icon-park-twotone', 'icon-park-solid']

# Two-layer Discord icons: the full icon goes in -primary, -secondary is left empty.
LAYERED = ['CircleCheckIcon', 'CircleErrorIcon', 'CircleExclamationPointIcon', 'CircleInformationIcon',
           'CircleMinusIcon', 'CirclePlayIcon', 'CirclePlusIcon', 'CircleQuestionIcon', 'CircleWarningIcon',
           'CircleXIcon', 'SettingsCircleIcon']


# Names a set uses for something else (seen on the contact sheets).
EXCLUDE = {
    'keyline-icons': r'^(delete)$',
    'lets-icons': r'^(up|down|left|right|remove|sound|desktop|mobile|return)$',
    'icon-park-outline': r'^(expand-.*|connection)$',
    'icon-park-twotone': r'^(expand-.*|connection)$',
    'icon-park-solid': r'^(expand-.*|connection)$',
}


def main(sets_dir, out):
    result = {}
    for p in SETS:
        d = json.load(open(f'{sets_dir}/{p}.json', encoding='utf-8'))
        have = set(d['icons']) | set(d.get('aliases', {}))
        if p in EXCLUDE:
            have = {n for n in have if not re.match(EXCLUDE[p], n)}
        m = {}
        for key, cands in MAP.items():
            name = key.rstrip('!')
            pick = next((n for n in cands if n in have), None)
            if pick:
                m[name] = pick
        result[p] = m
        print(f'{p:20} {len(m)}/{len(MAP)}')
    json.dump(result, open(out, 'w'), indent=1)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
