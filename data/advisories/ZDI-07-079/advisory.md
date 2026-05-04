# ZDI-07-079: Hewlett-Packard HP-UX swagentd Buffer Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-07-079
- **ZDI-CAN:** ZDI-CAN-201
- **Date:** 2007-12-17
- **CVE:** CVE-2007-6195
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** HP-UX
- **Credit:** Tenable Network Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-07-079/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Hewlett-Packard HP-UX operating system. Authentication is not required to exploit this vulnerability. The specific flaw exists within the function sw_rpc_agent_init (opcode 0x04) defined in swagentd. Specific malformed arguments can cause function pointers to be overwritten and thereby result in arbitrary code execution.

## Additional Details

Hewlett-Packard has issued an update to correct this vulnerability. More details can be found in HP document ID #SB2294r1.

## Disclosure Timeline

- 2007-07-20 - Vulnerability reported to vendor
- 2007-12-17 - Coordinated public release of advisory
