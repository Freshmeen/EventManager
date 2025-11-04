import axios from "axios";
import {atom, action} from '@reatom/core';
import {BooksApi, BookRead} from './generated';

const API_URL = "http://localhost:8000/api/v1/books";

export const fetchBooks = async () => {
    const res = await axios.get(API_URL);
    return res.data;
};

export const addBook = async (title: string) => {
    const res = await axios.post(API_URL, {title});
    return res.data;
};



