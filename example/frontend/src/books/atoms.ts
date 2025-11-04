import {atom} from "@reatom/core";
import {Book} from "./types";

export const booksAtom = atom<Book[]>([]);
export const initialAtom = atom<boolean>(false);