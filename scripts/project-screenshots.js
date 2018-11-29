// This is some hacky madness to run some code at build time when imported by personal-projects.vue.
// I'm sure there's a better way to do this with webpack, but haven't figured it out yet.
const fs = require('fs');
const sizeOf = require('image-size');

const root = 'static/images/projects';
let rtn = {};
for(const project of fs.readdirSync(root)) {
  let dims = rtn[project] = {};
  for(const filename of fs.readdirSync(`${root}/${project}`)) {
    dims[filename.replace(/\.[^.]+$/, '')] = sizeOf(`${root}/${project}/${filename}`);
  }
}

module.exports = function() {
  return `export default ${JSON.stringify(rtn)}`;
};
