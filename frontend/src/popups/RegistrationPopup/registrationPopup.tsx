import styles from "./registrationPopup.module.css"
import { callPopup } from "../../model/actions"
import { useAction } from "@reatom/npm-react"
import { useState } from "react"
import { Link } from "react-router-dom"

function RegistrationPopup() {

    const closePopup = useAction(callPopup)

    const [registrationStage, setRegistrationStage] = useState(1)

    if (registrationStage == 1) {
      return(
        <>
          <div className={styles.popup}>
            <h2 className={styles.title}>Регистрация</h2>
            <div className={styles.input_fields}>
              <input className={styles.input_field} />
              <input className={styles.input_field} />
              <input className={styles.input_field} />
            </div>
            <button className={styles.submit_button  + ' ' + styles.submit_button_stage_1} 
              onClick={() => setRegistrationStage(2)}
            >
              Продолжить
            </button>
            <div className={styles.registration_stage}>1 из 2 шагов</div>
          </div>
        </>
      )
    }

    if (registrationStage == 2) {
      return(
        <>
          <div className={styles.popup}>
            <h2 className={styles.title}>Регистрация</h2>
            <div className={styles.input_fields}>
              <input className={styles.input_field} />
              <input className={styles.input_field} />
            </div>
            <Link to="/main">
              <button 
                className={styles.submit_button + ' ' + styles.submit_button_stage_2}
                onClick={() => closePopup(null)}
              >
                Продолжить
              </button>
            </Link>
            <div className={styles.registration_stage}>2 из 2 шагов</div>
          </div>
        </>
      )
    }
}

export {
    RegistrationPopup
}