# Python-Networking-Project

This project has the steps for setting up a mailing client by sending email through the STMP server with attachments. The following are Networking Basics and Security Information regarding this project. This information is also in the txt.files in this project:

 Networking Basics
 
Payload- 

Payload is the essential data that is being carried with a packet
It is used to distinguish between the 'interesting' information in a chunk of data or similar.

Header-

Headers are supplemental information located at the beginning of frames 
or packets. Commonly, headers are structured following a protocol. 
So, in a given position of a header, predetermined data must be available.
With TCP, the IPv6 header has a minimum of 20 bytes and a maximum of 60 bytes


Overhead- 
Additional data that you need in order to send your payload.

SMTP- 
The Simple Mail Transfer Protocol is an Internet standard communication protocol for electronic 
mail transmission.

Port Numbers-
way to identify a specific process to which an internet or other network message 
is to be forwarded when it arrives at a server. Port numbers is at the Transport
Layer (OSI Model) or the Host-to-Host layer (TCP/IP) layer.


Transport Layer-
The second layer in the TCP/IP model and the fourth layer in the OSI model.
 It is an end-to-end layer used to deliver messages to a host. 
 It is termed an end-to-end layer.

 Port 587-
 Outgoing SMTP Mail port (TLS/Start TLS Port) - used by various mail servers for relaying outgoing mail 
 as a modern alternative to port 25. Gmail, Apple MobileMe Mail, Yahoo SMTP server, etc. all use 
 this port.

 TLS-
 Transport Layer Security (TLS) is a cryptographic protocol designed to provide communications security over a computer network. 
 The protocol is widely used in applications such as email, instant messaging, and voice over IP, but its use in securing HTTPS 
 remains the most publicly visible.

 Security Info
 The following is needed for the sending process to work:

-Have an existing account for sending emails (recommended to make test email)
-Must have 2-Step Authenticator activated on gmail account 
-Must enable an App Password
-For security reasons when presenting, make sure to add password as a txt.file so it is not exposed
-DO NOT BUT ON GITHUB WITH PASSWORD ON THE TXT.FILE, REPLACE IT WITH ADD APP PASSWORD so it is not publically exposed

For projects assigning actual users, it is recommended to have OAuth 2 and import the OAuth2lib
