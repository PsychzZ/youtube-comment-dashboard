import {
  Button,
  Container,
  TextField,
  Alert,
  Fade,
  CircularProgress,
} from "@mui/material";
import NavBar from "../components/NavBar";
import { useContext } from "react";
import { VideoContext } from "../hooks/useLink";
import { PieChart } from "@mui/x-charts/PieChart";

export function VideoAnalysis() {
  const {
    commentStats,
    submitVideoUrl,
    notValidUrl,
    setOpen,
    open,
    videoUrl,
    setVideoUrl,
    setNotValidUrl,
    loading,
    setLoading,
  } = useContext(VideoContext);

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
            value={videoUrl.videoUrl}
            onChange={(event) => {
              setVideoUrl({ videoUrl: event.target.value });
              setNotValidUrl(false);
            }}
            error={notValidUrl}
          />
          <Button
            variant="contained"
            size="large"
            sx={{ margin: "5px" }}
            onClick={() => {
              submitVideoUrl(videoUrl);
              setLoading(true);
            }}
          >
            Submit
          </Button>
        </div>
        <div>
          <h2>Comments</h2>
          {loading ? (
            <div style={{ display: "flex", justifyContent: "center" }}>
              <CircularProgress />
            </div>
          ) : (
            <>
              {commentStats === undefined ? (
                <></>
              ) : (
                <>
                  <h3>Positive Comments: {commentStats.positive_count}</h3>
                  <h3>Neutral Comments: {commentStats.neutral_count}</h3>
                  <h3>Negative Comments: {commentStats.negative_count}</h3>
                  <div style={{ width: "80%", height: 300 }}>
                    <PieChart
                      series={[
                        {
                          data: [
                            {
                              label: "Positive",
                              value: commentStats.positive_count,
                            },
                            {
                              label: "Neutral",
                              value: commentStats.neutral_count,
                            },
                            {
                              label: "Negative",
                              value: commentStats.negative_count,
                            },
                          ],
                        },
                      ]}
                    ></PieChart>
                  </div>
                </>
              )}
            </>
          )}
        </div>
      </Container>
    </>
  );
}

export default VideoAnalysis;
