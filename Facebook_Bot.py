              ########## - Donwload Lib - #########
import time , json , string , os , re , random , uuid , subprocess , requests , sys , telebot ; from telebot import types ; from os import system
              ########## - Starting Code - #########
sTo = telebot.TeleBot('7129990147:AAH6-1P_2Kh0QF6h44Q6TGs8_PCXa-6_Tzk')
@sTo.message_handler(commands=['start'])
def Start(message):
	id_tele = message.from_user.id
	get_list = types.InlineKeyboardButton(text='- اضغط الصنع ملف.',callback_data='get_list')
	Add_Cookie = types.InlineKeyboardButton(text='-.من هنا ضيف حساب اضغط .',callback_data='Add_Cookie')
	Ron = types.InlineKeyboardMarkup(row_width=2);Ron.add(get_list,Add_Cookie)
	sTo.send_message(message.chat.id,text='- اهلاً #هلا بيك عزيزي في بوت صنع ملف ايديات فيس البوت مو الي بس حبيت خليكم تستفيدون منه\n- مبرمج البوت @lIIHII:',reply_markup=Ron)
@sTo.callback_query_handler(func=lambda call:True)
def Call(call):
	if call.data=='get_list':
		Msg = sTo.send_message(call.message.chat.id,text=f'- اهلإ بك عزيزي ارسل الايدي للسحب .')
		sTo.register_next_step_handler(Msg,Get_List)
	elif call.data=='Add_Cookie':
		Msg = sTo.send_message(call.message.chat.id,text=f'- اهلاّ بك عزيزي ارسل الحساب بهذا الشكل id:password .')
		sTo.register_next_step_handler(Msg,Add_Cookies)
pemisah = '|'
q="968"
qq="8280"
qqq="52729"
qqqq="420"
client_id = f"{qqqq}038{q}89{qq}485649{qqq}208"
sim_hini = str(random.randint(2e4,4e4))
trace_id = str(uuid.uuid4())
try:
	android = subprocess.check_output('getprop ro.product.brand', shell=True).decode('utf-8').replace('\n', '').upper()
	model = subprocess.check_output('getprop ro.product.model', shell=True).decode('utf-8').replace('\n', '').upper()
	carrier = '' + subprocess.check_output('getprop gsm.operator.alpha', shell=True).decode('utf-8').split(',')[1].replace('\n', '').upper()
except:
	android = random.choice(['TECNO', "INFINIX", "SAMSUNG"])
	model = random.choice(['LD2', "SM-J009", "SM-J505", "HOT12", "NOTE-11", "A5-PRO"])
	carrier = '' + random.choice(['02', 'Oramge', 'EE', "At&", "MTN", "Cricket"])
