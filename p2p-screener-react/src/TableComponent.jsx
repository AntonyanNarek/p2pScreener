import { Table, Flex } from "antd"
import { useState, useEffect } from "react"

const columns = [
    {
        title: 'Мейкер',
        dataIndex: 'maker',
        key: 'maker'
    },
    {
        title: 'Цена',
        dataIndex: 'price',
        key: 'price'
    },
    {
        title: 'Детали',
        dataIndex: 'info',
        key: 'info'
    },
]

export function TableComponent({data}) {

    const [parsedBuy, setParsedBuy] = useState([])
    const [parsedSell, setParsedSell] = useState([])

    useEffect(() => {
        if(data.buy !== undefined && data.sell !== undefined){
            var buyKey = 0
            var sellKey = 0
            var buyTemp = []
            var sellTemp = []
            for (const [key, value] of Object.entries(data.buy)){
                console.log(value);
                for (const order in value){
                    console.log(order);
                    buyTemp.push({key: "buy" + buyKey++, maker: 'maker', price: value[order].price, info:  value[order].name})
                }
            }
            setParsedBuy(buyTemp)
            for (const [key, value] of Object.entries(data.sell)){
                console.log(value);
                for (const order in value){
                    console.log(order);
                    sellTemp.push( ...parsedSell, {key: "sell" + sellKey++ ,maker: 'maker', price:  value[order].price, info:  value[order].name})
                }
            }
            setParsedSell(sellTemp)
        }        
    }, [data])

    return (
        <Flex justify="space-evenly" gap={10}>
            <Table columns={columns} dataSource={parsedBuy} style={{ width: '100%' }} />
            <Table columns={columns} dataSource={parsedSell} style={{ width: '100%' }} />
        </Flex>

    )
}
