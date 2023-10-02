from flask import Flask, render_template, request, redirect, session,jsonify
from web3 import Web3
import secrets
import pandas
import datetime

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)
web3 = Web3(Web3.HTTPProvider('YOUR_OWN_PROVIDER_URL'))

FILENAME = 'NFT_data.csv'

NFT_data = pandas.read_csv(FILENAME).to_dict('records')

# Define a route for the main page
@app.route('/')
def index():

    return render_template('index.html', nfts=NFT_data)

# Define a route for the Item details page
@app.route('/item_details/<int:item_id>')
def item_details(item_id):
    nft = [nft for nft in NFT_data if nft['id'] == item_id][0]
    print(nft)
    transactions = eval([nft for nft in NFT_data if nft['id'] == item_id][0]['transaction_history'])
    print(transactions)

    return render_template('item_details.html', nft=nft, transaction_history=transactions)

@app.route('/login', methods=['POST'])
def login():
    user_address = Web3.toChecksumAddress(request.json['address'])

    session['logged_in'] = True
    session['user_address'] = user_address
    session['balance'] = round(web3.eth.get_balance(user_address) / 10**18, 5)
        
    
    return {'status': 'success'}

@app.route('/login', methods=['GET'])
def login_form():
    return render_template('login.html')

@app.route('/logout')
def logout():
    # delete logged in from session  
    del session['logged_in']
    session['user_address'] = ''
    return redirect('/')


@app.route('/profile')
def profile():
    try:
        session['logged_in']
        # Get the user's NFTs
        user_address = session['user_address']

        nfts = [nft for nft in NFT_data if nft['owner'] == user_address]

        return render_template('profile.html', nfts=nfts)
    except Exception as e:
        print(e)
        return redirect('/login')


"""
1.Check the blockchain to ensure that the buyer has sufficient funds to purchase the NFT.
2.Send a transaction to transfer the funds from the buyer's wallet to the seller's wallet via metamask
3.Update the off-chain NFT data to reflect the new owner and the transaction history.
"""

def check_balance(address, price_eth):
    balance = web3.toWei(web3.eth.get_balance(address) / 10**18, 'ether')
    price_eth = web3.toWei(price_eth, 'ether')
    
    print(balance, price_eth)
    if balance >= price_eth:
        print("enoough funds, proceed")
        return True
    else:
        print('insufficient funds, abort')
        return False
    
def build_transaction(buyer_address, price_eth, seller_address):
    buyer_address = Web3.toChecksumAddress(buyer_address)
    seller_address = Web3.toChecksumAddress(seller_address)
    transaction = {
        'type': '0x2',
        'from': buyer_address,
        'to': seller_address,
        'value': hex(web3.toWei(price_eth, 'ether')),
        'chainId': 5




    }
    gas = web3.eth.estimateGas(transaction)
    transaction['gas'] = gas
    
    
    print(transaction)
    return transaction

# send transaction to frontend

@app.route('/buy/<int:item_id>', methods=['POST'])
def buy_item(item_id):
    nft = [nft for nft in NFT_data if nft['id'] == item_id][0]
    price_eth = float(nft['price'].replace(' ETH', ''))
    seller_address = nft['owner']
    buyer_address = Web3.toChecksumAddress(request.json.get('address'))
    
    

    print(f"transaction: {buyer_address} -> {seller_address} for {price_eth} ETH")
    
    # check if the buyer has sufficient funds
    if check_balance(buyer_address, price_eth):
        # build the transaction
        transaction = build_transaction(buyer_address, price_eth, seller_address)
        # send the transaction to the frontend
        return jsonify({'transaction': transaction})
    else:
        return jsonify({'error': 'Insufficient funds'})
    
    

@app.route('/buy/<int:item_id>/complete', methods=['POST'])
def complete_purchase(item_id):
    global NFT_data
    tx_hash = request.json.get('txHash')
    sold_price = request.json.get('soldPrice')
    # hex to string
    sold_price = web3.fromWei(int(sold_price, 16), 'ether')
    
    # do something with the transaction hash
    print(f"Transaction hash: {tx_hash}")

    UpdateData(item_id, session['user_address'], sold_price, tx_hash)
    

    return render_template('index.html', nfts=NFT_data)
    
    
def UpdateData(item_id, new_owner, sold_price, tx_hash):
    
    # Update the NFT_data.csv file
    df = pandas.read_csv(FILENAME)
    df.loc[df['id'] == item_id, 'owner'] = new_owner
    
    # add transaction history 
    # sample: {'id': 1, 'buyer': 'Kristen Harvey', 'price': '1 ETH', 'date': '2023-05-01'}
    
    transaction_list = df.loc[df['id'] == item_id, 'transaction_history'].apply(eval).tolist()[0]
    transaction_list.append({'id': len(transaction_list), 'buyer': new_owner, 'price': sold_price, 'date': datetime.datetime.now().strftime("%Y-%m-%d"), 'tx_hash': tx_hash})
    
    df.loc[df['id'] == item_id, 'transaction_history'] = str(transaction_list)

    df.to_csv(FILENAME, index=False)
    
    # Update the NFT_data variable
    global NFT_data
    NFT_data = pandas.read_csv(FILENAME).to_dict('records')
    
    return True

    
    

    

if __name__ == '__main__':
    app.run(debug=True)
