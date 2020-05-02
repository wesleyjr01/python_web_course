# What are Metaclasses in Python ?
* What "abstract" means in Python, is, this thing what we are using that is abstract, exists but isn't defined yet.
* We have a Model Class, but this model class isn't an actual thing in our proggram, it is the definition of what a thing should be, or should contain.
* The child classes that inherit the Abstract Class will have to override the abstract methods defined in the Abstract Class. This is the perfec way of enforcing the definition of methods in child classes.
* Not all methods defined inside a abstract class must be @abstractmethods.