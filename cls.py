
class Dog:
  def __init__(self, name, breed, owner):
    self.name = name
    self.breed = breed
    self.owner = owner

  def bark(self):
    print("Woof")

class Owner:
  def __init__(self, name, address):
    self.name = name
    self.address = address

owner1 = Owner('Alice', '123 Main St')
dog1 = Dog('Buddy', 'Golden Retriever', owner1)
dog2 = Dog('Joe', 'German Shepherd', Owner('John', '10 Downing Street'))
print(dog2.owner.name)


#print(help(Developer))
dev1 = Developer("john", "doe", 50000, "Python")
print(dev1.pay)
dev1.apply_raise()
print(dev1.pay)


#Personalisation 
#user.username
class User:
  def __init__(self, username, email):
    self.username = username
    self.email = email

  def say_hello(self, user):
    print(f"Hello, {user.username}!")

user1 = User("John Doe", "johnd@company.com")
user1.say_hello(user1)


from datetime import datetime
#self._email.  making it private     protected
#self.__password. impossible to access the variable    private 
class User:
  def __init__(self, name, email, password):
    self.name = name
    self._email = email
    self.__password = password



  def get_email(self):
    print(f"Email accessed at {datetime.now()}")
    return self._email

  @property   #Python way for a gettter
  def email(self):
    print(f"Email accesed at {datetime.now()}")
    return self._email
  
  def set_email(self, new_email):
    if "@" in new_email:
      self._email = new_email
    else:
      raise TypeError("Invalid Error")
    
  @email.setter  #python way of a setter
  def email(self, new_email):
    if "@" in new_email:
      self._email = new_email



  def get_password(self):
    return self.__password
  
user4 = User("Jane", "jane@example.com", "pass123")
print(user4.get_password())
user4.set_email("janedoe@company.com")
print(user4.get_email())
print(user4.email) #python way for a getter
