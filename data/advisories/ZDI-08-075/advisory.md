# ZDI-08-075: EMC Control Center SST_CTGTRANS Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-08-075
- **ZDI-CAN:** ZDI-CAN-398
- **Date:** 2008-11-20
- **CVE:** CVE-2008-5419
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** EMC
- **Affected Products:** Control Center
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-08-075/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on systems with vulnerable installations of EMC Control Center. Authentication is not required to exploit this vulnerability. The specific flaw exists in the Master Agent service (msragent.exe) which listens by default on TCP port 10444. While processing SST_CTGTRANS requests the process copies packet data into a fixed length stack buffer. Exploitation allows for arbitrary code execution under the context of the SYSTEM user.

## Additional Details

For ControlCenter 5.2 SP5 Software navigate in Powerink to the following location: Support > Software Downloads and Licensing > Downloads C > ControlCenter v 5.x > 5.2 SP5 Patch 4433 For ControlCenter 6.0 Software navigate in Powerlink to the following location: Support > Software Downloads and Licensing > Downloads C > ControlCenter v 6.x > 6.0 Patch 4434

## Disclosure Timeline

- 2008-09-23 - Vulnerability reported to vendor
- 2008-11-20 - Coordinated public release of advisory
