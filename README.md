IoT Gateway

This is WIP demo project to build a simple python  IoT gateway able to run a standard platform such as Raspberry Pi or a small PC. 
The gateway will aggregate information that other local programs will provide as files using JSON syntax. The gateway will aggreagte the information from those files and communicate back to (in teh current version) an Azure Event Hub.
This approach alows modular development of new programs that monitor new sensors or do any other relevant edge processing. The only requiremtn is for those programs to provide tjheir telemetry in JSON  forrmat and dump it in predefined location.