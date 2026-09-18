# minimus-math

数学宏包，提供数学符号、算符、快捷命令和数学排版环境。

## 引入的宏包

### `amsmath`、`amsthm`、`amssymb`、`mathtools`、`mathrsfs`

AMS数学系列宏包。

| 宏包 | 说明 |
|------|------|
| `amsmath` | 提供`align`、`gather`、`split`等数学环境 |
| `amsthm` | 提供`theroem`、`proof`等定理环境 |
| `amssymb` | 提供`\mathbb`、`\mathcal`等数学字体符号 |
| `mathtools` | 提供`\mathmakebox`、`\mathclap`、`\mathllap`、`\mathrlap`等增强命令 |
| `mathrsfs` | 提供`\mathscr`命令，排版花体字母（如$\mathscr{E}$） |

方程编号设为按节递增（`\numberwithin{equation}{section}`）。

### `physics`

数学符号的便捷排版。

| 宏包 | 说明 |
|------|------|
| `physics` | 提供`\vb`、`\dd`、`\qty`等命令，用于更方便排版数学符号 |

尽管这个包的名字叫`physics`，但实际上提供了许多便捷数学命令，解决了许多数学排版的痛点
- 向量用`\vb{a}`和`\vb*{\alpha}`
- 微分用`\dd{x}`，导数用`\dv{y}{x}`和`\pdv{y}{x}`
- 自适应括号用`\qty(...)`、`\qty[...]`、`\qty{...}`

### `siunitx`

物理量与物理单位的排版。

| 宏包 | 说明 |
|------|------|
| `siunitx` | 提供`\qty`、`\unit`、`\num`等命令，用于排版带单位的物理量 |

`siunitx`旧版的排版带单位量的命令是`\SI{1}{\us}`，而新版是`\qty{1}{\us}`。

`siunitx`的`\qty`命令与`physics`宏包表示自适应括号的`\qty`命令存在命名冲突，因此不可用，存在以下重命名

| 命令 | 说明 |
|------|------|
| `\qnum{value}{unit}` | 原`\qty`，排版物理量 |
| `\qnumlist{values}{unit}` | 原`\qtylist`，排版物理量列表 |
| `\qnumrange{low}{high}{unit}` | 原`\qtyrange`，排版物理量范围 |
| `\qnumproduct{values}` | 原`\qtyproduct`，排版物理量乘积 |

若追求兼容性，可以继续使用`\SI`的命令。

预配置设置：

| 设置项 | 值 | 说明 |
|--------|-----|------|
| `list-separator` | `{, }` | 列表分隔符 |
| `list-pair-separator` | `{, }` | 两元素列表分隔符 |
| `list-final-separator` | `{, }` | 多元素最终分隔符 |
| `list-units` | `repeat` | 列表中每个值重复单位 |
| `range-phrase` | `{\,\text{\textasciitilde{}}\,}` | 范围连接符 |
| `range-units` | `single` | 范围只保留一个单位 |
| `product-symbol` | `{\times}` | 乘积符号 |
| `product-units` | `repeat` | 乘积中每个值重复单位 |
| `group-digits` | `none` | 不分组数字 |
| `inter-unit-product` | `{\cdot}` | 单位间用`·`连接 |

额外定义的二进制单位：

| 命令 | 说明 | 命令 | 说明 | 命令 | 说明 | 命令 | 说明 |
|------|------|------|------|------|------|------|------|
| `\Kibi` | K | `\KB` | KB | `\Kb` | Kb | `\Kbps` | Kbps |
| `\Mebi` | M | `\MB` | MB | `\Mb` | Mb | `\Mbps` | Mbps |
| `\Gibi` | G | `\GB` | GB | `\Gb` | Gb | `\Gbps` | Gbps |
| `\Tebi` | T | `\TB` | TB | `\Tb` | Tb | `\Tbps` | Tbps |
| `\Pebi` | P | `\PB` | PB | `\Pb` | Pb | `\Pbps` | Pbps |
| `\Exbi` | E | `\EB` | EB | `\Eb` | Eb | `\Ebps` | Ebps |
| `\Zebi` | Z | `\ZB` | ZB | `\Zb` | Zb | `\Zbps` | Zbps |
| `\Yobi` | Y | `\YB` | YB | `\Yb` | Yb | `\Ybps` | Ybps |

