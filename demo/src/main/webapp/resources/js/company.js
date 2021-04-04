//function setStatus(status,urlId,url,userId){
function setStatus(status,urlId,url_string){
	window.open("www.google.com", url_string, "");
	$.ajax({    
		type : "POST",
		url : "updateUrlStatus",
		data :{
			status : status,
			urlId : urlId,
			action : "companyData"
		},
		success : function(data){
			 		 
		},
		error : function(e){
			consloe.log("Error ::: "+e);
		}
	});	
}

