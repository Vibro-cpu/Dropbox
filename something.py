import dropbox

class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token
    
    def upload_file(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.access_token)
        f = open(file_from,"rb")
        dbx.files_upload(f.read(),file_to)

def main():
    access_token = "sl.BBJvYDxI5pZ0A1l9QYSfL49bj9HxllmDuzAvgr8l5gyEvGoTyU3Sbwv2IAMIhzpjNsppDAsXB1ohmpXMjyCIqoULRDA_KJmRUawPEKa25wukwNwrta0s5dejZL7uLmTvrEKjQK3E5xvx"
    transfer_data = TransferData(access_token)
    file_from = input("Enter File Name to Transfer to Dropbox : ")
    file_to = input("Enter Full Path to Upload to Dropbox : ")
    transfer_data.upload_file(file_from, file_to)
    print("File Has Been Moved")

main()