\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{vsp-beamer}

% -------------------------------- %
% Forward options to <vsp-beamer-theme>
% red/purple/nailong         -> Color scheme
% tutorial/report            -> Cover style
% shtu                       -> ShanghaiTech variant
% sectionpages/nosectionpages -> Automatic section pages
\DeclareOption{red}{\PassOptionsToPackage{red}{vsp-beamer-theme}}
\DeclareOption{purple}{\PassOptionsToPackage{purple}{vsp-beamer-theme}}
\DeclareOption{nailong}{\PassOptionsToPackage{nailong}{vsp-beamer-theme}}
\DeclareOption{shtu}{\PassOptionsToPackage{shtu}{vsp-beamer-theme}}
\DeclareOption{tutorial}{\PassOptionsToPackage{tutorial}{vsp-beamer-theme}}
\DeclareOption{report}{\PassOptionsToPackage{report}{vsp-beamer-theme}}
\DeclareOption{sectionpages}{\PassOptionsToPackage{sectionpages}{vsp-beamer-theme}}
\DeclareOption{nosectionpages}{\PassOptionsToPackage{nosectionpages}{vsp-beamer-theme}}
% Process options
\ProcessOptions\relax

% -------------------------------- %
% Load document class <beamer>
% aspectratio=169 -> Use 16:9 frame
% 10pt            -> Use 10pt base font
\LoadClass[aspectratio=169,10pt,noamsthm]{beamer}

% -------------------------------- %
% Load package <ctex> : Chinese support
% UTF8         -> Use UTF-8 encoding
% fontset=none -> Disable ctex font setting
\RequirePackage[UTF8,fontset=none]{ctex}

% -------------------------------- %
% Load the VSP theme
\RequirePackage{vsp-beamer-theme}
