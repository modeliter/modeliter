class Model:
    def fit(self, data):
        pass

    def predict(self, data):
        pass

class ModelPackage:
    def __init__(self, model):
        self.model = model

    def generate(self):
        pass
    

class ModelPackagePublisher:
    def __init__(self, index_url):
        self.index_url = index_url

    def publish(self, model_package):
        pass

m = Model()
m.fit(1)
mp = ModelPackage(m)
mp.generate()
p = ModelPackagePublisher("http://localhost:8080")
p.publish(mp)
