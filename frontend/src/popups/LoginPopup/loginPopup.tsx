import styles from "./loginPopup.module.css"
import { callPopup } from "../../model/actions"
import { useAction } from "@reatom/npm-react"
import { Link } from "react-router-dom"

function LoginPopup() {

    const closePopup = useAction(callPopup)
    const callRegistrationPopup = useAction(callPopup)

    return(
      <>
        <div className={styles.popup}>
          <h2 className={styles.title}>Вход</h2>
          <div className={styles.input_fields}>
            <input className={styles.input_field} />
            <input className={styles.input_field} />
          </div>
          <Link to="/main">
            <button className={styles.submit_button} onClick={() => closePopup(null)}>Продолжить</button>
          </Link>
          <div className={styles.transtition + ' ' + styles.registration_transition} 
            onClick={() => callRegistrationPopup("registration")}
          >
            регистрация
          </div>
          <div className={styles.transtition + ' ' + styles.password_recovery_transition}>
            забыли пароль?
          </div>
        </div>
      </>
    )
}

export {
    LoginPopup
}