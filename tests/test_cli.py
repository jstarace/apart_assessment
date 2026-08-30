from apart_assessment.cli import main


def test_main(capsys) -> None:
    main()
    assert capsys.readouterr().out == "Apart assessment environment is ready.\n"
