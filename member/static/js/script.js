function idCheck(){
	//alert('a');
	if(regForm.memid.value === ''){
		alert("회원아이디입력");
		regForm.memid.focus();
	}else{
		url = "/member/idcheck?memid=" + regForm.memid.value;
		window.open(url, 'memid', 'toolbar=no, width=300, height=150, top=200, left=300');
	}
}

function zipCheck(){
	url = "/member/zipcheck?check=y";
	window.open(url, 'zip', 'toolbar=no, width=500, height=300, top=200, left=300');
}

function send(zipcode, a1, a2, a3, a4){
	opener.document.regForm.zipcode.value = zipcode;
	if(a4 == "None") a4 == "";
	var addr = a1 + " " + a2 + " " + a3 + " " + a4;
	opener.document.regForm.address.value = addr;
	window.close();
}

function inputCheck(){
	if(regForm.memid.value === ""){
		alert("회원 아이디 입력");
		regForm.memid.focus();
		return;
	}
	
	if(regForm.passwd.value === ""){
		alert("비밀번호 입력");
		regForm.passwd.focus();
		return;
	}
	
	if(regForm.passwd.value !== regForm.repasswd.value){
		alert("비밀번호 불일치");
		regForm.passwd.focus();
		return;
	}
	
	//...생략
	
	regForm.submit();
}