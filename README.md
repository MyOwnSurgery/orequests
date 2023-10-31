# ORequests
## A more object-oriented approach to HTTP requests. Following Elegant Objects ideas [link to author`s website](https://www.yegor256.com/)


## Examples:
### 1) Send a request
#### 1.1) Simple GET request
```python
Response("www.example.com").value()
```
#### 1.2) A more configurable GET request
##### Create a request using StrInput class or any of Request classes
```python
req = StrInput(
    "\r\n".join(
        ["GET / HTTP/1.1", "Host: www.example.com", "Connection: Close\r\n\r\n"]
    )
)
```
##### or
```python
req = Request(
    st_line="GET / HTTP/1.1",
    headers={"Connection": "Close", "Host": "www.example.com"},
)
```
##### or
```python
req = GetRequest(
    uri="/",
    headers={"Connection": "Close", "Host": "www.example.com"},
)
```
##### then send a request using Wire
```python
HtWire("www.example.com").send(req)
```
#### 1.3) POST Request with payload
```python
HtWire("www.example.com").send(
    PostRequest(
        uri="/",
        headers={
            "Connection": "Close",
            "Host": "www.example.com",
        },
        body=JsonBody(input_={"msg": "Hello, World!"}),
    )
)
```
### 2) Parse a response
#### Once you got a response
```python
response = HtWire("www.example.com").send(
    StrInput(
        "\r\n".join(
            ["GET / HTTP/1.1", "Host: www.example.com", "Connection: Close\r\n\r\n"]
        )
    )
)
response
# HTTP/1.1 200 OK\r\nContent-Type: application/json\r\n\r\n{"msg": "Hello, World!"}
```
#### You can get the head of the response by
```python
head = Head(input_=response)
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
body = Body(input_=response)
body.value()
# {"msg": "Hello, World!"} (str)
body = JsonBody(input_=response)
body.value()
# {"msg": "Hello, World!"} (dict)
```
### 3) Batch requests
#### You can send multiple requests using one tcp connection
```python
result = HtWire("www.example.com").send(
    RequestsBatch(
        requests=[
            Request(
                st_line="GET /point1 HTTP/1.1",
                headers={"Connection": "Keep-Alive", "Host": "www.example.com"},
            ),
            Request(
                st_line="GET /point2 HTTP/1.1",
                headers={"Connection": "Keep-Alive", "Host": "www.example.com"},
            ),
            Request(
                st_line="GET /point3 HTTP/1.1",
                headers={"Connection": "Close", "Host": "www.example.com"},
            ),
        ]
    )
)
```
#### Then get individual responses by using the Responses class
```python
responses = Responses(input_=result)
for response in responses.value():
    response
# HTTP/1.1 200 OK\r\nContent-Type: application/json\r\n\r\n{"msg": "Hello from point1"}
# HTTP/1.1 200 OK\r\nContent-Type: application/json\r\n\r\n{"msg": "Hello from point2"}
# HTTP/1.1 200 OK\r\nContent-Type: application/json\r\n\r\n{"msg": "Hello from point3"}
```
### 4) Combining wires by using the power of decorators
#### 4.1) Add a timeout to your request by just passing your original wire to HtTimedWire
```python
HtTimedWire(HtWire("www.example.com"), timeout=3.0).send(
    StrInput(
        "\r\n".join(
            ["GET / HTTP/1.1", "Host: www.example.com", "Connection: Close\r\n\r\n"]
        )
    )
)
```
#### 4.2) Add an auto redirection the similar way
```python
AutoRedirect(HtWire("www.example.com")).send(
    StrInput(
        "\r\n".join(
            ["GET / HTTP/1.1", "Host: www.example.com", "Connection: Close\r\n\r\n"]
        )
    )
)
```
#### 4.3) Add a retry mechanism by using retry strategies and backoffs
```python
HtRetryWire(
    HtWire("www.example.com"),
    strategy=StdRetry(
        total=3, retry_statuses=[500], backoff=ConstantBackoff(value=1.0)
    ),
).send(
    StrInput(
        "\r\n".join(
            ["GET / HTTP/1.1", "Host: www.example.com", "Connection: Close\r\n\r\n"]
        )
    )
)
```


## The package is at lazy development stage :)