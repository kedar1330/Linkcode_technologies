class payment_gateway:
    def payment_process(self,obj):
        print("payment process started")
        if hasattr(obj,"pay"):
            obj.pay()
        else:
            print("method not found")
        print("Payment finally done")