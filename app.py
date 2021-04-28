from flask import Flask
from flask_restful import Resource, Api, reqparse, abort, marshal, fields

# Initalize flask
app = Flask(__name__)
api = Api(app)


# Schema For the Book Request JSON
tagFields = {
    "type": fields.String,
    "owner": fields.String,
    "ownerContact": fields.String,
    "cretedDate": fields.String,
    "cretedBy": fields.String,
    "approvedDate": fields.String,
    "approvedBy": fields.String,
    "version": fields.String,
    "currVersion": fields.String,
    "approvedSatus": fields.String,
    "state": fields.String,
    "dependencies": fields.String,
    "effective": fields.String,
    "field_name": fields.String,
    "revenue": fields.String,
    "alias": fields.String,
    "operation": fields.String
}

# A List of Dicts to store all of the books
tags = [{
    "pk": "Tag01",
    "pk_data": [ {
      "sk": "1A",
      "sk_data": {
        "type": "calc",
            "owner": "auto",
            "ownerContact": "auto@capitalone.com",
            "cretedDate": "2021/03/15 12:00:00",
            "createdBy": "tfe641",
            "approvedDate": "2021/03/16 12:00:00",
            "approvedBy": "dfx213",
            "version": "v0",
            "currVersion": "v1",
            "approvedStatus": "pending",
            "state": "active",
            "dependencies": [],
            "effective": "2021/03/16",
            "fields": [{
                "field_name": "",
                "revenue": "",
                "alias": "A"
            },
            {
                "field_name": "",
                "revenue": "",
                "alias": "B"
            }],
            "operation": "A-B"
      }
    },
    {
      "sk": "TAG#AUTO#63q12ah#v1",
      "sk_data": {
            "type": "calc",
            "owner": "auto",
            "ownerContact": "auto@capitalone.com",
            "cretedDate": "2021/03/15 12:00:00",
            "createdBy": "tfe6411",
            "approvedDate": "2021/03/16 12:00:00",
            "approvedBy": "dfx213",
            "version": "v1",
            "approvedStatus": "approved",
            "state": "pending",
            "dependencies": [],
            "effective": "2021/03/16",
            "fields": [{
                "field_name": "",
                "revenue": "",
                "alias": "A"
            },
            {
                "field_name": "",
                "revenue": "",
                "alias": "B"
            }],
            "operation": "A-B"
      }
    }
    ]
  },

  {
    "pk": "Tag02",
    "pk_data": [ {
      "sk": "TAG#AUTO#63q12ah#v2",
      "sk_data": {
        "type": "calc",
            "owner": "auto",
            "ownerContact": "auto@capitalone.com",
            "cretedDate": "2021/03/15 12:00:00",
            "createdBy": "tfe641",
            "approvedDate": "2021/03/16 12:00:00",
            "approvedBy": "dfx213",
            "version": "v0",
            "currVersion": "v1",
            "approvedStatus": "approved",
            "state": "active",
            "dependencies": [],
            "effective": "2021/03/16 12:00:00",
            "targetDataset": "REFERENCE_DID",
            "joinFields": "acctID",
            "targetFields": "DID"
      }
    }]
  }
  ]
  


PORT = 5000
HOST = '0.0.0.0'

# GET Method calls

# 0.0.0.0:5000/getActiveTag

class GetActiveTag(Resource):
    def __init__(self):
        pass

    def get(self):
        print("inside taglist get")
        value = {"sk":[]}

        for j in range(len(tags)):
            for i in range(len(tags[j]['pk_data'])):
                if tags[j]['pk_data'][i]['sk_data']['state'] == "active":
                    getTags = tags[j]['pk_data'][i]['sk']
                    print("****",getTags)
                    value['sk'].append(getTags)
        print(value)
        return value

# 0.0.0.0:5000/getTagVersionHistory/1A - use only this url for this api 

class GetTagVersionHistory(Resource):
    def __init__(self):
        pass

    def get(self, tag):
        print("inside taglist get")
        value = {}
        print(">>", tag)

        for j in range(len(tags)):
            for i in range(len(tags[j]['pk_data'])):
                print("inside inner for", tags[j]['pk_data'][i]['sk'])
                if tags[j]['pk_data'][i]['sk'] == tag:
                    print("inside if")
                    getVersion = {"getVersion":tags[j]['pk_data'][i]['sk_data']['version']}
                    print(getVersion)
                    value.update(getVersion)
        return value

# 0.0.0.0:5000/getTagBySpecificUser/tfe641 - you can change createdby value in json and calls api

class GetTagBySpecificUser(Resource):
    def __init__(self):
        pass

    def get(self, createdBy):
        print("inside taglist get")
        value = {"tagBySpecificUser":[]}

        for j in range(len(tags)):
            for i in range(len(tags[j]['pk_data'])):
                if tags[j]['pk_data'][i]['sk_data']['createdBy'] == createdBy:
                    getTags = tags[j]['pk_data'][i]['sk']
                    value['tagBySpecificUser'].append(getTags)
        return value

# 0.0.0.0:5000/getTagByApprovalStatus/approved - call api using this url

class GetTagByApprovalStatus(Resource):
    def __init__(self):
        pass

    def get(self, approvedStatus):
        print("inside taglist get")
        value = {"approvedStatus": []}

        for j in range(len(tags)):
            for i in range(len(tags[j]['pk_data'])):
                if tags[j]['pk_data'][i]['sk_data']['approvedStatus'] == approvedStatus:
                    getTags = tags[j]['pk_data'][i]['sk']
                    value['approvedStatus'].append(getTags)
        return value

# api.add_resource(TagList, "/tags")
api.add_resource(GetActiveTag, "/getActiveTag")
api.add_resource(GetTagVersionHistory, "/getTagVersionHistory/<string:tag>")
api.add_resource(GetTagBySpecificUser, "/getTagBySpecificUser/<string:createdBy>")
api.add_resource(GetTagByApprovalStatus, "/getTagByApprovalStatus/<string:approvedStatus>")


if __name__ == "__main__":
	print("server running in port %s" %(PORT))
	app.run(host=HOST, port=PORT)