import {BooksModel} from "./model";
import Books from "./view/Books";

export default function BooksComponent() {
    return (
        <BooksModel>
            <Books/>
        </BooksModel>
    )
}