import garak.probes.base


class UncappedIterativeProbe(garak.probes.base.IterativeProbe):
    """Minimal iterative probe for exercising the base probe loop."""

    active = True

    def _create_init_attempts(self):
        return []

    def _generate_next_attempts(self, last_attempt):
        return []


def test_iterative_probe_allows_unset_soft_prompt_cap():
    probe = UncappedIterativeProbe()
    probe.follow_prompt_cap = True
    probe.soft_probe_prompt_cap = None
    probe.max_calls_per_conv = 1

    assert probe.probe(None) == []
    assert probe.max_attempts_before_termination == float("inf")
