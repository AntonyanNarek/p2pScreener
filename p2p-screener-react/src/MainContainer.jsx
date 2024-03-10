import { FilterComponent } from "./FilterComponent"
import './App.css'
import { TableComponent } from "./TableComponent"
import { Flex } from "antd"
import axios from 'axios'
import { useState, useEffect } from "react"


const url = '127.0.0.1:80'

export function MainContainer() {

    const [data, setData] = useState([])
    const [request, setRequest] = useState({})
    const [filter, setFilter] = useState({})

    const changeRequestState = (key, value) => {
        // console.log(key + " " + value);
        setRequest({
            ...request,
            [key]: value
        })
    }

    const changeFilterState = (key, value) => {
        console.log(key + " " + value);
        setFilter({
            ...request,
            [key]: value
        })
    }


    const onSearchButtonClick = (e) => {
        e.preventDefault()
        console.log(request);
        axios.post('http://' + url + '/orders/filter',
            request
        ).then((response) => {
            setData(response.data)
            console.log(response.data)
        })
    }

    return (
        <div className='main-container'>
            <Flex vertical='vertical' justify="space-evenly" gap={10}>

                <FilterComponent onSearchButtonClick={onSearchButtonClick} changeRequestState={changeRequestState} changeFilterState={changeFilterState}/>
                <TableComponent data={data} />
            </Flex>
        </div>
    )
}