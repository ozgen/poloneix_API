import PoloniexAPI
import Secret_APIKEY  # write your own secret key and api in a file
import Utils
import UtilsIO

command_1 = "return24Volume"
command_2 = "returnTicker"
command_3 = "returnOrderBook"
req = {"currencyPair": "BTC_XRP"}

mypoloneix = PoloniexAPI.poloniex(APIKey=Secret_APIKEY.API_KEY, Secret=Secret_APIKEY.SECRET)
data = mypoloneix.api_query(Utils.command_returnMarketTradeHistory, Utils.BTC_DOGE)
UtilsIO.writeFile("BTC_DODGE.json", data)
