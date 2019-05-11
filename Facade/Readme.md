# Descriptions.
A Facade Pattern just simply is pattern to hide the complex of subsystem and provide for client a simple inteface to use.
They don't limit client to access to subsystem. With this implementing we can make loose couple for modules.

In this example we will create an example to build a Weather App.

Logic Flow:
1. Customer give the city and country information to get the weather information. If it's stored we just return,
if not go to step 2.
2. Depend on city and country information, client need to call api to get the information, Using parser to parse those 
informations, convert the temp, build Weather object, store the final result to caching layer and return result
to client.
