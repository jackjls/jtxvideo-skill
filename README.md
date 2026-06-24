# jtxvideo-skill

`jtxvideo-skill` is a personal Codex skill for producing Jiang Tongxue's AI-finance talking-head short videos with a staged Codex + HyperFrames workflow.

It turns a recorded Chinese talking-head video into a reviewable video project by enforcing this sequence:

1. Preprocess video to stable H.264 / 30fps / fixed keyframes.
2. Transcribe first and output SRT before any edit planning.
3. Wait for SRT confirmation.
4. Analyze transcript structure.
5. Generate a storyboard table.
6. Wait for storyboard confirmation.
7. Copy the project `design.md`.
8. Generate a HyperFrames HTML / CSS / GSAP project.
9. Review visuals and export a 2K 60fps publishing version.

## Repository Structure

```text
.
├── skills/
│   └── jtxvideo-skill/
│       ├── SKILL.md
│       ├── agents/
│       │   ├── openai.yaml
│       │   └── interface.yaml
│       ├── design.md
│       └── templates/
├── scripts/
│   └── validate_skill.py
├── .github/workflows/
│   └── validate.yml
├── LICENSE
└── VERSION
```

## Install

Copy the skill folder into your Codex skills directory:

```bash
mkdir -p ~/.codex/skills
cp -R skills/jtxvideo-skill ~/.codex/skills/
```

Restart Codex after installing or updating the skill.

## Usage

Use this prompt:

```text
用 jtxvideo-skill 处理这个口播视频，按预处理、SRT 确认、文案结构、分镜表、设计、HyperFrames 渲染和 2K60 导出的流程走。
```

The skill is intentionally review-gated. It should not jump directly from source video to a finished edit.

## Maintenance

Validate before committing:

```bash
python3 scripts/validate_skill.py skills/jtxvideo-skill
```

The GitHub Actions workflow runs the same validation on every push and pull request.

