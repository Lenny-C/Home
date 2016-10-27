class JSON:
    def __init__(self, success=True, code=200, errMsg = None, data=None):
        self.success = success
        self.code = code
        self.errMsg = errMsg
        self.data = data
    def __repr__(self):  
        return '<JSON(%s,%s,%s,%s)>' % (self.success, self.code, self.errMsg, self.data) 
    
def convert_to_builtin_type(obj):  
    print 'default(', repr(obj), ')'  
    # Convert objects to a dictionary of their representation  
#     d = { '__class__':obj.__class__.__name__,  
#           '__module__':obj.__module__,  
#         }  
    d = obj.__dict__
#     d.update(obj.__dict__)  
    return d  