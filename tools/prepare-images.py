"""从相邻项目的已公开配图生成网站用 WebP，不修改输入。"""

from argparse import ArgumentParser
from pathlib import Path

from PIL import Image


ASSETS = (
    ("cs-systems-lab", ("docs", "validation", "cache-comparison.png"), "systems-lab.webp", (1280, 800), (0, 540, 1280, 1340)),
    ("supply-chain-risk-core", ("assets", "readme-risk-core.png"), "risk-overview.webp", (1440, 800), None),
    ("cumcm-2023-multibeam", ("assets", "readme-multibeam.png"), "multibeam.webp", (1080, 600), None),
    ("nanjing-weather-visualization", ("assets", "readme-weather-overview.png"), "weather.webp", (1080, 675), None),
    ("campus-news-portal", ("docs", "validation", "root-portal.png"), "news-portal.webp", (1080, 675), (0, 0, 1280, 800)),
)


def prepare(projects_root: Path, output: Path) -> None:
    output.mkdir(parents=True, exist_ok=True)
    for repo, relative, name, size, crop_box in ASSETS:
        source = projects_root.joinpath(repo, *relative)
        with Image.open(source) as original:
            original.load()
            image = original.convert("RGB")
            if crop_box is not None:
                left, top, right, bottom = crop_box
                if not (0 <= left < right <= image.width and 0 <= top < bottom <= image.height):
                    raise ValueError(f"裁切范围超出原图，需重新确认：{source}")
                image = image.crop(crop_box)
            if image.width * size[1] != image.height * size[0]:
                raise ValueError(f"图片宽高比发生变化，需重新确认裁切：{source}")
            image = image.resize(size, Image.Resampling.LANCZOS)
            target = output / name
            image.save(target, format="WEBP", quality=92, method=6)
            print(f"{name}: {size[0]} x {size[1]}, {target.stat().st_size} bytes")


if __name__ == "__main__":
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("--projects-root", type=Path, required=True)
    args = parser.parse_args()
    prepare(args.projects_root.resolve(strict=True), Path(__file__).resolve().parents[1] / "assets")
