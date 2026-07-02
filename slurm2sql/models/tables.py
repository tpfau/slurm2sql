
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, Float, String, BigInteger, Text, engine, Table, MetaData


Base = declarative_base()

class Slurm(Base):
    __tablename__ = 'slurm'
    # Basic identifiers
    id = Column(Integer, primary_key=True, autoincrement=True)
    JobID = Column(String, unique=True, index=True)
    JobIDnostep = Column(String, index=True)
    JobIDonly = Column(BigInteger)
    JobStep = Column(String)
    ArrayTaskID = Column(Integer)
    JobIDRawOnly = Column(Integer)

    # Metadata
    JobName = Column(String)
    User = Column(String, index=True)
    Group = Column(String)
    Account = Column(String)
    SubmitLine = Column(Text)
    Billing = Column(Integer)

    # Times and runtime info
    State = Column(String)
    Timelimit = Column(Float)
    Elapsed = Column(Float)
    Time = Column(Integer, index=True)
    Submit = Column(Integer)
    Start = Column(Integer, index=True)
    End = Column(Integer)
    QueueTime = Column(Integer)
    Partition = Column(String)
    ExitCodeRaw = Column(String)
    ExitCode = Column(Integer)
    ExitSignal = Column(Integer)
    NodeList = Column(String)
    Priority = Column(Integer)
    ConsumedEnergy = Column(Integer)

    # Nodes
    ReqNodes = Column(Integer)
    NNodes = Column(Integer)
    AllocNodes = Column(Integer)

    # Resources
    ReqTRES = Column(Text)
    NTasks = Column(Integer)
    AllocTRES = Column(Text)
    TRESUsageInTot = Column(Text)
    TRESUsageOutTot = Column(Text)

    # CPU
    NCPUS = Column(Integer)
    ReqCPUS = Column(Integer)
    AllocCPUS = Column(Integer)
    CPUTime = Column(Float)
    TotalCPU = Column(Float)
    UserCPU = Column(Float)
    SystemCPU = Column(Float)
    CPUEff = Column(Float)
    MinCPU = Column(Float)
    MinCPUNode = Column(String)
    MinCPUTask = Column(String)

    # Memory
    TotalMem = Column(Float)
    AllocMem = Column(Float)
    MemEff = Column(Float)
    ReqMem = Column(Float)
    ReqMemNode = Column(Float)
    ReqMemCPU = Column(Float)
    AveRSS = Column(Float)
    MaxRSS = Column(Float)
    MaxRSSNode = Column(String)
    MaxRSSTask = Column(String)
    MaxPages = Column(BigInteger)
    MaxVMSize = Column(Float)

    # Disk
    AveDiskRead = Column(BigInteger)
    AveDiskWrite = Column(BigInteger)
    MaxDiskRead = Column(BigInteger)
    MaxDiskWrite = Column(BigInteger)
    TotDiskRead = Column(Float)
    TotDiskWrite = Column(Float)

    # GPU
    ReqGPUS = Column(Float)
    Comment = Column(Text)
    GpuEff = Column(Float)
    NGpus = Column(Float)
    GpuType = Column(String)
    GpuUtil = Column(Float)
    GpuMem = Column(Float)
    GpuUtilTot = Column(Float)
    GpuMemTot = Column(Float)

class MetaSlurmLastUpdate(Base):
    __tablename__ = 'meta_slurm_lastupdate'
    id = Column(Integer, primary_key=True)
    update_time = Column(Float)

