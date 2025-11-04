import {BooksApi} from "../api/generated";
import {action} from "@reatom/core";
import {booksAtom, initialAtom} from "./atoms";
import {remapApiBookReadsToBooks} from "./remap";
import {Book} from "./types";
import {ToastException} from "../common/components/Toast/ToastException";

const api = new BooksApi();


export const loadBooksAction = action((ctx) => {
    api.getBooks()
        .then(books => {
            booksAtom(ctx, remapApiBookReadsToBooks(books.data));
            initialAtom(ctx, true);
        })
})

export const addBookAction = action((ctx, book: Book) => {
    api.createBook({
        title: book.title
    }).then(book => {
        booksAtom(ctx, (books: Book[], ctx): Book[] => {
            return [...books, book.data];
        })
    }).catch(response => {
        throw new ToastException(response.response.data.message, "error")
    })
})