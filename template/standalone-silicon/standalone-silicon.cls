\ProvidesClass{standalone-silicon}

% -------------------------------- %
% Load package <etoolbox> : Toolbox for class and package
\RequirePackage{etoolbox}
% Load package <xparse> : New way to define command and environment
\RequirePackage{xparse} 

% -------------------------------- %
% Load document class <standalone>
\LoadClass{standalone}

% -------------------------------- %
% Load package <ctex> : Support for chinese
\RequirePackage{ctex}

% -------------------------------- %
% Font Setting
\setCJKmainfont[AutoFakeSlant]{Noto Serif CJK SC}
\setCJKsansfont[AutoFakeSlant]{Noto Sans CJK SC}
\setCJKmonofont[AutoFakeBold,AutoFakeSlant]{FandolFang}

