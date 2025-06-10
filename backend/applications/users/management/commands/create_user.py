from applications.users.models import User
User.objects.create_user(username="pepe@email.com", password="Putthabo_1")
user = User.objects.get(username="pepe@email.com")
print(user.is_active)