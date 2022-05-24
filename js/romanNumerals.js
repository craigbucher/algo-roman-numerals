function toRoman(num){	
    let result = '';	
    // map of all possible combinations / divisors	
    const map = {	
      M: 1000,	
      CM: 900,	
      D: 500,	
      CD: 400,	
      C: 100,	
      XC: 90,	
      L: 50,	
      XL: 40,	
      X: 10,	
      IX: 9,	
      V: 5,	
      IV: 4,	
      I: 1,	
    };	
    // iterate through the map	
    for (key in map){	
      // add key for each time number is divisible by key value	
      result += key.repeat(Math.floor(num / map[key]));	
      // new number = remainder from previous calculation	
      num %= map[key];	
    }	
    return result;	
  }

  console.log(toRoman(2439)); // should return MMCDXXXIX