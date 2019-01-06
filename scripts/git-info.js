const spawnSync = require('child_process').spawnSync;
const moment = require('moment');

const desc = spawnSync('git', ['describe', '--all', '--long', '--abbrev=40', '--dirty'], {encoding: 'utf8'}).stdout.trim();
const [hash, ts] = spawnSync('git', ['show', '-s', '--format=%H %ct'], {encoding: 'utf8'}).stdout.trim().split(' ');

const rtn = {
  description: desc.replace(/^heads\//, ''),
  hash: hash,
  commitDate: moment(parseInt(ts) * 1000).format('MMMM Do, YYYY'),
};

module.exports = function() {
  return `export default ${JSON.stringify(rtn)}`;
};
