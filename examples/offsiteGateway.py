# Include the Flask framework
from flask import Flask, url_for, request, redirect, render_template, session
app = Flask(__name__)

# Include the Dwolla REST Client
from dwolla import DwollaGateway

# Include any required keys
import _keys

# Instantiate a new Dwolla Gateway...
# And set the redircet URL to '/redirect'
# on our local server
Dwolla = DwollaGateway(_keys.apiKey, _keys.apiSecret, 'http://localhost:5000/redirect')


'''
    EXAMPLE 1: (simple example) 
      Create a new offsite gateway checkout
      session, with 1 test product, and
      a minimum of parameters
'''
@app.route("/example1")
def example1():
    # Clears out any previous products
    Dwolla.start_gateway_session()
    
    # Add first product; Price = $10, Qty = 1
    Dwolla.add_gateway_product('Test 1', 10)
    
    # Creates a checkout session, and return the URL
    # Destination ID: 812-626-8794
    url = Dwolla.get_gateway_URL('812-626-8794')

    return 'To begin the checkout process, send the user off to <a href="%s">%s</a>' % (url, url)


'''
    EXAMPLE 2: (in-depth example) 
      Create a new offsite gateway checkout
      session, with 2 test products, a
      discount, add shipping costs, tax,
      and order ID, and a memo/note
'''
@app.route("/example2")
def example2():
    # Set the server mode to test mode
    Dwolla.set_mode('TEST')
    
    # Clears out any previous products
    Dwolla.start_gateway_session()
    
    # Add first product; Price = $10, Qty = 1
    Dwolla.add_gateway_product('Test 1', 10, 'Test product')
    
    # Add first product; Price = $6, Qty = 2
    Dwolla.add_gateway_product('Test 2', 6, 'Another Test product', 2)
    
    # Creates a checkout session, and return the URL
    # Destination ID: 812-626-8794
    # Order ID: 10001
    # Discount: $24.85
    # Shipping: $0.99
    # Tax: $1.87
    # Memo: 'This is a great purchase'
    # Callback: 'http://requestb.in/1fy628r1' (you'll need to create your own bin at http://requestb.in/)
    url = Dwolla.get_gateway_URL('812-626-8794', '10001', 24.85, 0.99, 1.87, 'This is a great purchase', 'http://requestb.in/1fy628r1')

    return 'To begin the checkout process, send the user off to <a href="%s">%s</a>' % (url, url)


'''
    EXAMPLE 3: (Verifying an offsite gateway signature) 
      Verify the signature returned from
      Dwolla's offsite gateway redirect
'''
@app.route("/redirect")
def redirect():
    # Grab Dwolla's proposed signature
    signature = request.args.get("signature")
    
    # Grab Dwolla's checkout ID
    checkout_id = request.args.get("checkoutId")
    
    # Grab the reported total transaction amount
    amount = request.args.get("amount")

    # Verify the proposed signature
    did_verify = Dwolla.verify_gateway_signature(signature, checkout_id, amount)

    if did_verify:
        html = "<p>Dwolla's signature verified successfully. You should go ahead and process the order.</p>"
    else:
        html = "<p>Dwolla's signature failed to verify. You shouldn't process the order before some manual verification.</p>"

    return html




# Run the app
if __name__ == "__main__":
    app.run(debug=True)