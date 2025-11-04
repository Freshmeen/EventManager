import {createContext, PropsWithChildren, useContext, useEffect} from "react";
import {loadBooksAction, addBookAction} from "./actions";
import {booksAtom, initialAtom} from "./atoms";
import {useAction} from "@reatom/npm-react";

const actions = {
    loadBooksAction,
    addBookAction,
}

const atoms = {
    booksAtom,
    initialAtom,
}

const BooksContext = createContext({atoms, actions});

export function BooksModel({children}: PropsWithChildren) {
    const loadBooks = useAction(loadBooksAction);
    useEffect(() => {
        loadBooks();
    }, []);
    return (
        <BooksContext.Provider value={{actions, atoms}}>
            {children}
        </BooksContext.Provider>
    )
}

export function useBooksModel() {
    const context = useContext(BooksContext);
    if (!context) {
        throw new Error("useBooks must be used within a BooksProvider");
    }
    return context;
}