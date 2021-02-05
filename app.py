from flask import Flask, render_template
app = Flask(__name__)

@app.route('/card/name=<string:name>&title=<string:title>&company=<string:company>&mobile=<string:mobile>&email=<string:email>&addr1=<string:addr1>&locality=<string:locality>&state=<string:state>&postcode=<string:postcode>&country=<string:country>&photourl=<string:photourl>&officenumber=<string:officenumber>&linkedin=<string:linkedin>&github=<string:github>&facebook=<string:facebook>')
def view_card(name, title, company, mobile, email, addr1, locality, state, postcode, country, photourl, officenumber, linkedin, github, facebook):
	return render_template('card.html', name=name, title=title, company=company, mobile=mobile, email=email, addr1=addr1, locality=locality, state=state, postcode=postcode, country=country, photourl=photourl, officenumber=officenumber, linkedin=linkedin, github=github, facebook=facebook)
