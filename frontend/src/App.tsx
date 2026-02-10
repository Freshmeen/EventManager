import Base from "./base/Base";
import "./App.css"
import MainPage from "./events/mainPage/MainPage";

export default function App() {
    console.log("App rendered");
    return (
        <>
            {/*<Helmet>*/}
            {/*    <title>Event Manager</title>*/}
            {/*    <meta name="description" content="Приложение для управления событиями"/>*/}
            {/*</Helmet>*/}
            <Base>
                <MainPage/>
            </Base>
        </>

    );
}
