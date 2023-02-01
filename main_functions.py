import csv
import itertools
from query_price import *
from site_dictionary import *

all_sites = [
    cardbrawlers,
    skyfox,
    darkfoxtcg,
    frankscloset,
    kanzengames,
    enterthebattlefield,
    thecgrealm,
    laboitemystere,
    jeux3dragons,
    firstplayer,
    fusiongamingonline,
    atlascollectables,
    topdeckhero,
    cardseternal,
    ebay,
    facetoface,
    duelkingdom,
    ygohustle,
    essentialcards,
    lapieuvrebarbue,
    reddragon,
    godsarena,
    cartamagica,
    gamekeeper,
    lexpedition,
    gamezilla,
    exorgames,
    commonboxgames]

def build_result_table():
    table = []
    #for site in all_sites:
    for site in all_sites:
        table.append([site["name"]])
    return table

def fill_result(table, searches):
    cardbrawlers_prices = []
    skyfox_prices = []
    darkfoxtcg_prices = []
    frankscloset_prices = []
    kanzengames_prices = []
    enterthebattlefield_prices = []
    thecgrealm_prices = []
    laboitemystere_prices = []
    jeux3dragons_prices = []
    firstplayer_prices = []
    fusiongamingonline_prices = []
    atlascollectables_prices = []
    topdeckhero_prices = []
    cardseternal_prices = []
    dollys_prices = []
    ebay_prices = []
    facetoface_prices = []
    duelkingdom_prices = []
    ygohustle_prices = []
    trinityhobby_prices = []
    essentialcards_prices = []
    lapieuvrebarbue_prices = []
    reddragon_prices = []
    godsarena_prices = []
    cartamagica_prices = []
    gamekeeper_prices = []
    lexpedition_prices = []
    gamezilla_prices = []
    comichunter_prices = []
    exorgames_prices = []
    commonboxgames_prices = []
    #market_prices = []
    for site in table:
        for s in searches:
            search = s[0]
            if site[0] == cardbrawlers["name"]:
                try:
                    price = binderpos_results(cardbrawlers, search) * cardbrawlers["tax"] * (1-cardbrawlers["discount"])
                except:
                    price = "ERROR"
                cardbrawlers_prices.append(price)
                #cardbrawlers_prices.append((price,cardbrawlers['shipping']*cardbrawlers["tax"],s[1]))
            elif site[0] == skyfox["name"]:
                try:
                    price = binderpos_results(skyfox, search) * skyfox["tax"] * (1-skyfox["discount"])
                except:
                    price = "ERROR"
                skyfox_prices.append(price)
                #skyfox_prices.append((price,skyfox['shipping']*skyfox["tax"],s[1]))
            elif site[0] == frankscloset["name"]:
                try:
                    price = binderpos_results(frankscloset, search) * frankscloset["tax"] * (1-frankscloset["discount"])
                except:
                    price = "ERROR"
                frankscloset_prices.append(price)
                #frankscloset_prices.append((price,frankscloset['shipping']*frankscloset["tax"],s[1]))
            elif site[0] == enterthebattlefield["name"]:
                try:
                    price = binderpos_results(enterthebattlefield, search) * enterthebattlefield["tax"] * (1-enterthebattlefield["discount"])
                except:
                    price = "ERROR"
                enterthebattlefield_prices.append(price)
                #enterthebattlefield_prices.append((price,enterthebattlefield['shipping']*enterthebattlefield["tax"],s[1]))
            elif site[0] == laboitemystere["name"]:
                try:
                    price = binderpos_results(laboitemystere, search) * laboitemystere["tax"] * (1-laboitemystere["discount"])
                except:
                    price = "ERROR"
                laboitemystere_prices.append(price)
                #laboitemystere_prices.append((price,laboitemystere['shipping']*laboitemystere["tax"],s[1]))
            elif site[0] == darkfoxtcg["name"]:
                try:
                    price = binderpos_results(darkfoxtcg, search) * darkfoxtcg["tax"] * (1-darkfoxtcg["discount"])
                except:
                    price = "ERROR"
                darkfoxtcg_prices.append(price)
                #darkfoxtcg_prices.append((price,darkfoxtcg['shipping']*darkfoxtcg["tax"],s[1]))
            elif site[0] == kanzengames["name"]:
                try:
                    price = binderpos_results(kanzengames, search) * kanzengames["tax"] * (1-kanzengames["discount"])
                except:
                    price = "ERROR"
                kanzengames_prices.append(price)
                #kanzengames_prices.append((price,kanzengames['shipping']*kanzengames["tax"],s[1]))
            elif site[0] == thecgrealm["name"]:
                try:
                    price = binderpos_results(thecgrealm, search) * thecgrealm["tax"] * (1-thecgrealm["discount"])
                except:
                    price = "ERROR"
                thecgrealm_prices.append(price)
                #thecgrealm_prices.append((price,thecgrealm['shipping']*thecgrealm["tax"],s[1]))
            elif site[0] == atlascollectables["name"]:
                try:
                    price = (crystalcommerce_results(atlascollectables, search) + atlascollectables["addcardship"]) * atlascollectables["tax"] * (1-atlascollectables["discount"])
                except:
                    price = "ERROR"
                atlascollectables_prices.append(price)
                #atlascollectables_prices.append((price,atlascollectables['shipping']*atlascollectables["tax"],s[1]))
            elif site[0] == jeux3dragons["name"]:
                try:
                    price = (crystalcommerce_results(jeux3dragons, search) + jeux3dragons["addcardship"]) * jeux3dragons["tax"] * (1-jeux3dragons["discount"])
                except:
                    price = "ERROR"
                jeux3dragons_prices.append(price)
                #jeux3dragons_prices.append((price,jeux3dragons['shipping']*jeux3dragons["tax"],s[1]))
            elif site[0] == firstplayer["name"]:
                try:
                    price = crystalcommerce_results(firstplayer, search) * firstplayer["tax"] * (1-firstplayer["discount"])
                except:
                    price = "ERROR"
                firstplayer_prices.append(price)
                #firstplayer_prices.append((price,firstplayer['shipping']*firstplayer["tax"],s[1]))
            elif site[0] == fusiongamingonline["name"]:
                try:
                    price = crystalcommerce_results(fusiongamingonline, search) * fusiongamingonline["tax"] * (1-fusiongamingonline["discount"])
                except:
                    price = "ERROR"
                fusiongamingonline_prices.append(price)
                #fusiongamingonline_prices.append((price,fusiongamingonline['shipping']*fusiongamingonline["tax"],s[1]))
            elif site[0] == dollys["name"]:
                try:
                    price = (crystalcommerce_results(dollys, search) + dollys["addcardship"]) * dollys["tax"] * (1-dollys["discount"])
                except:
                    price = "ERROR"
                dollys_prices.append(price)
                #dollys_prices.append((price,dollys['shipping']*dollys["tax"],s[1]))
            elif site[0] == topdeckhero["name"]:
                try:
                    price = (crystalcommerce_results(topdeckhero, search) + topdeckhero["addcardship"]) * topdeckhero["tax"] * (1-topdeckhero["discount"])
                except:
                    price = "ERROR"
                topdeckhero_prices.append(price)
                #topdeckhero_prices.append((price,topdeckhero['shipping']*topdeckhero["tax"],s[1]))
            elif site[0] == cardseternal["name"]:
                try:
                    price = crystalcommerce_results(cardseternal, search) * cardseternal["tax"] * (1-cardseternal["discount"])
                except:
                    price = "ERROR"
                cardseternal_prices.append(price)
                #cardseternal_prices.append((price,cardseternal['shipping']*cardseternal["tax"],s[1]))
            elif site[0] == ebay["name"]:
                try:
                    price = ebay_results(search) * ebay["tax"] * (1-ebay["discount"])
                except:
                    price = "ERROR"
                ebay_prices.append(price)
                #ebay_prices.append((price,ebay['shipping']*ebay["tax"],s[1]))
            elif site[0] == facetoface["name"]:
                try:
                    price = facetoface_results(search) * facetoface["tax"] * (1-facetoface["discount"])
                except:
                    price = "ERROR"
                facetoface_prices.append(price)
                #facetoface_prices.append((price,facetoface['shipping']*facetoface["tax"],s[1]))
            elif site[0] == duelkingdom["name"]:
                try:
                    price = duelkingdom_results(search) * duelkingdom["tax"] * (1-duelkingdom["discount"])
                except:
                    price = "ERROR"
                duelkingdom_prices.append(price)
                #duelkingdom_prices.append((price,duelkingdom['shipping']*duelkingdom["tax"],s[1]))
            elif site[0] == ygohustle["name"]:
                try:
                    price = ygohustle_results(search) * ygohustle["tax"] * (1-ygohustle["discount"])
                except:
                    price = "ERROR"
                ygohustle_prices.append(price)
                #ygohustle_prices.append((price,ygohustle['shipping']*ygohustle["tax"],s[1]))
            elif site[0] == trinityhobby["name"]:
                try:
                    price = trinityhobby_results(search) * trinityhobby["tax"] * (1-trinityhobby["discount"])
                except:
                    price = "ERROR"
                trinityhobby_prices.append(price)
                #trinityhobby_prices.append((price,trinityhobby['shipping']*trinityhobby["tax"],s[1]))
            elif site[0] == essentialcards["name"]:
                try:
                    price = essentialcards_results(search) * essentialcards["tax"] * (1-essentialcards["discount"])
                except:
                    price = "ERROR"
                essentialcards_prices.append(price)
                #essentialcards_prices.append((price,essentialcards['shipping']*essentialcards["tax"],s[1]))
            elif site[0] == lapieuvrebarbue["name"]:
                try:
                    price = lapieuvrebarbue_results(search) * lapieuvrebarbue["tax"] * (1-lapieuvrebarbue["discount"])
                except:
                    price = "ERROR"
                lapieuvrebarbue_prices.append(price)
                #lapieuvrebarbue_prices.append((price,lapieuvrebarbue['shipping']*lapieuvrebarbue["tax"],s[1]))
            elif site[0] == reddragon["name"]:
                try:
                    price = binderpos_results(reddragon, search) * reddragon["tax"] * (1-reddragon["discount"])
                except:
                    price = "ERROR"
                reddragon_prices.append(price)
            elif site[0] == godsarena["name"]:
                try:
                    price = crystalcommerce_results(godsarena, search) * godsarena["tax"] * (1-godsarena["discount"])
                except:
                    price = "ERROR"
                godsarena_prices.append(price)
            elif site[0] == cartamagica["name"]:
                try:
                    price = crystalcommerce_results(cartamagica, search) * cartamagica["tax"] * (1-cartamagica["discount"])
                except:
                    price = "ERROR"
                cartamagica_prices.append(price)
            elif site[0] == gamekeeper["name"]:
                try:
                    price = crystalcommerce_results(gamekeeper, search) * gamekeeper["tax"] * (1-gamekeeper["discount"])
                except:
                    price = "ERROR"
                gamekeeper_prices.append(price)
            elif site[0] == lexpedition["name"]:
                try:
                    price = lexpedition_results(search) * lexpedition["tax"] * (1-lexpedition["discount"])
                except:
                    price = "ERROR"
                lexpedition_prices.append(price)
            elif site[0] == gamezilla["name"]:
                try:
                    price = binderpos_results(gamezilla, search) * gamezilla["tax"] * (1-gamezilla["discount"])
                except:
                    price = "ERROR"
                gamezilla_prices.append(price)
            elif site[0] == comichunter["name"]:
                try:
                    price = crystalcommerce_results(comichunter, search) * comichunter["tax"] * (1-comichunter["discount"])
                except:
                    price = "ERROR"
                comichunter_prices.append(price)
            elif site[0] == exorgames["name"]:
                try:
                    price = binderpos_results(exorgames, search) * exorgames["tax"] * (1-exorgames["discount"])
                except:
                    price = "ERROR"
                exorgames_prices.append(price)
            elif site[0] == commonboxgames["name"]:
                try:
                    price = binderpos_results(commonboxgames, search) * commonboxgames["tax"] * (1-commonboxgames["discount"])
                except:
                    price = "ERROR"
                commonboxgames_prices.append(price)

            #market_prices.append(tcgplayer(search))
    dict = {table[0][0]: cardbrawlers_prices,
            table[1][0]: skyfox_prices,
            table[2][0]: darkfoxtcg_prices,
            table[3][0]: frankscloset_prices,
            table[4][0]: kanzengames_prices,
            table[5][0]: enterthebattlefield_prices,
            table[6][0]: thecgrealm_prices,
            table[7][0]: laboitemystere_prices,
            table[8][0]: jeux3dragons_prices,
            table[9][0]: firstplayer_prices,
            table[10][0]: fusiongamingonline_prices,
            table[11][0]: atlascollectables_prices,
            table[12][0]: topdeckhero_prices,
            table[13][0]: cardseternal_prices,
            table[14][0]: ebay_prices,
            table[15][0]: facetoface_prices,
            table[16][0]: duelkingdom_prices,
            table[17][0]: ygohustle_prices,
            table[18][0]: essentialcards_prices,
            table[19][0]: lapieuvrebarbue_prices,
            table[20][0]: reddragon_prices,
            table[21][0]: godsarena_prices,
            table[22][0]: cartamagica_prices,
            table[23][0]: gamekeeper_prices,
            table[24][0]: lexpedition_prices,
            table[25][0]: gamezilla_prices,
            table[26][0]: exorgames_prices,
            table[27][0]: commonboxgames_prices}
    driver.quit()
    return dict

