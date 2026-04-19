import subprocess


def translate_text(text: str, target_lang: str) -> tuple[str, str]:
    result = subprocess.run(
        ["crow", "-i", "-b", "-t", target_lang],
        input=text,
        text=True,
        capture_output=True,
    )
    return result.stdout.strip(), result.stderr.strip()
