const fs = require('fs');
const sizeOf = require('image-size');

let rtn = {};
const dirs = ['projects'];

for(const dir of dirs) {
  const root = `static/images/${dir}`;
  rtn[dir] = {};
  for(const subdir of fs.readdirSync(root)) {
    let dims = rtn[dir][subdir] = {};
    for(const filename of fs.readdirSync(`${root}/${subdir}`)) {
      dims[filename.replace(/\.[^.]+$/, '')] = sizeOf(`${root}/${subdir}/${filename}`);
    }
  }
}

module.exports = function() {
  return `export default ${JSON.stringify(rtn)}`;
};
