import { useAtom } from "@reatom/npm-react"
import styles from "./basePopup.module.css"
import { popupTypeAtom } from "../../model/actions"
import { RegistrationPopup } from "../RegistrationPopup/registrationPopup"
import { LoginPopup } from "../LoginPopup/loginPopup"

function BasePopup() {

    const [popupType] = useAtom(popupTypeAtom)

    if (popupType == null) {
      return(
        <></>
      )
    }

    if (popupType == "registration") {
      return(
        <>
          <div className={styles.base_popup}>
            <RegistrationPopup />
          </div>
        </>
      )
    }

    if (popupType == "login") {
      return(
        <>
          <div className={styles.base_popup}>
            <LoginPopup />
          </div>
        </>
      )
    }
    
}

export {
    BasePopup
}