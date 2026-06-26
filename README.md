# jtxvideo-skill

`jtxvideo-skill` 是一套用于 **Codex + HyperFrames 口播视频制作** 的标准化 Skill。

它不是普通剪辑模板，而是把一条录好的中文口播视频，按可审核、可复用、可持续迭代的流程，制作成适合 AI 金融、产业分析、工具评测等内容发布的视频工程。

## 项目背景

这个 Skill 沉淀了一套 **Codex + HyperFrames 口播视频生产方法**，目标是把“先理解内容、再设计剪辑、最后生成工程”的流程标准化。

这套视频流程强调：

- 先理解口播内容，再做剪辑设计
- 先让用户审核 SRT、文案结构和分镜，再生成视频工程
- 画面风格专业、克制、可信，不做花哨模板感
- 重点通过动态关键词、真实素材和完整字幕表达
- 避免喊单感、荐股感和夸张营销感

## 适用场景

适合处理这类视频：

- AI 金融口播视频
- 财报 / 产业链 / 公司事件解读
- AI 工具实测类视频
- 投研方法论讲解
- 需要用 HyperFrames 生成 HTML / CSS / GSAP 动画工程的视频
- 需要固定生产流程、方便反复复用的创作者视频项目

不适合：

- 纯娱乐剪辑
- 不需要 SRT 审核和分镜审核的快速剪辑
- 强特效、强模板、强包装的带货视频
- 直接从素材跳到成片、没有人工审核环节的视频生产

## 核心流程

Skill 强制按以下顺序推进：

1. 创建项目目录
2. 预处理视频
3. 提取音频并转写 SRT
4. 等待用户确认 SRT
5. 分析文案结构
6. 等待用户确认文案结构
7. 生成分镜表
8. 等待用户确认分镜表
9. 生成项目 `design.md`
10. 生成 HyperFrames 工程
11. 生成预览版并做视觉审核
12. 输出 2K / 60fps 发布版

关键原则：

**AI 不直接剪视频，先把剪辑逻辑做成可审核的计划。**

## 横屏与竖屏规则

每个项目必须先用 `ffprobe` 判断源视频方向，再选择设计规则。

| 源视频方向 | 审核画布 | 最终画布 | 设计策略 |
| --- | --- | --- | --- |
| 横屏 | `2560x1440` | `2560x1440 / 60fps` | 可以使用“左素材 / 右人物”的资料分屏布局 |
| 竖屏 | `1080x1920` | `1440x2560 / 60fps` | 人物必须始终在屏幕上，素材和动效只能作为叠加解释层 |

竖屏特别规则：

- 人物始终是主画面
- 素材不能全屏接管画面
- 外部截图、图表、封面图只做上方浮层、侧边浮层或短时证据条
- 动态重点字不能遮挡眼睛、嘴巴和底部字幕
- 如果某句话弹窗突兀，就删除弹窗，只保留完整字幕

横屏特别规则：

- 当素材本身是重点时，可以让素材成为主视觉
- 长时间资料讲解可采用左素材、右人物同步布局
- 分屏背景必须是静态虚化图，不能出现第二个动态讲话人物
- 字幕要独立放在底部安全区，不和素材卡片重叠

## 视频风格

默认风格是：

- AI 金融黑金商务风
- 投研简报感
- 大数字、少文字、强重点
- 完整字幕作为基础理解层
- 真实素材优先，少做抽象卡片
- 人物保持透亮，不盖重黑膜

禁忌：

- 从上到下滚动的金色线条
- 金光乱飞、粒子爆炸、霓虹闪烁
- 过度卡片化
- 文字堆满屏幕
- 提前暴露口播还没讲到的关键数字
- 把竖屏视频做成全屏 PPT

## 仓库结构

```text
.
├── skills/
│   └── jtxvideo-skill/
│       ├── SKILL.md
│       ├── agents/
│       │   ├── interface.yaml
│       │   └── openai.yaml
│       ├── design.md
│       └── templates/
│           ├── design-default.md
│           ├── storyboard-template.md
│           └── workflow-checklist.md
├── scripts/
│   └── validate_skill.py
├── .github/
│   └── workflows/
│       └── validate.yml
├── LICENSE
├── README.md
└── VERSION
```

## 安装方式

本仓库按 Agent Skills 通用方式安装，推荐使用 `npx skills add`。

`npx skills` 会根据目标 Agent 自动写入对应目录。全局安装时，通用 Skill 会放在 `~/.agents/skills`，并同步到 Claude Code、Codex 等 Agent 可识别的位置。

### 全局安装到当前 Agent

```bash
npx skills add https://github.com/jackjls/jtxvideo-skill --skill jtxvideo-skill -g
```

### 指定安装到 Claude Code

```bash
npx skills add https://github.com/jackjls/jtxvideo-skill --skill jtxvideo-skill --agent claude-code -g
```

### 安装到所有已支持 Agent

```bash
npx skills add https://github.com/jackjls/jtxvideo-skill --skill jtxvideo-skill --agent '*' -g
```

### 查看仓库内可安装的 Skill

```bash
npx skills add https://github.com/jackjls/jtxvideo-skill --list
```

安装或更新后，重启对应客户端。

## 使用方式

在 Codex 或 Claude Code 中提供口播视频，并明确调用 Skill：

```text
用 $jtxvideo-skill 处理这个口播视频，按预处理、SRT 确认、文案结构、分镜表、设计、HyperFrames 渲染和 2K60 导出的流程走。
```

如果有素材图、表格、截图，也一起提供：

```text
这是口播视频和两张素材图。先转写 SRT，我确认后再分析结构。素材要放在合适位置，但竖屏视频人物必须一直在画面里。
```

## 产物目录

每个视频项目通常会生成：

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
  design.md
  index.html
  renders/
    review.mp4
    final-2k60.mp4
```

## 质量检查

每次生成视频前后要检查：

- SRT 是否已由用户确认
- 文案结构是否已由用户确认
- 分镜表是否已由用户确认
- 横屏 / 竖屏规则是否选择正确
- 重点数字是否与口播时间对齐
- 字幕是否避开抖音 UI
- 人物是否透亮
- 音频是否完整
- 输出规格是否为 2K / 60fps

视频工程常用检查：

```bash
npx hyperframes validate
npx hyperframes inspect --samples 12
npx hyperframes snapshot --at 1.0,10.0,30.0 --describe false
ffprobe -v error -show_entries stream=width,height,r_frame_rate,duration -of default=noprint_wrappers=1 renders/final-2k60.mp4
```

如果用户指出某个时间点闪烁或弹窗异常，必须从实际渲染出的 MP4 抽帧检查，而不能只看 HyperFrames snapshot：

```bash
ffmpeg -ss 56.2 -i renders/review.mp4 -vf fps=5 -t 2.4 renders/probe-%03d.jpg
```

## 维护方式

修改 Skill 后运行校验：

```bash
python3 scripts/validate_skill.py skills/jtxvideo-skill
```

提交前建议检查：

```bash
git status --short
git diff --stat
```

## 许可证

本项目使用 [MIT License](LICENSE)。
