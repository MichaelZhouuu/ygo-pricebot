from main_functions import *

# query_price TEST

#search = "MP21-EN232"
#loop_sites(search)
#print(ebay_results(search))
#print(facetoface_results(search))
#print(binderpos_results(laboitemystere, search))
#test_site('searches.csv')

#'''
# main_functions TEST


# WEBSCRAPE FOR PRICES
def scrape():
    search = pd.read_csv("searches.csv", names = ['search', 'quantity',''])
    search = search.drop('',axis=1)
    empty_table = build_result_table()
    # The list
    list1 = search["search"].tolist()
    list2 = search["quantity"].tolist()
    merged_list = [(list1[i], list2[i]) for i in range(0, len(list1))]
    filled_table = fill_result(empty_table, merged_list)
    filled_df = pd.DataFrame(filled_table, index=search["search"])
    filled_df.to_csv('search_result.csv')
    #filled_df.to_csv('sub_result.csv')

# COMBINE A NEW SEARCH QUERY WITH EXISTING SEARCH RESULTS CSV
def add_to_search():
    search = pd.read_csv("new_searches.csv", names = ['search', 'quantity',''])
    search = search.drop('',axis=1)
    empty_table = build_result_table()

    list1 = search["search"].tolist()
    list2 = search["quantity"].tolist()
    merged_list = [(list1[i], list2[i]) for i in range(0, len(list1))]
    filled_table = fill_result(empty_table, merged_list)
    filled_df = pd.DataFrame(filled_table, index=search["search"])
    filled_df.to_csv('new_search_result.csv')
    filled_df.to_csv("search_result.csv", mode='a')
    search.to_csv("searches.csv", mode='a',index=False, header=False)

# USE SEARCH RESULTS TO COME UP WITH OPTIMAL BUYLIST
def buylist():
    result = pd.read_csv("search_result.csv")
    search = pd.read_csv("searches.csv", names = ['search', 'quantity',''])
    search = search.drop('',axis=1)
    buylist = optimal_purchases(result, search["search"].values.tolist())
    buylist = buylist.sort_values(by=['Store'])
    buylist.to_csv('buylist.csv')
    print("TOTAL: $" + str(sum(buylist["Total Price"]) + sum(buylist["Shipping"])))

#scrape()
#add_to_search()
buylist()
