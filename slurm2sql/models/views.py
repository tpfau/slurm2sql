"""
Setup for views. For type checking during dev, the classes 
have Elements that can be used in sqlalchemy calls which , in production
get mapped to the actual db objects via imperative mappings. 
"""
from typing import TYPE_CHECKING
from sqlalchemy import Column, Integer, Float, String, Text, Table, MetaData
from sqlalchemy.orm import registry, Mapped
mapper_registry = registry()

metadata = MetaData()


class Allocation:
    if TYPE_CHECKING:
        id : Mapped[int]
        JobID : Mapped[str]
        JobIDnostep : Mapped[int]
        JobIDonly : Mapped[int]
        JobStep : Mapped[str]
        ArrayTaskID : Mapped[int]
        JobIDRawOnly : Mapped[int]

        # Metadata
        JobName : Mapped[str]
        User : Mapped[str]
        Group : Mapped[str]
        Account : Mapped[str]
        SubmitLine : Mapped[str]
        Billing : Mapped[int]

        # Times and runtime info
        State : Mapped[str]
        Timelimit : Mapped[float]
        Elapsed : Mapped[float]
        Time : Mapped[int]
        Submit : Mapped[int]
        Start : Mapped[int]
        End : Mapped[int]
        QueueTime : Mapped[int]
        Partition : Mapped[str]
        ExitCodeRaw : Mapped[str]
        ExitCode : Mapped[int]
        ExitSignal : Mapped[int]
        NodeList : Mapped[str]
        Priority : Mapped[int]
        ConsumedEnergy : Mapped[int]

        # Nodes
        ReqNodes : Mapped[int]
        NNodes : Mapped[int]
        AllocNodes : Mapped[int]

        # Resources
        ReqTRES : Mapped[str]
        NTasks : Mapped[int]
        AllocTRES : Mapped[str]
        TRESUsageInTot : Mapped[str]
        TRESUsageOutTot : Mapped[str]

        # CPU
        NCPUS : Mapped[int]
        ReqCPUS : Mapped[int]
        AllocCPUS : Mapped[int]
        CPUTime : Mapped[float]
        TotalCPU : Mapped[float]
        UserCPU : Mapped[float]
        SystemCPU : Mapped[float]
        CPUEff : Mapped[float]
        MinCPU : Mapped[float]
        MinCPUNode : Mapped[str]
        MinCPUTask : Mapped[str]

        # Memory
        TotalMem : Mapped[float]
        AllocMem : Mapped[float]
        MemEff : Mapped[float]
        ReqMem : Mapped[float]
        ReqMemNode : Mapped[float]
        ReqMemCPU : Mapped[float]
        AveRSS : Mapped[float]
        MaxRSS : Mapped[float]
        MaxRSSNode : Mapped[str]
        MaxRSSTask : Mapped[str]
        MaxPages : Mapped[int]
        MaxVMSize : Mapped[float]

        # Disk
        AveDiskRead : Mapped[int]
        AveDiskWrite : Mapped[int]
        MaxDiskRead : Mapped[int]
        MaxDiskWrite : Mapped[int]
        TotDiskRead : Mapped[float]
        TotDiskWrite : Mapped[float]

        # GPU
        ReqGPUS : Mapped[float]
        Comment : Mapped[str]
        GpuEff : Mapped[float]
        NGpus : Mapped[float]
        GpuType : Mapped[str]
        GpuUtil : Mapped[float]
        GpuMem : Mapped[float]
        GpuUtilTot : Mapped[float]
        GpuMemTot : Mapped[float]
    

