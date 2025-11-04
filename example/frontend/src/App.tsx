import BooksComponent from "./books/BooksComponent";
import "./App.css";
import {ToastProvider} from "./common/components/Toast/ToastContext";

export default function App() {
    return (
        <ToastProvider>
            <div className="app">
                <h1 className="title">Книги</h1>
                <BooksComponent/>
            </div>
        </ToastProvider>
    );
}