### `mhchem`

化学式排版。

| 宏包 | 说明 |
|------|------|
| `mhchem` | 提供`\ce`命令，用于排版化学式 |

### `esint`

更多积分符号。

| 宏包 | 说明 |
|------|------|
| `esint` | 提供`\oiint`、`\oint`、`\varint`等额外积分符号 |

### `extarrows`

带文字的长箭头。

| 宏包 | 说明 |
|------|------|
| `extarrows` | 提供`\xlongequal{text}`等可伸缩的文字箭头 |

### `upgreek`

直立希腊字母。

| 宏包 | 说明 |
|------|------|
| `upgreek` | 提供`\upalpha`、`\upbeta`、`\uppsi`等直立希腊字母，用于数学模式 |

### `xfrac`

小型行内分数。

| 宏包 | 说明 |
|------|------|
| `xfrac` | 提供`\sfrac{num}{den}`命令，排版小型行内分数 |

### `mathdots`

更多省略号符号。

| 宏包 | 说明 |
|------|------|
| `mathdots` | 提供`\iddots`（逆对角线省略号）等额外省略号命令 |

### `nicematrix`

高级矩阵排版。

| 宏包 | 说明 |
|------|------|
| `nicematrix` | 提供`\pNiceMatrix`等命令，支持带行列标签的矩阵、块矩阵等 |

### `yhmath`

宽重音符号。

| 宏包 | 说明 |
|------|------|
| `yhmath` | 提供`\wideparen`、`\widehat`、`\widetilde`等宽重音符号命令 |

### `accents`

下方重音符号。

| 宏包 | 说明 |
|------|------|
| `accents` | 提供`\underaccent`命令，用于在符号下方添加重音 |

### `longdivision`

长除法排版。

| 宏包 | 说明 |
|------|------|
| `longdivision` | 提供`\longdivision`命令，自动排版数学长除法竖式 |

### `relsize`

数学缩放。

| 宏包 | 说明 |
|------|------|
| `relsize` | 提供`\mathlarger`和`\mathsmaller`命令，用于缩放数学符号的大小 |

## 自定义命令

### `\e`、`\i`、`\j`、`\k`

常用数学常数的快捷写法，统一为正体。

| 命令 | 说明 |
|------|------|
| `\e` | 自然常数$\mathrm{e}$ |
| `\i` | 数学的虚数单位$\mathrm{i}$ |
| `\j` | 工程的虚数单位$\mathrm{j}$ |
| `\k` | 四元数虚数$\mathrm{k}$ |

### `\N`、`\Z`、`\Q`、`\R`、`\C`、`\emptyset`

常用数集的快捷写法。

| 命令 | 说明 |
|------|------|
| `\N` | 自然数集$\mathbb{N}$ |
| `\Z` | 整数集$\mathbb{Z}$ |
| `\Q` | 有理数集$\mathbb{Q}$ |
| `\R` | 实数集$\mathbb{R}$ |
| `\C` | 复数集$\mathbb{C}$ |
| `\emptyset` | 空集，重定义为$\varnothing$ |

### `\dx`、`\dy`、`\dz`

微分的快捷写法，依赖`physics`的`\dd`命令。

| 命令 | 说明 |
|------|------|
| `\dx` | 对$x$的微分$\mathrm{d}x$ |
| `\dy` | 对$y$的微分$\mathrm{d}y$ |
| `\dz` | 对$z$的微分$\mathrm{d}z$ |

### `\vi`、`\vj`、`\vk`

单位向量的快捷写法，依赖`physics`的`\vb*`命令。

| 命令 | 说明 |
|------|------|
| `\vi` | 单位向量$\mathbf{i}$ |
| `\vj` | 单位向量$\mathbf{j}$ |
| `\vk` | 单位向量$\mathbf{k}$ |

### `\Sum`、`\Prod`、`\BigCap`、`\BigCup`、`\BigOplus`、`\BigOdot`、`\BigOtimes`