allocation_view = Table("allocations", metadata, 
    Column("id",Integer, primary_key=True, autoincrement=True),
    Column("JobID",String, unique=True, index=True),
    Column("JobIDnostep",Integer, index=True),
    Column("JobIDonly",Integer),
    Column("JobStep",String),
    Column("ArrayTaskID",Integer),
    Column("JobIDRawOnly",Integer, index=True),
    # Metadata
    Column("JobName",String),
    Column("User",String, index=True),
    Column("Group",String),
    Column("Account",String),
    Column("SubmitLine",Text),
    Column("Billing",Integer),
    # Times and runtime info
    Column("State",String),
    Column("Timelimit",Float),
    Column("Elapsed",Float),
    Column("Time",Integer, index=True),
    Column("Submit",Integer),
    Column("Start",Integer, index=True),
    Column("End",Integer),
    Column("QueueTime",Integer),
    Column("Partition",String),
    Column("ExitCodeRaw",String),
    Column("ExitCode",Integer),
    Column("ExitSignal",Integer),
    Column("NodeList",String),
    Column("Priority",Integer),
    Column("ConsumedEnergy",Integer),

    # Nodes
    Column("ReqNodes",Integer),
    Column("NNodes",Integer),
    Column("AllocNodes",Integer),

    # Resources
    Column("ReqTRES",Text),
    Column("NTasks",Integer),
    Column("AllocTRES",Text),
    Column("TRESUsageInTot",Text),
    Column("TRESUsageOutTot",Text),

    # CPU
    Column("NCPUS",Integer),
    Column("ReqCPUS",Integer),
    Column("AllocCPUS",Integer),
    Column("CPUTime",Float),
    Column("TotalCPU",Float),
    Column("UserCPU",Float),
    Column("SystemCPU",Float),
    Column("CPUEff",Float),
    Column("MinCPU",Float),
    Column("MinCPUNode",String),
    Column("MinCPUTask",String),

    # Memory
    Column("TotalMem",Float),
    Column("AllocMem",Float),
    Column("MemEff",Float),
    Column("ReqMem",Float),
    Column("ReqMemNode",Float),
    Column("ReqMemCPU",Float),
    Column("AveRSS",Float),
    Column("MaxRSS",Float),
    Column("MaxRSSNode",String),
    Column("MaxRSSTask",String),
    Column("MaxPages",Integer),
    Column("MaxVMSize",Float),

    # Disk
    Column("AveDiskRead",Integer),
    Column("AveDiskWrite",Integer),
    Column("MaxDiskRead",Integer),
    Column("MaxDiskWrite",Integer),
    Column("TotDiskRead",Float),
    Column("TotDiskWrite",Float),

    # GPU
    Column("ReqGPUS",Float),
    Column("Comment",Text),
    Column("GpuEff",Float),
    Column("NGpus",Float),
    Column("GpuType",String),
    Column("GpuUtil",Float),
    Column("GpuMem",Float),
    Column("GpuUtilTot",Float),
    Column("GpuMemTot",Float)
)

class Step:
    if TYPE_CHECKING:
        id : Mapped[int]
        JobID : Mapped[str]
        JobIDnostep : Mapped[int]
        JobIDonly : Mapped[int]
        JobStep : Mapped[str]
        ArrayTaskID : Mapped[int]
        JobIDRawOnly : Mapped[int]

        # Metadata
        JobName : Mapped[str]
        User : Mapped[str]
        Group : Mapped[str]
        Account : Mapped[str]
        SubmitLine : Mapped[str]
        Billing : Mapped[int]

        # Times and runtime info
        State : Mapped[str]
        Timelimit : Mapped[float]
        Elapsed : Mapped[float]
        Time : Mapped[int]
        Submit : Mapped[int]
        Start : Mapped[int]
        End : Mapped[int]
        QueueTime : Mapped[int]
        Partition : Mapped[str]
        ExitCodeRaw : Mapped[str]
        ExitCode : Mapped[int]
        ExitSignal : Mapped[int]
        NodeList : Mapped[str]
        Priority : Mapped[int]
        ConsumedEnergy : Mapped[int]

        # Nodes
        ReqNodes : Mapped[int]
        NNodes : Mapped[int]
        AllocNodes : Mapped[int]

        # Resources
        ReqTRES : Mapped[str]
        NTasks : Mapped[int]
        AllocTRES : Mapped[str]
        TRESUsageInTot : Mapped[str]
        TRESUsageOutTot : Mapped[str]

        # CPU
        NCPUS : Mapped[int]
        ReqCPUS : Mapped[int]
        AllocCPUS : Mapped[int]
        CPUTime : Mapped[float]
        TotalCPU : Mapped[float]
        UserCPU : Mapped[float]
        SystemCPU : Mapped[float]
        CPUEff : Mapped[float]
        MinCPU : Mapped[float]
        MinCPUNode : Mapped[str]
        MinCPUTask : Mapped[str]

        # Memory
        TotalMem : Mapped[float]
        AllocMem : Mapped[float]
        MemEff : Mapped[float]
        ReqMem : Mapped[float]
        ReqMemNode : Mapped[float]
        ReqMemCPU : Mapped[float]
        AveRSS : Mapped[float]
        MaxRSS : Mapped[float]
        MaxRSSNode : Mapped[str]
        MaxRSSTask : Mapped[str]
        MaxPages : Mapped[int]
        MaxVMSize : Mapped[float]

        # Disk
        AveDiskRead : Mapped[int]
        AveDiskWrite : Mapped[int]
        MaxDiskRead : Mapped[int]
        MaxDiskWrite : Mapped[int]
        TotDiskRead : Mapped[float]
        TotDiskWrite : Mapped[float]

        # GPU
        ReqGPUS : Mapped[float]
        Comment : Mapped[str]
        GpuEff : Mapped[float]
        NGpus : Mapped[float]
        GpuType : Mapped[str]
        GpuUtil : Mapped[float]
        GpuMem : Mapped[float]
        GpuUtilTot : Mapped[float]
        GpuMemTot : Mapped[float]
    pass

