import { Select, Flex, Space, InputNumber, Checkbox, Collapse, Button } from "antd"
import { useState } from "react";

export function FilterComponent({ onSearchButtonClick, changeRequestState, changeFilterState }) {

    const currencyChange = (value) => {
        // console.log(`currency selected ${value}`);
        changeRequestState( 'currency', value )
    };
    
    const coinChange = (value) => {
        // console.log(`coin selected ${value}`);
        changeRequestState( 'coin', value )
    };
    
    const payMethodChange = (value) => {
        // console.log(`payMethod selected ${value}`);
        changeFilterState( 'payMethod', value)
    };
    
    const minValueChange = (value) => {
        // console.log(`minValue selected ${value}`);
        changeFilterState( 'minValue', value )
    };
    
    const maxValueChange = (value) => {
        // console.log(`maxValue selected ${value}`);
        changeFilterState( 'maxValue', value )
    };
    
    const marketChange = (value) => {
        // console.log(`market selected ${value}`);
        changeRequestState( 'market', value )
    };
    
    const securityChange = (e) => {
        // console.log(`security selected ${e.target.checked}`);
        changeFilterState( 'security', e.target.checked )
    };

    const collapseFilterItems = [
        {
            key: '1',
            label: 'Дополнительные фильтры поиска',
            children:
                <Flex vertical='vertical' justify="space-evenly" gap='small'>
                    <Space size={30}>
                        Способ платежа:
                        <Select mode="multiple" allowClear id='payMethodSelector' onChange={payMethodChange} style={{ width: 200 }}
                            options={[
                                {
                                    value: 'Sberbank',
                                    label: 'СБЕР'
                                },
                                {
                                    value: 'ADV',
                                    label: 'Advcash'
                                },
                                {
                                    value: 'TINK',
                                    label: 'Tinkoff'
                                },
                                {
                                    value: 'SBP',
                                    label: 'SBP'
                                }
                            ]}
                        />
                    </Space>
                    <Space size={30}>
                        Объём от:
                        <InputNumber
                            id='minValueInput'
                            onChange={minValueChange}
                            addonBefore={'₽'}
                            style={{
                                width: '100%',
                            }}
                            controls={false}
                        />
                        до:
                        <InputNumber
                            id='maxValueInput'
                            onChange={maxValueChange}
                            addonBefore={'₽'}
                            style={{
                                width: '100%',
                            }}
                            controls={false}
                        />
                    </Space>
                    <Space size={30} style={{ width: '100%' }}>
                        Биржи:
                        <Select id='marketSelect' mode="multiple" allowClear onChange={marketChange} style={{ width: 200 }}
                            options={[
                                {
                                    value: 'kucoin',
                                    label: 'KuCoin'
                                },
                                {
                                    value: 'bybit',
                                    label: 'Bybit'
                                },
                                {
                                    value: 'huobi',
                                    label: 'Huobi'
                                },
                                {
                                    value: 'commex',
                                    label: 'Commex'
                                }
                            ]}
                        />
                    </Space>
                    <Space size={10} style={{ width: '100%' }}>
                        Безопасный мейкер: <Checkbox id="securityCheckbox" onChange={securityChange}/>
                    </Space>
                </Flex>
        }
    ]

    return (
        <div className='filter-container'>
            <Flex vertical='vertical' justify="space-evenly" gap={10}>
                <Space size={50} style={{ marginTop: '1rem' }}>
                    <Select showSearch id='currencySelector' onChange={currencyChange} placeholder='Валюта' style={{ width: 120 }}
                        options={[
                            {
                                value: 'RUB',
                                label: 'RUB'
                            }
                        ]}
                    />
                    <Select showSearch id='coinSelector' onChange={coinChange} placeholder='Монета' style={{ width: 120 }} options={[
                        {
                            value: 'USDT',
                            label: 'USDT'
                        },
                        {
                            value: 'BTC',
                            label: 'BTC'
                        },
                        {
                            value: 'ETH',
                            label: 'ETH'
                        }
                    ]} />
                    <Button type="primary" onClick={onSearchButtonClick}> ОК </Button>
                </Space>
                <Collapse items={collapseFilterItems} size="small" />

            </Flex>

        </div>
    )
}