def backtrack(ssB):
    min_ix = []
    for row in np.arange(len(ssB), 0, -1):
        min_ix = [np.min(np.where(ssB[row-1,]==min(ssB[row-1,])))] + min_ix
    return min_ix

def smallest_sum(og):
    df = og.copy()
    # Have everything in the first row be including shipping+tax
    for col in range(0,len(df.columns)):
        price = df.loc[df.index[0], df.columns[col]][0]
        ship = df.loc[df.index[0], df.columns[col]][1]
        quantity = df.loc[df.index[0], df.columns[col]][2]
        if price != 9999:
            df.at[df.index[0], df.columns[col]] = price * quantity + ship
        else:
            df.at[df.index[0], df.columns[col]] = 9999
    ans = np.empty((len(df),len(df.columns),))
    all_paths = []
    # Go through each element in the first row to find min path
    for paths in range(0, len(df.columns)):
        df2 = df.copy()
        ans[0,:] = df2.iloc[0]
        # For Current path find its min path
        price = df2.at[df2.index[0], df2.columns[paths]]
        if price != 9999:
            sites_idx = []
            for row in range(1, len(df2)):
                # Use index of first row as previous index since we are starting from there
                if row == 1:
                    mn = price
                    prev_idx = paths
                    sites_idx.append(prev_idx)
                else:
                    mn = min(ans[row-1,:])
                    prev_idx = np.min(np.where(ans[row-1,] == mn))
                    sites_idx.append(prev_idx)
                for col in range(0, len(df2.columns)):
                    # Check if current index was a previous index, we know if to add shipping or not
                    if col in sites_idx:
                        ans[row,col] = mn + df2.iloc[row,col][0] * df2.iloc[row,col][2]
                    else:
                        ans[row,col] = mn + df2.iloc[row,col][0] * df2.iloc[row,col][2] + df2.iloc[row,col][1]
            all_paths.append(ans.copy())
        mini = 999999
        for path in all_paths:
            #curr = backtrack(path)
            #for each in curr
            if min(path[1,]) < mini:
                mini = min(path[1,])
                p = path
    return p

