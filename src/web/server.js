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

var stores = function (request, response) {
    var reqURI = url.parse("http://" + request.headers.host + request.url);
    var params = reqURI.query;
    var tms = params.substr(params.indexOf('=') + 1);
    var terms = tms.replace("%20", " ");
    console.log(terms)
    var MongoClient = require('mongodb').MongoClient;
    MongoClient.connect("mongodb://localhost", function(err, client) {
      if(err) { throw err; }
      var db = client.db('CS432FP')
      db.collection('storeinfo').find({City:terms}).toArray(function (findErr, result) {
        if (findErr) throw findErr;
        response.writeHead(200, {
            'Content-Type':'application/json',
            'Access-Control-Allow-Origin':'*'
        });
        response.write(JSON.stringify(result));
        response.end();
        client.close();
      });
    });
    /*var reqURI = url.parse("http://" + request.headers.host + request.url);
    var params = reqURI.query;
    var terms = params.substr(params.indexOf('=') + 1);
    mdb.open(function (err, db) {
        db.command(
            {
                'text'   : 'storeinfo',    // Command to execute :  on collection
                'search' : terms,       // Search term to query with
                'limit'  : 5000         // Max number of results to return
            },
            function (err, obj) {
                var res = {
                    'data'   : (err ? null : (obj.results ? obj.results : null)),
                    'error'  : (err ? err : null),
                    'message': (err ? err.message : 'JSON response for a tweets query'),
                    'stats'  : obj.stats,
                    'terms'  : terms
                };
                response.writeHead(200, {
                    'Content-Type':'application/json',
                    'Access-Control-Allow-Origin':'*'
                });
                response.write(JSON.stringify(res));
                response.end();
                db.close();
            });
    });*/
};

/*var mdbServer = new mongo.Server('localhost', 27017, {'auto_reconnect' : true});
var mdb = mongo.Db('CS432FP', mdbServer);*/

http.createServer(router).listen(8080);

/*http.createServer(router) {
  res.writeHead(200, {'Content-Type': 'text/plain'});
  res.end('Sneed!');
}).listen(8081);
*/
