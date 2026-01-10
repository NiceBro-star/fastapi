import os, json

class Read_Response:
    def __init__(self, path):
        self.path = path

    def __call__(self):
        return Read_Response.read_response(self.path)

    @staticmethod
    def read_response(path: str):
        cur_dir = os.path.dirname(__file__)
        file_path = os.path.join(cur_dir, path)

        if not os.path.exists(file_path):
            print("The file doesn't exist.")
        
        with open(file_path, mode="r", encoding="utf-8") as f:
            return json.loads(f.read())
    