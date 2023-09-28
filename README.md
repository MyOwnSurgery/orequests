# ORequests
## A more object-oriented approach to HTTP requests

## Examples:
### 1) Send a request
#### 1.1) GET request
```python
HtWire(your_url).send("\r\n".join([
    "GET / HTTP/1.1", 
    f"Host: {your_host}",
    "Connection: Close\r\n\r\n"]))
```
### 2) PUT Request with payload
```python
msg = '{"msg": "Hello"}'
HtWire(your_url).send("\r\n".join([
    "PUT / HTTP/1.1",
    f"Host: {your_host}",
    "Content-Type: application/json",
    f"Content-Length: {len(msg)}",
    "Connection: Close", f'\r\n{msg}\r\n\r\n']))
```
### 2) Parse a response
#### Once you got a response
```python
response = HtWire(your_url).send("\r\n".join([
    "GET / HTTP/1.1", f"Host: {your_host}",
    "Connection: Close\r\n\r\n"]))
response
# HTTP/1.1 200 OK\r\nContent-Type: application/json\r\n\r\n{"msg": "HELLO"}
```
#### You can get the head of the response by
```python
head = Head(response)
head.value()
# HTTP/1.1 200 OK\r\nContent-Type: application/json
ct_header = Header(head, 'Content-Type')
ct_header.value()
# application/json
headers = Headers(head)
headers.value()
# {'Content-Type': 'application/json'}
```
#### Or get the body
```python
body = Body(response)
body.value()
# {"msg": "HELLO"}
```
### 3) Combining wires by using the power of decorators
#### Add a timeout to your request by just passing your original wire to HtTimedWire
```python
HtTimedWire(wire, timeout=3.0).send("\r\n".join([
    "GET / HTTP/1.1", "Host: www.google.com",
    "Connection: Close\r\n\r\n"
]))
```
#### Add a retry mechanism to your request the similar way
```python
HtRetryWire(wire, attempts=3, retry_statuses=[500]).send("\r\n".join([
    "GET / HTTP/1.1", "Host: www.google.com",
    "Connection: Close\r\n\r\n"
]))
```
#### Add an auto redirection
```python
AutoRedirect(wire).send("\r\n".join([
    "GET / HTTP/1.1", "Host: www.google.com",
    "Connection: Close\r\n\r\n"
]))
```

## The package is at lazy development stage :)