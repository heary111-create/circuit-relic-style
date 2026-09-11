# 使用示例 / Examples

以下是文字示例，用于说明调用方式与检查标准，不是已执行的图像生成记录。使用自己的参考图；不要把私密或未经授权的图片加入公开 Issue。

## 1. 人物肖像

**请求：** 使用 Circuit Relic Style 转换这张单人站姿图，保留抬起的右手和长外套轮廓。

- 头部、手势和长外套轮廓保持可辨识。
- 身体转为密集铜走线和银色焊点；外套转为深绿焊膜与 IC 密集区域。
- 外围维持青绿色 PCB 和黑色背景，不因原图背景为红色就默认铺满红色。
- 检查左右手方向、主体数量和原图横竖比例。

## 2. 湖面与分叉标志物

**请求：** 保留湖面倒影、远山和中央顶部呈双叉形的红色长杆。

- 天空转为低密度深蓝焊膜；远山转为层叠线路；水面转为水平走线。
- 保留长杆长度、分叉数量与方向，用深红色导电结构构成。
- 根据参考图保留倒影位置，不引入任何特定作品的武器设定。

## 3. 多翼主体

**请求：** 转换这张六翼主体图，保留六片翅膀与放射方向。

- 翅膀转为细长电路分支，羽片转为平行走线束。
- 用焊点链表现翼缘，中心线路密度高于外围。
- 检查数量是否仍为六片，是否保留左右展开节奏。

## 4. 完整英文提示词（虚构输入）

假设参考图为一只站在弧形树枝上的猫头鹰：

```text
Transform the supplied reference image into photorealistic Circuit Relic Style PCB artwork.
Subject: one owl with a rounded head and two clearly separated circular eyes.
Pose: perched upright, facing forward, talons resting on one curved branch.
Iconic elements: two circular eyes, folded wing outlines, and a single curved branch.
Preserve the subject count, silhouette, proportions, pose and composition.
Reconstruct the owl entirely from copper traces, vias, silver solder joints,
microchips, resistors and capacitors. Use concentric sensor sockets for the eyes,
parallel routing for feather groups, and thick conductive rails for the branch.
Integrate the subject into one complete turquoise rectangular PCB with four
gold-plated corner mounting holes and a pure black outer background.
Keep the portrait orientation, dense routing inside the owl and sparse components
around it. Use a small deep-red conductive accent only at the central chest.
Use sharp top-down product photography, controlled soft lighting and realistic
metallic reflections. Avoid skin, feathers as organic material, superficial circuit
texture overlays, neon glow, floating parts, extra subjects, logos and text.
The result is PCB artwork, not a fabrication-ready electrical design.
```

## 5. 透明背景与文字覆盖

**请求：** PCB 外围透明，在底部丝印位置加入“RELIC 01”。

- 保留完整板体，仅去除外围背景；不要把棋盘格绘制成背景。
- 从默认负面提示词中去除与用户文字要求冲突的项。
- 若已生成文件，检查实际 alpha 通道与文字拼写；无透明能力时说明限制。

## 常见问题

| 现象 | 修正方向 |
| --- | --- |
| 只是给普通人物叠电路纹理 | 明确皮肤、衣物和背景都由电子结构重构 |
| 主体认不出或姿态改变 | 重新写清轮廓句、姿态和 1–3 个辨识元素 |
| 画面像霓虹赛博朋克 | 强化实体焊点、铜走线和柔和产品摄影光线 |
| 线路密度处处相同 | 提高主体密度，降低外围元件密度 |
| 红色铺满画面 | 将红色限定到选定标志物，除非用户明确另有要求 |
