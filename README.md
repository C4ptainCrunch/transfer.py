# transfer.py

It's just like [https://transfer.sh/](https://transfer.sh/) but you can self-host it. And it's Python3.

You only have to `curl --upload-file ./hello.txt http://your.domain.pink/upload/SECRET_KEY/hello.txt` and you get back a link to your file `http://your.domain.pink/f/t0k3n/hello.txt`

# Run

    virtualenv ve
    source ve/bin/activate
    nano local_config.py # inspire yourself from config.py
    python app.py

Configure your web server to reverse-proxy `http://localhost:5000` (of the port you have chosen) and to serve `MEDIA_DIR` as `/f/`. That's all !

Example for nginx :

    server {
        server_name your.domain.pink;

        location / {
            proxy_pass        http://localhost:5000;
            proxy_set_header   Host              $host;
            proxy_set_header   X-Real-IP         $remote_addr;
            proxy_set_header   X-Forwarded-For   $proxy_add_x_forwarded_for;
            proxy_set_header   X-Forwarded-Proto $scheme;
        }

        location /f {
            alias /path/to/my/media_dir; # by default it's /path/where/you/cloned/transfer.py/media
        }
    }


# License

Why not [MIT](https://opensource.org/licenses/MIT) ?


# Note

If you like bash, you can also use @titouanc's 2 SLOC version : https://github.com/titouanc/homefiles/blob/master/bin/imgtitou
