# ZDI-13-001: Oracle Outside In CorelDRAW File Parsing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-001
- **ZDI-CAN:** ZDI-CAN-1563
- **Date:** 2013-02-01
- **CVE:** CVE-2013-0418
- **CVSS:** 5.4
- **CVSS Vector:** AV:A/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Oracle
- **Affected Products:** Outside In
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-001/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Oracle Outside In. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of RIFF files. When processing a LIST record, the size field is treated as a signed integer during input validation but is then treated as an unsigned integer when copying data. This can be leveraged by a remote attacker can leverage to gain code execution under the context of the user running the application.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/topics/security/cpujan2013-1515902.html

## Disclosure Timeline

- 2012-11-14 - Vulnerability reported to vendor
- 2013-02-01 - Coordinated public release of advisory
