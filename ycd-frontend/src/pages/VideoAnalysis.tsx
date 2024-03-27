import {
  Button,
  Container,
  TextField,
  Alert,
  Snackbar,
  Fade,
} from "@mui/material";
import NavBar from "../components/NavBar";
import { useEffect, useState } from "react";

function VideoAnalysis() {
  const [videoUrl, setVideoUrl] = useState<string>("");
  const [notValidUrl, setNotValidUrl] = useState<boolean>(false);
  const [open, setOpen] = useState<boolean>(true);

  useEffect(() => {
    if (notValidUrl) {
      setOpen(true);
    }
  }, [videoUrl, notValidUrl]);

  function submitVideoUrl() {
    if (videoUrl) {
      console.log("Video URL submitted:", videoUrl);
      const test = videoUrl?.split("v=")[1];
      const videoId = test?.split("&")[0];
      if (videoId !== undefined) {
        console.log(videoId);
      } else {
        setNotValidUrl(true);
      }
    }
  }

  return (
    <>
      <NavBar />
      <div>
        {notValidUrl ? (
          <div>
            <Fade in={open} timeout={1000}>
              <Alert
                severity="error"
                variant="filled"
                sx={{
                  width: "25%",
                  display: "flex",
                  float: "right",
                  m: "1em auto",
                  right: "0",
                  position: "absolute",
                }}
                onClose={() => {
                  setOpen(false);
                }}
              >
                Invalid URL
              </Alert>
            </Fade>
          </div>
        ) : (
          <></>
        )}
      </div>
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
            value={videoUrl}
            onChange={(event) => {
              setVideoUrl(event.target.value);
              setNotValidUrl(false);
            }}
            error={notValidUrl}
          />
          <Button
            variant="contained"
            size="large"
            sx={{ margin: "5px" }}
            onClick={() => {
              submitVideoUrl();
            }}
          >
            Submit
          </Button>
          <Snackbar
            anchorOrigin={{ vertical: "top", horizontal: "right" }}
            open={false}
            message="Invalid URL"
          />
        </div>
      </Container>
    </>
  );
}

export default VideoAnalysis;
