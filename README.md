# Github Action Test

![example workflow](https://github.com/bjtj/githubactiontest/actions/workflows/python-unittest-main.yml/badge.svg)

python-unittest-main.yml (main branch)

![python unittest workflow dev branch](https://github.com/bjtj/githubactiontest/actions/workflows/python-unittest-main.yml/badge.svg)

python-unittest.yml (dev branch)

![python unittest workflow dev branch](https://github.com/bjtj/githubactiontest/actions/workflows/python-unittest.yml/badge.svg?branch=dev)


## PyTest

<https://docs.pytest.org/en/7.4.x/>

e.g.)

```bash
$ pytest
=========================== test session starts ============================
platform linux -- Python 3.x.y, pytest-7.x.y, pluggy-1.x.y
rootdir: /home/sweet/project
collected 1 item

test_sample.py F                                                     [100%]

================================= FAILURES =================================
_______________________________ test_answer ________________________________

    def test_answer():
>       assert inc(3) == 5
E       assert 4 == 5
E        +  where 4 = inc(3)

test_sample.py:6: AssertionError
========================= short test summary info ==========================
FAILED test_sample.py::test_answer - assert 4 == 5
============================ 1 failed in 0.12s =============================
```


## Adding a workflow status badge

<https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/adding-a-workflow-status-badge>

```
https://github.com/<OWNER>/<REPOSITORY>/actions/workflows/<WORKFLOW_FILE>/badge.svg
```
