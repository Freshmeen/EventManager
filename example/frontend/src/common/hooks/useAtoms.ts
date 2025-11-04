import {useAtom} from "@reatom/npm-react";
import {Atom} from "@reatom/core";

export default function useAtoms(atoms: Atom<any>[]): Array<any> {
    if (atoms.length == 0) {
        return [];
    }
    const [firstAtom, ...otherAtoms] = atoms;
    const [first] = useAtom(firstAtom);
    return [first, ...useAtoms(otherAtoms)]
}