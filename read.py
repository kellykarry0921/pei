import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

#doc_ref = db.document("靜宜資管/tcyang")
#doc = doc_ref.get()
#result = doc.to_dict()
#print("文件內容為：{}".format(result))
#print("教師姓名："+result.get("name"))
#print("教師郵件：" + result["mail"])

collection_ref = db.collection("靜宜資管")
#docs = collection_ref.where("mail","==", "tcyang@pu.edu.tw").get()
#docs = collection_ref.order_by("lab").limit(3).get()
docs = collection_ref.order_by("mail", direction=firestore.Query.DESCENDING).limit(3).get()
for doc in docs:
    print("文件內容：{}".format(doc.to_dict()))
