import re
import os
from typing import Dict
import sys
import subprocess
from datetime import datetime
def run_command(cmd):    
           
    #LOG.debug(' '.join(cmd))
    error_handling = {'errors':'replace'} if sys.version_info[0]>=3 else {}
    p = subprocess.Popen(cmd,
                         stdout=subprocess.PIPE, universal_newlines=True,
                         **error_handling)
    return p.stdout


class SQUEUE:
    def __init__(self):
        job_data = parse_squeue_output()
        print(job_data)
        self.pending_data = {
            job["ID"]: {
                "start": datetime.fromisoformat(job["Start"]).timestamp() if job["Start"].strip() != "N/A" else None,
                "nodes": job["Nodes"] if job["Nodes"].strip() != "(null)" else None,
                "state": job["State"],
            }
            for job in job_data
            if job["State"] == "PENDING"
        }

    def get_start_time(self, id):        
        return (
            self.pending_data[id]["start"]
            if id in self.pending_data
            else None
        )
    def get_scheduled_ids(self):
        return [key for key, value in self.pending_data.items() if value["nodes"] is not None]
    
    def get_update(self, id):
        if id in self.pending_data:
            return {
                "Start": self.pending_data[id]["start"],
                "NodeList": self.pending_data[id]["nodes"],                
            }
        else:
            return None
    def get_nodes(self, id):        
        expected_nodes = (
            self.pending_data[id] if id in self.pending_data else None
        )
        return expected_nodes

    def __str__(self):
        return str(self.pending_data)

    def __repr__(self):
        return str(self.pending_data)


def parse_squeue_output() -> Dict[str, str]:
    """
    Parses the SQUEUE output to extract Scheduled Nodes and Expected Start Time.

    Args:
        output (str): The SQUEUE command output as a string.

    Returns:
        List[Tuple[str, str]]: A list of tuples containing (Scheduled Nodes, Expected Start Time).
    """
    output = run_command(["squeue", "-O", "JobArrayID,StartTime,SchedNodes,State", "--state=PENDING"])    
    results = []
    for i, line in enumerate(output):
        # Match the expected format
        match = re.search(
            r"(?P<ID>\S+)\s+(?P<Start>\S+)\s+(?P<Nodes>\S+)\s+(?P<State>\S+)\s*",
            line,
        )
        if match:
            results.append(match.groupdict())
    return results
