% rebase('layout.tpl', title=title, year=year)

% import json
% with open('companies.json') as f:
%     companies = json.load(f)

<div class="jumbotron">
    <h1>Our partners</h1>
    <p class="lead">Our general partners</p>


%for companie in companies:
    <div class="panel panel-default">
    <div class="panel-heading" align="center"><h2><strong>{{ companie["name"] }}</strong></h2></div>
    <div class="panel-body">{{ companie["description"] }}</div>
    <div class="panel-body"><address><em><small><small>Our address: {{ companie["address"] }}</small></small></em></address></div>
    </div>
         
%end

</div>

<h3> Join us </h3>
<form action="/companies" method="post">
<p><input type="text" size="80" name="COMPANY_NAME" placeholder="Your company name"></p>
<p><textarea rows="4" cols="80" name="COMPANY_DESCRIPTION" placeholder="Describe your company, why do you want to work with us"></textarea></p> 
<p><input type="text" size="80" name="COMPANY_ADDRESS" placeholder="Address"></p>
<p><input type="text" size="80" name="COMPANY_PHONE" placeholder="Phone"></p>
<p><input type="text" size="80" name="INTEREST_" placeholder="Phone"></p>
<p><input type="submit" value="Send" class="btn btn-default" name="ADD_BTN"></p>
</form>