# Requirements
`pip3 install flask piexif uwsgi`

# Debugging
### http (runs a http web server on http://0.0.0.0:9900):

```shell
sh ./debug.sh
```



# Running

### http (runs a http web server on http://0.0.0.0:9900):

```shell
sh ./uwsgi-http.sh
```

nginx:
```
    proxy_pass http://0.0.0.0:9900;
```


### socket (runs as an uwsgi socket on 0.0.0.0:9900):

```shell
sh ./uwsgi-socket.sh
```

nginx:
```
    include    uwsgi_params;
    uwsgi_pass 0.0.0.0:9900;
```