import {useState, useRef} from "react";
import styles from "./Books.module.css";
import {useBooksModel} from "../model";
import useAtoms from "../../common/hooks/useAtoms";
import useActions from "../../common/hooks/useActions";
import BookComponent from "./Book";
import {Book} from "../types";
import Button from "../../common/components/Button/Button";
import {ToastException} from "../../common/components/Toast/ToastException";
import {useToast} from "../../common/components/Toast/ToastContext";

export default function Books() {
    const {atoms, actions} = useBooksModel()
    const {booksAtom, initialAtom} = atoms;
    const {addBookAction, loadBooksAction} = actions;
    const [initial, books] = useAtoms([initialAtom, booksAtom])
    const [addBook, loadBooks] = useActions([addBookAction, loadBooksAction]);

    const titleRef = useRef<HTMLInputElement>(null);

    const [error, setError] = useState("");

    const handleAdd = () => {
        if (!titleRef.current) {
            setError("Введите название книги");
            return;
        }

        setError("");
        addBook({ title: titleRef.current.value });
        titleRef.current.value = "";
    };

    const {showToast} = useToast();

    return (
        <div className={styles.container}>
            <div className={styles.inputs}>
                <input
                    placeholder="title"
                    ref={titleRef}
                    className={styles.input + (error ? " " + styles.inputError : "")}
                    onChange={() => setError("")}
                />

                <Button onClick={handleAdd}>
                    Добавить
                </Button>

                <Button onClick={loadBooks}>
                    Обновить
                </Button>

                <Button onClick={() => {
                    showToast("Ещё не реализовано");
                }} type="negative">
                    Очистить
                </Button>
            </div>

            {error && <div className={styles.error}>{error}</div>}

            <div className={styles.books}>
                {initial && books.map((book: Book) =>
                    <BookComponent key={book.id} book={book}/>
                )}
            </div>
        </div>
    )
}
