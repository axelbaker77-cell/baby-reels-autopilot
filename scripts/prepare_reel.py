#!/usr/bin/env python3
"""Prepare a realistic Indian baby Reel brief without paid APIs.

This first free setup creates a daily story, video-generation prompt and caption.
It does not fabricate a video or publish to Instagram; those require a video
provider and Meta publishing credentials, configured separately.
"""
from __future__ import annotations
import json
import os
import random
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "output"
OUT.mkdir(exist_ok=True)

IDEAS = [
    {
        "title": "नन्हा शेफ और छुपा हुआ लड्डू",
        "hook": "जब मम्मी ने पूछा—लड्डू किसने खाया?",
        "beats": [
            "0-3s: प्यारा भारतीय toddler रसोई के दरवाज़े पर मासूम चेहरा बनाकर खड़ा है।",
            "3-8s: उसके गाल पर हल्का सा बेसन/लड्डू का चूरा दिखता है; वह पीछे छुपे खाली प्लेट को धीरे से सरकाता है।",
            "8-13s: मम्मी की आवाज़ सुनकर बच्चा कैमरे की तरफ देखकर मज़ेदार मासूम मुस्कान देता है।",
        ],
        "punchline": "बच्चा: मैंने तो बस quality check किया! (बच्चे की प्यारी, हल्की आवाज़)",
    },
    {
        "title": "होमवर्क से बचने की स्मार्ट तरकीब",
        "hook": "जब पापा ने होमवर्क पूछा…",
        "beats": [
            "0-3s: प्यारा भारतीय toddler मेज़ पर खुली कॉपी के सामने बैठा है।",
            "3-8s: वह पेंसिल उठाता है, फिर खिलौने को कॉपी पर रखकर ऐसे देखता है जैसे खिलौना होमवर्क करेगा।",
            "8-13s: बच्चा कैमरे की तरफ गंभीर चेहरा बनाकर फिर खिलखिलाता है।",
        ],
        "punchline": "बच्चा: पापा, team work चल रहा है!",
    },
    {
        "title": "नन्हा डांस मास्टर",
        "hook": "घर में गाना बजते ही…",
        "beats": [
            "0-3s: भारतीय toddler रंगीन आरामदायक कपड़ों में कमरे में खड़ा है।",
            "3-8s: वह दो-तीन प्यारे, सुरक्षित और सरल toddler dance moves करता है।",
            "8-13s: एक छोटा सा funny freeze pose और बड़ी मुस्कान।",
        ],
        "punchline": "बच्चे का confident expression ही punchline है।",
    },
]

def main() -> None:
    day = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    seed = int(day.replace("-", ""))
    idea = random.Random(seed).choice(IDEAS)
    prompt = (
        "Create a photorealistic, wholesome vertical Instagram Reel, 9:16, "
        "10–15 seconds, featuring a fictional Indian toddler (clearly fictional, "
        "not resembling a real child or celebrity). Natural Indian home setting, "
        "warm daylight, realistic skin texture, expressive but age-appropriate "
        "facial expressions, natural toddler movement, cinematic phone-camera "
        "look, stable framing, clean background. No unsafe actions, no adult "
        "themes, no logos, no watermarks, no text baked into the image. "
        + " ".join(idea["beats"]) + " "
        + idea["punchline"]
    )
    caption = (
        f'{idea["hook"]}\n\n{idea["punchline"]}\n'
        "#IndianBaby #FunnyBaby #BabyReels #CuteBaby #FunnyReels #DesiBaby"
    )
    data = {
        "date_utc": day,
        "style": "realistic",
        "format": {"aspect_ratio": "9:16", "duration_seconds": "10-15"},
        "title": idea["title"],
        "hook": idea["hook"],
        "story_beats": idea["beats"],
        "video_prompt": prompt,
        "caption": caption,
        "status": "brief_ready_video_not_generated",
        "note": "No paid service is called. Configure a video provider before generation and Meta Graph API credentials before publishing."
    }
    (OUT / "reel-brief.json").write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    md = f'# {idea["title"]}\n\n**Hook:** {idea["hook"]}\n\n'
    md += "\n".join(f"- {b}" for b in idea["beats"])
    md += f'\n\n**Punchline:** {idea["punchline"]}\n\n## Video prompt\n\n{prompt}\n\n## Caption\n\n{caption}\n'
    (OUT / "reel-brief.md").write_text(md, encoding="utf-8")
    print("Created output/reel-brief.json and output/reel-brief.md")

if __name__ == "__main__":
    main()
