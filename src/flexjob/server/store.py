from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from flexjob.db import models
from flexjob.protos.google.longrunning import operations_pb2


class OpsStore:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def set_ops(self, ops: operations_pb2.Operation) -> operations_pb2.Operation:
        instance, job_id = ops.name.split("/")
        self.session.add(models.FlexJob(job_id=job_id, instance=instance))
        await self.session.commit()
        return ops

    async def get_ops(self, instance: str, job_id: str) -> operations_pb2.Operation:
        query = (
            select(models.FlexJob)
            .where(models.FlexJob.instance == instance, models.FlexJob.job_id == job_id)
            .limit(1)
        )
        result = await self.session.execute(query)
        ops = result.scalars().one()
        return operations_pb2.Operation(name=f"{ops.instance}/{ops.job_id}")
