from flask import Flask, render_template, request

app = Flask(__name__)
app.debug=True

@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':

        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        ##Add details to cloud
        from google.appengine.api import app_identity
        import cloudstorage as gcs

        #GEt default bucket name
        default_bucket_name = app_identity.get_default_gcs_bucket_name()

        ## filename
        filename = '/' + default_bucket_name + '/users.txt'

        ## Read from cloud
        try:
            gcs_file = gcs.open(filename)
            contents = gcs_file.read()
        except:
            gcs_file = gcs.open(filename, 'w', content_type='text/plain')
            contents = ""

        gcs_file.close()

        ##add details
        contents += "\n" + str(username) + "\t" + str(email) + "\t" + str(password)

        ##write back
        gcs_file = gcs.open(filename, 'w', content_type='text/plain')
        gcs_file.write(contents)
        gcs_file.close()

        return "form submitted!"

    return render_template('index.html')

if __name__ == '__main__':
    app.run()
