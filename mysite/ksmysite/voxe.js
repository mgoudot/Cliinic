var http = require("http");
var voxe = exports;
var result = "";
var candidatures = [
  "4f1ec52e6e27d70001000007",
  "4f1eddf96e27d7000100008b",
  "4f2c143202b7400005000029",
  "4f1888db5c664f0001000119",
  "4f188a59f8104a0001000004",
  "4f1887545c664f000100010f",
  "4f1888945c664f0001000116",
  "4f188a20f8104a0001000002",
  "4f1ec53e997d28000100000d",
  "4f242b3269b233000100002b",
];
var candidaturesNom = [
  "Nathalie Artaud",
  "François Bayrou",
  "Jacques Cheminade",
  "Nicolas Dupont-Aignan",
  "François Hollande",
  "Eva Joly",
  "Marine Le Pen",
  "Jean-Luc Mélenchon",
  "Philippe Poitou",
  "Nicolas Sarkozy",
]
var idx = Math.floor(Math.random()*10);

var options = {
  host: 'voxe.org',
  port: 80,
  path: '/api/v1/propositions/search?candidacyIds='+candidatures[idx],
  //method: 'get'
};


http.get(options, function(res) {
  //console.log("Got response: " + res.statusCode + "\n" + res.response);
  res.setEncoding('utf8');
  res.on('data', function (chunk) {
    //console.log('BODY: ' + chunk);
    result += chunk;
    try {
      var res = JSON.parse(result);
      //console.log(res.response);
      //console.log("so far so good");
      process(res);
    } catch(e) {
        //console.log("not yet");
    }
  });
}).on('error', function(e) {
  console.log("Got error: " + e.message);
});


function process(obj) {
    var question = {list: { fields: {question: "", reponse: "",  mauvaise1: "", mauvaise2: "", mauvaise3: "", theme: ""}}};
    question.list.fields.reponse = candidaturesNom[idx];
    candidatures.splice(idx,1);
    candidaturesNom.splice(idx,1);
    var i = obj.response.propositions.length;
    var px = Math.floor(Math.random()*i);
    //console.log(obj.response.propositions[px].text);
    question.list.fields.question = obj.response.propositions[px].text;
    //console.log(obj).response.propositions[px].tag;
    for (var x = 1;x<=3; x++) {
      var idxx = Math.floor(Math.random()*candidatures.length);
      //console.log(candidaturesNom[idxx]);
      question.list.fields["mauvaise"+x] = candidaturesNom[idxx];
      candidatures.splice(idxx,1);
      candidaturesNom.splice(idxx,1);
    }
    console.log(question);
    return question;
    
  };