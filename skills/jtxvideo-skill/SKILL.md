---
name: jtxvideo-skill
description: >
  Produce Jiang Tongxue's AI-finance talking-head Douyin videos from recorded口播视频
  using the approved staged workflow: preprocess, transcribe SRT, wait for confirmation,
  analyze structure, storyboard, design, HyperFrames render, review, and export 2K 60fps.
  Use when the user asks to process口播视频, make同款剪辑风格, generate AI金融黑金商务视频,
  or says to use jtxvideo-skill. Do not use for generic video editing that skips
  SRT/storyboard approval.
---

# JTX Video Skill

## Purpose

Turn a recorded Chinese talking-head video into the user's standard AI-finance Douyin video:

- the speaker is the visual anchor
- motion graphics explain finance/AI/product events
- the style is black-gold business, not flashy template editing
- the workflow is staged and reviewable
- final export includes a 2K 60fps version for publishing

## Non-Negotiable Workflow

Never jump straight from source video to a finished edit. Move in this order:

1. **Create project folder**
   - Use `hyperframes-runs/<project-slug>/`.
   - Keep all generated files inside the project folder.

2. **Preprocess source video**
   - Convert the input video to stable H.264 at 30fps with fixed keyframes.
   - Default command shape:
     ```bash
     ffmpeg -i input.mp4 -c:v libx264 -g 30 -keyint_min 30 -r 30 output_keyed.mp4
     ```
   - Save as `workflow/01_preprocessed_keyed.mp4` and copy/use as `assets/talk-main-keyed.mp4`.

3. **Extract audio and transcribe**
   - Extract clean audio, usually `workflow/01_audio_16k.wav`.
   - Use a Chinese-capable high-accuracy transcription model. Do not use `.en` Whisper models for Chinese.
   - First output to the user must be the SRT file path and content summary only.
   - Save SRT as `workflow/01_audio_16k.srt`.

4. **SRT 文件确认**
   - Do not analyze the script, storyboard, or render before the user confirms SRT.

5. **Analyze content structure**
   - Segment the transcript into content types:
     - 开场钩子
     - 痛点呈现
     - 正误对比
     - 流程清单
     - 方法论讲解
     - 案例 / 数据
     - 行动号召
     - 金融观点 / 市场判断
     - AI工具实测 / 产品事件
   - Save as `workflow/05_content_structure_for_review.md`.
   - Ask the user to review.

6. **文案结构确认**
   - Do not generate storyboard until confirmed.

7. **Generate storyboard**
   - Use `templates/storyboard-template.md` as the schema.
   - Include time range,口播内容,文案类型,画面策略,动效元素,音效建议,审核关注点.
   - Save as `workflow/06_storyboard_for_review.md`.
   - Ask the user to review.

8. **分镜表确认**
   - Do not generate HyperFrames code before storyboard confirmation.

9. **设计确认并生成项目 design.md**
   - Copy `templates/design-default.md` into the project as `design.md`.
   - Adapt only what the current video needs.
   - Keep the approved defaults unless the user asks otherwise.

10. **Generate HyperFrames project**
    - Use one continuous talking-head video as the base layer.
    - Do not repeatedly mount many slices of the same MP4; it can cause gray preview, freezing, or the speaker disappearing.
    - Put cards, captions, and visual explanations in separate timed overlay layers.
    - Main video must be muted; use a separate `<audio>` track.

11. **最终视觉确认**
    - Generate preview/review renders.
    - Use screenshots/contact sheets for visual checks.
    - Apply user feedback on subtitle height, size, transparency, person brightness, card placement, and motion restraint.

12. **Final export**
    - Render a high-quality 1080x1920 60fps master.
    - Re-mux full original audio after HyperFrames rendering.
    - Export final 2K portrait version: `1440x2560 / 60fps`.
    - Verify with `ffprobe`.

## Default File Contract

Use this structure:

```text
hyperframes-runs/<project-slug>/
  assets/
    talk-main-keyed.mp4
    talk-main-audio.m4a
  workflow/
    01_preprocessed_keyed.mp4
    01_audio_16k.wav
    01_audio_16k.srt
    05_content_structure_for_review.md
    06_storyboard_for_review.md
  templates/            # optional project-local copies
  design.md
  index.html
  renders/
    review.mp4
    contact-sheet.jpg
    preview-frame.jpg
    final-2k60.mp4
```

## Visual Defaults

Use `templates/design-default.md` as the source of truth for:

- AI金融黑金商务风
- transparent, readable subtitle bar
- bright speaker/person layer
- restrained cards and motion
- no noisy gold line or flashy decoration
- Douyin-safe subtitles

## Quality Gates

Before telling the user a render is ready:

- Run `npx hyperframes validate`.
- Run `npx hyperframes inspect --samples 12` or denser for risky layouts.
- Run `ffprobe` on final MP4.
- Confirm video stream dimensions, frame rate, and duration.
- Confirm audio duration is complete and close to video duration.
- Generate at least one preview frame or contact sheet.

## Export Defaults

Review version:

- `1080x1920`
- `30fps` or `60fps` depending on iteration speed
- complete audio remuxed from the original processed audio

Final publishing version:

- `1440x2560`
- `60fps`
- H.264 High Profile
- AAC audio
- `+faststart`

Recommended final encode shape:

```bash
ffmpeg -i master_1080p60.mp4 \
  -vf "scale=1440:2560:flags=lanczos,fps=60" \
  -c:v libx264 -preset slow -crf 17 -pix_fmt yuv420p \
  -profile:v high -level 5.2 -movflags +faststart \
  -c:a copy final-2k60.mp4
```

## Avoid

- Do not cut before SRT confirmation.
- Do not skip storyboard review.
- Do not make the production process itself appear in the video unless that is the topic.
- Do not add full-height scrolling gold lines or flashy decorative effects.
- Do not darken the entire speaker with a heavy black overlay.
- Do not put subtitles too low where Douyin UI covers them.
- Do not make subtitle backgrounds fully opaque black.
- Do not invent financial facts, stock claims, prices, dates, or performance data.
- Do not imply investment advice or喊单.

## Response Style

When running this skill, report the current stage and next approval point. Keep the user in control of:

- SRT confirmation
- 文案结构确认
- 分镜表确认
- 设计确认
- 最终视觉确认

If the user says "继续", continue to the next unblocked stage.
