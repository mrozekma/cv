const _ = require('lodash');

export default function(mtime) {
  const now = new Date();
  const date = new Date(mtime * 1000);

  let mtimeStr = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'][date.getUTCMonth()];
  mtimeStr += _.padStart(date.getUTCDate(), 3);
  if(date.getUTCFullYear() == now.getUTCFullYear()) {
    mtimeStr += ' ' + _.padStart(date.getUTCHours(), 2, '0') + ':' + _.padStart(date.getUTCMinutes(), 2, '0');
  } else {
    mtimeStr += '  ' + date.getUTCFullYear();
  }
  return mtimeStr;
}
