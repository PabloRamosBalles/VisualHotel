Para poder inicializar la aplicación es necesario hacer estos pasos:

!Elegir la rama reserve-logic! (Main esta en render pero los fetch de GET parecen no funcionar, https://vhotel.onrender.com)

Front
1. cd frontend
2. npm install
3. npm run serve

Backend
1. cd backend
2. pip install -r requirements.txt
3. python manage.py runserver 8001
4. Para poder acceder a la pagina de administracion es necesario crear un superuser: python manage.py createsuperuser

pagina de administracion local --> http://localhost:8001/admin
