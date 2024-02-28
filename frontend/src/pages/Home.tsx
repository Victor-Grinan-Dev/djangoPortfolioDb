import {Box, CssBaseline} from '@mui/material';
import PrimaryAppBar from './templates/PrimaryAppBar';

const style = {
  display: "flex",
  flexDirection: "column",
  alignItems:"center",
}

const Home = () => {
  return (
    <Box component="section" sx={style}>
      <CssBaseline />
      <PrimaryAppBar />  
    </Box>
  )
}

export default Home;