求和符号的快捷写法，例如`\Sum[sub][sup]`展开为`\sum_{sub}^{sup}`。

| 命令 | 说明 |
|------|------|
| `\Sum[sub][sup]` | 累加$\sum$ |
| `\Prod[sub][sup]` | 累乘$\prod$ |
| `\BigCap[sub][sup]` | 交$\bigcap$ |
| `\BigCup[sub][sup]` | 并$\bigcup$ |
| `\BigOplus[sub][sup]` | 加$\bigoplus$ |
| `\BigOdot[sub][sup]` | 点积$\bigodot$ |
| `\BigOtimes[sub][sup]` | 叉积$\bigotimes$ |

| 序号 | 格式 | 类型 | 说明 |
|------|------|------|------|
| 1 | `[sub]` | 可选 | 下限，默认无 |
| 2 | `[sup]` | 可选 | 上限，默认无 |

### `\Int`、`\Idnt`、`\Itnt`、`\Ilnt`、`\Ilot`、`\Isnt`、`\Isot`

积分符号的快捷写法，例如`\Int[sub][sup]`展开为`\int{sub}^{sup}`。

其中`\Ilnt`和`\Isnt`的引入是历史遗留问题，它们与`\Int`和`\Idnt`没有区别。

| 命令 | 说明 |
|------|------|
| `\Int[low][high]` | 一重积分$\int$ |
| `\Idnt[low][high]` | 二重积分$\iint$（Double） |
| `\Itnt[low][high]` | 三重积分$\iiint$ （Triple）|
| `\Ilnt[low][high]` | 线积分$\int$ （Line）|
| `\Ilot[low][high]` | 闭合线积分$\oint$ (Line O)|
| `\Isnt[low][high]` | 面积分$\iint$ （Surface）|
| `\Isot[low][high]` | 闭合面积分$\oiint$ （Surface O） |

| 序号 | 格式 | 类型 | 说明 |
|------|------|------|------|
| 1 | `[low]` | 可选 | 积分下限，默认无 |
| 2 | `[high]` | 可选 | 积分上限，默认无 |

### `\Lim`

极限符号的快捷写法，例如`\Lim[a]`和`\Lim[a][b]`分别生成`\lim_{a}`和`\lim_{a\to b}`。

| 命令 | 说明 |
|------|------|
| `\Lim[a][b]` | 极限$\lim$ |

| 序号 | 格式 | 类型 | 说明 |
|------|------|------|------|
| 1 | `[a]` | 可选 | `\to`前的内容 |
| 2 | `[b]` | 可选 | `\to`后的内容 |

若`\Lim`后只有一个方括号，则该方括号的内容会完整作为下标，没有`\to`生成。

### `\Grad`、`\Div`、`\Curl`

文字版本的向量算符。

| 命令 | 说明 |
|------|------|
| `\Grad` | 梯度$\operatorname{grad}$ |
| `\Div` | 散度$\operatorname{div}$ |
| `\Curl` | 旋度$\operatorname{curl}$ |

### `\Var`、`\Cov`

文字版本的方差与协方差。

| 命令 | 说明 |
|------|------|
| `\Var` | 方差$\operatorname{Var}$ |
| `\Cov` | 协方差$\operatorname{Cov}$ |

### `\arsinh`、`\arcosh`、`\artanh`、`\arcoth`、`\arsech`、`\arcsch`、`\atantwo`

反双曲函数与`atan2`的快捷写法。

| 命令 | 说明 |
|------|------|
| `\arsinh` | 反双曲正弦$\operatorname{arsinh}$ |
| `\arcosh` | 反双曲余弦$\operatorname{arcosh}$ |
| `\artanh` | 反双曲正切$\operatorname{artanh}$ |
| `\arcoth` | 反双曲余切$\operatorname{arcoth}$ |
| `\arsech` | 反双曲正割$\operatorname{arsech}$ |
| `\arcsch` | 反双曲余割$\operatorname{arcsch}$ |
| `\atantwo` | 计算机的`atan2`函数$\operatorname{atan2}$ |

