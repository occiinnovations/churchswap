# ChurchSwap

Churchswap is a person detection system that automatically manages camera switching during church services. Using YOLOv8 computer vision, it monitors a podium area via an input source such as OBS or an ATEM. When someone is at the podium, the system keeps the focused camera view active. When the podium zone is empty, it automatically switches to an alternative source or a sub-source.

I'd define a sub-source as switching sources within OBS instead of switching from OBS to ATEM, for example.

This enables seamless, hands-free camera management for livestreaming without requiring a dedicated operator to manually switch between views.

## Update

Churchswap will be getting combined into autOBS to form a new project called **Nodary**. This new project is highly experimental, but for the most part, Churchswap will not be significantly updated. This repo will retain functioning code.

## Installation

```bash
python -m pip install -r requirements.txt

python 'src/main.py'
```

## Intended Use

This project was designed to be used locally in a church Audio/Visual setting, however it has the ability to be utilized in various different scenarios. Churchswap is most efficient when working with stationary cameras, and is most efficient with multiple systems.
