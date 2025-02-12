# yt_downloaderm_v1.02.1

**[Youtube DownloadErm 中文版](https://hackmd.io/@luouo/rk6KPN0qA)**

**[Youtube DownloadErm Eng ver](https://hackmd.io/@luouo/rJrqq17C0)**

![image](https://github.com/user-attachments/assets/83cca4a6-2cb8-49c6-a87f-38ec45165dae)

## Introduction
Why did I create this tool? Simply put, I got fed up with the web-based YouTube download tools. They are filled with ads, slow, and can't download videos longer than an hour. So, this tool was born.

## Usage Instructions

1. Enter the YouTube link.
2. Click the "Search Resolution" button.
3. Select the desired resolution.
4. Choose either MP4 or MP3 format.
5. Select the file save location.
6. Choose the download method.
7. Click the "Download Video" button to start downloading.

## Download Method Descriptions

1. **No Processing**:  
   Downloads the entire video without any modifications, providing the fastest speed.

2. **Quick Cut**:  
   Downloads the entire video first and then trims it based on the user's selected time range using the ffmpeg tool. The resulting video may be slightly longer than the specified time range.  
   Example: If the "Start Time" is set to "00:05:20" and the "End Time" is "00:06:20", the final video might range from "00:05:18" to "00:06:22", with a total length of approximately 1 minute and 4 seconds.

3. **Detailed Cut**:  
   After performing a Quick Cut, the video is further decoded and re-encoded, ensuring the final output matches the exact time range selected by the user.

**Execution Time (MP4)**: No Processing < Quick Cut < Detailed Cut  
**Execution Time (MP3)**: No Processing < Quick Cut = Detailed Cut  

**Note**: When downloading in MP3 format, the execution time and result for Quick Cut and Detailed Cut are the same.

## Advantages

1. **No Ads**: Absolutely no built-in ads, providing a smoother user experience.
2. **High Quality**: Supports high-quality downloads (up to 8K) with stable resolution.
3. **No Time Limit**: Allows downloading videos longer than an hour, with no limit on the number of downloads.
4. **Unlimited Speed**: Download speed is solely dependent on the user's internet connection.
5. **Basic Editing**: Offers basic video editing features for downloaded videos.

## Changelog 

*2024/10/2 ver1.02* 
- Fixed the issue where "Search Resolution" caused an error.
- Now, by selecting the "Playlist?" option on the right, you can download entire playlists.

*2025/2/12 ver1.02.1*
- Fix the issue where the entire program cannot download videos properly.
- Fix the issue where specific videos cannot be downloaded.
