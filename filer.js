// filer.js
const fs = require('fs')
const path = require('path')
const mv = require('mv')

const home = require('os').homedir()
const downloads = home + "/Downloads"

const FILE_TYPES = JSON.parse(fs.readFileSync("extensions.json"))



fs.readdir(downloads, (err, items) => {

    for(var item in items) {
        item = downloads + "/" + items[item]
        itemExtension = path.extname(item)
        
        if(itemExtension) {
            for(var type in FILE_TYPES) {
                console.log(FILE_TYPES[type])
                //type = downloads + "/" + type
                
                if(itemExtension.slice(1) in FILE_TYPES[type]) {
                    mv(item, type + "/" + item, (err) => {
                        console.log(err)
                    })
                }
            }
        }
        
    }
})

// Check if file type directory exists. Create if it doesn't.
for(var type in FILE_TYPES) {
    //console.log(file)
    type = downloads + "/" + type
    if(!fs.existsSync(type)) {
        fs.mkdirSync(type)
    }
}