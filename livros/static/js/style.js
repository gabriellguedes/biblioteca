var MyQuestion = function(mymsg, mypath){
    this.mymsg = mymsg;
    this.mypath = mypath;
};
MyQuestion.prototype.question = function(){
    var q = confirm(this.mymsg);
    if(q){
        window.location = this.mypath;
    } else {
        return false;
    }
};