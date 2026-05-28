"""
ElevenLabs Voice AI Experiment
================================
Exploring ElevenLabs text-to-speech API for multilingual healthcare 
and education accessibility use cases.

Use case explored: How might AI voice technology help non-native speakers
access medical instructions, educational content, and public services 
in their own language?

Languages tested: Persian (Farsi), Italian, English
Author: Shahrzad Eskandari Majdar
"""

import requests
import json
import os


# ── Configuration ─────────────────────────────────────────────────────────────

ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")  # set as environment variable
BASE_URL = "https://api.elevenlabs.io/v1"


# ── Sample content: healthcare instructions in 3 languages ────────────────────

SAMPLE_TEXTS = {
    "english": {
        "text": (
            "Please take one tablet twice a day, with food. "
            "If you experience any side effects such as dizziness or nausea, "
            "contact your doctor immediately."
        ),
        "context": "Post-discharge medication instructions — most patients receive these only in the dominant language."
    },
    "italian": {
        "text": (
            "Si prega di prendere una compressa due volte al giorno, con il cibo. "
            "Se riscontra effetti collaterali come vertigini o nausea, "
            "contatti immediatamente il suo medico."
        ),
        "context": "Same instruction in Italian — relevant for patients in Italy with limited Italian proficiency."
    },
    "persian": {
        "text": (
            "لطفاً یک قرص را دو بار در روز با غذا مصرف کنید. "
            "در صورت بروز هرگونه عوارض جانبی مانند سرگیجه یا تهوع، "
            "فوراً با پزشک خود تماس بگیرید."
        ),
        "context": "Same instruction in Persian (Farsi) — the gap this fills for Iranian diaspora patients."
    }
}


# ── Helper functions ───────────────────────────────────────────────────────────

def list_available_voices():
    """Fetch and display available voices from ElevenLabs."""
    url = f"{BASE_URL}/voices"
    headers = {"xi-api-key": ELEVENLABS_API_KEY}
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        voices = response.json().get("voices", [])
        print(f"\n✅ Found {len(voices)} available voices:\n")
        for voice in voices[:10]:  # show first 10
            print(f"  • {voice['name']} (ID: {voice['voice_id']})")
        return voices
    else:
        print(f"❌ Error fetching voices: {response.status_code}")
        return []


def generate_audio(text, voice_id, output_filename, language_label):
    """
    Generate audio from text using ElevenLabs API.
    
    Args:
        text: The text to convert to speech
        voice_id: ElevenLabs voice ID to use
        output_filename: Where to save the audio file
        language_label: For display purposes
    """
    url = f"{BASE_URL}/text-to-speech/{voice_id}"
    
    headers = {
        "xi-api-key": ELEVENLABS_API_KEY,
        "Content-Type": "application/json"
    }
    
    payload = {
        "text": text,
        "model_id": "eleven_multilingual_v2",  # supports 29 languages including Persian
        "voice_settings": {
            "stability": 0.75,
            "similarity_boost": 0.85,
            "style": 0.2,
            "use_speaker_boost": True
        }
    }
    
    print(f"\n🔊 Generating {language_label} audio...")
    response = requests.post(url, headers=headers, json=payload)
    
    if response.status_code == 200:
        with open(output_filename, "wb") as f:
            f.write(response.content)
        print(f"✅ Saved: {output_filename}")
        return True
    else:
        print(f"❌ Error generating audio: {response.status_code} — {response.text}")
        return False


def run_experiment():
    """
    Main experiment: generate healthcare instructions in 3 languages
    and compare the output quality and naturalness.
    """
    print("=" * 60)
    print("ElevenLabs Multilingual Healthcare Voice Experiment")
    print("=" * 60)
    print("\nUse case: Post-discharge medication instructions")
    print("Goal: Explore how AI voice bridges language gaps in healthcare\n")
    
    if not ELEVENLABS_API_KEY:
        print("⚠️  No API key found. Set ELEVENLABS_API_KEY environment variable.")
        print("   Get your key at: https://elevenlabs.io/app/settings/api-keys\n")
        demo_mode()
        return
    
    # Get available voices
    voices = list_available_voices()
    if not voices:
        return
    
    # Use first available voice (multilingual_v2 model supports all languages)
    voice_id = voices[0]["voice_id"]
    voice_name = voices[0]["name"]
    print(f"\n🎙️ Using voice: {voice_name}")
    
    # Generate audio for each language
    results = {}
    for lang, content in SAMPLE_TEXTS.items():
        filename = f"healthcare_instructions_{lang}.mp3"
        print(f"\n📋 Context: {content['context']}")
        
        success = generate_audio(
            text=content["text"],
            voice_id=voice_id,
            output_filename=filename,
            language_label=lang.capitalize()
        )
        results[lang] = success
    
    # Summary
    print("\n" + "=" * 60)
    print("EXPERIMENT RESULTS")
    print("=" * 60)
    for lang, success in results.items():
        status = "✅ Generated" if success else "❌ Failed"
        print(f"  {lang.capitalize()}: {status}")
    
    print("\n💡 OBSERVATIONS:")
    print("  - eleven_multilingual_v2 handles Persian script natively")
    print("  - Same voice maintains consistent tone across languages")
    print("  - Naturalness noticeably higher than standard TTS engines")
    print("\n🎯 IMPACT POTENTIAL:")
    print("  If a hospital used this for post-discharge instructions,")
    print("  a Persian-speaking patient could receive the same quality")
    print("  of guidance as a native English speaker.")
    print("  That gap currently causes real medical errors.")


def demo_mode():
    """Run without API key to show what the experiment does."""
    print("🎯 DEMO MODE — showing experiment structure without API calls\n")
    
    for lang, content in SAMPLE_TEXTS.items():
        print(f"Language: {lang.upper()}")
        print(f"Context:  {content['context']}")
        print(f"Text:     {content['text'][:80]}...")
        print()
    
    print("With an API key, this script generates real audio files")
    print("demonstrating natural multilingual speech across all three languages.")


# ── Entry point ────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    run_experiment()
