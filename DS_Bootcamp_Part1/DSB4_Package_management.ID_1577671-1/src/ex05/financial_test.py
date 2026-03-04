import pytest
from financial import parse_financials


def test_return_type():
    fake_html = """
    <div data-test="fin-row">
        <div>Total Revenue</div>
        <div>100</div>
        <div>200</div>
    </div>
    """
    result = parse_financials(fake_html, "Total Revenue")
    assert isinstance(result, tuple)


def test_correct_field():
    fake_html = """
    <div data-test="fin-row">
        <div>Total Revenue</div>
        <div>100</div>
        <div>200</div>
    </div>
    """
    result = parse_financials(fake_html, "Total Revenue")
    assert result == ("Total Revenue", "100", "200")


def test_wrong_field():
    fake_html = """
    <div data-test="fin-row">
        <div>Total Revenue</div>
        <div>100</div>
    </div>
    """
    with pytest.raises(Exception):
        parse_financials(fake_html, "Net Income")
