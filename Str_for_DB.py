class Str_for_DB:
    def srt_for_banks(self,banks):
        txt=''
        for b_key, b_value in banks.items():
            if b_value==True:
                txt+=b_key+" "
        return txt
    def srt_for_curr(self,curr):
        txt=''
        for b_key, b_value in curr.items():
            if b_value==True:
                txt+=b_key+" "
        return txt