### `\Beta`、`\PolyGamma`、`\BesselJ`、`\BesselN`、`\BesselH`、`\BesselI`、`\BesselK`、`\LegendreP`、`\LegendreQ`、`\SphericalY`、`\HermiteH`、`\FermiF`、`\hodge`

特殊函数的快捷写法。

| 命令 | 说明 |
|------|------|
| `\Beta` | Beta函数$\operatorname{B}$ |
| `\PolyGamma` | PolyGamma函数$\operatorname{\psi}$ |
| `\BesselJ` | 第一类Bessel函数$\operatorname{J}$ |
| `\BesselN` | 第二类Bessel函数$\operatorname{N}$ |
| `\BesselH` | 第三类Bessel函数$\operatorname{H}$ |
| `\BesselI` | 第一类修正Bessel函数$\operatorname{I}$ |
| `\BesselK` | 第二类修正Bessel函数$\operatorname{K}$ |
| `\LegendreP` | 第一类Legendre函数$\operatorname{P}$ |
| `\LegendreQ` | 第二类Legendre函数$\operatorname{Q}$ |
| `\SphericalY` | 球谐函数$\operatorname{Y}$ |
| `\HermiteH` | Hermite多项式$\operatorname{H}$ |
| `\FermiF` | Fermi函数$\operatorname{F}$ |
| `\hodge` | Hodge星算子$\star$ |

### `\diag`、`\subspace`、`\rangespace`、`\nullspace`、`\vspan`、`\piv`、`\rowpiv`、`\colpiv`、`\Obig`

矩阵计算相关符号的快捷写法。

其中`\vspan`的命名是用于规避已经被定义的`\span`命令。

| 命令 | 说明 |
|------|------|
| `\diag` | 对角矩阵$\operatorname{diag}$ |
| `\subspace` | 子空间$\mathcal{S}$ |
| `\rangespace` | 列空间$\mathcal{R}$ |
| `\nullspace` | 零空间$\mathcal{N}$ |
| `\vspan` | 张成空间$\operatorname{span}$ |
| `\piv` | 主元$\operatorname{piv}$ |
| `\rowpiv` | 行主元$\operatorname{rowpiv}$ |
| `\colpiv` | 列主元$\operatorname{colpiv}$ |
| `\Obig` | 大O记号$\mathcal{O}$ |

### `\aff`、`\conv`、`\cone`、`\polyhedra`、`\Symm`、`\Herm`、`\dom`、`\epi`、`\hypo`、`\minimize`、`\maximize`、`\find`、`\subto`、`\relint`

凸优化相关符号的快捷写法。

| 命令 | 说明 |
|------|------|
| `\aff` | 仿射包$\operatorname{aff}$ |
| `\conv` | 凸包$\operatorname{conv}$ |
| `\cone` | 锥包$\operatorname{cone}$ |
| `\polyhedra` | 多面体$\mathcal{P}$ |
| `\Symm` | 对称矩阵集$\mathbb{S}$ |
| `\Herm` | 厄米矩阵集$\mathbb{H}$ |
| `\dom` | 定义域$\operatorname{dom}$ |
| `\epi` | 上图$\operatorname{epi}$ |
| `\hypo` | 下图$\operatorname{hypo}$ |
| `\minimize` | 极小化$\operatorname{minimize}$ |
| `\maximize` | 极大化$\operatorname{maximize}$ |
| `\find` | 求解$\operatorname{find}$ |
| `\subto` | 约束条件$\operatorname{subject\ to}$ |
| `\relint` | 相对内部$\operatorname{relint}$ |

### `\sgn`、`\rect`、`\sinc`、`\erfc`、`\dirac`

工程函数符号的快捷写法。

| 命令 | 说明 |
|------|------|
| `\sgn` | 符号函数$\operatorname{sgn}$ |
| `\rect` | 矩形函数$\operatorname{rect}$ |
| `\sinc` | 采样函数$\operatorname{sinc}$ |
| `\erfc` | 互补误差函数$\operatorname{erfc}$ |
| `\dirac` | Dirac冲激函数$\delta$ |

### `\softmax`、`\sigmoid`、`\ReLU`

