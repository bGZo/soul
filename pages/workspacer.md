title:: workspacer
description:: A tiled windows manager
tags:: #deprecated 
source:: [workspacer/workspacer: a tiling window manager for Windows](https://github.com/workspacer/workspacer)  ![](https://img.shields.io/github/stars/workspacer/workspacer)
document:: [configuring workspacer](https://workspacer.org/config/)
changelog:: [changelog](https://workspacer.org/changelog/)
created:: [[20220427]]
description:: [Tiling window manager - Wikipedia](https://en.wikipedia.org/wiki/Tiling_window_manager); [windows 下有没有这样的分屏工具-(内有图)? - V2EX](https://www.v2ex.com/t/429177#; )

- ## What
  collapsed:: true
  - ### Configure
    collapsed:: true
    - ```
      #r "C:\Users\15517\bin\workspacer-0.9.11.81\workspacer.Shared.dll"
      #r "C:\Users\15517\bin\workspacer-0.9.11.81\plugins\workspacer.Bar\workspacer.Bar.dll"
      #r "C:\Users\15517\bin\workspacer-0.9.11.81\plugins\workspacer.ActionMenu\workspacer.ActionMenu.dll"
      #r "C:\Users\15517\bin\workspacer-0.9.11.81\plugins\workspacer.FocusIndicator\workspacer.FocusIndicator.dll"
      using System;
      using workspacer;
      using workspacer.Bar;
      using workspacer.ActionMenu;
      using workspacer.FocusIndicator;
      Action<IConfigContext> doConfig = (context) => {
          // Uncomment to switch update branch (or to disable updates)
          // context.Branch = Branch.None;
          context.AddBar(new BarPluginConfig(){
              BarTitle = "workspacer.Bar",
              FontSize = 14,
              DefaultWidgetBackground = new Color(67, 67, 67),
              // DefaultWidgetForeground = Color.White,
              // BackgroundColor = "white",
              FontName = "Sarasa Mono SC",
              RightWidgets = () => new IBarWidget[] {
                  new workspacer.Bar.Widgets.TimeWidget(1000,"yyyy-MM-dd  hh:mm:ss"),
                  new workspacer.Bar.Widgets.BatteryWidget(),
                  new workspacer.Bar.Widgets.ActiveLayoutWidget(),
                  },
          });
          context.WorkspaceContainer.CreateWorkspaces("[one]", "[two]", "[three]", "[four]", "[five]");
          // context.WorkspaceContainer.CreateWorkspaces(" 1 ", " 2 ", " 3 ", " 4 ", " 5 ");
          context.AddFocusIndicator();
          var actionMenu = context.AddActionMenu();
          context.CanMinimizeWindows = true; // false by default
          //unsubscribe, alt right/left always bugs.
          context.Keybinds.Unsubscribe(KeyModifiers.Alt, Keys.Left);
          context.Keybinds.Unsubscribe(KeyModifiers.Alt, Keys.Right);
          context.Keybinds.Unsubscribe(KeyModifiers.Alt, Keys.Space);
      };
      return doConfig;
      ```
  - ### Shortcut
    collapsed:: true
    - | keybind          | description                                          |
      |------------------|------------------------------------------------------|
      | alt-shift-e      | toggle enabled/disabled                              |
      | alt-shift-c      | close focused window                                 |
      | alt-space        | next layout engine                                   |
      | alt-shift-space  | previous layout engine                               |
      | alt-n            | reset layout                                         |
      | alt-j            | focus next window                                    |
      | alt-k            | focus previous window                                |
      | alt-m            | focus primary window                                 |
      | alt-enter        | swap focus and primary window                        |
      | **alt-shift-j**      | swap focus and next window                           |
      | **alt-shift-k**      | swap focus and previous window                       |
      | **alt-h**            | shrink primary area                                  |
      | **alt-l**            | expand primary area                                  |
      | alt-comma        | increment number of primary windows                  |
      | alt-period       | decrement number of primary windows                  |
      | **alt-t**            | toggle tiling for focused window                     |
      | alt-p            | open action menu                                     |
      | alt-shift-q      | quit workspacer                                      |
      | alt-q            | restart workspacer                                   |
      | alt-left         | switch to left workspace                             |
      | alt-right        | switch to right workspace                            |
      | **alt-{1..9}**       | switch to workspace {1..9}                           |
      | alt-{wer}        | focus monitor {123}                                  |
      | alt-shift-{wer}  | move focused window to monitor {123}                 |
      | alt-shift-{1..9} | move focused window to workspace {1..9}              |
      | alt-o            | dump window debug output for all windows             |
      | alt-shift-o      | dump window debug output for window under the cursor |
      | alt-shift-i      | toggle debug window                                  |
      | alt-shift-/      | toggle keybind dialog                                |
      via: [key bindings](https://workspacer.org/keybindings/)