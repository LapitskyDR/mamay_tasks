import connexion
from entity.db_creator import create_db
import os
app = connexion.App(__name__, specification_dir='./')
app.add_api('./interface/swagger_admin.yml')
if os.environ['DB_CREATE'] == 'True':
    create_db()
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
