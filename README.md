# MIDI to Jianpu

## Project Overview

This tool primarily converts MIDI files into Jianpu musical notation.

This project is built for an individual who is learning the Erhu and is made primarily to help with learning new songs that don't have their Jianpu notation easily available, such as the majority of western music.

## Tech Stack

- Code: Python, with Gradio and MIDO + UV for managing the virtual environment and unittest for unit testing
- Deployment: Hugging Face Spaces
- Development in two parallel repos, a development one for GitHub and a production one for Hugging Face Spaces

## Features

- Upload a MIDI file and show the Jianpu notation for a given channel as a string.
- Transpose the MIDI file by a given semitone and octave offset, changing the song into a key that is easier to play.
- Change the time interval multiplier - this is a relative but not an accurate time scale which allows the user to adjust the time spacings, showing how long to wait between playing notes or for how long to hold the note for.
- Download the altered MIDI file, with the selected channel and transposition - allowing the user to play the modified song locally to hear something that represents the notes better than the original file.

## Run

The app is available on [Hugging Face Spaces](https://huggingface.co/spaces/jadeprideaux/MIDItoJianpu).

Run app locally: `uv run app.py`

Run tests with: `uv run python -m unittest discover -s test -p "*_test.py"`

## File Structure

```bash
├── code/ - a module for the various functional elements of the program
├── test/ - a module for the unit tests of the project
├── app.py - the project's entry point and interface
```

## Development Methodology

This project followed an agile goal based sprints with the following steps in each cycle.

- Plan: Decide on the most important system requirements with the client and define the goal for the sprint.
- Design: Decide how to build the system to meet these requirements.
- Develop: Implement the systems to fulfil the given requirements.
- Test: Simple manual testing to check features work as intended followed by some basic unit tests.
- Deploy: Deploy to Hugging Face Spaces.
- Review: User testing session, to check how well goals have been met and review the overall sprint.

The user testing session is done after deployment since this is just a personal tool and it doesn't need to be perfect at that stage. This also helps with doing user testing remotely.

The review session at the end of one sprint if often combined with the planning session of the next sprint so that discussions can involve how well the tool has met the requirements and what needs to be considered for the next sprint.
