import json
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import func

from models.db import Vulnerability, SeverityLevel

async def seed_data(session: AsyncSession):
    existing = await session.scalar(select(func.count(Vulnerability.id)))
    if existing > 0:
        return

    with open("seed/vulnerabilities.json") as f:
        data = json.load(f)

    severity_cache = {}
    for item in data:
        sev_name = item["severity"]
        if sev_name not in severity_cache:
            severity = SeverityLevel(name=sev_name)
            session.add(severity)
            await session.flush()
            severity_cache[sev_name] = severity
        else:
            severity = severity_cache[sev_name]

        vuln = Vulnerability(
            name=item["name"],
            keyword=item["keyword"],
            class_id=item["class_id"],
            severity=severity
        )
        session.add(vuln)

    await session.commit()