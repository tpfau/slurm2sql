
from typing import TYPE_CHECKING
from sqlalchemy import Column, Integer, Float, String, Text, Table, MetaData
from sqlalchemy.orm import registry
mapper_registry = registry()

metadata = MetaData()


class Allocation:
    if TYPE_CHECKING:
        id : Integer
        JobID : String
        JobIDnostep : Integer
        JobIDonly : Integer
        JobStep : String
        ArrayTaskID : Integer
        JobIDRawOnly : Integer

        # Metadata
        JobName : String
        User : String
        Group : String
        Account : String
        SubmitLine : Text
        Billing : Integer

        # Times and runtime info
        State : String
        Timelimit : Float
        Elapsed : Float
        Time : Integer
        Submit : Integer
        Start : Integer
        End : Integer
        QueueTime : Integer
        Partition : String
        ExitCodeRaw : String
        ExitCode : Integer
        ExitSignal : Integer
        NodeList : String
        Priority : Integer
        ConsumedEnergy : Integer

        # Nodes
        ReqNodes : Integer
        NNodes : Integer
        AllocNodes : Integer

        # Resources
        ReqTRES : Text
        NTasks : Integer
        AllocTRES : Text
        TRESUsageInTot : Text
        TRESUsageOutTot : Text

        # CPU
        NCPUS : Integer
        ReqCPUS : Integer
        AllocCPUS : Integer
        CPUTime : Float
        TotalCPU : Float
        UserCPU : Float
        SystemCPU : Float
        CPUEff : Float
        MinCPU : Float
        MinCPUNode : String
        MinCPUTask : String

        # Memory
        TotalMem : Float
        AllocMem : Float
        MemEff : Float
        ReqMem : Float
        ReqMemNode : Float
        ReqMemCPU : Float
        AveRSS : Float
        MaxRSS : Float
        MaxRSSNode : String
        MaxRSSTask : String
        MaxPages : Integer
        MaxVMSize : Float

        # Disk
        AveDiskRead : Integer
        AveDiskWrite : Integer
        MaxDiskRead : Integer
        MaxDiskWrite : Integer
        TotDiskRead : Float
        TotDiskWrite : Float

        # GPU
        ReqGPUS : Float
        Comment : Text
        GpuEff : Float
        NGpus : Float
        GpuType : String
        GpuUtil : Float
        GpuMem : Float
        GpuUtilTot : Float
        GpuMemTot : Float
    

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
        id : Integer
        JobID : String
        JobIDnostep : Integer
        JobIDonly : Integer
        JobStep : String
        ArrayTaskID : Integer
        JobIDRawOnly : Integer

        # Metadata
        JobName : String
        User : String
        Group : String
        Account : String
        SubmitLine : Text
        Billing : Integer

        # Times and runtime info
        State : String
        Timelimit : Float
        Elapsed : Float
        Time : Integer
        Submit : Integer
        Start : Integer
        End : Integer
        QueueTime : Integer
        Partition : String
        ExitCodeRaw : String
        ExitCode : Integer
        ExitSignal : Integer
        NodeList : String
        Priority : Integer
        ConsumedEnergy : Integer

        # Nodes
        ReqNodes : Integer
        NNodes : Integer
        AllocNodes : Integer

        # Resources
        ReqTRES : Text
        NTasks : Integer
        AllocTRES : Text
        TRESUsageInTot : Text
        TRESUsageOutTot : Text

        # CPU
        NCPUS : Integer
        ReqCPUS : Integer
        AllocCPUS : Integer
        CPUTime : Float
        TotalCPU : Float
        UserCPU : Float
        SystemCPU : Float
        CPUEff : Float
        MinCPU : Float
        MinCPUNode : String
        MinCPUTask : String

        # Memory
        TotalMem : Float
        AllocMem : Float
        MemEff : Float
        ReqMem : Float
        ReqMemNode : Float
        ReqMemCPU : Float
        AveRSS : Float
        MaxRSS : Float
        MaxRSSNode : String
        MaxRSSTask : String
        MaxPages : Integer
        MaxVMSize : Float

        # Disk
        AveDiskRead : Integer
        AveDiskWrite : Integer
        MaxDiskRead : Integer
        MaxDiskWrite : Integer
        TotDiskRead : Float
        TotDiskWrite : Float

        # GPU
        ReqGPUS : Float
        Comment : Text
        GpuEff : Float
        NGpus : Float
        GpuType : String
        GpuUtil : Float
        GpuMem : Float
        GpuUtilTot : Float
        GpuMemTot : Float
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
        JobID : String
        User : String
        Partition : String
        JobName : String
        SubmitLines : Text
        Account : String
        State : String
        NodeList : String
        Time : Integer
        TimeLimit : Float
        Start : Integer
        End : Integer
        NNodes : Integer
        ReqTRES : Text
        Elapsed : Float
        NCPUS : Integer
        CPUeff : Float
        cpu_s_reserved : Float
        cpu_s_used : Float
        MemReq : Float
        AllocMem : Float
        TotalMem : Float
        MaxRSS : Float
        MemEff : Float
        mem_s_reserved : Float
        NGpus : Float
        GPUType : String
        gpu_s_reserved : Float
        gpu_s_used : Float
        GpuEff : Float
        GpuMem : Float
        MaxDiskRead : Integer
        MaxDiskWrite : Integer
        TotDiskRead : Float
        TotDiskWrite : Float
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
