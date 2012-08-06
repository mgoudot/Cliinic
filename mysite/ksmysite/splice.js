function process(obj) {
    var question = {};
    i = obj.response.propositions.length;
    px = Math.floor(Math.random()*i);
    question.list.fields.question = obj.response.propositions[px].text;
    question.list.fields.reponse = candidaturesNom[idx];
    candidatures.splice(idx,1);
    candidaturesNom.splice(idx,1);
    console.log(question);
    for (var x = 1;x<=3; x++) {
      var idxx = Math.floor(Math.random()*candidatures.length);
      //console.log(candidaturesNom[idxx]);
      candidatures.splice(idxx,1);
      candidaturesNom.splice(idxx,1);
      question.list.fields["mauvaise"+x] = candidaturesNom[idxx] 
    }
    console.log(question);
  };