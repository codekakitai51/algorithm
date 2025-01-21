class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        res = []
        products.sort()
        prefix = ""

        for cha in searchWord:
            prefix += cha
            suggested = []
            lenS = 0

            for product in products:
                if product.startswith(prefix):
                    suggested.append(product)
                    lenS += 1
                if lenS == 3:
                    break
            
            res.append(suggested)
        
        return res