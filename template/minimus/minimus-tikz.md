# minimus-tikz

绘图工具宏包，提供TikZ绘图、电路图、时序图和化学分子式排版支持。

## 引入的宏包

### `tikz`

TikZ绘图核心。

| 宏包 | 说明 |
|------|------|
| `tikz` | 提供`tikzpicture`环境和全套绘图命令 |

预加载的库：

| 库 | 用途 |
|----|------|
| `calc` | 坐标计算 |
| `intersections` | 交点计算 |
| `angles` | 角度绘制 |
| `perspective` | 简单3D投影 |
| `positioning` | 相对定位 |
| `shapes.geometric` | 几何形状节点 |
| `shapes.arrows` | 箭头形状节点 |
| `shapes.symbols` | 符号形状节点 |
| `quotes` | 引号语法标注 |
| `fit` | 包围盒节点 |

### `circuitikz`

电路图绘制。

| 宏包 | 说明 |
|------|------|
| `circuitikz` | 提供`circuitikz`环境和电路元件命令 |

预配置（`\PassOptionsToPackage`和`\ctikzset`）：

| 选项 | 说明 |
|------|------|
| `europeanresistors` | 欧式方块电阻 |
| `americaninductors` | 美式波浪电感 |
| `americanvoltages` | 美式电压符号 |
| `americancurrents` | 美式电流符号 |
| `RPvoltages` | 电源方向 |
| `voltage/distance from node=0.85` | 电压标记距节点距离 |
| `resistors/scale=0.65` | 电阻缩放 |
| `capacitors/scale=0.75` | 电容缩放 |
| `inductors/scale=0.70` | 电感缩放 |
| `diodes/scale=0.75` | 二极管缩放 |
| `sources/scale=0.9` | 独立源缩放 |
| `csources/scale=0.9` | 受控源缩放 |
| `tripoles/mos style/arrows` | MOS管：箭头 + 圆圈 |
| `logic ports=ieee` | 逻辑门风格 |
| `logic ports/scale=0.65` | 逻辑门缩放 |
| `quadpoles/transformer/inner=1.0` | 变压器移除水平线 |
| `quadpoles/transformer/width=1.0` | 变压器移除水平线 |


### `tikz-timing`

时序图绘制。

| 宏包 | 说明 |
|------|------|
| `tikz-timing` | 提供`tikztimingtable`环境和时序标记命令 |

预加载的库：

| 库 | 说明 |
|----|------|
| `either` | 双态符号`E` |
| `overlays` | 覆盖层 |
| `counters` | 计数器 |
| `advnodes` | 高级节点 |

背景层和前景层已预定义（`background`、`foreground`）。

### `ifthen`

条件判断。

| 宏包 | 说明 |
|------|------|
| `ifthen` | 提供`\ifthenelse`命令，用于`\fliprotate`内部逻辑 |

### `chemfig`

化学分子式。

| 宏包 | 说明 |
|------|------|
| `chemfig` | 提供`\chemfig`命令，排版化学分子结构式 |

## 自定义命令

### `\fliprotate`、`f++r+`

MOS管有时需要翻转和旋转，但文字不应被一并变换，需要反变换补偿，以下样式和命令组合来解决这个问题。

```latex
\path (0,0) node[nmos,f+-r+] {\fliprotate+-{$M_1$}+} ;
```

| 命令 | 说明 |
|------|------|
| `\fliprotate+-+-{text}+-` | 对`{text}`应用翻转/旋转补偿，7个`+`/`-`标记的排列决定补偿方式 |

| 序号 | 格式 | 类型 | 说明 |
|------|------|------|------|
| 1 | `+` | 标记 | 第一个标记 |
| 2 | `-` | 标记 | 第二个标记 |
| 3 | `+` | 标记 | 第三个标记 |
| 4 | `-` | 标记 | 第四个标记 |
| 5 | `{text}` | 必选 | 要显示的文字 |
| 6 | `+` | 标记 | 第五个标记 |
| 7 | `-` | 标记 | 第六个标记 |

该命令的参数组合经过精心构造，用法上和样式一一对应，用于补偿样式对文字的影响。

- 第一组`+/-`控制MOS是否沿X翻转。
- 第二组`+/-`控制MOS是否沿Y翻转。
- 第三组`+/-`控制MOS是否逆时针旋转90度。
- 样式作用顺序是X翻转、Y翻转、逆时针90度旋转。

样式是关键，只关心要什么方向的MOS管，文字用对应命令即一定对。

| 样式 | 命令 | X翻转 | Y翻转 | 逆时针90度旋转 |
|------|------|-------|-------|----------------|
| `f++r+` | `\fliprotate++{text}++` | 0 | 0 | 0 |
| `f-+r+` | `\fliprotate-+{text}++` | 1 | 0 | 0 |
| `f+-r+` | `\fliprotate+-{text}++` | 0 | 1 | 0 |
| `f--r+` | `\fliprotate--{text}++` | 1 | 1 | 0 |
| `f++r-` | `\fliprotate++{text}+-` | 0 | 0 | 1 |
| `f-+r-` | `\fliprotate-+{text}+-` | 1 | 0 | 1 |
| `f+-r-` | `\fliprotate+-{text}+-` | 0 | 1 | 1 |
| `f--r-` | `\fliprotate--{text}+-` | 1 | 1 | 1 |

### `semi thick`、`tlvdd`、`tlvss`、`mw`、`mh`

预定义的TikZ样式。

| 命令/样式 | 说明 |
|------|------|
| `semi thick` | `semithick`的别名 |
| `tlvdd` | 尾部向下的VDD |
| `tlvss` | 尾部向上的VSS |
| `mw=len` | `minimum width=len`的简写 |
| `mh=len` | `minimum height=len`的简写 |
