import {Book as BookType} from "../types";
import styles from "./Book.module.css";

type BookProps = {
    book: BookType
}

export default function Book({book}: BookProps) {
    return (
        <div className={styles.book}>
            <b>{book.id}</b> {book.title}
        </div>
    );
}
