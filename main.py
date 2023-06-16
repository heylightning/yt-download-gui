import streamlit as st
from pytube import YouTube

temp = []
st.set_page_config(page_title='A .pmWEB creation.', layout='wide')
st.header("Download audios and videos from any YouTube link 🔗")
st.caption('A .pmWEB creation. Sourced at heylightning/yt-download-gui')

ytLink = st.text_input("Enter the YT link here:", placeholder='Example: https://www.youtube.com/watch?v=Xu6oHc_20ow')

try:
    if len(ytLink) > 5 and ytLink[ : 24] == 'https://www.youtube.com/':
        link = YouTube(str(ytLink))
        option = st.radio(
            "Choose your option:",
            ('None', 'Audio', 'Video'))
        if option == 'Audio':
            st.write('You selected Audio.')
            if st.button("Compute", key='audioCompBTN'):
                st.caption('Operation in progress... please do not click anywhere.')
                audio = link.streams.filter(only_audio=True).first()
                st.caption('Downloading audio...')
                audioLink = audio.download(output_path='./audio_files')
                st.success(f"Audio file downloaded successfully! You can download the file from here or can access the file already downloaded file from: {audioLink}", icon='✅')

                st.subheader('Audio Preview')
                audio_file = open(str(audioLink), 'rb')
                audio_bytes = audio_file.read()
                st.audio(audio_bytes, format='audio/ogg')

        elif option == 'Video':
            st.write('You selected Video.')
            if st.button("Compute", key='videoCompBTN'):
                st.caption('Operation in progress... please do not click anywhere.')
                stream = link.streams.filter(file_extension='mp4').first()
                st.caption('Downloading video...')
                videoLink = stream.download(output_path='./video_files')
                st.success(f"Audio file downloaded successfully! You can download the file from here or can access the file already downloaded file from: {videoLink}", icon='✅')

                st.subheader('Video Preview')
                video_file = open(str(videoLink), 'rb')
                video_bytes = video_file.read()
                st.video(video_bytes, format='video/mp4')

except Exception as err:
    st.error(f'Error: {err}', icon='❌')
