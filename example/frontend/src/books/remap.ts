import {BookRead} from "../api/generated";
import {Book} from "./types";

export function remapApiBookReadsToBooks(books: BookRead[]): Book[] {
    return books.map(book => {
        return {
            id: book.id,
            title: book.title,
        };
    })
}