深度学习常用激活函数的快捷写法。

| 命令 | 说明 |
|------|------|
| `\softmax` | softmax函数$\operatorname{softmax}$ |
| `\sigmoid` | sigmoid函数$\operatorname{sigmoid}$ |
| `\ReLU` | ReLU函数$\operatorname{ReLU}$ |

### `\kB`、`\Emf`

物理常量与电磁量符号的快捷写法。

| 命令 | 说明 |
|------|------|
| `\kB` | 玻尔兹曼常数$k_{\mathrm{B}}$ |
| `\Emf` | 电动势$\mathscr{E}$ |

### `\FT`、`\LT`

傅里叶变换与拉普拉斯变换的快捷写法，带`*`表示逆变换。

| 命令 | 说明 |
|------|------|
| `\FT*[content]` | 傅里叶变换$\mathcal{F}\{x\}$ $\mathcal{F}^{-1}\{x\}$ |
| `\LT[content]` | 拉普拉斯变换$\mathcal{L}\{x\}$ $\mathcal{L}^{-1}\{x\}$ |

| 序号 | 格式 | 类型 | 说明 |
|------|------|------|------|
| 1 | `*` | 标记 | 逆变换 / 正变换 |
| 2 | `[content]` | 可选 | 变换对象 |

### `\delt`、`\detv`

差分与差分比的快捷写法。

| 命令 | 说明 |
|------|------|
| `\delt{x}` | $\Delta x$ |
| `\detv{x}{y}` | $\dfrac{\Delta x}{\Delta y}$，差分形式的导数 |

### `\zp`、`\zm`

$0_+$与$0_-$的快捷写法。

| 命令 | 说明 |
|------|------|
| `\zp` | $0_{+}$ |
| `\zm` | $0_{-}$ |

### `\anglebkt`、`\floor`、`\ceil`、`\<`

自适应括号的快捷写法，带`*`时自动缩放大小。

| 命令 | 说明 |
|------|------|
| `\anglebkt*{content}` | 尖括号$\langle\rangle$，带`*`时自适应大小 |
| `\floor*{content}` | 下取整$\lfloor\rfloor$，带`*`时自适应大小 |
| `\ceil*{content}` | 上取整$\lceil\rceil$，带`*`时自适应大小 |
| `\<content>` | 尖括号简写，始终自适应大小$\left\langle x\right\rangle$ |

| 序号 | 格式 | 类型 | 说明 |
|------|------|------|------|
| 1 | `*` | 标记 | 自适应大小 |
| 2 | `{content}` | 必选 | 括号内的内容 |

### `\xpar`、`\xhat`、`\xwav`、`\xvec`、`\xbar`、`\bbar`

宽重音符号的快捷写法。

| 命令 | 说明 |
|------|------|
| `\xpar{content}` | `\wideparen`的别名，上方宽弧 |
| `\xhat{content}` | `\widehat`的别名，上方宽帽 |
| `\xwav{content}` | `\widetilde`的别名，上方宽波浪线 |
| `\xvec{content}` | `\overrightarrow`的别名，上方宽箭头 |
| `\xbar{content}` | `\overline`的别名，上方宽线 |
| `\bbar{content}` | `\underaccent{\bar}`的别名，下方添加短线的重音符号 |

### `\mal`、`\mas`、`\te`

数学缩放和缩写的快捷写法。

| 命令 | 说明 |
|------|------|
| `\mal{content}` | `\mathlarger`的别名，放大数学符号 |
| `\mas{content}` | `\mathsmaller`的别名，缩小数学符号 |
| `\te{content}` | `\mathrm`的缩写，如`\te{sin}`输出$\mathrm{sin}$ |

### `\forcezero`、`\forceline`

方程强制居中命令。默认情况下中等长度的编号公式会偏向标签一侧，这两个命令可以纠正。

| 命令 | 说明 |
|------|------|
| `\forcezero[width]{content}` | 将公式置入零宽盒子强制居中，标签保持同行 |
| `\forceline[width]{content}` | 将公式置入行宽盒子强制居中，标签移至下一行 |

