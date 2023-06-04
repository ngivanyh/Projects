const specific_date = new Date('2023-06-01');

const month = [];

const getDayCount = (year, month) => {
    if (month === 2) {
        if (year % 4 === 0) {
            if (year % 100 === 0) {
                if (year % 400 === 0) {
                    return 29; // Leap year
                } else {
                    return 28; // Not a leap year
                }
            } else {
            return 29; // Leap year
            }
        } else {
            return 28; // Not a leap year
        }
    } else if (month === 1, 3, 5, 7, 8, 10, 12) {
        return 31;
    } else {
        return 30
    }
        
}

const push_zero = (cnt) => {
    let push_times = 0;
    while (push_times != cnt) {
        month.append(0);
        push_times += 1;
    }
} 

const append = (day_cnt) => {
    let cnt = 1;
    if (date.getDay === 0) {
        while (cnt != day_cnt) {
            month.append(cnt);
            cnt += 1;
        }
    } else if (date.getDay === 1) {
        push_zero(1);

    }
}