def buyfrom(indexes, df):
        price = []
        total = []
        store = []
        ship = []
        i=0
        for row in range(0, len(df)):
            p = df.iloc[row, indexes[i]][0]
            price.append(p)
            total.append(p*df.iloc[row, indexes[i]][2])
            if df.columns[indexes[i]] in store:
                ship.append(0)
                store.append(df.columns[indexes[i]])
            else:
                ship.append(df.iloc[row, indexes[i]][1])
                store.append(df.columns[indexes[i]])
            i=i+1
        data = {'Price': price,
                'Total Price': total,
                'Shipping': ship,
                'Store': store}
        new_df = pd.DataFrame(data, index=df.index)
        return new_df

def input_data(result):
    quantities = pd.read_csv("searches.csv", header=None).set_index(0)
    quantities = quantities.reindex(list(result.index))
    q = quantities[1].values.tolist()
    df = result.copy()
    df2 = df.copy()
    for col in range(0, len(df.columns)):
        for row in range(0, len(df)):
            val = df.iloc[row,col]
            for site in all_sites:
                if df.columns[col] == site['name']:
                    shipping = site['shipping']
                    tax = site['tax']
            shipping = shipping*tax
            df.at[df.index[row], df.columns[col]] = shipping
            df2.at[df2.index[row], df2.columns[col]] = q[row]
    return [df, df2]

def optimal_purchases(result, idxs):
    result = result.set_index('search').replace('ERROR',np.nan).dropna(axis=1, how='all').astype(float)
    result = result.sort_values(by = list(result.columns), axis=0, ascending=False).replace(np.nan, 9999)
    result1 = result.copy()
    result2 = input_data(result1)
    shippingdf = result2[0]
    quantitydf = result2[1]

    p = result.values.tolist()
    s = shippingdf.values.tolist()
    q = quantitydf.values.tolist()
    new_result = []
    for row in range(0, len(p)):
        new_result.append([])
        for col in range(0, len(p[row])):
            new_result[row].append([p[row][col], s[row][col], q[row][col]])

    new_result = pd.DataFrame(new_result, columns = result.columns, index = result.index)

    ssB = smallest_sum(new_result)
    idx = backtrack(ssB)
    buylist = buyfrom(idx, new_result)
    buylist.sort_values(by=['Store'])
    return buylist
