export function findParent(node, tag) {
  for(let seek = node.$parent; seek; seek = seek.$parent) {
    if(seek.$vnode.componentOptions.tag == tag) {
      return seek;
    }
  }
  throw `Parent <${tag}> not found`;
}

export function* iterChildren(root, tag) {
  for(const child of root.$children) {
    if(child.$vnode.componentOptions.tag == tag) {
      yield child;
    }
    yield* iterChildren(child, tag);
  }
}
