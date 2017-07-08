function percentual(votos,soma){
	var resultado=(votos/soma)*100;
	
	return document.write(resultado+"%");
}
function ConfirmarAlteracao(){		
if (confirm ("Deseja realmente realizar essa ação?")){
	
	return true;
}	
		
	
else{		
	
return false;
}

}

function ConfirmarVoto(){		
if (confirm ("Deseja realmente confirmar seu voto?")){
	
	return true;
}	
		
	
else{		
	
return false;
}

}