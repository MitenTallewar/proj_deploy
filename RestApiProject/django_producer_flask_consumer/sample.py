import requests
STUDENT_OP_BASE_URI = 'http://localhost:8000/api/v1/student/'

class candidate:

    def __init__(self,id,name,age,address,active=None):
        self.candId=id
        self.candName=name
        self.candAge=age

        self.candAddress =address

    def __str__(self):
        return f'''
        Id:{self.candId}
        name:{self.candName}
        Age:{self.candAge}
        Address:{self.candAddress}
        
        '''
        
    def __repr__(self):
        return str(self)



def process_response(res):
    res =res.json()  #---this can be serialize data from Django and convert into the json format
    if type(res)==list:#---convert this data into the flask format i.e list
        candidates=[]
        for stud in res:
            candidates.append(candidate(**stud))
        return candidates

    else:
        return candidate(**res)

def get_all_student(): #--get all the student data into the flask format and get all the data fetch
    response= requests.get(STUDENT_OP_BASE_URI)#get all the data from STUDENT_OP_BASE_URI = 'http://localhost:8000/api/v1/student/'
    return process_response(response)


def get_single_student(stid):
    if stid>0:  #--to check the data is prasent or not
        response=requests.get(STUDENT_OP_BASE_URI+str(stid))##-- fetch the single value by using stid
        if response.json().get('detail'):
            return response.json().get('detail') # this return the value od single json()  formated data
        return process_response(response)# to send a response to the  method

    else:
        return 'Invalid id'

def delete(stid):
    if stid>0:
        response= requests.delete(STUDENT_OP_BASE_URI+str(stid))

        if response.status_code!=204:   #---if status code is 204 means student is not prasent
            print("no student with id...!")

        else:
            print('student record remover...',response.status_code)

    else:
        print('invalid id')


def update_student(cand):
    stud_dict= {

        "id": cand.candId,
        "name": cand.candName,
        "age": cand.candAge,
        "address": cand.candAdress,
    }

    response = requests.put(STUDENT_OP_BASE_URI+str(cand.candId)+"/",josn=stud_dict)#---put method is use for the updation purpose
    print(response.status_code)

def create_student(cand):
    stud_dict= {
        "id": cand.candId,
        "name": cand.candName,
        "age": cand.candAge,
        "address": cand.candAdress,
            }
    response= requests.post(STUDENT_OP_BASE_URI,json=stud_dict)#--post method is use for data creation joson data get and convert to the other format
    print(response.status_code)

if __name__ == '__main__':
    candidate=get_all_student()
    print(candidate)
    #can =candidate(id=2,name='ttttt',age=30,fees=11111,address='pune',active='y')
    #update_student(can)