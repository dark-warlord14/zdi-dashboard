# ZDI-12-150: Oracle Outside In XPM Processing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-150
- **ZDI-CAN:** ZDI-CAN-1481
- **Date:** 2012-08-22
- **CVE:** N/A
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Oracle
- **Affected Products:** Outside In
- **Credit:** gwslabs.com
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-150/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable products utilizing the Oracle Outside In Technology. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of XPM files. When parsing the chars_per_pixel element the code within vsgdsf.dll does not validate that the data can fit within a stack buffer prior to copying it. This can be leveraged by a remote attacker to execute code under the context of the user running the application.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/topics/security/cpuapr2012-366314.html

## Disclosure Timeline

- 2011-12-19 - Vulnerability reported to vendor
- 2012-08-22 - Coordinated public release of advisory
