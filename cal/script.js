// // const specific_date = new Date('2023-04-01');
const done = document.getElementById("btn");
const usr_year = document.getElementById("year");
const user_month = document.getElementById("month");
const cal_head = document.getElementById("cal_header");
const actual_cal = document.getElementById("cal");
 
done.addEventListener('click', function() {
    const getDays = (year, month) => {
        let days = 0;
        if (month === 2) {
            if (year % 4 === 0) {
                if (year % 100 === 0) {
                    if (year % 400 === 0) {
                        days = 29;
                        return days; // Leap year
                    } else {
                        days = 28;
                        return days; // Not a leap year
                    }
                } else {
                    days = 29;
                    return days; // Leap year
                }
            } else {
                days = 28;
                return days; // Not a leap year
            }
        } else if (month === 1, month === 3, month === 5, month === 7, month === 8, month === 10, month === 12) {
            days = 31;
            return days;
        } else {
            days = 30;
            return days;
        }
            
    }
    
    const push_zero = (total) => {
        let push_times = 0;
        while (push_times != total) {
            cal.push(0);
            push_times += 1;
        }
    } 
    
    const pushUntilFull = (count, totalDays) => {
        while (count != totalDays) {
            count += 1;
            cal.push(count);
        }
    }
    
    const append = (day_cnt, spe_date) => {
        let cnt = 0;
        if (spe_date.getDay() === 0) {
            pushUntilFull(cnt, day_cnt);
        } else if (spe_date.getDay() === 1) {
            push_zero(1);
            pushUntilFull(cnt, day_cnt);
        } else if (spe_date.getDay() === 2) {
            push_zero(2);
            pushUntilFull(cnt, day_cnt);
        } else if (spe_date.getDay() === 3) {
            push_zero(3);
            pushUntilFull(cnt, day_cnt);
        } else if (spe_date.getDay() === 4) {
            push_zero(4);
            pushUntilFull(cnt, day_cnt);
        } else if (spe_date.getDay() === 5) {
            push_zero(5);
            pushUntilFull(cnt, day_cnt);
        } else if (spe_date.getDay() === 6) {
            push_zero(6);
            pushUntilFull(cnt, day_cnt);
        }
    }
    
    const cal = [];
    console.log("clicked");
    let year = usr_year.value;
    let month = user_month.value;
    let output = year.toString() + "/" + month.toString();

    console.log(typeof year, typeof month);

    cal_head.innerText = output;

    let specific_date_str = "";

    if (month > 9) {
        specific_date_str = year.toString() + "-" + month.toString() + "-01";
    } else {
        specific_date_str = year.toString() + "-0" + month.toString() + "-01";
    }
    let int_month = Number(month);
    let int_year = Number(year);
    // console.log(typeof specific_date_str);

    // console.log(specific_date_str);

    const specific_date = new Date(specific_date_str);

    let noOfDays = getDays(int_year, int_month);

    append(noOfDays, specific_date);

    console.log(cal, specific_date);

    let table = "<td></td>";

    var day = 0;
    let result = "<table>";
    for (let i = 0; i < 5; i++) {
        result += "<tr>";
        for (let index = 0; index < 7; index++) {
            if (cal[day] === 0 || typeof cal[day] === "undefined") {
                result += "<td> </td>";
            } else {
                result += "<td>" + cal[day] + "</td>";
            }
            day ++;
        }
        result += "</tr>";
    }

    result += "</table>"

    console.log(result);

    actual_cal.innerHTML = result;
});