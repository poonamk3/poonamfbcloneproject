import pytest
lists=[]

data = {
	"message":[
	{
         "channel": "channel",
         "to": "56465144",
         "from": "froms"
     }
	]
}
data2 ={
	"message":[
	{
         "from": "froms"
     }
	]
	
}

def for_one_messages_wo_encryption():
	data2['message'][0]['name']="poonam"
	lists.append(data2['message'])
	data2['messages'] = lists
	return data2
data3=for_one_messages_wo_encryption()

def for_one():
	data2['message'][0]['last']="dipesh"
	lists.append(data2['message'])
	data2['messages'] = lists
	return data2
data4=for_one()



# data['message'][0]['content'] = "Here is my messages"
# data2['message'][0]['con']="whatsapp"
msg=[data3]
@pytest.mark.parametrize("number",msg)
def test_foo(number):
	# import pdb;pdb.set_trace()
	print(number)
	assert data

# Poonam Dhangar