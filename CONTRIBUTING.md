# Contributing

OpenScorbot is a legacy robotics engineering project.

## Development model

Maintenance follows GitFlow without rewriting the original project history.

```mermaid
gitGraph
    commit id: "master"
    branch develop
    checkout develop
    commit id: "integration"

    branch feature/documentation
    checkout feature/documentation
    commit id: "change"

    checkout develop
    merge feature/documentation

    branch release/x.y.z
    checkout release/x.y.z
    commit id: "release prep"

    checkout master
    merge release/x.y.z tag: "vx.y.z"

    checkout develop
    merge master
```

Use:

- `master` for the stable historical state.
- `develop` for integrated maintenance work.
- `feature/<name>` for isolated improvements.
- `release/<version>` for curated repository releases.

## Preservation rules

Do not remove or alter original contributor credits.

Avoid destructive modernization of legacy sources unless the change is clearly documented.

Changes should distinguish between:

- historical behavior
- documentation-only updates
- compatibility fixes
- new functionality

## Hardware-dependent changes

Any change affecting communication, homing or movement should state:

- robot/controller hardware used
- operating system
- Python version
- PyUSB version
- whether behavior was tested on real hardware

## Safety

This software can command physical robot motion.

Do not treat unverified changes as safe for hardware execution.
