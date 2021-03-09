d={}
class employee:
	def sal(self,name,addr,pan,basic,tds=0,ded=0):
		self.name=name
		self.addr=adress
		self.pan=panno
		self.basic=basic
		self.tds=tds
		self.ded=ded
		self.hra=int(1.15*self.basic)
		self.gross=self.basic+self.hra
		netsal=self.basic+self.hra-(self.tds+self.ded)
		return netsal

	def accept(self):
		name=input("Enter the name :")
		addr=input("Enter adress address")
		pan=input("Enter the pan no")
		basic=int(input("Enter the basic Salery"))
		tds=int(input("Enter employ tds"))
		ded=int(input("Enter employ Deduction"))
		self.netsal=self.sal(name,address,pan,basic,tds,ded)

	def display(self):
		print(self.name)
		print(self.address)
		print(self.pan)
		print(self.basic)
		print(self.netsal)

	def search(self,name):
		for k,v in d.items():
			print(k)
			print(v)
		if k == name:
			print(v.__dict__)
while True:
	print("*"*50)
	print("1.enter employee detauills")
	print("2.display employ detsaills")
	print("3.enter employee update dictneary")
	print("4.enter employee search employ")
	print("5.enter employee exit")
	print("*"*50)
	ch=int(input("enter a choice:"))
	print("*"*50)
	if ch==1:
		e=employee()
		print(id(e))
		e.accept()
	elif ch==2:
		print("display the employee details")
		e.display()
	elif ch==3:
		d.update({e.name:e})
		print(d)
	elif ch==4:
		e.search(input("enter the name:"))
	elif ch==5:
		break
	else:
		print("please ente valid choice")
	print("*"*50)


