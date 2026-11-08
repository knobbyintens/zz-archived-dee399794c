"""Batch runner template."""

from nettlewood.engine.runner import Runner, RunnerConfig


def build_runner(stages):
    return Runner(stages, RunnerConfig(max_stage_attempts=5))
