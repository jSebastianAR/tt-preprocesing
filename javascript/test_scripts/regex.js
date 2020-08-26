import XRegExp from 'xregexp';
import Xrand from 'xrand';

const REGEX_NONALPHANUMERIC = XRegExp("[^ \w]");
const re = /[^ \w]/g
var static_list = ["Cr!uz#eli'z Pizza","#Hello World$$","A#B$C%D/E*F-G+H","Hola mundo","Bu)3y(y%yyy#","Noo_13oo..OOO+00"];

//console.log(XRegExp.match(static_list,REGEX_NONALPHANUMERIC))

//console.log(XRegExp.match(static_list,re))
//console.log(static_list.match(re))

function clean_pattern(pattern){

    let list_match = XRegExp.match(pattern,re)
    console.log(`Pattern: ${pattern}`)
    if(list_match.length>0){
        console.log(`Matches: ${list_match}`)
        let cleaned_pattern = pattern.replace(re,'')
        console.log(`Cleaned string: ${cleaned_pattern}`)
        return cleaned_pattern
    }else{
        console.log(`Cleaned string: ${pattern}`)
        return pattern
    }    
}

const xrand = new Xrand(0,static_list.length-1);
const random = xrand => static_list[xrand.generate()];

function get_random(){
    let xrand = new Xrand(0,static_list.length-1);
    return static_list[xrand.generate()]
}

clean_pattern(random(xrand))
