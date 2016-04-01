from flask import Flask, request
from werkzeug import secure_filename
import string
import random
import os

import config

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = config.MEDIA_DIR

MISS = set("oO0iIlL")
POOL = list(set(string.ascii_uppercase + string.ascii_lowercase + string.digits) - MISS)


@app.route('/upload/%s/<path:path>' % config.SECRET, methods=['PUT'])
def upload_file(path):
    data = request.data
    if data:
        filename = secure_filename(path)
        seed = ''.join(random.choice(POOL) for _ in range(config.SEED_LEN))
        dirname = os.path.join(app.config['UPLOAD_FOLDER'], seed)

        os.mkdir(dirname)
        with open(os.path.join(dirname, filename), 'wb') as fd:
            fd.write(data)

        return "{}/f/{}/{}\n".format(config.ROOT, seed, filename)
    else:
        return "No file found"


if __name__ == '__main__':
    app.run(debug=config.DEBUG)
