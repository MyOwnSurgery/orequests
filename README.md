# ORequests
## A more object-oriented approach to HTTP requests

## Examples:
### 1) Send a request
#### 1.1) Simple GET request
```python
Response("www.example.com").send()
```
#### 1.2) A more configurable GET request
```python
HtWire("www.example.com").send(
    "\r\n".join(
        ["GET / HTTP/1.1", "Host: www.example.com", "Connection: Close\r\n\r\n"]
    )
)
```
#### 1.3) POST Request with payload
```python
msg = '{"msg": "Hello"}'
HtWire("www.example.com").send(
    "\r\n".join(
        [
            "POST / HTTP/1.1",
            "Host: www.example.com",
            "Content-Type: application/json",
            f"Content-Length: {len(msg)}",
            "Connection: Close",
            f"\r\n{msg}\r\n\r\n",
        ]
    )
)
```
### 2) Parse a response
#### Once you got a response
```python
response = HtWire("www.example.com").send(
    "\r\n".join(
        ["GET / HTTP/1.1", "Host: www.example.com", "Connection: Close\r\n\r\n"]
    )
)
response
# HTTP/1.1 200 OK\r\nContent-Type: application/json\r\n\r\n{"msg": "HELLO"}
```
#### You can get the head of the response by
```python
head = Head(response=response)
head.value()
# HTTP/1.1 200 OK\r\nContent-Type: application/json
ct_header = Header(head=head, name='Content-Type')
ct_header.value()
# application/json
headers = Headers(head=head)
headers.value()
# {'Content-Type': 'application/json'}
```
#### Or get the body by
```python
body = Body(response=response)
body.value()
# {"msg": "HELLO"}
```
### 3) Combining wires by using the power of decorators
#### 3.1) Add a timeout to your request by just passing your original wire to HtTimedWire
```python
HtTimedWire(HtWire("www.example.com"), timeout=3.0).send(
    "\r\n".join(
        ["GET / HTTP/1.1", "Host: www.example.com", "Connection: Close\r\n\r\n"]
    )
)
```
#### 3.2) Add an auto redirection the similar way
```python
AutoRedirect(HtWire("www.example.com")).send(
    "\r\n".join(
        ["GET / HTTP/1.1", "Host: www.example.com", "Connection: Close\r\n\r\n"]
    )
)
```
#### 3.3) Add a retry mechanism by using retry strategies and backoffs
```python
HtRetryWire(
    HtWire("www.example.com"),
    strategy=StdRetry(
        total=3, retry_statuses=[500], backoff=ConstantBackoff(value=1.0)
    ),
).send(
    "\r\n".join(
        ["GET / HTTP/1.1", "Host: www.example.com", "Connection: Close\r\n\r\n"]
    )
)
```


## The package is at lazy development stage :)