from pyremote import interest_index_scoring as iis

class GetPyRemote:

    def __init__(self):
        self.mlblivedata = iis.MLBLiveData()

    def get_interest_index(self):
        interest_index_df = self.mlblivedata.get_interest_index_df()
        return interest_index_df

    def get_live_situation(self):
        live_situation = self.mlblivedata.get_live_situation_df()
        return live_situation

    
if __name__ == '__main__':
    print(GetPyRemote().get_live_situation())