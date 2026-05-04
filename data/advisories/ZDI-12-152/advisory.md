# ZDI-12-152: Oracle Outside In Excel MergeCells Record Parsing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-152
- **ZDI-CAN:** ZDI-CAN-1483
- **Date:** 2012-08-22
- **CVE:** N/A
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Oracle
- **Affected Products:** Outside In
- **Credit:** gwslabs.com
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-152/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of applications that utilize Oracle's Outside In Technology. User interaction is required to exploit this vulnerability in that the target must visit open a malicious file. The specific flaw exists within the parsing of Excel files. When handling the MergeCells record, the process does not properly validate size values which can lead to an integer overflow. The resulting value is used to allocate a heap buffer which can be corrupted by an attacker to execute arbitrary code under the context of the application.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/topics/security/cpuapr2012-366314.html

## Disclosure Timeline

- 2011-12-19 - Vulnerability reported to vendor
- 2012-08-22 - Coordinated public release of advisory
