import Vue from 'vue';
import { ExtendedVue } from 'vue/types/vue';

// There must be a better way to recover a component's name, but I can't find it
const re = /^vue-component-[0-9]+-(.+)$/;

export function findParent<A extends Vue, B, C, D, E>(root: Vue, ctor: ExtendedVue<A, B, C, D, E>): InstanceType<typeof ctor> {
	// This causes warnings if ctor has required props
	const name = new ctor().$options.name;
	if(name === undefined) {
		throw new Error("Can't search for unnamed component");
	}
	for(let seek = root.$parent; seek; seek = seek.$parent) {
		const match = seek.$vnode.tag?.match(re);
		if(match?.[1] === name) {
			return seek as InstanceType<typeof ctor>;
		}
	}
	throw new Error(`Parent '${name}' not found`);
}

export function* iterChildren<A extends Vue, B, C, D, E>(root: Vue, ctor: ExtendedVue<A, B, C, D, E>): IterableIterator<InstanceType<typeof ctor>> {
	const name = new ctor().$options.name;
	if(name === undefined) {
		throw new Error("Can't search for unnamed component");
	}
	for(const child of root.$children) {
		const match = child.$vnode.tag?.match(re);
		if(match?.[1] === name) {
			yield child as InstanceType<typeof ctor>;
		}
		yield* iterChildren(child, ctor);
	}
}