def Get_List(message):
	try :
		Token = open('token-{message.from_user.id}.txt', 'r').read()
	except:
		sTo.send_message(message.chat.id,text="عذرًا عزيزي عليك تسجيل الدخول بـ حساب اولاً .")
	try:
					uid=str(message.text)
					headers = {"X-Graphql-Client-Library": "graphservice", "X-Graphql-Request-Purpose": "fetch",
							   "X-Fb-Privacy-Context": "2368177546817046", "X-Fb-Background-State": "1",
							   "X-Fb-Net-Hni": "41001", "X-Fb-Sim-Hni": "41001",
							   "Authorization": "OAuth " + Token + "",
							   "X-Fb-Session-Id": "nid=DQGq3fmNKvVh;tid=135;nc=1;fc=1;bc=0;cid=ef0e330bff1cd312f36aa5f2c69c59a9",
							   "X-Fb-Connection-Type": "WIFI", "X-Fb-Device-Group": "4481", "X-Tigon-Is-Retry": "False",
							   "X-Fb-Rmd": "cached=0;state=URL_ELIGIBLE", "X-Fb-Ta-Logging-Ids": f"graphql:{trace_id}",
							   "X-Fb-Friendly-Name": "SuggestionsFriendListContentQuery",
							   "X-Fb-Request-Analytics-Tags": "graphservice", "Priority": "u=0",
							   "Accept-Encoding": "gzip, deflate", "X-Fb-Http-Engine": "Liger", "X-Fb-Client-Ip": "True",
							   "X-Fb-Server-Cluster": "True", "X-Fb-Connection-Token": "ef0e330bff1cd312f36aa5f2c69c59a9",
							   "Content-Type": "application/x-www-form-urlencoded", "Content-Length": "567"}
					data = {
						'User-Agent': '[FBAN/FB4A;FBAV/396.1.0.28.104;FBBV/429650999;FBDM/{density=2.25,width=720,height=1452};FBLC/en_US;FBRV/437165341;FBCR/' + carrier + ';FBMF/' + android + ' MOBILE LIMITED;FBBD/' + android + ';FBPN/com.facebook.katana;FBDV/' + model + ';FBSV/10;FBOP/1;FBCA/arm64-v8a:;]',
						'client_doc_id': client_id,
						'method': 'post',
						'locale': 'en_US',
						'pretty': 'false',
						'format': 'json',
						'variables': '{"profile_id":' + uid + ',"suggestion_friends_paginating_first":2500}',
						'fb_api_req_friendly_name': 'SuggestionsFriendListContentQuery',
						'fb_api_caller_class': 'graphservice',
						'fb_api_analytics_tags': '["At_Connection","GraphServices"]',
						'client_trace_id': trace_id,
						'server_timestamps': 'true',
						'purpose': 'fetch'
					}
					posted = requests.post("https://graph.facebook.com/graphql", headers=headers, data=data).json()
					try:
						data = posted['data']['user']['friends']['edges']
						#print(data)
					except:
						sTo.send_message(message.chat.id,text="عذرًا عزيزي ، هنالك خطأ ما .")
					if len(data) < 100:
						print('')
					else:
						for edge in data:
							node = edge['node']
							open(f'Id-{message.from_user.id}.txt', 'a', encoding='utf-8').write(node['id'] + '\n')
							idss = len(open(f'Id-{message.from_user.id}.txt','r').readlines())
						
	except KeyError:
					pass
	except requests.exceptions.ConnectionError:
					sTo.send_message(message.chat.id,text="عذرًا عزيزي ، حدث خطأ في الاتصال .")
	sTo.send_document(message.chat.id,open(f'Id-{message.from_user.id}.txt', 'rb'),caption='- تم الستخراج الملف ايديات بل نجاح تكدر تنزله وضيفه [ {} ] .'.format(idss))
	os.system(f'rm -rf Id-{message.from_user.id}.txt')
                ######## - Add Cookies - #######
try:
	import mechanize
	br = mechanize.Browser()
	br.set_handle_robots(False)
	br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
except:
	os.system('pip install mechanize')
def Add_Cookies(message):
		em , ps = str(message.text).split(":")
		os.system('rm -rf token-{message.from_user.id}.txt')
		e="5990"
		ee="655"
		eee="59"
		tok1 = f"2377{e}9{eee}1{ee}"
		ei="0f140aabedfb65"
		ei2="a2263b1"
		tok2 = f"25257C{ei}ac27a739ed1{ei2}"
		us = f'Mozilla/5.0 (Linux; Android {str(random.randint(4,11))}.0; Nexus 5 Build/MRA{str(random.randint(30,60))}N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36 Edg/111.0.{str(random.randint(1600,1661))}.41'
		br.addheaders = [('User-Agent', us)]
		li = "b-ap"
		lo = "od/auth.l"
		op="3f555f98"
		op2 = "d7aa0c"
		op3="58f522efm"
		sig=f"{op}fb61fc{op2}44f{op3}"
		p = br.open(
			'https://'+li+'i.facebook.com/meth'+lo+'ogin?access_token='+tok1+'%'+tok2+'&format=json&sdk_version=1&email=' + em + '&locale=en_US&password=' + ps + '&sdk=ios&generate_session_cookies=1&sig='+sig+'')
		po = json.load(p)
		if 'access_token' in po:
			sTo.send_message(message.chat.id,text="تم اضافة الحساب .")
			open('token-{message.from_user.id}.txt','w').write(po['access_token'])
		else:
			if 'www.facebook.com' in po['error_msg']:
				sTo.send_message(message.chat.id,text='عذرًا عزيزي ولكن الحساب مقفول هوية .')
			else:
				sTo.send_message(message.chat.id,text="الحساب غير صحيح .")
if __name__=="__main__":
	sTo.infinity_polling()
