var fs = require('fs'),
    xml2js = require('xml2js');
 
var parser = new xml2js.Parser();

kjv_xml = fs.readFileSync('./kjv.xml', 'utf-8');

fs.writeFileSync('./kjv.json', '', {flag: 'a'});
fs.unlinkSync('./kjv.json');

var bible;
var book;
var chatper;
var verse;

var jsonResult = {};
jsonResult.books = [];
jsonResult.content = [];

parser.parseString(kjv_xml, function (err, data) {

    bible = data.bible;
    book = bible.book;

    for (var i=0; i<book.length; i++) {

        jsonResult.books.push(book[i].$.num);
        jsonResult.content.push([]);

        chapter = book[i].chapter;

        for (var j=0; j<chapter.length; j++) {

            jsonResult.content[i].push([]);

            verse = chapter[j].verse;

            for (var k=0; k<verse.length; k++) {

                if (verse[k]._ == null) {

                    if (verse[k].span._ == null) {
                        // console.log(verse[k].span[0]);
                        jsonResult.content[i][j].push(verse[k].span[0]._);
                    } else {
                        jsonResult.content[i][j].push(verse[k].span._);
                    }
                } else {
                    jsonResult.content[i][j].push(verse[k]._);
                }

                // line_content = book[i].$.num + ' ' + (j+1) + ':' + (k+1) + ' ' + verse[k]._ + '\r\n';

                //console.log(verse[k]._)
                // fs.writeFileSync('kjv.js', line_content, {flag: 'a'});

            }

        }

    }

    fs.writeFileSync('kjv.json', JSON.stringify(jsonResult, null, 4), {flag: 'w'});

    // console.log(result);
    console.log('Done');
});