steps_view = Table("steps", metadata,
    Column("id",Integer, primary_key=True, autoincrement=True),
    Column("JobID",String, unique=True, index=True),
    Column("JobIDnostep",Integer, index=True),
    Column("JobIDonly",Integer),
    Column("JobStep",String),
    Column("ArrayTaskID",Integer),
    Column("JobIDRawOnly",Integer, index=True),

    # Metadata
    Column("JobName",String),
    Column("User",String, index=True),
    Column("Group",String),
    Column("Account",String),
    Column("SubmitLine",Text),
    Column("Billing",Integer),

    # Times and runtime info
    Column("State",String),
    Column("Timelimit",Float),
    Column("Elapsed",Float),
    Column("Time",Integer, index=True),
    Column("Submit",Integer),
    Column("Start",Integer, index=True),
    Column("End",Integer),
    Column("QueueTime",Integer),
    Column("Partition",String),
    Column("ExitCodeRaw",String),
    Column("ExitCode",Integer),
    Column("ExitSignal",Integer),
    Column("NodeList",String),
    Column("Priority",Integer),
    Column("ConsumedEnergy",Integer),

    # Nodes
    Column("ReqNodes",Integer),
    Column("NNodes",Integer),
    Column("AllocNodes",Integer),

    # Resources
    Column("ReqTRES",Text),
    Column("NTasks",Integer),
    Column("AllocTRES",Text),
    Column("TRESUsageInTot",Text),
    Column("TRESUsageOutTot",Text),

    # CPU
    Column("NCPUS",Integer),
    Column("ReqCPUS",Integer),
    Column("AllocCPUS",Integer),
    Column("CPUTime",Float),
    Column("TotalCPU",Float),
    Column("UserCPU",Float),
    Column("SystemCPU",Float),
    Column("CPUEff",Float),
    Column("MinCPU",Float),
    Column("MinCPUNode",String),
    Column("MinCPUTask",String),

    # Memory
    Column("TotalMem",Float),
    Column("AllocMem",Float),
    Column("MemEff",Float),
    Column("ReqMem",Float),
    Column("ReqMemNode",Float),
    Column("ReqMemCPU",Float),
    Column("AveRSS",Float),
    Column("MaxRSS",Float),
    Column("MaxRSSNode",String),
    Column("MaxRSSTask",String),
    Column("MaxPages",Integer),
    Column("MaxVMSize",Float),

    # Disk
    Column("AveDiskRead",Integer),
    Column("AveDiskWrite",Integer),
    Column("MaxDiskRead",Integer),
    Column("MaxDiskWrite",Integer),
    Column("TotDiskRead",Float),
    Column("TotDiskWrite",Float),

    # GPU
    Column("ReqGPUS",Float),
    Column("Comment",Text),
    Column("GpuEff",Float),
    Column("NGpus",Float),
    Column("GpuType",String),
    Column("GpuUtil",Float),
    Column("GpuMem",Float),
    Column("GpuUtilTot",Float),
    Column("GpuMemTot",Float)
)
class Eff:
    if TYPE_CHECKING:
        JobID : Mapped[str]
        User : Mapped[str]
        Partition : Mapped[str]
        JobName : Mapped[str]
        SubmitLines : Mapped[str]
        Account : Mapped[str]
        State : Mapped[str]
        NodeList : Mapped[str]
        Time : Mapped[int]
        TimeLimit : Mapped[float]
        Start : Mapped[int]
        End : Mapped[int]
        NNodes : Mapped[int]
        ReqTRES : Mapped[str]
        Elapsed : Mapped[float]
        NCPUS : Mapped[int]
        CPUeff : Mapped[float]
        cpu_s_reserved : Mapped[float]
        cpu_s_used : Mapped[float]
        MemReq : Mapped[float]
        AllocMem : Mapped[float]
        TotalMem : Mapped[float]
        MaxRSS : Mapped[float]
        MemEff : Mapped[float]
        mem_s_reserved : Mapped[float]
        NGpus : Mapped[float]
        GPUType : Mapped[str]
        gpu_s_reserved : Mapped[float]
        gpu_s_used : Mapped[float]
        GpuEff : Mapped[float]
        GpuMem : Mapped[float]
        MaxDiskRead : Mapped[int]
        MaxDiskWrite : Mapped[int]
        TotDiskRead : Mapped[float]
        TotDiskWrite : Mapped[float]
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
