import { AppBar, Box, Button, Link, Toolbar } from '@mui/material'
// import MenuIcon from '@mui/icons-material/Menu';

import "./appBarStyle.css"


const PrimaryAppBar = () => {
//   const theme = useTheme();
  return (
  <AppBar>
    <Toolbar variant='dense' sx={{height:50}}>
        <Box>
            <Button sx={{color: "white"}}>Menu</Button>
        </Box>
        <Link href="/" 
            sx={{
                color:"white",
                textDecoration: "none",
                cursor: "pointer",
                }}>
                Victor Griñán
        </Link>

    </Toolbar>
  </AppBar>)
}

export default PrimaryAppBar