from hashlib import md5 as H
import requests as r
import azure.functions as func
import json
def main(req: func.HttpRequest) -> func.HttpResponse:
    
        try:
            req_body = req.get_json()
            env = (req_body.get('env')) or (req.params.get('env'))
            tcp_id=req_body.get('tcpId')
            session_id=req_body.get('sessionId')
        except ValueError:
            pass
        if env and tcp_id and session_id:
            tcpid_updated=  tcp_id+"_"+env
            sessionId_updated=session_id+"_"+env
            req_body.update({"tcpId":tcpid_updated })
            sessionid_hash=H(tcpid_updated.encode())
            sessionid_hash=sessionid_hash.hexdigest()
            req_body.update({"sessionId": sessionId_updated})
            #req_body['key']= ' World'
            
            url="https://jsonplaceholder.typicode.com/todos"
            x= r.post(url,json=req_body)
            c=type(req_body)
           # req_body.add(2, 'forGeeks')
           
            return func.HttpResponse(f" Target_Response : {x.status_code} {c} || Target_Reason : {x.reason}\n\n {x.text}")
           # return json.dumps( x)
        else:
         return func.HttpResponse(
              status_code=400
        )


   
       
        
   

