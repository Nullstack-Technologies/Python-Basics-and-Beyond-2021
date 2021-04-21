var flag = 0;

function changeThings(){
    if (flag == 0) {
        // Change the image
        document.getElementById('img-01').src = "corona_sad.png";

        // Change the texts
        document.getElementById('p-1').innerHTML = "I cannot infect You!!";
        
        // chnage the button content
        document.getElementById('myButton').innerHTML = "I Don't wear a mask";

        // flag reset
        flag = 1;

    }
    else{
        // Change the image
        document.getElementById('img-01').src = "corona_happy.png";

        // Change the texts
        document.getElementById('p-1').innerHTML = "Time to infect You!";
        
        // chnage the button content
        document.getElementById('myButton').innerHTML = "I Wear a Mask";

        // flag reset
        flag = 0;

    }
}