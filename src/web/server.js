var http = require('http');
var url = require('url');
var mongo = require('mongodb')

var router = function(request, response) {
    var reqURI = url.parse(request.headers.host + request.url);
    if (reqURI.pathname == '/tweets') {
        stores(request, response);
    } else  {
        var res = {
            'data':null,
            'error':null,
            'message':'You did not ask to query a valid collection.',
            'terms':null
        };
        response.writeHead(200, {
            'Content-Type':'application/json',
            'Access-Control-Allow-Origin':'*'
        });
        response.write(JSON.stringify(res));
        response.end();
    }
};

var stores = async function (request, response) {
    var reqURI = url.parse("http://" + request.headers.host + request.url);
    var params = reqURI.query;
    var tms = params.substr(params.indexOf('=') + 1);
    var terms = tms.replace("%20", " ");
    console.log(terms)
    const {MongoClient} = require('mongodb');
    const client = new MongoClient(/*key here*/);
    await client.connect();
    var db = client.db('CS480KFP')
    db.collection('stores').find({City:terms}).toArray(function (findErr, result) {
      if (findErr) throw findErr;
      response.writeHead(200, {
          'Content-Type':'application/json',
          'Access-Control-Allow-Origin':'*'
      });
      response.write(JSON.stringify(result));
      response.end();
      client.close();
    });
};

http.createServer(router).listen(8080);
