class Singleton(object):
    def __new__(self):
        if not hasattr(self, 'instance'):
            self.instance = super(Singleton, self).__new__(self)
        return self.instance


singleton = Singleton()
new_singleton = Singleton()

print(singleton is new_singleton)

singleton.singl_variable = "Singleton Variable"
print(new_singleton.singl_variable)

if __name__ == '__main__':
    pass
