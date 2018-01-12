import PoloniexAPI
import Secret_APIKEY  # write your own secret key and api in a file
import Utils
import UtilsIO



mypoloneix = PoloniexAPI.poloniex(APIKey=Secret_APIKEY.API_KEY, Secret=Secret_APIKEY.SECRET)
data = mypoloneix.api_query(Utils.command_returnMarketTradeHistory, Utils.BTC_DOGE)
UtilsIO.writeFile("BTC_DODGE.json", data)
