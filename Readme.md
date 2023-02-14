DNS-over-TLS Proxy


Listens for both TCP and UDP messages on native configured port. Converts plain UDP packets to TCP by prefixing message with a two bytes length field which the incoming UDP message have.

By default establishes SSL connection with Cloudflare DNS (1.1.1.1) over 853 port. Python function 'create_default_context' from build-in ssl library was used to establish connection with nameserver.

Default buffer size is set to 1024

What are the security concerns for this kind of service?
the process running on the server should be limited with the inbound/outbound access ,this leads to less expose.

Considering a microservice architecture; how would you see this the dns to dns-over-tls proxy used?
It can be integrated with the other client applicatio by runnig this alog with the other services in the node.

What other improvements do you think would be interesting to add to the project?

for now its just a script , there is room for lot of improvements, this is completely new concept but challenging to me need to analysis more for the improvement part.
Error handling.
A health check endpoint.

How to run it.
a Dockerfile is provided. Build it running
```
docker build . -t dotproxy:1
```
After the build just run the image with:
```
docker run -p 127.0.0.2:53:8853 -p 127.0.0.2:53:9953/udp dotproxy:1
```

NOTE:before building configure the HOST and PORT ,if the
