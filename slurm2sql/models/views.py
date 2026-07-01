
from typing import TYPE_CHECKING
from sqlalchemy import Column, Integer, Float, String, Text, Table, MetaData
from sqlalchemy.orm import registry, Mapped
mapper_registry = registry()

metadata = MetaData()


class Allocation:
    if TYPE_CHECKING:
        id : Mapped[Integer]
        JobID : Mapped[String]
        JobIDnostep : Mapped[Integer]
        JobIDonly : Mapped[Integer]
        JobStep : Mapped[String]
        ArrayTaskID : Mapped[Integer]
        JobIDRawOnly : Mapped[Integer]

        # Metadata
        JobName : Mapped[String]
        User : Mapped[String]
        Group : Mapped[String]
        Account : Mapped[String]
        SubmitLine : Mapped[Text]
        Billing : Mapped[Integer]

        # Times and runtime info
        State : Mapped[String]
        Timelimit : Mapped[Float]
        Elapsed : Mapped[Float]
        Time : Mapped[Integer]
        Submit : Mapped[Integer]
        Start : Mapped[Integer]
        End : Mapped[Integer]
        QueueTime : Mapped[Integer]
        Partition : Mapped[String]
        ExitCodeRaw : Mapped[String]
        ExitCode : Mapped[Integer]
        ExitSignal : Mapped[Integer]
        NodeList : Mapped[String]
        Priority : Mapped[Integer]
        ConsumedEnergy : Mapped[Integer]

        # Nodes
        ReqNodes : Mapped[Integer]
        NNodes : Mapped[Integer]
        AllocNodes : Mapped[Integer]

        # Resources
        ReqTRES : Mapped[Text]
        NTasks : Mapped[Integer]
        AllocTRES : Mapped[Text]
        TRESUsageInTot : Mapped[Text]
        TRESUsageOutTot : Mapped[Text]

        # CPU
        NCPUS : Mapped[Integer]
        ReqCPUS : Mapped[Integer]
        AllocCPUS : Mapped[Integer]
        CPUTime : Mapped[Float]
        TotalCPU : Mapped[Float]
        UserCPU : Mapped[Float]
        SystemCPU : Mapped[Float]
        CPUEff : Mapped[Float]
        MinCPU : Mapped[Float]
        MinCPUNode : Mapped[String]
        MinCPUTask : Mapped[String]

        # Memory
        TotalMem : Mapped[Float]
        AllocMem : Mapped[Float]
        MemEff : Mapped[Float]
        ReqMem : Mapped[Float]
        ReqMemNode : Mapped[Float]
        ReqMemCPU : Mapped[Float]
        AveRSS : Mapped[Float]
        MaxRSS : Mapped[Float]
        MaxRSSNode : Mapped[String]
        MaxRSSTask : Mapped[String]
        MaxPages : Mapped[Integer]
        MaxVMSize : Mapped[Float]

        # Disk
        AveDiskRead : Mapped[Integer]
        AveDiskWrite : Mapped[Integer]
        MaxDiskRead : Mapped[Integer]
        MaxDiskWrite : Mapped[Integer]
        TotDiskRead : Mapped[Float]
        TotDiskWrite : Mapped[Float]

        # GPU
        ReqGPUS : Mapped[Float]
        Comment : Mapped[Text]
        GpuEff : Mapped[Float]
        NGpus : Mapped[Float]
        GpuType : Mapped[String]
        GpuUtil : Mapped[Float]
        GpuMem : Mapped[Float]
        GpuUtilTot : Mapped[Float]
        GpuMemTot : Mapped[Float]
    

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
        id : Mapped[Integer]
        JobID : Mapped[String]
        JobIDnostep : Mapped[Integer]
        JobIDonly : Mapped[Integer]
        JobStep : Mapped[String]
        ArrayTaskID : Mapped[Integer]
        JobIDRawOnly : Mapped[Integer]

        # Metadata
        JobName : Mapped[String]
        User : Mapped[String]
        Group : Mapped[String]
        Account : Mapped[String]
        SubmitLine : Mapped[Text]
        Billing : Mapped[Integer]

        # Times and runtime info
        State : Mapped[String]
        Timelimit : Mapped[Float]
        Elapsed : Mapped[Float]
        Time : Mapped[Integer]
        Submit : Mapped[Integer]
        Start : Mapped[Integer]
        End : Mapped[Integer]
        QueueTime : Mapped[Integer]
        Partition : Mapped[String]
        ExitCodeRaw : Mapped[String]
        ExitCode : Mapped[Integer]
        ExitSignal : Mapped[Integer]
        NodeList : Mapped[String]
        Priority : Mapped[Integer]
        ConsumedEnergy : Mapped[Integer]

        # Nodes
        ReqNodes : Mapped[Integer]
        NNodes : Mapped[Integer]
        AllocNodes : Mapped[Integer]

        # Resources
        ReqTRES : Mapped[Text]
        NTasks : Mapped[Integer]
        AllocTRES : Mapped[Text]
        TRESUsageInTot : Mapped[Text]
        TRESUsageOutTot : Mapped[Text]

        # CPU
        NCPUS : Mapped[Integer]
        ReqCPUS : Mapped[Integer]
        AllocCPUS : Mapped[Integer]
        CPUTime : Mapped[Float]
        TotalCPU : Mapped[Float]
        UserCPU : Mapped[Float]
        SystemCPU : Mapped[Float]
        CPUEff : Mapped[Float]
        MinCPU : Mapped[Float]
        MinCPUNode : Mapped[String]
        MinCPUTask : Mapped[String]

        # Memory
        TotalMem : Mapped[Float]
        AllocMem : Mapped[Float]
        MemEff : Mapped[Float]
        ReqMem : Mapped[Float]
        ReqMemNode : Mapped[Float]
        ReqMemCPU : Mapped[Float]
        AveRSS : Mapped[Float]
        MaxRSS : Mapped[Float]
        MaxRSSNode : Mapped[String]
        MaxRSSTask : Mapped[String]
        MaxPages : Mapped[Integer]
        MaxVMSize : Mapped[Float]

        # Disk
        AveDiskRead : Mapped[Integer]
        AveDiskWrite : Mapped[Integer]
        MaxDiskRead : Mapped[Integer]
        MaxDiskWrite : Mapped[Integer]
        TotDiskRead : Mapped[Float]
        TotDiskWrite : Mapped[Float]

        # GPU
        ReqGPUS : Mapped[Float]
        Comment : Mapped[Text]
        GpuEff : Mapped[Float]
        NGpus : Mapped[Float]
        GpuType : Mapped[String]
        GpuUtil : Mapped[Float]
        GpuMem : Mapped[Float]
        GpuUtilTot : Mapped[Float]
        GpuMemTot : Mapped[Float]
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
        JobID : Mapped[String]
        User : Mapped[String]
        Partition : Mapped[String]
        JobName : Mapped[String]
        SubmitLines : Mapped[Text]
        Account : Mapped[String]
        State : Mapped[String]
        NodeList : Mapped[String]
        Time : Mapped[Integer]
        TimeLimit : Mapped[Float]
        Start : Mapped[Integer]
        End : Mapped[Integer]
        NNodes : Mapped[Integer]
        ReqTRES : Mapped[Text]
        Elapsed : Mapped[Float]
        NCPUS : Mapped[Integer]
        CPUeff : Mapped[Float]
        cpu_s_reserved : Mapped[Float]
        cpu_s_used : Mapped[Float]
        MemReq : Mapped[Float]
        AllocMem : Mapped[Float]
        TotalMem : Mapped[Float]
        MaxRSS : Mapped[Float]
        MemEff : Mapped[Float]
        mem_s_reserved : Mapped[Float]
        NGpus : Mapped[Float]
        GPUType : Mapped[String]
        gpu_s_reserved : Mapped[Float]
        gpu_s_used : Mapped[Float]
        GpuEff : Mapped[Float]
        GpuMem : Mapped[Float]
        MaxDiskRead : Mapped[Integer]
        MaxDiskWrite : Mapped[Integer]
        TotDiskRead : Mapped[Float]
        TotDiskWrite : Mapped[Float]
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
