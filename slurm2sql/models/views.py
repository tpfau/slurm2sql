
from sqlalchemy import Column, Integer, Float, String, Text, Table, MetaData
from sqlalchemy.orm import registry
mapper_registry = registry()

metadata = MetaData()


class Allocation:
    pass

allocation_view = Table("allocations", metadata, 
Column("id",Integer, primary_key=True),
Column("\1",String, index=True),
Column("   JobIDnostep",Integer, index=True),
Column("JobStep",String),
Column("User",String, index=True),
Column("State",String),
Column("Start",Integer),
Column("End",Integer),
Column("Elapsed",Float),
Column("NCPUS",Integer),
Column("TotalCPU",Float),
Column("AllocMem",Float),
Column("TotalMem",Float),
Column("MemEff",Float),
Column("NGpus",Float),
Column("GpuEff",Float),
Column("NodeList",String),
Column("Partition",String),
Column("ReqTRES",Text),
Column("AllocTRES",Text),
Column("TRESUsageInTot",Text),
Column("Comment",Text)
)

class Step:
    pass

steps_view = Table("steps", metadata,
Column("id",Integer, primary_key=True),
Column("JobID",String, index=True),
Column("JobIDnostep",Integer, index=True),
Column("JobStep",String),
Column("User",String, index=True),
Column("State",String),
Column("Start",Integer),
Column("End",Integer),
Column("Elapsed",Float),
Column("NCPUS",Integer),
Column("TotalCPU",Float),
Column("AllocMem",Float),
Column("TotalMem",Float),
Column("MemEff",Float),
Column("NGpus",Float),
Column("GpuEff",Float),
Column("NodeList",String),
Column("Partition",String),
Column("ReqTRES",Text),
Column("AllocTRES",Text),
Column("TRESUsageInTot",Text),
Column("Comment",Text)
)
class Eff:
    pass

eff_view = Table("eff", metadata,
Column("JobID",String, primary_key=True),
Column("User",String),
Column("Partition",String),
Column("JobName",String),
Column("SubmitLines",Text),
Column("Account",String),
Column("State",String),
Column("NodeList",String),
Column("Time",Integer),
Column("TimeLimit",Float),
Column("Start",Integer),
Column("End",Integer),
Column("NNodes",Integer),
Column("ReqTRES",Text),
Column("Elapsed",Float),
Column("NCPUS",Integer),
Column("CPUeff",Float),
Column("cpu_s_reserved",Float),
Column("cpu_s_used",Float),
Column("MemReq",Float),
Column("AllocMem",Float),
Column("TotalMem",Float),
Column("MaxRSS",Float),
Column("MemEff",Float),
Column("mem_s_reserved",Float),
Column("NGpus",Float),
Column("GPUType",String),
Column("gpu_s_reserved",Float),
Column("gpu_s_used",Float),
Column("GpuEff",Float),
Column("GpuMem",Float),
Column("MaxDiskRead",Integer),
Column("MaxDiskWrite",Integer),
Column("TotDiskRead",Float),
Column("TotDiskWrite",Float),
)

mapper_registry.map_imperatively(Allocation, allocation_view)
mapper_registry.map_imperatively(Step, steps_view)
mapper_registry.map_imperatively(Eff, eff_view)
