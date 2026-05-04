# ZDI-15-173: EMC AutoStart ftAgent Opcode 83 Subcode 22 SQL Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-173
- **ZDI-CAN:** ZDI-CAN-2799
- **Date:** 2015-05-07
- **CVE:** CVE-2015-0538
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:S/C:C/I:C/A:C
- **Affected Vendors:** EMC
- **Affected Products:** AutoStart
- **Credit:** Aniway.Anyway@gmail.com
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-173/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of EMC AutoStart. Authentication is required to exploit this vulnerability, but can be easily bypassed. The specific flaw exists within ftAgent.exe which listens on TCP port 8045, when handling opcode 83 subcode 22. The vulnerability is caused by lack of input validation before using a remotely supplied string to construct SQL queries. By sending a crafted request to a vulnerable system, a remote attacker can exploit this vulnerability to execute arbitrary code in the context of SYSTEM.

## Additional Details

EMC has issued an update to correct this vulnerability. More details can be found at: http://seclists.org/bugtraq/2015/May/att-25/ESA-2015-084.txt

## Disclosure Timeline

- 2015-04-01 - Vulnerability reported to vendor
- 2015-05-07 - Coordinated public release of advisory
