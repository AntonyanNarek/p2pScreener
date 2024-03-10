import { Layout } from 'antd'
import './AppLayout.css'
import { MainContainer } from './MainContainer';

const { Content, Footer } = Layout;

export function AppLayout() {
    return (
        <Layout>
            <Content className='content'>
                p2p screener
                <MainContainer />
            </Content>
            <Footer>
                Footer
            </Footer>
        </Layout>
    )
}