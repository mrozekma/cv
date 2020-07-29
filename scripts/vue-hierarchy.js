export function* iterChildren(root, tag) {
	for(const child of root.$children) {
		if(child.$vnode.componentOptions.tag == tag) {
			yield child;
		}
		yield* iterChildren(child, tag);
	}
}
