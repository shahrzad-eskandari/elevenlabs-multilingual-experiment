# 🔊 ElevenLabs Multilingual Healthcare Voice Experiment

Exploring how AI voice technology can bridge language gaps in healthcare, 
education, and accessibility for non-native speakers.

## The Problem

When a patient is discharged from hospital in a country where they don't speak 
the dominant language fluently, they often receive critical medical instructions 
they cannot fully understand. This causes real, preventable medical errors.

The same gap exists in education, public services, and emergency communication.

## What This Explores

Using the **ElevenLabs multilingual v2 model** to generate natural-sounding 
post-discharge medication instructions in three languages simultaneously:

- 🇬🇧 **English** — baseline
- 🇮🇹 **Italian** — for Persian-speaking patients living in Italy  
- 🇮🇷 **Persian (Farsi)** — native language, highest comprehension

The experiment tests whether a single AI voice model can maintain consistent 
tone, naturalness, and clarity across all three — and whether the quality gap 
vs. standard TTS engines is meaningful enough to change real outcomes.

## Setup

```bash
pip install requests

# Set your ElevenLabs API key
export ELEVENLABS_API_KEY="your_key_here"

python experiment.py
```

Get a free API key at [elevenlabs.io](https://elevenlabs.io/app/settings/api-keys)

## Output

The script generates three `.mp3` files:
- `healthcare_instructions_english.mp3`
- `healthcare_instructions_italian.mp3`  
- `healthcare_instructions_persian.mp3`

Run without an API key to see the demo mode and experiment structure.

## Why This Matters

> "ElevenLabs is deploying the technology most likely to change what it means 
> for someone to receive medical guidance in their own language and voice."

This experiment is a small, personal exploration of that idea — built by 
someone who has experienced the language barrier in healthcare firsthand.

---

**Author:** Shahrzad Eskandari Majdar  
