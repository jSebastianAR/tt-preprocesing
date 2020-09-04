const list_objs = [1,'2',666,{buey:'no'}]

export function printElements(list = list_objs){
    list.forEach((element) => {
        console.log(element)
    })    
};

export function printList(list){
    console.log(list)
}

const args = {
    'printElements':    printElements,
    'printList':        printList
}

export default args;
//export default printElements;

