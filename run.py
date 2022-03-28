import connexion

app = connexion.App(__name__, specification_dir='./')
app.add_api('../interface/swagger_admin.yml')
app.run(host='0.0.0.0', port=5000, debug=False)