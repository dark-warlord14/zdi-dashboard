# ZDI-15-171: EMC AutoStart ftAgent Opcode 20 Subcode 2060 Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-171
- **ZDI-CAN:** ZDI-CAN-2861
- **Date:** 2015-05-07
- **CVE:** CVE-2015-0538
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:S/C:C/I:C/A:C
- **Affected Vendors:** EMC
- **Affected Products:** AutoStart
- **Credit:** Brian Gorenc of HP's Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-171/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of EMC AutoStart. Authentication is required to exploit this vulnerability, but can be easily bypassed. The specific flaw exists within ftAgent.exe which listens on TCP port 8045, when handling opcode 20 subcode 2060. The vulnerability is caused by lack of input validation before using a remotely supplied string to create a process. By sending a crafted request to a vulnerable system, a remote attacker can exploit this vulnerability to execute arbitrary code in the context of SYSTEM.

## Additional Details

EMC has issued an update to correct this vulnerability. More details can be found at: http://seclists.org/bugtraq/2015/May/att-25/ESA-2015-084.txt

## Disclosure Timeline

- 2015-04-02 - Vulnerability reported to vendor
- 2015-05-07 - Coordinated public release of advisory
