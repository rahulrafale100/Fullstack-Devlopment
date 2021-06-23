function handleUpdate(resp) {
    $("#details").html(resp);          //It will show content on the same page itself
}
function handleClick(event) {
    var link = event.target;
    console.log(link['href']);       // It will take out only href part only
    $.get(link).done(handleUpdate);
    event.preventDefault();          //it  prevent to reload it and go to next page
    }
function main() {
    $("a.joblink").click(handleClick);  //It will get <a href=url_for........something /> in index.html file
}
$(main);  // $ sign tells call the main after page is loaded

///A hook is a function which is called when some action is taken or done by user