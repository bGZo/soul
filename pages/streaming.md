collapsed:: true
also:: 串流
created:: [[20230531]]
tags:: #game

- ## Why
  - in correct place.
- ## How
  - [[windows]]
    - 软件推荐
      - [[moonlight]]
        logseq.order-list-type:: number
      - Steam Link 
        logseq.order-list-type:: number
        collapsed:: true
        - [Google Play](https://play.google.com/store/apps/details?id=com.valvesoftware.steamlink&hl=en_SG&gl=US)
          logseq.order-list-type:: number
        - DONE Some games control is error. #wontfix
        - DONE Cannot play local game. #wontfix
    - 解除自带的限制
      - RDP Host Group Policies via: {{nav-ri https://www.reddit.com/r/sysadmin/comments/fv7d12/pushing_remote_fx_to_its_limits}}
        logseq.order-list-type:: number
        collapsed:: true
        - Computer Configuration > Policies > Administrative Template > Windows Components > Remote Desktop Services > Remote Desktop Session Host > Connections
          logseq.order-list-type:: number
          collapsed:: true
          - Select RDP Transfer Protocols = **Enabled**
            logseq.order-list-type:: number
            Set Transport Type to: "Use both UDP and TCP"
        - Computer Configuration > Policies > Administrative Template > Windows Components > Remote Desktop Services > Remote Desktop Session Host > Remote Session Enviorment
          logseq.order-list-type:: number
          collapsed:: true
          - Use hardware graphics adapters for all Remote Desktop Services Sessions = **Enabled**
            logseq.order-list-type:: number
          - Prioritize H.264/AVC 444 graphics mode for Remote Desktop Connections = **Enabled**
            logseq.order-list-type:: number
          - Configure H.264/AVC Hardware encoding for Remote Desktop Connections = **Enabled**
            logseq.order-list-type:: number
            Set "Prefer AVC hardware encoding" to **"Always attempt"**
          - Configure compression for Remote FX data = **Enabled**
            logseq.order-list-type:: number
            Set RDP compression algorithem: **"Do not use an RDP compression algorithm"**
          - Configure image quality for RemoteFX Adaptive Graphics = **Enabled**
            logseq.order-list-type:: number
            Set Image Quality to "**High"** (lossless seemed too brutal over WAN connections.)
          - Enable RemoteFX encoding for RemoteFX clients designed for Windows Server 2008R2 SP1 = **Enabled**.
            logseq.order-list-type:: number
        - Computer Configuration > Policies > Administrative Template > Windows Components > Remote Desktop Services > Remote Desktop Session Host > Remote Session Enviorment > Remote FX for Windows Server 2008R2
          logseq.order-list-type:: number
          collapsed:: true
          - Configure Remote FX = **Enabled**
            logseq.order-list-type:: number
          - Optimize visual experience when using Remote FX = **Enabled**
            logseq.order-list-type:: number
            Set Screen capture rate (frames per second) = **Highest (best quality)**
            Set Screen Image Quality = **Highest (best quality)**
          - Optimize visual experience for remote desktop sessions = **Enabled**
            logseq.order-list-type:: number
            Set Visual Experience = **Rich Multimedia**
      - ~~解锁 60 帧~~ via: {{nav-ri https://blog.csdn.net/csdn_life18/article/details/108250846}}
        logseq.order-list-type:: number
        collapsed:: true
        - `regedit.msc`
          logseq.order-list-type:: number
          - `计算机\HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server\WinStations`
            logseq.order-list-type:: number
            - 新建 `DWORD (32位)` 值，命名 `DWMFRAMEINTERVAL`
              logseq.order-list-type:: number
            - 十进制 `15`
              logseq.order-list-type:: number
- ## What
  -
-
-