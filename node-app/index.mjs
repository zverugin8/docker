import fs from 'fs'

fs.appendFile('my-file.txt', 'File created by Node.js', (err) => {
    if (err) throw err
    console.log('File created')

})

setTimeout(()  => console.log('The end'), 60000 )