| 序号 | 格式 | 类型 | 说明 |
|------|------|------|------|
| 1 | `[width]` | 可选 | 盒子宽度（`width\linewidth`），默认`0.4`（`\forcezero`）或`1.0`（`\forceline`） |
| 2 | `{content}` | 必选 | 公式内容 |

## 自定义环境

### `Equation`

单行公式环境。

```latex
\begin{Equation}*[label]!!
    ...
\end{Equation}
```

| 序号 | 格式 | 类型 | 说明 |
|------|------|------|------|
| 1 | `*` | 标记 | 公式不编号 |
| 2 | `[label]` | 可选 | 标签，格式为`eq:label`，默认无 |
| 3 | `!` | 标记 | 强制零宽居中（`!`）|
| 4 | `!` | 标记 | 强制行宽居中（`!!`） |

```latex
\begin{Equation}[myequation]
    f(x) = ax^4 + bx^3 + cx^2 + dx + e
\end{Equation}
```

### `Split`

多行对齐的长公式环境。

```latex
\begin{Split}*[label]{factor}!!
    ...
\end{Split}
```

| 序号 | 格式 | 类型 | 说明 |
|------|------|------|------|
| 1 | `*` | 标记 | 公式不编号 |
| 2 | `[label]` | 可选 | 标签，格式为`eq:label`，默认无 |
| 3 | `{factor}` | 可选 | 行间距缩放因子（`\jot`倍数），默认`1.0` |
| 4 | `!` | 标记 | 强制零宽居中（`!`） |
| 5 | `!` | 标记 | 强制行宽居中（`!!`） |

```latex
\begin{Split}[quadratic]
    f(x) &= ax^4 + bx^3 \\
         &+ cx^2 + dx + e
\end{Split}
```

### `Multline`

阶梯排列的长公式环境。

```latex
\begin{Multline}*[label]{factor}&{width}!!
    ...
\end{Multline}
```

| 序号 | 格式 | 类型 | 说明 |
|------|------|------|------|
| 1 | `*` | 标记 | 公式不编号 |
| 2 | `[label]` | 可选 | 标签，格式为`eq:label`，默认无 |
| 3 | `{factor}` | 可选 | 行间距缩放因子（`\jot`倍数），默认`1.0` |
| 4 | `&` | 分隔 | 无实际作用，用于分隔`{factor}`和`{width}` |
| 5 | `{width}` | 可选 | 总宽度（`\linewidth`倍数），默认自适应 |
| 6 | `!` | 标记 | 强制零宽居中 |
| 7 | `!` | 标记 | 强制行宽居中（`!!`） |

```latex
\begin{Multline}[long]
    f(x) = ax^4 + bx^3 \\
         + cx^2 + dx + e
\end{Multline}
```
### `Align`

公式组对齐环境，每行可独立编号。

```latex
\begin{Align}*[prefix]{factor}
    ...
\end{Align}
```

| 序号 | 格式 | 类型 | 说明 |
|------|------|------|------|
| 1 | `*` | 标记 | 公式不编号 |
| 2 | `[prefix]` | 可选 | 标签前缀，使用`\id{a}`得到`eq:prefixa`，默认无 |
| 3 | `{factor}` | 可选 | 行间距缩放因子），默认`1.0` |

```latex
\begin{Align}[sys]
    x + y &= 5 \id{a} \\
    x - y &= 3 \id{b}
\end{Align}
```

### `Gather`

公式组居中环境，每行可独立编号。

```latex
\begin{Gather}*[prefix]{factor}
    ...
\end{Gather}
```

| 序号 | 格式 | 类型 | 说明 |
|------|------|------|------|
| 1 | `*` | 标记 | 公式不编号 |
| 2 | `[prefix]` | 可选 | 标签前缀（`\id{a}`产生`eq:prefixa`），默认无 |
| 3 | `{factor}` | 可选 | 行间距缩放因子，默认`1.0` |

```latex
\begin{Gather}[poly]
    f(x) = x^4 + 2x^3 - x^2 + 3x + 1 \id{a} \\
    g(x) = 2x + 5 \id{b}
\end{Gather}
```
