
#  Backup Script config file #
----------------------------------------------------------


Python Script for backup network devices . The customer needed a script to make a diary backup of the config files of their networks devices like router, switches and access point which it should be fit to their heterogeneous collection on brands.

The script run like automatic task in win server 2012. It cnnect with device using ssh or http protocol. Once it connected, executed the sequence of commands in ssh connection and get requests in http connection until download the config file from device.

If you want to use it, you must replace the variables. 

Some requirements:

* Developed at windows platform

* Python version: 2.7