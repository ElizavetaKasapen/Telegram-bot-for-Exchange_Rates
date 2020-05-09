class Str_for_DB:
    def srt_for_banks(self,banks):
        for b_key, b_value in banks.items():
            if b_value==True:
                txt+="\n"+b_key+"\n"
        return txt
    def srt_for_curr(self,curr):
        for b_key, b_value in curr.items():
            if b_value==True:
                txt+="\n"+b_key+"\n"
        return txt