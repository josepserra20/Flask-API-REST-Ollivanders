from repository.query import query

class Services():

    
    def getStock():
        return query.get_stock()
    
    def getName(name):
        return query.getStockByName(name)

            