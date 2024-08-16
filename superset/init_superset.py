from superset.app import create_app
from superset import security_manager, db
from flask_migrate import upgrade as db_upgrade
from flask_appbuilder.security.sqla.models import User
import os

superset_username=os.getenv('SUPERSET_USER_NAME')
superset_password=os.getenv('SUPERSET_USER_PASSWOR')

def init_superset():
    app = create_app()  # Créez l'application Flask
    with app.app_context():
        # Vérifier si l'utilisateur superset_username existe déjà
        admin_user = db.session.query(User).filter_by(username=f'{superset_username}').first()
        if not admin_user:
            # Créer l'utilisateur administrateur
            security_manager.add_user(
                first_name='Admin',
                last_name='User',
                email='admin@admin.com',
                role=security_manager.find_role('Admin'),
                username=f'{superset_username}',
                password=f'{superset_password}'
            )
            print(f"Admin, user: {superset_username}, created")

        # Exécuter les migrations de la base de données
        db_upgrade()

        # Synchroniser les rôles et permissions par défaut
        security_manager.sync_role_definitions()
        print("Roles and permissions synced")

if __name__ == "__main__":
    init_superset()
