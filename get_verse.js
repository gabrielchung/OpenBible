function get_verse(bible_reference_str) {

    var fs = require('fs');
    var obj = JSON.parse(fs.readFileSync('bible_books.json', 'utf8'));

    // get book index

    var book_name = bible_reference_str.split(' ')[0];
    var book_index = 0;

    for (book_index=0; book_index<obj.length; book_index++) {
        if (book_name === obj[book_index].key) {
            break;
        }
    }

    // get chapter and verse number
    var tmp = bible_reference_str.split(' ')[1];
    var chapter_number = tmp.split(':')[0];
    var verse_number = tmp.split(':')[1];

    var fs = require('fs');
    var kjv = JSON.parse(fs.readFileSync('kjv.json', 'utf8'));

    return  kjv.content[book_index][chapter_number-1][verse_number-1];

}

console.log(process.argv[2]);
console.log(get_verse(process.argv[2]));
//console.log(JSON.parse(get_verse(process.argv[2])));