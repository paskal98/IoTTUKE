import React, { useEffect, useState } from 'react';
import { InputText } from 'primereact/inputtext';
import { Form, Field } from 'react-final-form';
import { Button } from 'primereact/button';
import styles from "./DevicesList.module.css"
import { Dropdown } from 'primereact/dropdown';
import { Calendar } from 'primereact/calendar';
import { Checkbox } from 'primereact/checkbox';
import { Dialog } from 'primereact/dialog';
import { Divider } from 'primereact/divider';
import { classNames } from 'primereact/utils';


function DeviceDetailed(){


    const [showMessage, setShowMessage] = useState(false);
    const [formData, setFormData] = useState({});





    const validate = (data) => {
        let errors = {};

        if (!data.name) {
            errors.name = 'Name is required.';
        }

        if (!data.serialNumber) {
            errors.serialNumber = 'serialNumber is required.';
        }



        return errors;
    };


    const onSubmit = (data, form) => {
        setFormData(data);
        setShowMessage(true);

        form.restart();
    };
    const isFormFieldValid = (meta) => !!(meta.touched && meta.error);
    const getFormErrorMessage = (meta) => {
        return isFormFieldValid(meta) && <small className="p-error">{meta.error}</small>;
    };

    const dialogFooter = <div className="flex justify-content-center"><Button label="OK" className="p-button-text" autoFocus onClick={() => setShowMessage(false) } /></div>;

    return (
        <div className="form-demo">
            <Dialog visible={showMessage} onHide={() => setShowMessage(false)} position="top" footer={dialogFooter}
                    showHeader={false} breakpoints={{'960px': '80vw'}} style={{width: '30vw'}}>
                <div  className={styles.add__device__success__msg__container}>
                    <i className="pi pi-check-circle" style={{fontSize: '5rem', color: 'var(--green-500)'}}></i>
                    <h5>Oh, Great!</h5>
                    <p style={{lineHeight: 1.5, textIndent: '1rem'}}>
                        Your device with name <b>{formData.name}</b> and serial-number <b>{formData.serialNumber}</b>
                        Was successfully added to system
                    </p>
                </div>
            </Dialog>

            <div className="flex justify-content-center">
                <div style={{marginBottom:"2.rem"}} className="card">
                    <div className={styles.device__header__text}>Add new Device</div>
                    <Form onSubmit={onSubmit}
                          initialValues={{name: '', serialNumber: ''}}
                          validate={validate} render={({handleSubmit}) => (
                        <form onSubmit={handleSubmit} className="p-fluid">
                            <Field name="name" render={({input, meta}) => (
                                <div className="field">
                                    <span className="p-float-label">
                                        <InputText id="name" {...input} autoFocus
                                                   className={classNames({'p-invalid': isFormFieldValid(meta)})}/>
                                        <label htmlFor="name"
                                               className={classNames({'p-error': isFormFieldValid(meta)})}>Name*</label>
                                    </span>
                                    {getFormErrorMessage(meta)}
                                </div>
                            )}/>

                            <Field name="serialNumber" render={({input, meta}) => (
                                <div className="field">
                                    <span className="p-float-label">
                                        <InputText id="serialNumber" {...input} autoFocus
                                                   className={classNames({'p-invalid': isFormFieldValid(meta)})}/>
                                        <label htmlFor="serialNumber"
                                               className={classNames({'p-error': isFormFieldValid(meta)})}>serialNumber*</label>
                                    </span>
                                    {getFormErrorMessage(meta)}
                                </div>
                            )}/>


                            <Button type="submit" label="Add device" className="mt-2"/>
                        </form>
                    )}/>
                </div>
            </div>
        </div>
    );
}


export default DeviceDetailed;