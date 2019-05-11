#Advantage:
The goal is to move instances creating to subclasses
1. Make code not tied to concrete classes but to interfacrs.It separates interfaces from their implementations.
2. It decouple the code that creates objects from the code that uses them, reducing the complexity of maintenance.
To add a new class, you need to add an additional else-if clause.
