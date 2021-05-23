% rebase('layout.tpl', title=title, year=year)

<h1 align="center"> Join us </h1>
<form action="/companies" method="post" align="center">
<p><input type="text" size="90" name="COMPANY_NAME" placeholder="Your company name"></p>
<p><textarea rows="4" cols="60" name="COMPANY_DESCRIPTION" placeholder="Describe your company, why do you want to work with us"></textarea></p> 
<p><input type="text" size="60" name="COMPANY_ADDRESS" placeholder="Address"></p>
<p><input type="text" size="50" name="COMPANY_PHONE" placeholder="Phone"></p>
<p><input type="submit" value="Join" class="btn btn-default" name="ADD_BTN"></p>
</form>

<div class="jumbotron">
    <h1>Our partners</h1>
    <p class="lead">Our general partners</p>

% import json
% with open('companies.json') as f:
%     companies = json.load(f)

%for company in companies: # вывод компаний-партнёров
    <div class="panel panel-default">
    <div class="panel-heading" align="center"><h2><strong>{{ company["name"] }}</strong></h2></div>
    <div class="panel-body">{{ company["description"] }}.</div>
    <div class="panel-body">
        <address>
            <em>
                <small>
                    <small>
                        Our phone: {{ company["phone"] }} </br> 
                        Our address: {{ company["address"] }}
                    </small>
                </small>
            </em>
        </address>
    </div>
    </div>
         
%end

</div>