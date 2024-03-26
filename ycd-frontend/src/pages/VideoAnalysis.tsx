import { Button, Container, TextField } from "@mui/material";
import NavBar from "../components/NavBar";

function VideoAnalysis() {
  // Add your component logic here

  return (
    <>
      <NavBar />
      <Container>
        <h1>Video Analysis</h1>
        <div>
          <TextField
            color="primary"
            size="medium"
            variant="filled"
            label="Enter Video URL"
            sx={{
              width: "50%",
              input: { color: "white" },
              label: { color: "white" },
              position: "center",
            }}
          />
          <Button variant="contained" size="large" sx={{ margin: "5px" }}>
            Submit
          </Button>
        </div>
      </Container>
    </>
  );
}

export default VideoAnalysis;
