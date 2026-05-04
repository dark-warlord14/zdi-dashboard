# ZDI-20-547: (Pwn2Own) Triangle Microworks SCADA Data Gateway DNP3 GET_FILE_INFO Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-547
- **ZDI-CAN:** ZDI-CAN-10266
- **Date:** 2020-04-16
- **CVE:** CVE-2020-10615
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Triangle MicroWorks
- **Affected Products:** SCADA Data Gateway
- **Credit:** Incite Team: Steven Seeley and Chris Anastasio
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-547/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Triangle Microworks SCADA Data Gateway. Authentication is not required to exploit this vulnerability. The specific flaw exists with the handling of opcodes for GET_FILE_INFO. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerablity to execute code in the context of SYSTEM.

## Additional Details

Triangle MicroWorks has issued an update to correct this vulnerability. More details can be found at: https://www.us-cert.gov/ics/advisories/icsa-20-105-03

## Disclosure Timeline

- 2020-01-28 - Vulnerability reported to vendor
- 2020-04-16 - Coordinated public release of advisory
- 2020-04-16 - Advisory Updated
