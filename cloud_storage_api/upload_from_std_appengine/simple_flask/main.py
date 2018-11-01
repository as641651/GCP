from flask import Flask


app = Flask(__name__)
app.debug=True

@app.route('/')
def hello():
   from google.appengine.api import app_identity
   import cloudstorage as gcs

   #GEt default bucket name
   default_bucket_name = app_identity.get_default_gcs_bucket_name()

   out = "Default bucket : " + default_bucket_name

   ## Write to cloud
   filename = '/' + default_bucket_name + '/new.txt'
   gcs_file = gcs.open(filename, 'w', content_type='text/plain')
   gcs_file.write('abcde\n')
   gcs_file.write('Hello!' + '\n')
   gcs_file.close()

   ## Read from cloud
   gcs_file = gcs.open(filename)
   contents = gcs_file.read()
   gcs_file.close()

   out += "<p>Contents :</p>"
   out += "<p>" + contents + "</p>"

   #files CANNOT be appended as the objects are immutable. to append you have to read, modify contents and overwrite 

   #List items 
   blist = gcs.listbucket('/' + default_bucket_name)
   print(list(blist))

   return out 



if __name__ == '__main__':
    app.run()
